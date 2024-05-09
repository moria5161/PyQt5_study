# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

window = QWidget()  # 一般参数信息会传递到QWidget类的init初始化方法中
window.move(500, 200)
window.resize(500, 500)


def Changecao():
    new_content = label.text() + "哎呦你干嘛"
    label.setText(new_content)
    # label.resize(label.width() + 60, label.height())
    label.adjustSize()  # 根据标签内容自适应调整标签大小
    pass



label = QLabel(window)
label.setText("哎呦你干嘛")
label.move(100, 100)
label.setStyleSheet("background-color: cyan;")

btn = QPushButton(window)
btn.setText("出坤")
btn.move(100, 200)
btn.clicked.connect(Changecao)  # 建立信号与槽机制,设置一个点击按钮的信号发射链接,然后执行槽的代码


# red = QWidget(window)
# red.resize(100, 100)  # 注意resize是改变用户区域的宽高,不是整个窗口框架的宽高
# red.setStyleSheet("background-color: red;")

window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
