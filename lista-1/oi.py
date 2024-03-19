import cv2 as cv

img = cv.imread("Imagens/Palazzo_Farnese_Fassade.jpg")
cv.imshow("oi", img)
cv.waitKey(0); cv.destroyAllWindows()