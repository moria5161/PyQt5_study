# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

window = QWidget()  # 没有父控件的控件就被叫做窗口
window.resize(500, 500)
# window.setObjectName("哎呦你干嘛")
window.setWindowTitle("哎呦你干嘛")
print(window.windowTitle())
# print(window.objectName())

# print(QWidget.__bases__)  # 这里__bases__只会找到该方法的上一代父类方法
# print(QWidget.mro())  # 这里mro会找到该方法所继承方法以及祖上所有方法

red = QWidget(window)
red.resize(100, 100)
red.move(400, 0)
red.setStyleSheet("background-color: red;")
#
# green = QWidget(window)
# green.resize(100, 100)
# green.move(400, 50)
# green.setStyleSheet("background-color: green;")

window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
