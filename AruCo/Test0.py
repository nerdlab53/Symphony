import cv2
import numpy as np

video = cv2.VideoCapture(0)
# frame = cv2.imread(video)
while True:
    # reads frames from a camera
    ret, frame = video.read()
    original = frame.copy()
    mask = np.zeros(frame.shape, dtype=np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY_INV + cv2.ADAPTIVE_THRESH_MEAN_C)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)
        break

    close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=4)
    close = cv2.cvtColor(close, cv2.COLOR_BGR2GRAY)
    result = cv2.bitwise_and(original, original, mask=close)
    result[close == 0] = (255, 255, 255)

    cv2.imshow('result', result)
    cv2.waitKey(1)
# video.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()