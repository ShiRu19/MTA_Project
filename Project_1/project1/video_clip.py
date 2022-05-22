import cv2
import os

path = 'frames'
if not os.path.isdir(path):
    os.mkdir(path)
else:
    raise Exception('path \'frames\' already exsists, please delete to continue')

video_file = 'helmet1.mp4'
capture_fps = 10
cap = cv2.VideoCapture(video_file)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
ratio = int(fps/capture_fps)

if ratio <=0:
    raise Exception('Video fps is lower then capture fps')

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    if i%ratio == 0:
        
        img_path = '{}/{:0>4d}.png'.format(path, int(i/ratio))
        cv2.imwrite(img_path,frame)
 
    i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()