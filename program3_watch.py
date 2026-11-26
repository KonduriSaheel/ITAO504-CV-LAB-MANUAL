import cv2

img = cv2.imread("input.jpg")
template = cv2.imread("watch_template.jpg")

if img is None or template is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

h, w = temp.shape

result = cv2.matchTemplate(
    gray, temp, cv2.TM_CCOEFF_NORMED)

_, max_val, _, max_loc = cv2.minMaxLoc(result)

if max_val >= 0.65:
    x, y = max_loc
    cv2.rectangle(img, (x, y), (x+w, y+h),
                  (0, 255, 0), 3)
    print("Watch Detected!")
else:
    print("Watch Not Detected!")

cv2.imshow("Watch Detection", img)

cv2.imwrite("watch_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()