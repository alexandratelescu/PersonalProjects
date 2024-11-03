from UserInterface.PoseDetection import PoseDetector
import cv2

class pushUpsDetector(PoseDetector):

    def __init__(self, mode=False, upBody=0, smooth=1, detectionCon=0.5, trackCon=0.5):

        super().__init__(mode, upBody, smooth, detectionCon, trackCon)

        self.pushUps_count = 0
        self.left_arm_state = "up"
        self.right_arm_state = "up"

    def calculate_arm_angle(self, img, side, draw=True):

        if side == "left":
            shoulder, elbow, wrist = 11, 13, 15
        else:
            shoulder, elbow, wrist = 12, 14, 16

        angle = self.findAngle(img, shoulder, elbow, wrist, draw)

        if side == "left":
            angle = 360 - angle

        return angle

def run_pushUps_detection(repetitions):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = pushUpsDetector()
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
            left_arm_angle = detector.calculate_arm_angle(img, side="left", draw=True)
            right_arm_angle = detector.calculate_arm_angle(img, side="right", draw=True)

            if (left_arm_angle > 160 and detector.left_arm_state == "up" and
                    right_arm_angle > 160 and detector.right_arm_state == "up"):
                detector.left_arm_state = "down"
                detector.right_arm_state = "down"

            if (left_arm_angle < 70 and detector.left_arm_state == "down" and
                    right_arm_angle < 70 and detector.right_arm_state == "down"):
                if not counting_complete:
                    detector.pushUps_count += 1
                    if detector.pushUps_count >= repetitions:
                        counting_complete = True

                detector.left_arm_state = "up"
                detector.right_arm_state = "up"

            if not counting_complete:
                remaining_reps = repetitions - detector.pushUps_count
                cv2.putText(img, f"Push-ups Count: {detector.pushUps_count}", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.putText(img, f"Remaining: {remaining_reps}", (10, 100),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "All repetitions completed!", (10, 140),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.imshow("Image", img)

        if cv2.waitKey(20) & 0xFF == ord('e'):
            break

    cap.release()

    cv2.destroyAllWindows()
