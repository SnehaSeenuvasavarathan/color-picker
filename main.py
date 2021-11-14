import cv2
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
while (True):
    _, frame=cap.read()
    hsv_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _=frame.shape
    midx=int(height/2)
    midy=int(width/2)
    center_pix=hsv_frame[midx, midy]
    cv2.circle(frame, (midx, midy), 5, (255, 0, 0), 3)
    hue_val=center_pix[0]
    color="undefined"
    if hue_val<5:
        color="red"
    elif hue_val<22:
        color="orange"
    elif hue_val<33:
        color="yellow"
    elif hue_val < 78:
        color = "green"
    elif hue_val < 131:
        color = "blue"
    elif hue_val < 170:
        color = "violet"
    else:
        color="red"
    print(center_pix)
    bgr=frame[midx, midy]
    b,g,r=int(bgr[0]), int(bgr[1]), int(bgr[2])
    cv2.putText(frame, color, (10, 70), 0, 2, (b, g, r), 2)
    cv2.imshow("color detector", frame)
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()