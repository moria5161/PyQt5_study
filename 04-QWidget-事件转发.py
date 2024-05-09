# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):            # 顶层窗口的类
    def mousePressEvent(self, a0):
        print("顶层窗口鼠标按下")

    pass


class MidWindow(QWidget):         # 中间窗口的类
    def mousePressEvent(self, a0):
        print("中间控件被按下")
    pass


class Label(QLabel):              # 标签的类
    def mousePressEvent(self, a0):
        print("标签被按下")
        # a0.accept()
        # print(a0.isAccepted())
        a0.ignore()

    pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = Window()

mid_window = MidWindow(window)

# 2.2 设置控件
window.setWindowTitle("事件转发")
window.resize(500, 500)

mid_window.resize(300, 300)
mid_window.setAttribute(Qt.WA_StyledBackground, True)
mid_window.setStyleSheet("background-color: cyan;")

label = Label(mid_window)
label.setText("这是一个标签")
label.setStyleSheet("background-color: red;")
label.move(100, 100)

btn = QPushButton(mid_window)
btn.setText("我是一个按钮")
btn.setStyleSheet("background-color: green;")
btn.move(100, 150)


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
