import cv2
import numpy as np

# VARIABLES

# True while mouse button down, False while mouse button up
drawing = False
ix,iy = -1,-1

# FUNCTION
def draw_rectangle(event, x,y, flags, param):

  global ix,iy,drawing
  
  if event == cv2.EVENT_LBUTTONDOWN:
    drawing = True
    ix,iy = x,y
    
  elif event == cv2.EVENT_MOUSEMOVE:
    if drawing == True:
      cv2.circle(img, (ix,iy), int(np.sqrt(abs(x-ix)**2+abs(y-iy)**2)), (0,0,255), -1)
  
  elif event == cv2.EVENT_LBUTTONUP:
    drawing = False

cv2.namedWindow(winname="my_drawing")
cv2.setMouseCallback("my_drawing", draw_rectangle)

# SHOWING IMAGE WITH OPENCV
img = cv2.imread("jupiter.jpg")
#img = np.zeros((512,1024,3))
while True:
  cv2.imshow("my_drawing",img)  
  if cv2.waitKey(1) & 0xFF == 27:
    break

cv2.destroyAllWindows()