from PyQt5.Qt import *


class Window(QWidget):  # 这里Window继承了父类QWidget的所有方法，但是子类中自动调用__init__时并没有用上父类的方法。
    def __init__(self):
        super().__init__()
        self.setWindowTitle("交互状态案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        label = QLabel(self)
        label.setText("哎呦你干嘛")
        # label.resize(200, 20)
        label.move(100, 50)
        label.hide()

        le = QLineEdit(self)
        # le.setText("这是一个文本框")
        le.move(100, 100)

        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(100, 150)
        btn.setEnabled(False)

        def text_cao(a):
            print("文本发生了改变", a)
            # if len(a) > 0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)
            # 直接把判定条件放到setEnabled()中，实现的也是True或者False
            btn.setEnabled(len(a) > 0)

        le.textChanged.connect(text_cao)

        def check():
            # 1. 获取文本框内容
            content = le.text()
            # 2. 判定是否为 只因你太美
            if content == "只因你太美":
                label.setText("口令正确，登录成功")
            else:
                label.setText("口令错误，登录失败")

            label.adjustSize()
            label.show()

        btn.pressed.connect(check)

        pass


if __name__ == '__main__':
    import sys
    # 1.创建一个应用对象
    app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

    window = Window()
    # 2.3 展示控件
    window.show()
    # 3.应用程序的执行，进入到消息循环
    sys.exit(app.exec_())
