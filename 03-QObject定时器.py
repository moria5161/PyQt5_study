# 0.导入需要的包和模块

from PyQt5.Qt import *
import sys


class MyObject(QObject):
    def timerEvent(self, evt):  # 子类继承父类后重写了模块
        print(evt, "1")
    pass


class MyLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("10")
        self.move(100, 100)
        self.setStyleSheet("font-size: 24px;")
        self.timer_id = self.startTimer(1000)  # 会返回值,需要接收

    def timerEvent(self, *args, **kwargs):
        print("你干嘛")
        # 获取当前标签内容
        current_sec = int(self.text())  # 直接获取的话是字符串,用int转换成整数形式
        current_sec -= 1
        self.setText(str(current_sec))  # 将整数形式转换为字符串形式

        if current_sec == 0:
            print("停止")
            self.killTimer(self.timer_id)

class MyWidget(QWidget):
    def timerEvent(self, *args, **kwargs):
        # print("哎呦你干嘛")
        current_w = self.width()  # 获取窗口原本的宽度
        current_h = self.height()  # 获取窗口原本的高度
        self.resize(current_w + 10, current_h + 10)

# 1.创建一个应用对象


app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作

# 2.1 创建控件

window = MyWidget()


# 2.2 设置控件
window.setWindowTitle("QObject定时器的使用")
window.resize(500, 500)

window.startTimer(100)

# 2.3 展示控件

window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
