from UserInterface.PoseDetection import PoseDetector
import cv2

class RussianTwistsDetector(PoseDetector):

    def __init__(self, mode=False, upBody=0, smooth=1, detectionCon=0.5, trackCon=0.5):

        super().__init__(mode, upBody, smooth, detectionCon, trackCon)

        self.twists_count = 0
        self.torso_state = "center"

    def calculate_torso_angle(self, img, side, draw=True):

        if side == "left":
            shoulder1, shoulder2, hip = 11, 12, 23
        else:
            shoulder1, shoulder2, hip = 12, 11, 24

        angle = self.findAngle(img, shoulder1, shoulder2, hip, draw)

        if side == "right":
            angle = 360 - angle

        return angle


def run_russianTwists_detection(repetitions):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = RussianTwistsDetector()
    counting_complete = False

    while True:

        success, img = cap.read()

        if not success:
            print("Error: Could not read frame.")
            break

        img_resized = cv2.resize(img, (1200, 700))
        img = detector.findPose(img_resized)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            left_angle = detector.calculate_torso_angle(img, side="left", draw=True)
            right_angle = detector.calculate_torso_angle(img, side="right", draw=True)

            if left_angle >= 55 and right_angle < 55:
                if detector.torso_state == "center":
                    detector.torso_state = "left"
                elif detector.torso_state == "right":
                    detector.twists_count += 1
                    detector.torso_state = "center"
            elif right_angle >= 55 and left_angle < 55:
                if detector.torso_state == "center":
                    detector.torso_state = "right"
                elif detector.torso_state == "left":
                    detector.twists_count += 1
                    detector.torso_state = "center"

            if not counting_complete:
                remaining_reps = repetitions - detector.twists_count
                cv2.putText(img, f"Twists Count: {detector.twists_count}", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.putText(img, f"Remaining: {remaining_reps}", (10, 100),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

                if detector.twists_count >= repetitions:
                    counting_complete = True
            else:
                cv2.putText(img, "All repetitions completed!", (10, 140),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Image", img)

        if cv2.waitKey(20) & 0xFF == ord('e'):
            break

    cap.release()

    cv2.destroyAllWindows()

