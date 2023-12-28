from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(800, 600)
mainline = QVBoxLayout()

window.setLayout(mainline)
window.show()
app.exec()