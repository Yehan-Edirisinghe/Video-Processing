import cv2 as cv
import numpy as np
from numpy.ctypeslib import as_ctypes

import ctypes as c
from multiprocessing import Process,RawArray

import time

path_input  = r"C:\Users\Yehan\Documents\Python\Video-Processing\test.mp4"
path_output = r"C:\Users\Yehan\Documents\Python\Video-Processing\output.avi"

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
        
        tmp = np.zeros(frame.shape,dtype=np.uint8)

        t = RawArray(c.c_uint8, (frame.shape[0]*frame.shape[1]*frame.shape[2]))
        
        t_np = np.frombuffer(t,dtype=np.uint8).reshape(frame.shape)
        
        np.copyto(t_np,tmp)

        p1 = Process(target=func, args=(frame,oldFrame,t, range(0,int(frame_height/2)),range(frame_width)))
        p1.start()
        p1.join()

        # func(frame,oldFrame,tmp,range(frame_height),range(frame_width))

        out.write(t_np)

        oldFrame[:] = frame

        # cv.imshow('frame', cv.cvtColor(frame, cv.COLOR_BGR2GRAY))
        cv.imshow('frame', cv.cvtColor(t_np, cv.COLOR_BGR2GRAY))
        
        counter += 1

    cap.release()
    cv.destroyAllWindows()


def func(frame,oldFrame,tmp,xlim,ylim):

    for x in xlim:
            for y in ylim:

                # tmp[x,y,i] = abs(oldFrame[x,y,i]-frame[x,y,i])
                tmp[x,y,0] = 255
                tmp[x,y,1] = 255
                tmp[x,y,2] = 0

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