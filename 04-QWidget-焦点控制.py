# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mousePressEvent(self, a0):
        # print(self.focusWidget())
        # self.focusNextChild()  # 点击窗口实现聚焦往下一个控件传递
        # self.focusPreviousChild()  # 点击窗口实现聚焦往下一个控件传递

        pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("焦点控制")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(100, 100)

le3 = QLineEdit(window)
le3.move(150, 150)

# le2.setFocus()

# 设置通过tab键传递焦点
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
