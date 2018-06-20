import cv2

def main():
    imgpath = "db.jpg"
    img = cv2.imread(imgpath)

    outpath = "db_new.jpg"

    cv2.imshow('img_1', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('img_1')

if __name__ == "__main__":
    main()