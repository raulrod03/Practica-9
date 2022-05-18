import cv2

image = cv2.imread("imagen_001.jpg")
template = cv2.imread("template_001.jpg")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)#cambia imagen a tonalidades grises

res = cv2.matchTemplate(image_gray, template_gray, cv2.TM_SQDIFF)#metodo usado
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

x1, y1 = min_loc
x2, y2 = min_loc[0] + template.shape[1], min_loc[1] + template.shape[0]#coordenadas 

cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.imshow("Template", template)
cv2.waitKey(0)
cv2.destroyAllWindows()
