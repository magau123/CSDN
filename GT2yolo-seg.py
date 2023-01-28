import copy
import cv2
import os
import shutil
import numpy as np


path = "./mask/test/"
files = os.listdir(path)
for file in files:
    img = cv2.imread(path+file)
    # img = cv2.imread(path)
    H,W=img.shape[0:2]
    print(H,W)
    # img1 = cv2.imread("./images/train2017/ponding_sample_1.jpg")
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,bin_img = cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cnt,hit = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)
    # cv2.drawContours(img1,cnt,-1,(0,255,0),5)
    cnt = list(cnt)
    f = open("./labels/test2017-seg/{}.txt".format(file.split(".")[0]), "a+")
    for j in cnt:
        result = []
        pre = j[0]
        for i in j:
            if abs(i[0][0] - pre[0][0]) > 30 or abs(i[0][1] - pre[0][1]) > 30:
                pre = i
                temp = list(i[0])
                temp[0] /= W
                temp[1] /= H
                result.append(temp)
                # cv2.circle(img1,i[0],1,(0,0,255),2)
        print(result)
        print(len(result))

        # if len(result) != 0:

        if len(result) != 0:
            f.write("0 ")
            for line in result:
                line = str(line)[1:-2].replace(",","")
                # print(line)
                f.write(line+" ")
            f.write("\n")
    f.close()
# cv2.imshow("test",img1)
# cv2.waitKey()