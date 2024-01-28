from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import game
import saveload
#import pygame
#import enemes
#import tank
#import bullets
#import time
#import random
import settings
from saveload import dota
dota = {}


app = QApplication([])
app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
        color : #ffffff;
        font-size: 15px;
        min-width: 1px;
        min-height : 1px;
        margin : 1 px;
    }

    QPushButton {
        background-color: #cc0000;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        min-width: 100px;
        min-height: 50px;
        font-size: 15px;
        font-family: none;

    }

    QPushButton:hover {
        background-color: #ff2200;
        color : #ffffff;
        border-radius: 10px ;
        border-color: #111111;
        border-style: none;
        border-width: 10px;
        min-height: 50px;
        min-width: 100px;
        font-size: 15px;
        font-family: none;

    }

    QPushButton#butonstart {
        background-color: #0000ff;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #0000ff;
        border-style: solid;
        min-width: 100px;
        min-height: 50px;
        font-size: 15px;
        font-family: none;

    }

    QPushButton#butonstart:hover {
        background-color: #3333dd;
        color : #000000;
        border-radius: 10px ;
        border-color: #00ff55;
        border-style: none;
        border-width: 10px;
        min-height: 50px;
        min-width: 100px;
        font-size: 15px;
        font-family: none;

    }



    QLineEdit {
        background-color: #111111 ;
        color : #ffffff;
        font-size: 15px;
        border-color: #000000;
        border-style: none;
        border-width: 1px;
        border-radius: 5px ;
        min-height: 30px;
    }

    QLineEdit:hover {
        background-color: #151515 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        min-height: 50px;
    }


    QLabel{
        background-color: #000000 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
    }

    QLabel:hover{
        background-color: #000000 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #000000;
        border-style: solid;
        border-width: 3px;
    }

