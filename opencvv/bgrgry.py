import cv2

image = cv2.imread("opencvv\DSC_8804.JPG")
resized = cv2.resize(image, (300,300))
if image is not None:
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale",gray)
    cv2.imwrite("grayscale.png",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image")