from UserInterface.PoseDetection import PoseDetector
import cv2

class SquatsDetector(PoseDetector):

    def __init__(self, mode=False, upBody=0, smooth=1, detectionCon=0.5, trackCon=0.5):

        super().__init__(mode, upBody, smooth, detectionCon, trackCon)

        self.squats_count = 0
        self.left_leg_state = "up"
        self.right_leg_state = "up"

    def calculate_leg_angle(self, img, side, draw=True):

        if side == "left":
            hip, knee, ankle = 23, 25, 27
        else:
            hip, knee, ankle = 24, 26, 28

        angle = self.findAngle(img, hip, knee, ankle, draw)

        if side == "left":
            angle = 360 - angle

        return angle


def run_squats_detection(repetitions):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = SquatsDetector()
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
            left_leg_angle = detector.calculate_leg_angle(img, side="left", draw=True)
            right_leg_angle = detector.calculate_leg_angle(img, side="right", draw=True)

            if (left_leg_angle > 160 and detector.left_leg_state == "up" and
                    right_leg_angle > 160 and detector.right_leg_state == "up"):
                detector.left_leg_state = "down"
                detector.right_leg_state = "down"

            if (left_leg_angle < 90 and detector.left_leg_state == "down" and
                    right_leg_angle < 90 and detector.right_leg_state == "down"):
                if not counting_complete:
                    detector.squats_count += 1
                    if detector.squats_count >= repetitions:
                        counting_complete = True

                detector.left_leg_state = "up"
                detector.right_leg_state = "up"

            if not counting_complete:
                remaining_reps = repetitions - detector.squats_count
                cv2.putText(img, f"Squats Count: {detector.squats_count}", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.putText(img, f"Remaining: {remaining_reps}", (10, 100),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else :
                cv2.putText(img, "All repetitions completed!", (10, 140),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Image", img)

        if cv2.waitKey(20) & 0xFF == ord('e'):
            break

    cap.release()

    cv2.destroyAllWindows()
