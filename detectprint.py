import numpy as np
import cv2
import sys

image = cv2.imread(sys.argv[1])


colors = {
    "red_lower" : "[  0   0 255]",
    "red_upper" : "[  0   0 127]",
    "blue_lower" : "[255  38   0]",
    "blue_upper" : "[255  38   0]",
    "yellow_lower" : "[  0 216 255]",
    "yellow_upper" : "[  0 216 255]",
    "gray_lower" : "[160 160 160]",
    "gray_upper" : "[160 160 160]"
}

boundaries = [
    ([0, 0, 255], [127, 0, 255]), #red
    ([255, 38, 0], [255, 38, 0]), #blue
    ([0, 216, 255], [0, 216, 255]), #yellow
    ([160, 160, 160], [160, 160, 160]) #gray
]

# loop over the boundaries
for (lower, upper) in boundaries:

    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = np.uint8)
    upper = np.array(upper, dtype = np.uint8)

    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # show the images
    cv2.imshow("Climbing Holds", np.hstack([image, output]))

    cv2.waitKey(0)