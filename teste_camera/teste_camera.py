import cv2
from pyzbar.pyzbar import decode
from PIL import Image 
import qrapp2 

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if webcam.isOpened():
   validacao, frame = webcam.read()
   while validacao:
      validacao, frame = webcam.read()
      cv2.imshow("Imagem da Webcam", frame)
      key = cv2.waitKey(2)
      if cv2.waitKey(33) == ord('a'):
         cv2.imwrite("Foto.png",frame)
         filename = cv2.imread("Foto.png")
         qrapp2.lerQR(filename)
         break
      
      #cv2.imwrite("Foto.png",frame)
webcam.release()


cv2.destroyAllWindows()



