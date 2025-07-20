import cv2

image = cv2.imread("opencvv\DSC_8804.JPG")

if image is not None:
    h, w, c = image.shape
    print(f"Image loaded:\nHeight: {h}\nWidth: {w}\nColor: {c}")
else:
    print("Could not load image")