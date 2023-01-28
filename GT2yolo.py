import copy

import cv2
import os
import shutil
import numpy as np

path = "./mask/train/"
files = os.listdir(path)
for file in files:
    img = cv2.imread(path+file)


    #1->255####
    # print(img.shape)
    # for i in range(len(img)):
    #     for j in range(len(img[0])):
    #         if img[i][j] == 1:
    #             img[i][j]print(file) = 255
    #             print(img[i][j])
    # cv2.imwrite("./mask/{}".format(file),img)

    #get_bbox

    # path = "./mask/ponding_sample_103.png"
    # img = cv2.imread(path)
    img_w = img.shape[1]
    img_h = img.shape[0]
    print(img.shape,img_w,img_h)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cnts,_ = cv2.findContours(img.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    boxs = []
    for i, contour in enumerate(cnts):
        area = cv2.contourArea(contour)  # 计算包围形状的面积
        rect = cv2.minAreaRect(contour)  # 检测轮廓最小外接矩形，得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        temp =[0]
        temp.append(rect[0][0])
        temp.append(rect[0][1])
        temp.append(rect[1][0])
        temp.append(rect[1][1])
        temp[1] /= img_w
        temp[2] /= img_h
        temp[3] /= img_w
        temp[4] /= img_h
        # box = np.int0(cv2.boxPoints(rect))
        boxs.append(temp)   # 最后剩下的有用的框

    # np.set_printoptions(suppress=True)
    # np.set_printoptions(precision=3)  # 设精度为3
    # np.savetxt("./labels/train2017/{}.txt".format(file.split(".")[0]), boxs)
    f = open("./labels/train2017/{}.txt".format(file.split(".")[0]), "w+")
    for line in boxs:
        line = str(line)[1:-2].replace(",","")
        print(line)
        f.write(line+"\n")
    f.close()

