import cv2 as cv
import numpy as np
from threading import Thread

path_input = '/home/peppo/Documents/Video_processing/test.mp4'
path_output = '/home/peppo/Documents/Video_processing/output.mp4'

def render(cap,out):

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    oldFrame = np.zeros((frame_height,frame_width,3))

    while cap.isOpened():

        ret, frame = cap.read() 

        if not ret:             # if frame is read correctly ret is True
            print("Can't receive frame (stream end?). Exiting ...")
            break


        tmp = np.zeros(frame.shape,dtype=np.uint8)

        threads = list()
        k = 2
        for i in range(k):

            x = Thread(target=func, args=(frame,oldFrame,tmp,range(int((i+1)*frame_height/k)),range(int(frame_width))),daemon=True)
            x.start()
            threads.append(x)

        for i in range(k):
            threads[i].join()
        
        out.write(tmp)

        oldFrame[:] = frame

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)

        if cv.waitKey(1) == ord('q'):
            break


    cap.release()
    cv.destroyAllWindows()
    cap.release()


def func(frame,oldFrame,tmp,xlim,ylim):

    for x in xlim:
            for y in ylim:

                for i in range(3):
                    
                    # tmp[x,y,i] = abs(oldFrame[x,y,i]-frame[x,y,i])
                    tmp[x,y,i] = frame[x,y,i]

    # return tmp

if __name__ == '__main__':

    cap = cv.VideoCapture(path_input)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    out = cv.VideoWriter(path_output,cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

    render(cap,out)