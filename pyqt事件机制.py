import sys
from PyQt5.Qt import *

class App(QApplication): # 继承QApplication的类
    def notify(self, recevier, evt):
        if recevier.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(recevier, evt)
        return  super().notify(recevier, evt) # 这里调用父类的方法,必须返回才能输出结果

    pass

class Btn(QPushButton):
    def event(self, evt):
        # print("按钮被点击了哈哈哈 ")
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)

        return super().event(evt)

    def mousePressEvent(self, e):
        print("鼠标被按下了..........")
    pass

app = App(sys.argv)  # 创建应用程序

window = QWidget()  # 一个窗口

btn = Btn(window)
btn.setText("按钮")
btn.move(100,100)

def cao():
    print("按钮被点击了")

btn.pressed.connect(cao)


window.show()  # 窗口展示

sys.exit(app.exec_())  # 应用程序的结束
