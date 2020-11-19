import cv2

CHARS = ' .,-~:;=!*#$@'  # 13

nw = 100

cap = cv2.VideoCapture('./Image/dance.mp4')

print("\x1b[2J", end='')

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = img.shape
    nh = int(h / w * nw)

    img = cv2.resize(img, (nw * 2, nh))

    for row in img:
        for pixel in row:  # pixel 0-255 -> CHARS 0-12
            index = int(pixel / 256 * len(CHARS))
            print(CHARS[index], end='')

        print()

    print('\x1b[H', end='')
