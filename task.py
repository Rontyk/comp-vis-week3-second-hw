import cv2
import os
import numpy as np

folder = "./"

FPS = 30
TRANSITION_SECONDS = 1
FRAMES = FPS * TRANSITION_SECONDS

image_files = sorted(os.listdir(folder))
images = []

for file in image_files:
    img = cv2.imread(os.path.join(folder, file))
    if img is not None:
        img = cv2.resize(img, (640, 480))
        images.append(img)

for i in range(len(images) - 1):
    img1 = images[i]
    img2 = images[i + 1]

    for alpha in np.linspace(1, 0, FRAMES):
        frame = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
        cv2.imshow("Slideshow", frame)
        cv2.waitKey(int(1000 / FPS))

cv2.destroyAllWindows()

