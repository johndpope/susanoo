# -*- coding: utf-8 -*-

import sys
import cv2 as cv


def detect(image_filename, cascade_filename):
    src_img = cv.imread(image_filename)
    if src_img is None:
        print('cannot load image')
        sys.exit(-1)
    dst_img = src_img.copy()
    cascade = cv.CascadeClassifier(cascade_filename)
    if cascade.empty():
        print('can not load cascade file')
        sys.exit(-1)
    objects = cascade.detectMultiScale(src_img, 1.1, 3)
    for (x, y, w, h) in objects:
        print(x, y, w, h)
        cv.rectangle(dst_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return dst_img

if __name__ == '__main__':
    result = detect(sys.argv[1], sys.argv[3])
    cv.imwrite(sys.argv[2], result)

