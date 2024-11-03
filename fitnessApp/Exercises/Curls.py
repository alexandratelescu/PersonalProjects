from UserInterface.PoseDetection import PoseDetector
import cv2

class CurlsDetector(PoseDetector):
    def __init__(self, mode=False, upBody=0, smooth=1, detectionCon=0.5, trackCon=0.5):

        super().__init__(mode, upBody, smooth, detectionCon, trackCon)

        self.left_arm_curl_count = 0
        self.left_arm_state = "down"
        self.right_arm_curl_count = 0
        self.right_arm_state = "down"

    def calculate_arm_angle(self, img, side, draw=True):

        if side == "left":
            shoulder, elbow, wrist = 11, 13, 15
        else:
            shoulder, elbow, wrist = 12, 14, 16

        angle = self.findAngle(img, shoulder, elbow, wrist, draw)

        if side == "right":
            angle = 360 - angle

        return angle

def run_curls_detection(left_reps, right_reps):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = CurlsDetector()
    counting_complete_left = False
    counting_complete_right = False

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

            if left_arm_angle < 40 and detector.left_arm_state == "down":
                detector.left_arm_state = "up"

            if left_arm_angle > 130 and detector.left_arm_state == "up":
                detector.left_arm_curl_count += 1
                if detector.left_arm_curl_count >= left_reps:
                    counting_complete_left = True
                detector.left_arm_state = "down"

            if right_arm_angle < 40 and detector.right_arm_state == "down":
                detector.right_arm_state = "up"

            if right_arm_angle > 130 and detector.right_arm_state == "up":
                detector.right_arm_curl_count += 1
                if detector.right_arm_curl_count >= right_reps:
                    counting_complete_right = True
                detector.right_arm_state = "down"

            if not counting_complete_left:
                remaining_reps_left = left_reps - detector.left_arm_curl_count# Display the counts
                cv2.putText(img, f"Left arm curls: {detector.left_arm_curl_count}", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.putText(img, f"Remaining curls for the left arm: {remaining_reps_left}", (10, 140),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "All left arm repetitions completed!", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            if not counting_complete_right:
                remaining_reps_right = right_reps - detector.right_arm_curl_count
                cv2.putText(img, f"Right arm curls: {detector.right_arm_curl_count}", (10, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                cv2.putText(img, f"Remaining curls for the right arm: {remaining_reps_right}", (10, 180),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            else:
                cv2.putText(img, "All right arm repetitions completed!", (10, 100),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)


        cv2.imshow("Image", img)

        if cv2.waitKey(20) & 0xFF == ord('e'):
            break

    cap.release()

    cv2.destroyAllWindows()