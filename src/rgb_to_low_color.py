import os

import cv2


PROJECT_DIR = os.getenv("PROJECT_DIR")


def main() -> int:
    cap = cv2.VideoCapture(f"{PROJECT_DIR}/res/vid.mp4")
    if not cap.isOpened():
        print("Cannot open input video")
        cap.release()
        return -1

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    size = cap.read()[1].shape[:2]
    out = cv2.VideoWriter(f"{PROJECT_DIR}/res/out.mp4", fourcc, 30, size)
    if not out.isOpened():
        print("Cannot open output video")
        cap.release()
        out.release()
        return -1

    code = 0
    while cv2.waitKey(1) != ord("q"):
        success, frame = cap.read()
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            code = -1
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)

        cv2.imshow("RGB", frame)
        cv2.imshow("GRAY", frame_gray)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return code


if __name__ == "__main__":
    exit(main())
