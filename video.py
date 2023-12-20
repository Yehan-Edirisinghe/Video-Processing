import cv2 as cv
import numpy as np

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
        

        modified = newFrame(frame,oldFrame)

        print(modified)
        out.write(modified)

        oldFrame[:] = frame

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)

        if cv.waitKey(1) == ord('q'):
            break


    cap.release()
    cv.destroyAllWindows()
    cap.release()

def newFrame(new,old):
    
    a = np.zeros(new.shape)

    for x in range(new.shape[0]):
        for y in range(new.shape[1]):
            for i in range(3):
                
                a[x,y,i] = abs(old[x,y,i]-new[x,y,i])*5

    return a.astype(np.uint8)

if __name__ == '__main__':

    cap = cv.VideoCapture(path_input)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    out = cv.VideoWriter(path_output,cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

    render(cap,out)