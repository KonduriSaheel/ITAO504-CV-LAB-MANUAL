import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found!")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w = img.shape[:2]

enlarge = cv2.resize(img, (w*2, h*2),
                     interpolation=cv2.INTER_CUBIC)

reduce = cv2.resize(img, (w//2, h//2),
                    interpolation=cv2.INTER_AREA)

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original")

plt.subplot(1, 3, 2)
plt.imshow(enlarge)
plt.title("Enlarged")

plt.subplot(1, 3, 3)
plt.imshow(reduce)
plt.title("Reduced")

plt.show()

print("Resizing Completed!")