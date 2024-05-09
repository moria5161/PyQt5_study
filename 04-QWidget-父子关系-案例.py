# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


# class Label(QLabel):
#     def mousePressEvent(self, ev):
#         self.setStyleSheet("background-color: red;")  # 让标签背景变色
# # 重写QLabel的方法有个弊端，需要把后面所有标签使用的方法换成我们定义的类的标签，比较麻烦。
#     pass


class Window(QWidget):
    def mousePressEvent(self, a0):  # 因为QLabel本身接收到鼠标事件并不会处理，就会传到父控件中
        local_x = a0.x()
        local_y = a0.y()

        sub_widget = self.childAt(local_x, local_y)  # childAt是获取窗口特定位置的控件
        # 如果鼠标点击位置没有控件，那么程序无法执行就会死掉，利用if语句作一个修改
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color: cyan")

    pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("父子关系案例")
window.resize(500, 500)

for i in range(1,11):
    label = QLabel(window)
    label.setText("标签" + str(i))  # 要把整形转为字符串类型
    label.move(40*i, 40*i)

# 如何实现点击某个标签就让背景变红呢？得监听标签的点击行为，需要重写方法。利用类继承重写。

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
