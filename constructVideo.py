import cv2
import os

path = './test_set/reconstruction/events'

files = os.listdir(path)

files = sorted(files)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('eventFrame.avi',fourcc, 60.0, (320,240))

# img = cv2.imread(os.path.join(path,x),0)


for x in files:
    img = cv2.imread(os.path.join(path,x))
    out.write(img)

out.release()
    
