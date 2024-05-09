# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class MyLabel(QLabel):  # self指代对象label
    def enterEvent(self, a0):
        print("鼠标进入了")
        self.setText("欢迎光临")

    def leaveEvent(self, a0):
        print("鼠标离开了")
        self.setText("谢谢回顾")

    def keyPressEvent(self, ev):  # 键盘按键消息事件
        # if ev.key() == Qt.Key_Tab:  # .key()代表普通键位
        #     print("用户点击了tab键位")
        # if ev.modifiers() == Qt.ControlModifier and ev.key() == Qt.Key_S:  # .modifiers()代表修饰键位
        #     print("ctrl + s")
        # .modifiers()同时满足两个修饰键位时用 | 连接
        if ev.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and ev.key() == Qt.Key_A:
            print("ctrl + shift + A")


class Window(QWidget):

    def mousePressEvent(self, ev):
        # print("鼠标按下")
        # 鼠标所在的点在整个屏幕中的位置
        self.mouse_x = ev.globalX()
        self.mouse_y = ev.globalY()
        # 窗口的本身的原始位置（之前已经学过，窗口左上角代表窗口的全局位置）
        self.origin_x = self.x()
        self.origin_y = self.y()

    def mouseMoveEvent(self, ev):
        print(ev.globalX(), ev.globalY())
        # 计算窗口移动的横纵变化量
        move_x = ev.globalX() - self.mouse_x
        move_y = ev.globalY() - self.mouse_y

        dest_x = self.origin_x + move_x
        dest_y = self.origin_y + move_y

        self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, ev):
        print("鼠标释放")

    pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("鼠标操作案例")
window.resize(500, 500)

label = MyLabel(window)
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")
label.grabKeyboard()  # 让标签能够捕获到键盘事件的消息

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
