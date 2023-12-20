import cv2 as cv
import numpy as np

path_input = '/home/peppo/Documents/Video_processing/test.mp4'
path_output = '/home/peppo/Documents/Video_processing/output.mjpg'

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

        for x in range(frame_height):
            for y in range(frame_width):
                for i in range(3):
                    
                    tmp[x,y,i] = abs(oldFrame[x,y,i]-frame[x,y,i])


        out.write(tmp)

        oldFrame[:] = frame

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)

        if cv.waitKey(1) == ord('q'):
            break


    cap.release()
    cv.destroyAllWindows()
    cap.release()

if __name__ == '__main__':

    cap = cv.VideoCapture(path_input)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    out = cv.VideoWriter(path_output,cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

    render(cap,out)