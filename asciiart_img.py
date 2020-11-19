import cv2

CHARS = ' .,-~:;=!*#$@'  # 13
nw = 100

img = cv2.imread('./Image/lunar.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


h, w = img.shape
nh = int(h / w * nw)

img = cv2.resize(img, (nw*2, nh))

for row in img:
    for pixel in row:  # pixel 0 ~ 255 -> CHARS 0~12
        index = int(pixel / 256 * len(CHARS))
        print(CHARS[index], end='')
    print()
