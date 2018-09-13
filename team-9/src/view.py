# -*- coding: utf-8 -*-

import os
# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

import tkinter as tk
from tkinter import filedialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import subprocess


class Ui_MainWindow(object):
    def __init__(self):
        self.sourceimgpath = "/home/zh/fast-style-transfer-master123/examples/in/1.jpg"
        self.saveimgname = "test.jpg"
        self.sourcevideopath = '/home/zh/fast-style-transfer-master123/examples/in/fox.mp4'
        self.savevideoname = 'fox.mp4'


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 260, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.LaXiaozu = QtWidgets.QLabel(self.centralwidget)
        self.LaXiaozu.setObjectName("LaXiaozu")
        self.LaXiaozu.setGeometry(QtCore.QRect(50, 30, 80, 20))
        self.LaXiaozu.setText("小组成员")

        self.label_name=QtWidgets.QLabel(self.frame)
        self.label_name.setObjectName("Disname")
        self.label_name.setText("组长：雷鑫\n组员：赵赫 郭子尧 林俊 王雪松 何俊洁")
        #self.horizontalLayout.addWidget(self.label)

        self.LaTrimg = QtWidgets.QLabel(self.centralwidget)
        self.LaTrimg.setObjectName("LaTrimg")
        self.LaTrimg.setGeometry(QtCore.QRect(50, 130, 80, 20))
        self.LaTrimg.setText("图片风格化")

        #图片风格化区
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(50, 150, 260, 120))
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")

        self.La_img = QtWidgets.QLabel(self.frame2)
        self.La_img.setObjectName("Seimg")
        self.La_img.setText("选择预风格化图片：")

        self.But_img = QtWidgets.QPushButton(self.frame2)
        self.But_img.setObjectName("Opimg")
        self.But_img.setText("打开文件")
        self.But_img.setGeometry(QtCore.QRect(120,0,80,20))
        self.But_img.clicked.connect(self.getfilename)

        self.La_style = QtWidgets.QLabel(self.frame2)
        self.La_style.setObjectName("Chostyle")
        self.La_style.setText("选择相应风格：")
        self.La_style.setGeometry(QtCore.QRect(0,30,90,20))

        self.ImgStyle = QtWidgets.QComboBox(self.frame2)
        self.ImgStyle.setObjectName("ImgStyle")
        self.ImgStyle.setGeometry(QtCore.QRect(120,30,120,20))
        self.ImgStyle.addItem("rain_princess")
        self.ImgStyle.addItem("la_muse")
        self.ImgStyle.addItem("ink")
        self.ImgStyle.addItem("scream")
        self.ImgStyle.addItem("udnie")
        self.ImgStyle.addItem("wave")
        self.ImgStyle.addItem("wreck")
        self.ImgStyle.addItem("panda")

        #提示输入风格化后的图片名
        self.La_ImagNa = QtWidgets.QLabel(self.frame2)
        self.La_ImagNa.setObjectName("ImgName")
        self.La_ImagNa.setGeometry(QtCore.QRect(0,60,120,20))
        self.La_ImagNa.setText("风格化后图片名：")

        #图片名称输入框
        self.ImgName = QtWidgets.QLineEdit(self.frame2)
        self.ImgName.setObjectName("SImgName")
        self.ImgName.setGeometry(QtCore.QRect(120,60,120,20))
        self.ImgName.textChanged.connect(self.getname)

        #风格化按钮
        self.ButtrImag = QtWidgets.QPushButton(self.frame2)
        self.ButtrImag.setGeometry(QtCore.QRect(160,90,80,20))
        self.ButtrImag.setText("转换")
        self.ButtrImag.clicked.connect(self.transimg)

        self.LaTrvideo = QtWidgets.QLabel(self.centralwidget)
        self.LaTrvideo.setObjectName("LaTrvideo")
        self.LaTrvideo.setGeometry(QtCore.QRect(50, 320, 80, 20))
        self.LaTrvideo.setText("视频风格化")

        #视频风格化区
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(50, 340, 260, 150))
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame2")

        self.La_video = QtWidgets.QLabel(self.frame3)
        self.La_video.setObjectName("Sevideo")
        self.La_video.setText("选择预风格化视频：")

        self.But_video = QtWidgets.QPushButton(self.frame3)
        self.But_video.setObjectName("Opvideo")
        self.But_video.setText("选择视频")
        self.But_video.setGeometry(QtCore.QRect(120, 0, 80, 20))
        self.But_video.clicked.connect(self.getvideopath)

        self.La_vistyle = QtWidgets.QLabel(self.frame3)
        self.La_vistyle.setObjectName("ChoVistyle")
        self.La_vistyle.setText("选择相应视频风格：")
        self.La_vistyle.setGeometry(QtCore.QRect(0, 30, 120, 20))

        self.VideoStyle = QtWidgets.QComboBox(self.frame3)
        self.VideoStyle.setObjectName("VideoStyle")
        self.VideoStyle.setGeometry(QtCore.QRect(120, 30, 120, 20))
        self.VideoStyle.addItem("rain_princess")
        self.VideoStyle.addItem("la_muse")
        self.VideoStyle.addItem("ink")
        self.VideoStyle.addItem("scream")
        self.VideoStyle.addItem("udnie")
        self.VideoStyle.addItem("wave")
        self.VideoStyle.addItem("wreck")
        self.VideoStyle.addItem("panda")

        self.La_batch = QtWidgets.QLabel(self.frame3)
        self.La_batch.setObjectName("Labatch")
        self.La_batch.setText("图像批量：")
        self.La_batch.setGeometry(QtCore.QRect(0, 60, 120, 20))

        self.Batch = QtWidgets.QComboBox(self.frame3)
        self.Batch.setObjectName("VideoStyle")
        self.Batch.setGeometry(QtCore.QRect(120, 60, 120, 20))
        self.Batch.addItem("1")
        self.Batch.addItem("2")
        self.Batch.addItem("3")
        self.Batch.addItem("4")

        # 提示输入风格化后的图片名
        self.La_VideoNa = QtWidgets.QLabel(self.frame3)
        self.La_VideoNa.setObjectName("VideoName")
        self.La_VideoNa.setGeometry(QtCore.QRect(0, 90, 120, 20))
        self.La_VideoNa.setText("风格化后视频名：")

        # 图片名称输入框
        self.ImgName = QtWidgets.QLineEdit(self.frame3)
        self.ImgName.setObjectName("SVideoName")
        self.ImgName.setGeometry(QtCore.QRect(120, 90, 120, 20))
        self.ImgName.textChanged.connect(self.getvideoname)

        # 风格化按钮
        self.ButtrVideo = QtWidgets.QPushButton(self.frame3)
        self.ButtrVideo.setGeometry(QtCore.QRect(160, 120, 80, 20))
        self.ButtrVideo.setText("转换")
        self.ButtrVideo.clicked.connect(self.tranvideo)

        self.LaStyleS = QtWidgets.QLabel(self.centralwidget)
        self.LaStyleS.setObjectName("LaStyleS")
        self.LaStyleS.setGeometry(QtCore.QRect(340, 30, 80, 20))
        self.LaStyleS.setText("风格展示区")

        #风格展示区
        self.frame4 = QtWidgets.QFrame(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(340, 50, 530,440))
        self.frame4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame4.setObjectName("frame2")

        #第一种风格显示
        self.SIlabel1 = QtWidgets.QLabel(self.frame4)
        self.SIlabel1.setObjectName("SIlabel1")
        self.SIlabel1.setGeometry(QtCore.QRect(5,5, 120,160))#前两个点表示坐标，后面的点表示大小
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/la_muse.jpg')
        self.SIlabel1.setPixmap(pixmap1)
        self.SIlabel1.setScaledContents(True)

        self.NAlabl1 =  QtWidgets.QLabel(self.frame4)
        self.NAlabl1.setObjectName("NAlabl1")
        self.NAlabl1.setGeometry(QtCore.QRect(30, 170, 80, 20))
        self.NAlabl1.setText("la_muse")

        #第二种风格显示
        self.SIlabel2 = QtWidgets.QLabel(self.frame4)
        self.SIlabel2.setObjectName("SIlabel2")
        self.SIlabel2.setGeometry(QtCore.QRect(135, 5, 120, 160))
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/rain_princess.jpg')
        self.SIlabel2.setPixmap(pixmap1)
        self.SIlabel2.setScaledContents(True)

        self.NAlabl2 = QtWidgets.QLabel(self.frame4)
        self.NAlabl2.setObjectName("NAlabl2")
        self.NAlabl2.setGeometry(QtCore.QRect(150, 170, 80, 20))
        self.NAlabl2.setText("rain_princess")

        #第三种风格显示
        self.SIlabel3 = QtWidgets.QLabel(self.frame4)
        self.SIlabel3.setObjectName("SIlabel3")
        self.SIlabel3.setGeometry(QtCore.QRect(265, 5, 120, 160))
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/the_scream.jpg')
        self.SIlabel3.setPixmap(pixmap1)
        self.SIlabel3.setScaledContents(True)

        self.NAlabl3 = QtWidgets.QLabel(self.frame4)
        self.NAlabl3.setObjectName("NAlabl3")
        self.NAlabl3.setGeometry(QtCore.QRect(300, 170, 80, 20))
        self.NAlabl3.setText("scream")

        #水墨画风格展示
        self.SIlabel3 = QtWidgets.QLabel(self.frame4)
        self.SIlabel3.setObjectName("SIlabelink")
        self.SIlabel3.setGeometry(QtCore.QRect(395, 5, 120, 160))
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/ink.jpg')
        self.SIlabel3.setPixmap(pixmap1)
        self.SIlabel3.setScaledContents(True)

        self.NAlabl3 = QtWidgets.QLabel(self.frame4)
        self.NAlabl3.setObjectName("NAlablink")
        self.NAlabl3.setGeometry(QtCore.QRect(440, 170, 80, 20))
        self.NAlabl3.setText("ink")

        #熊猫水墨风格
        self.SIlabel3 = QtWidgets.QLabel(self.frame4)
        self.SIlabel3.setObjectName("SIlabelink")
        self.SIlabel3.setGeometry(QtCore.QRect(395, 220, 120, 160))
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/panda.jpg')
        self.SIlabel3.setPixmap(pixmap1)
        self.SIlabel3.setScaledContents(True)

        self.NAlabl3 = QtWidgets.QLabel(self.frame4)
        self.NAlabl3.setObjectName("NAlablink")
        self.NAlabl3.setGeometry(QtCore.QRect(430, 385, 80, 20))
        self.NAlabl3.setText("panda")

        #第四种风格显示
        self.SIlabel4 = QtWidgets.QLabel(self.frame4)
        self.SIlabel4.setObjectName("SIlabel4")
        self.SIlabel4.setGeometry(QtCore.QRect(5, 220, 120, 160))
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/wreck.jpg')
        self.SIlabel4.setPixmap(pixmap1)
        self.SIlabel4.setScaledContents(True)

        self.NAlabl4 = QtWidgets.QLabel(self.frame4)
        self.NAlabl4.setObjectName("NAlabl4")
        self.NAlabl4.setGeometry(QtCore.QRect(30, 385, 80, 20))
        self.NAlabl4.setText("wreck")

        #第五种风格显示
        self.SIlabel5 = QtWidgets.QLabel(self.frame4)
        self.SIlabel5.setObjectName("SIlabel5")
        self.SIlabel5.setGeometry(QtCore.QRect(135, 220, 120, 160))
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/wave.jpg')
        self.SIlabel5.setPixmap(pixmap1)
        self.SIlabel5.setScaledContents(True)

        self.NAlabl5 = QtWidgets.QLabel(self.frame4)
        self.NAlabl5.setObjectName("NAlabl5")
        self.NAlabl5.setGeometry(QtCore.QRect(175, 385, 80, 20))
        self.NAlabl5.setText("wave")

        #第六种风格显示
        self.SIlabel6 = QtWidgets.QLabel(self.frame4)
        self.SIlabel6.setObjectName("SIlabel6")
        self.SIlabel6.setGeometry(QtCore.QRect(265, 220, 120, 160))
        pixmap1 = QPixmap('/home/zh/fast-style-transfer-master123/examples/style/udnie.jpg')
        self.SIlabel6.setPixmap(pixmap1)
        self.SIlabel6.setScaledContents(True)

        self.NAlabl6 = QtWidgets.QLabel(self.frame4)
        self.NAlabl6.setObjectName("NAlabl6")
        self.NAlabl6.setGeometry(QtCore.QRect(300, 385, 80, 20))
        self.NAlabl6.setText("udnie")

    def getname(self,text):
        self.saveimgname = text

    def getfilename(self):
        sourceimg = tk.filedialog.askopenfilename()
        self.sourceimgpath = sourceimg

    def getvideopath(self):
        sourcevide = tk.filedialog.askopenfilename()
        self.sourcevideopath = sourcevide

    def getvideoname(self,text):
        self.savevideoname = text

    def transimg(self):
        imagestyle = self.ImgStyle.currentText()
        cmd1 = "/home/zh/anaconda2/bin/python evaluate.py --checkpoint models/"+imagestyle+".ckpt"+" --in-path "+self.sourceimgpath+" --out-path examples/out/"+self.saveimgname
        cmd2 = "gwenview examples/out/"+self.saveimgname
        print(cmd1)
        cmd=cmd1+"&&"+ cmd2
        os.system(cmd)

    def tranvideo(self):
        videostyle = self.VideoStyle.currentText()
        batchsize = self.Batch.currentText()
        sourcevideo = self.sourcevideopath
        savevide = self.savevideoname
        #print(sourcevideo)
        cmd1 = "/home/zh/anaconda2/bin/python transform_video.py --in-path "+sourcevideo+" --checkpoint models/"+videostyle+".ckpt"+" --out-path examples/out/"+savevide+" --device /gpu:0 --batch-size "+batchsize
        cmd2="/usr/bin/vlc --started-from-file examples/out/"+savevide
        print(cmd2)
        cmd = cmd1 +"&&"+cmd2
        os.system(cmd)

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QWidget()
    ui=Ui_MainWindow()
    ui.setupUi(windows)
    windows.show()
    sys.exit(app.exec_())
