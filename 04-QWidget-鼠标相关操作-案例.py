# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()  # super().代表使用父类方法
        self.setWindowTitle("鼠标操作案例")
        self.resize(500, 500)
        self.move(200, 200)
        self.setMouseTracking(True)  # 设置鼠标跟踪

        pixmap = QPixmap("大脑.png").scaled(50, 50)
        cursor = QCursor(pixmap)
        self.setCursor(cursor)

        label = QLabel(self)
        self.label = label  # 让标签作为self的属性
        label.setText("哎呦你干嘛")
        label.move(200, 200)
        label.setStyleSheet("background-color: cyan")

    def mouseMoveEvent(self, a0):
        print("鼠标被移动了", a0.localPos())
        # label = self.findChild(QLabel)  # 父类中找子类控件
        self.label.move(int(a0.localPos().x()), int(a0.localPos().y()))
    pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
