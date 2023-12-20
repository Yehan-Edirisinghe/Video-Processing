import cv2 as cv
import numpy as np
from threading import Thread
import concurrent.futures as con
import time

path_input = '/home/peppo/Documents/Video_processing/test.mp4'
path_output = '/home/peppo/Documents/Video_processing/output.mp4'

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

        # k = 2
        # threads = []

        # for i in range(k):

        #     rng = range(int((i)*frame_height/k),int((i+1)*frame_height/k))

        #     # x = Process(target=func, args=(frame,oldFrame,tmp,rng,range(int(frame_width))),daemon=True)
            
        #     threads.append(x)

        # for i in range(k):
        #     threads[i].start()
        #     threads[i].join()
        
        # with con.ThreadPoolExecutor() as executor:
        #     futures = []

        #     k = 2
        #     for i in range(k):

        #         rng = range(int((i)*frame_height/k),int((i+1)*frame_height/k))

        #         x = executor.submit(target=func, args=(frame,oldFrame,tmp,rng,range(int(frame_width))),daemon=True)
            
        #         futures.append(x)

        func(frame,oldFrame,tmp,range(frame_height),range(frame_width))

        out.write(tmp)

        oldFrame[:] = frame

        
        cv.imshow('frame', cv.cvtColor(frame, cv.COLOR_BGR2GRAY))
        counter += 1

    cap.release()
    cv.destroyAllWindows()


def func(frame,oldFrame,tmp,xlim,ylim):

    for x in xlim:
            for y in ylim:

                for i in range(3):
                    
                    # tmp[x,y,i] = abs(oldFrame[x,y,i]-frame[x,y,i])
                    tmp[x,y,i] = 0

    # return tmp

if __name__ == '__main__':

    cap = cv.VideoCapture(path_input)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    out = cv.VideoWriter(path_output,cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


    a = time.time()
    render(cap,out)
    b = time.time()
    print(b-a)