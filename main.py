from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout


def play():
    media.play()

def stop():
    media.stop()

app = QApplication([])
win = QWidget()
win.resize(500, 700)
video = QVideoWidget()
media = QMediaPlayer()

media.setVideoOutput(video)

videos = ["31.avi", "123.mp4"]
path_to_video = "C:\\Users\\danil\\Pictures\\EasyEditor\\"
vid = QMediaContent(QUrl.fromLocalFile(path_to_video + videos[0]))

media.setMedia(vid)
media.play()
win_layout = QVBoxLayout()
win_layout.addWidget(video)

btn_play = QPushButton("Грати")
btn_stop = QPushButton("Стоп")
row = QHBoxLayout()
row.addWidget(btn_play)
row.addWidget(btn_stop)
win_layout.addLayout(row)

btn_play.clicked.connect(play)
btn_stop.clicked.connect(stop)

win.setLayout(win_layout)
win.show()
app.exec_()

