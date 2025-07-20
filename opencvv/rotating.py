import cv2

image = cv2.imread("opencvv\DSC_8804.JPG")
resized = cv2.resize(image, (300,300))

if image is None:
    print("Couldn't load the image")
else:
    (h, w) = resized.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(resized, M, (w,h))
    cv2.imshow("Original",image)
    cv2.imshow("Resized",resized)
    cv2.imshow("Rotated by 90",rotated)

    cv2.waitkey(0)
    cv2.destroyAllWindows