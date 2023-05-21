import cv2 
import numpy as np
cap = cv2.VideoCapture(0)

# Capturing the background
while True:
    ret,frame = cap.read()
    if ret == False:
        break
    cv2.imshow("Press x to capture background",frame)
    if cv2.waitKey(1) == ord('x'):
        background=frame
        break

# Capturing main video

while True:
    ret,frame = cap.read()
    if(ret == False):
        break
    # Converting it to hsv for more ease in colour segmentation
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # for green coloured cloak
    lower_bound = np.array([90, 50, 50])
    upper_bound = np.array([130, 255, 255])

    # the area covered by the cloak
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    cloak = cv2.bitwise_and(background, background, mask=mask)

    # the part excluding the cloak
    inverse_mask = cv2.bitwise_not(mask)  
    current_background = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    
    #combining both the parts and displaying the resultant frame
    combined = cv2.add(cloak, current_background)
    cv2.imshow("Invisible Cloak",combined)

    if(cv2.waitKey(1) == ord("q")):
        break


cv2.destroyAllWindows()
