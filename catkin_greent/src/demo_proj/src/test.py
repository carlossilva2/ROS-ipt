"""import time
import cv2
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)  # If you don't wait, the image will be dark
return_value, image = camera.read()
cv2.imwrite("opencv.png", image)
del(camera)  # so that others can use the camera as soon as possible"""

import pygame
import pygame.camera
import time

pygame.camera.init()
pygame.camera.list_cameras()
cam = pygame.camera.Camera("/dev/input/event3", (640, 480))
cam.start()
time.sleep(0.1)  # You might need something higher in the beginning
img = cam.get_image()
pygame.image.save(img, "frame.jpg")
cam.stop()