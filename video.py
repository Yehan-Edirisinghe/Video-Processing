import cv2 as cv
import numpy as np

path = '/home/peppo/Documents/Video_processing/test.mp4'


def play(cap):

    arr = np.array((cap.get(3),cap.get(4),3))
    
    list = []

    while cap.isOpened():

        ret, frame = cap.read()
        
        copy = np.empty_like(frame) 
        copy[:] = frame

        list.append(copy)

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
    cap.release()

    return np.array(list)


def write(out,frame):

    out.write(frame)

if __name__ == '__main__':

    cap = cv.VideoCapture(path)

    # frame_width = cap.get(3)
    # frame_height = cap.get(4)
    # fps = cap.get(5)

    # print((cap.read().))

    # out = cv.VideoWriter(filename='output.avi',fourcc=cv.VideoWriter_fourcc('M','J','P','G'), fps=fps, frameSize =(frame_width,frame_height))

    data = play(cap)
    print(data.size)