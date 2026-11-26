import cv2

cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

slow = cv2.VideoWriter(
    "slow.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps/2, (w, h))

fast = cv2.VideoWriter(
    "fast.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps, (w, h))

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    slow.write(frame)

    if count % 2 == 0:
        fast.write(frame)

    count += 1

cap.release()
slow.release()
fast.release()

print("Slow and Fast Videos Created!")