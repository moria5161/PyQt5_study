# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowFlags(Qt.FramelessWindowHint)  # 直接引用设置无边框的方法
        self.setWindowOpacity(0.9)
        self.setWindowTitle("顶层窗口操作案例")
        self.resize(500, 500)
        # 公共数据  将它们变成self的属性，就能被下面的def使用
        self.top_margin = 5
        self.btn_w = 50
        self.btn_h = 30
        # 使用下面的关于子控件的方法
        self.setup_ui()

    def setup_ui(self):  # 所有添加子控件的操作或者方法全部放在这里

        close_btn = QPushButton(self)
        self.close_btn = close_btn
        close_btn.resize(self.btn_w, self.btn_h)
        close_btn.setText("×")

        max_btn = QPushButton(self)
        self.max_btn = max_btn
        max_btn.resize(self.btn_w, self.btn_h)
        max_btn.setText("Max")

        min_btn = QPushButton(self)
        self.min_btn = min_btn
        min_btn.setText("Min")
        min_btn.resize(self.btn_w, self.btn_h)

        close_btn.pressed.connect(self.close)

        def max_normal():
            if self.isMaximized():
                self.showNormal()
                max_btn.setText("Max")
            else:
                self.showMaximized()
                max_btn.setText("Normal")
            pass

        max_btn.pressed.connect(max_normal)
        min_btn.pressed.connect(self.showMinimized)
        pass

    def resizeEvent(self, a0):
        # print("窗口大小发生改变")
        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        self.close_btn.move(close_btn_x, self.top_margin)

        max_btn_x = window_w - self.btn_w * 2
        self.max_btn.move(max_btn_x, self.top_margin)

        min_btn_x = max_btn_x - self.btn_w
        self.min_btn.move(min_btn_x, self.top_margin)
        pass

    def mousePressEvent(self, a0):
        # 鼠标点击时的位置（指的是在整个屏幕中的位置）
        self.mouse_x = a0.globalX()
        self.mouse_y = a0.globalY()

        # self（窗口）的初始位置
        self.origin_x = self.x()  # .x()是取窗口位置的x值
        self.origin_y = self.y()  # .y()是取窗口位置的y值

        pass

    def mouseMoveEvent(self, a0):
        # 这里鼠标发生了移动，通过监听来实现想要的操作

        # 计算鼠标横纵移动的量
        move_x = a0.globalX() - self.mouse_x
        move_y = a0.globalY() - self.mouse_y

        # 鼠标移动的量就是窗口需要的移动的量
        # 计算窗口移动后的横纵坐标
        dest_x = self.origin_x + move_x
        dest_y = self.origin_y + move_y

        self.move(dest_x, dest_y)
        pass

    def mouseReleaseEvent(self, a0):

        pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
# window = QWidget(flags=Qt.FramelessWindowHint)  # 对该窗口设定一个没有边框的标记
window = Window()


# 2.2 设置控件

# def close():
#     window.close()


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
