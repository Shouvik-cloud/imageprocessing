import cv2
import numpy as np

def main():
    # Start webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access camera")
        return

    print("Press ESC to exit")

    # HSV range for RED color
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame horizontally (optional)
        frame = cv2.flip(frame, 1)

        # Convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create masks for red color
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2

        # Remove noise
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=2)
        mask = cv2.dilate(mask, kernel, iterations=2)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 800:
                # Bounding box
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Centroid calculation
                M = cv2.moments(cnt)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])

                    # Draw center
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

                    # Show coordinates
                    text = f"X:{cx} Y:{cy}"
                    cv2.putText(frame, text, (cx + 10, cy),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2)

        # Display windows
        cv2.imshow("Robot Tracking", frame)
        cv2.imshow("Mask", mask)

        # Exit on ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
