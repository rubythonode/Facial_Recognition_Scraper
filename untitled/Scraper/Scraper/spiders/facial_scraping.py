import cv2
import numpy as np

# imagePath = 'C:\Users\HP-Admin\PycharmProjects\untitled\Scraper\Scraper\spiders\images_to_hash\18697892_1312963652084025_1769361018_o.jpg'
# CV_HAAR_SCALE_IMAGE = 'C:/Users/HP-Admin/PycharmProjects/untitled/Scraper/Scraper/spiders/XML/HAARCASCADES/'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(
    'C:/Users/HP-Admin/PycharmProjects/untitled/Scraper/Scraper/spiders/XML/HAARCASCADES/')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Read the image
img = cv2.imread('18697892_1312963652084025_1769361018_o.jpg', 0)
gray = cv2.cvtColor(1, img, 3, 4)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    # gray,
    # scaleFactor=1.3,
    # minNeighbors=5,
    # minSize=(0,30,30),
    # flags = cv2.CV_HAAR_SCALE_IMAGE
)

# print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
