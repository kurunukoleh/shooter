from PyQt5.QtWidgets import *
import json
import game

#import pygame
#import enemes
#import tank
#import bullets
#import time
#import random
import settings

dota = {}

app = QApplication([])
app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
        color : #ffffff;
        font-size: 15px;
        min-width: 1px;
        min-height : 1px;
        margin : 10 px;
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
        background-color: #00ff00;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #00ff00;
        border-style: solid;
        min-width: 100px;
        min-height: 50px;
        font-size: 15px;
        font-family: none;

    }

    QPushButton#butonstart:hover {
        background-color: #00ff55;
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
        min-height: 50px;
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
        border-color: #ff0000;
        border-style: solid;
        border-width: 3px;
    }

""")
window2 = QWidget()
window2.resize(800, 800)
mainline = QVBoxLayout()

pole1 = QLineEdit()
pole2 = QLineEdit()
pole3 = QLineEdit()
pole4 = QLineEdit()
pole5 = QLineEdit()
pole6 = QLineEdit()
pole7 = QLineEdit()

text1 = QLabel('Кількість астероїдів')
text2 = QLabel('Швидкість астероїдів')
text3 = QLabel('Розмір астероїдів')
text4 = QLabel('Швидкість корабля')
text5 = QLabel('Швидкість кулі')
text6 = QLabel('Фпс')
text7 = QLabel('Гучність музики')

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line7 = QHBoxLayout()

butonsave = QPushButton('зберегти налаштування')
butonskip = QPushButton('скинути налаштування')
butonstart = QPushButton('почати гру')
butonstart.setObjectName('butonstart')

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

mainline.addLayout(line1)
mainline.addLayout(line2)
mainline.addLayout(line3)
mainline.addLayout(line4)
mainline.addLayout(line5)
mainline.addLayout(line6)
mainline.addLayout(line7)
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

def save():
    dota['asteroid_count'] = pole1.text()
    dota['asteroid_speed']= pole2.text()
    dota['asteroid_size'] = pole3.text()
    dota['player_speed']= pole4.text()
    dota['bull_speed']= pole5.text()
    dota['fps']= pole6.text()
    dota['musik_volume'] = pole7.text()
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
    settings.asteroid_count = 30
    settings.player_speed = 2
    settings.asteroid_size = 50
    settings.player_speed = 5
    settings.bull_speed = 10
    settings.fps = 60
    settings.musik_volume = 60
    dota['asteroid_count'] = 30
    dota['asteroid_speed'] = 2
    dota['asteroid_size'] = 50
    dota['player_speed'] = 5
    dota['bull_speed'] = 10
    dota['fps'] = 60
    dota['musik_volume'] = 60
    with open('data.json', 'w', ) as f:
        json.dump(dota, f, indent=4)
    pole1.setText('30')
    pole2.setText('2')
    pole3.setText('50')
    pole4.setText('5')
    pole5.setText('10')
    pole6.setText('60')
    pole7.setText('60')
    #settings.new()



def start():
    window2.hide()
    app.quit()
    game.start()


butonsave.clicked.connect(save)
butonskip.clicked.connect(skip)
butonstart.clicked.connect(start)

window2.setLayout(mainline)
window2.show()
app.exec()