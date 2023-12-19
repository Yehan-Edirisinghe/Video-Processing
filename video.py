import cv2 as cv
import numpy as np

path = '/home/peppo/Documents/Video_processing/test.mp4'

cap = cv.VideoCapture(path)

def play():

    while cap.isOpened():
        ret, frame = cap.read()
        print(frame)
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    play()
    
cap.release
