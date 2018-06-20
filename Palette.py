import cv2
import numpy as np

def NullFunction():
    pass

def main():
    img1 = np.zeros((512, 512, 3), np.uint8)
    window1 = 'BGR Color Palette'
    cv2.namedWindow(window1)
    cv2.createTrackbar('B', window1, 0, 255, NullFunction)
    cv2.createTrackbar('G', window1, 0, 255, NullFunction)
    cv2.createTrackbar('R', window1, 0, 255, NullFunction)

    while (True):
        cv2.imshow(window1, img1)

        if cv2.waitKey(1) == 27:
            break

        blue = cv2.getTrackbarPos('B', window1)
        green = cv2.getTrackbarPos('G', window1)
        red = cv2.getTrackbarPos('R', window1)

        img1[:] = [blue, green, red]
        print(blue, green, red)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()