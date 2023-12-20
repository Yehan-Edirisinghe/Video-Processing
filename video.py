import cv2 as cv
import numpy as np
from threading import Thread
import concurrent.futures as con
import time

path_input = r"C:\Users\Yehan\Documents\Python\Video-Processing\test.mp4"
path_output = r'C:\Users\Yehan\Documents\Python\Video-Processing\output.avi'

def render(cap,out):

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    oldFrame = np.zeros((frame_height,frame_width,3))

    counter = 0

    while cap.isOpened():

        if counter >= 20:
            break

        if cv.waitKey(1) == ord('q'):   # exit the program
            break

        ret, frame = cap.read() 

        if not ret:             # if frame is read correctly ret is True
            print("Can't receive frame (stream end?). Exiting ...")
            break

        tmp = np.empty(frame.shape,dtype=np.uint8)

        func(frame,oldFrame,tmp,range(frame_height),range(frame_width))

        out.write(cv.cvtColor(tmp , cv.COLOR_BGR2GRAY))

        oldFrame[:] = frame

        
        # cv.imshow('frame', cv.cvtColor(frame, cv.COLOR_BGR2GRAY))
        cv.imshow('frame', cv.cvtColor(tmp, cv.COLOR_BGR2GRAY))
        
        counter += 1

    cap.release()
    cv.destroyAllWindows()


def func(frame,oldFrame,tmp,xlim,ylim):

    for x in xlim:
            for y in ylim:

                for i in range(3):
                    
                    tmp[x,y,i] = abs(oldFrame[x,y,i]-frame[x,y,i])
                    # tmp[x,y,i] = frame[x,y,i]

    # return tmp

if __name__ == '__main__':

    cap = cv.VideoCapture(path_input)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    out = cv.VideoWriter(path_output,cv.VideoWriter_fourcc(*'MJPG'), 10, (frame_width,frame_height))


    a = time.time()
    render(cap,out)
    b = time.time()
    print(b-a)