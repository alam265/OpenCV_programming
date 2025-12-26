import cv2

while True:
    pic = cv2.imread("../DATA/00-puppy.jpg")
    cv2.imshow('puppy',pic)
    # IF we've waited at least 1 ms AND we've pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break 

cv2.destroyAllWindows()