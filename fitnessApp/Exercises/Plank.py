from UserInterface.PoseDetection import PoseDetector
import cv2
import time

class PlankDetector(PoseDetector):

    def __init__(self, target_time, mode=False, upBody=0, smooth=1, detectionCon=0.5, trackCon=0.5):

        super().__init__(mode, upBody, smooth, detectionCon, trackCon)

        self.target_time = target_time
        self.plank_timer_started = False
        self.start_time = None

    def calculate_arm_angle(self, img, side, draw=True):

        if side == "left":
            shoulder, elbow, wrist = 11, 13, 15
        else:
            shoulder, elbow, wrist = 12, 14, 16

        angle = self.findAngle(img, shoulder, elbow, wrist, draw)
        return angle

    def is_in_plank_position(self, left_arm_angle, right_arm_angle):

        arm_threshold_min = 175
        arm_threshold_max = 190

        return (arm_threshold_min <= left_arm_angle <= arm_threshold_max and
                arm_threshold_min <= right_arm_angle <= arm_threshold_max)

def run_plank_detection(target_time):

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    detector = PlankDetector(target_time)

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

            if detector.is_in_plank_position(left_arm_angle, right_arm_angle):
                if not detector.plank_timer_started:
                    detector.plank_timer_started = True
                    detector.start_time = time.time()

                elapsed_time = time.time() - detector.start_time
                remaining_time = int(detector.target_time - elapsed_time)

                if remaining_time <= 0:
                    cv2.putText(img, "Plank completed!", (10, 60),
                                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                else:
                    cv2.putText(img, f"Time remaining: {remaining_time}s", (10, 60),
                                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            else:
                if detector.plank_timer_started:
                    detector.plank_timer_started = False
                    detector.start_time = None

                cv2.putText(img, "Align body to start timer", (10, 60),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        cv2.imshow("Plank Detection", img)

        if cv2.waitKey(20) & 0xFF == ord('e'):
            break

    cap.release()

    cv2.destroyAllWindows()