""")
window2 = QWidget()
window2.resize(800, 700)
mainline = QVBoxLayout()

pole1 = QLineEdit()
pole2 = QLineEdit()
pole3 = QLineEdit()
pole4 = QLineEdit()
pole5 = QLineEdit()
pole6 = QLineEdit()
pole7 = QLineEdit()
pole8 = QLineEdit()

text1 = QLabel('Кількість астероїдів')
text2 = QLabel('Швидкість астероїдів')
text3 = QLabel('Розмір астероїдів')
text4 = QLabel('Швидкість корабля')
text5 = QLabel('Швидкість кулі')
text6 = QLabel('Фпс')
text7 = QLabel('Гучність музики')
text8 = QLabel('Концентрація метеоритів')
text9 = QLabel('Кастомні налаштування')
text10 = QLabel('Скіни')
text11 = QLabel('Поточний скін :')
text12 = QLabel('гроші :')
img1 = QLabel('gh')
img2 = QLabel('gh')
img3 = QLabel('gh')

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line7 = QHBoxLayout()
line8 = QHBoxLayout()
line9 = QHBoxLayout()
line10 = QHBoxLayout()

imgsk1 = QPixmap(settings.rocket_texture)
imgsk2 = QPixmap(settings.rocket_texture2)
imgsk3 = QPixmap(settings.rocket_texture3)

imgsk1 = imgsk1.scaled(64 , 64)
imgsk2 = imgsk2.scaled(64 , 64)
imgsk3 = imgsk3.scaled(64 , 64)

img1.setPixmap(imgsk1)
img2.setPixmap(imgsk2)
img3.setPixmap(imgsk3)

butonsave = QPushButton('зберегти налаштування')
butonskip = QPushButton('скинути налаштування')
butonstart = QPushButton('почати гру')
butonstart.setObjectName('butonstart')
butomskin1 = QPushButton('зелений')
butomskin2 = QPushButton('синій')
butomskin3 = QPushButton('червоний')
butonbuysk2 = QPushButton('купити скін : синій')
butonbuysk3 = QPushButton('купити скін : червоний')

butomskin2.hide()
butomskin3.hide()

line1.addWidget(text1)
line1.addWidget(pole1)
line2.addWidget(text2)
line2.addWidget(pole2)
line3.addWidget(text3)
line3.addWidget(pole3)
line4.addWidget(text4)
line4.addWidget(pole4)
line5.addWidget(text5)
line5.addWidget(pole5)
line6.addWidget(text6)
line6.addWidget(pole6)
line7.addWidget(text7)
line7.addWidget(pole7)
line8.addWidget(text8)
line8.addWidget(pole8)
line9.addWidget(butomskin1)
line9.addWidget(butomskin2)
line9.addWidget(butomskin3)
line9.addWidget(butonbuysk2)
line9.addWidget(butonbuysk3)
line10.addWidget(img1)
line10.addWidget(img2)
line10.addWidget(img3)

mainline.addWidget(text12)
mainline.addWidget(text9)
mainline.addLayout(line8)
mainline.addLayout(line1)
mainline.addLayout(line2)
mainline.addLayout(line3)
mainline.addLayout(line4)
mainline.addLayout(line5)
mainline.addLayout(line6)
mainline.addLayout(line7)
mainline.addWidget(text10)
mainline.addLayout(line10)
mainline.addLayout(line9)
mainline.addWidget(text11)
mainline.addWidget(butonsave)
mainline.addWidget(butonskip)
mainline.addWidget(butonstart)

with open('data.json', 'r', encoding='utf-8') as f:
    dota = json.load(f)
pole1.setText(str(dota['asteroid_count']))
pole2.setText(str(dota['asteroid_speed']))
pole3.setText(str(dota['asteroid_size']))
pole4.setText(str(dota['player_speed']))
pole5.setText(str(dota['bull_speed']))
pole6.setText(str(dota['fps']))
pole7.setText(str(dota['musik_volume']))
pole8.setText(str(dota['asteroid_concentration']))
text12.setText("гроші : " + str(dota['balance']))
if dota['skin'] == "pixelartship.png":
    text11.setText("поточний скін : зелений")
if dota['skin'] == "pixelartship2.png":
    text11.setText("поточний скін : синій")
if dota['skin'] == "pixelartship3.png":
    text11.setText("поточний скін : червоний")

if dota["salesk2"] == 1:
    butonbuysk2.hide()
    butomskin2.show()

if dota["salesk3"] == 1:
    butonbuysk3.hide()
    butomskin3.show()


def buyskin2():
    if dota["balance"] >= 100:
        dota["balance"] -= 100
        dota["salesk2"] = 1
        with open('data.json', 'w', ) as f:
            json.dump(dota, f, indent=4)
        try:
            butonbuysk2.hide()
            butomskin2.show()
        except:
            pass
    else:
        print("ytvf uhjitq")


def buyskin3():
    if dota["balance"] >= 200:
        dota["balance"] -= 200
        dota["salesk3"] = 1
        with open('data.json', 'w', ) as f:
            json.dump(dota, f, indent=4)
        try:
            butonbuysk3.hide()
            butomskin3.show()
        except:
            pass
    else:
        print("ytvf uhjitq")


def setskin1():
    dota['skin'] = settings.rocket_texture
    text11.setText("поточний скін : зелений")

def setskin2():
    dota['skin'] = settings.rocket_texture2
    text11.setText("поточний скін : синій")

def setskin3():
    dota['skin'] = settings.rocket_texture3
    text11.setText("поточний скін : червоний")
def save():
    dota['asteroid_concentration'] = pole8.text()
    dota['asteroid_count'] = pole1.text()
    dota['asteroid_speed']= pole2.text()
    dota['asteroid_size'] = pole3.text()
    dota['player_speed']= pole4.text()
    dota['bull_speed']= pole5.text()
    dota['fps']= pole6.text()
    dota['musik_volume'] = pole7.text()
    #saveload.save()
    with open('data.json', 'w', ) as f:
        json.dump(dota, f, indent=4)
    #pole1.clear()
    #pole2.clear()
    #pole3.clear()
    #pole4.clear()
    #pole5.clear()
    #pole6.clear()
    #pole7.clear()
    #settings.new()

def skip():
    pole1.clear()
    pole2.clear()
    pole3.clear()
    pole4.clear()
    pole5.clear()
    pole6.clear()
    pole7.clear()
    pole8.clear()
    settings.musik_volume = 60
    dota['asteroid_count'] = 30
    dota['asteroid_speed'] = 2
    dota['asteroid_size'] = 50
    dota['player_speed'] = 5
    dota['bull_speed'] = 10
    dota['fps'] = 60
    dota['musik_volume'] = 60
    dota['asteroid_concentration'] = 100
    with open('data.json', 'w', ) as f:
        json.dump(dota, f, indent=4)

    pole1.setText('30')
    pole2.setText('2')
    pole3.setText('50')
    pole4.setText('5')
    pole5.setText('10')
    pole6.setText('60')
    pole7.setText('60')
    pole8.setText('100')
    #settings.new()


def start():
    window2.hide()
    app.quit()
    game.start()

butonsave.clicked.connect(save)
butonskip.clicked.connect(skip)
butonstart.clicked.connect(start)
butomskin1.clicked.connect(setskin1)
butomskin2.clicked.connect(setskin2)
butomskin3.clicked.connect(setskin3)
butonbuysk2.clicked.connect(buyskin2)
butonbuysk3.clicked.connect(buyskin3)

window2.setLayout(mainline)
window2.show()
app.exec()