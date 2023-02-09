# 레이아웃 절대적배치
import sys
from PyQt5.QtWidgets import *

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'), 0, 0)   # row : 0 , col : 0
        grid.addWidget(QLabel('Author'), 1, 0)  # row : 1 , col : 0
        grid.addWidget(QLabel('Review'), 2, 0)  # row : 2 , col : 0

        grid.addWidget(QLineEdit(), 0, 1) # row : 0 , col : 1
        grid.addWidget(QLineEdit(), 1, 1) # row : 1 , col : 1
        grid.addWidget(QTextEdit(), 2, 1) # row : 2 , col : 1

        btnOK = QPushButton('OK')
        btnCancel = QPushButton('Cancel')
        
        grid.addWidget(btnOK, 3, 1)
        grid.addWidget(btnCancel, 4, 1)

        # 필수 설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())
