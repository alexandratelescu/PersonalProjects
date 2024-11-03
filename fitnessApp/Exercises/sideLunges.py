from UserInterface.PoseDetection import PoseDetector
import cv2

class sideLungesDetector(PoseDetector):

    def __init__(self, mode=False, upBody=0, smooth=1, detectionCon=0.5, trackCon=0.5):

        super().__init__(mode, upBody, smooth, detectionCon, trackCon)

        self.left_leg_lunges_count = 0
        self.left_leg_state = "up"
        self.right_leg_lunges_count = 0
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


def run_sideLunges_detection(left_reps, right_reps):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = sideLungesDetector()
    counting_complete_left = False
    counting_complete_right = False

    while True:

        success, img = cap.read()

        if not success:
            break

        img_resized = cv2.resize(img, (1200, 700))
        img = detector.findPose(img_resized)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            left_leg_angle = detector.calculate_leg_angle(img, side="left", draw=True)
            right_leg_angle = detector.calculate_leg_angle(img, side="right", draw=True)

            if left_leg_angle > 150 and detector.left_leg_state == "up":
                detector.left_leg_state = "down"
            elif left_leg_angle < 85 and detector.left_leg_state == "down":
                if not counting_complete_left:
                    detector.left_leg_lunges_count += 1
                    if detector.left_leg_lunges_count >= left_reps:
                        counting_complete_left = True
                detector.left_leg_state = "up"

            if right_leg_angle > 150 and detector.right_leg_state == "up":
                detector.right_leg_state = "down"
            elif right_leg_angle < 85 and detector.right_leg_state == "down":
                if not counting_complete_right:
                    detector.right_leg_lunges_count += 1
                    if detector.right_leg_lunges_count >= right_reps:
                        counting_complete_right = True
                detector.right_leg_state = "up"

            if not counting_complete_left:
                remaining_reps_left = left_reps - detector.left_leg_lunges_count
                cv2.putText(img, f"Left leg lunges: {detector.left_leg_lunges_count}", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.putText(img, f"Remaining lunges for the left leg: {remaining_reps_left}", (10, 140),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "All left leg repetitions completed!", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            if not counting_complete_right:
                remaining_reps_right = right_reps - detector.right_leg_lunges_count
                cv2.putText(img, f"Right leg lunges: {detector.right_leg_lunges_count}", (10, 100),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.putText(img, f"Remaining lunges for the right leg: {remaining_reps_right}", (10, 180),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "All right leg repetitions completed!", (10, 100),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Image", img)

        if cv2.waitKey(20) & 0xFF == ord('e'):
            break

    cap.release()

    cv2.destroyAllWindows()
