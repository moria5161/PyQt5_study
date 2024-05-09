from PyQt5.Qt import *


class Window(QWidget):  # 这里Window继承了父类QWidget的所有方法，但是子类中自动调用__init__时并没有用上父类的方法。
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件消息的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        pass

    def showEvent(self, a0):
        print("窗口被展示出来")

    def closeEvent(self, a0):
        print("窗口被关闭了")

    def moveEvent(self, a0):
        print("窗口被移动了")
 
    def resizeEvent(self, a0):
        print("改变了尺寸大小")

    def enterEvent(self, a0):
        print("鼠标进来了")
        self.setStyleSheet("background-color: cyan;")

    def leaveEvent(self, a0):
        print("鼠标离开了")
        self.setStyleSheet("background-color: yellow;")

    # 还有很多事件可以监听。。。。。。
        

if __name__ == '__main__':
    import sys
    # 1.创建一个应用对象
    app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

    window = Window()
    # 2.3 展示控件
    window.show()
    # 3.应用程序的执行，进入到消息循环
    sys.exit(app.exec_())
