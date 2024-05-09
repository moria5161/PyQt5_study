# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class MyWindow(QWidget):
    def mouseMoveEvent(self, a0):
        print("鼠标移动了")

    pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = MyWindow()

# 2.2 设置控件
window.setWindowTitle("鼠标操作")
window.resize(500, 500)
window.setMouseTracking(True)
print(window.hasMouseTracking())

# pixmap = QPixmap("大脑.png")  # 双引号中间是图片路径，可以定义鼠标图形
# new_pixmap = pixmap.scaled(50, 50)
# cursor = QCursor(new_pixmap, -1, -1)  # 创建鼠标 后面两个参数是规定鼠标图形哪个部分作为有效点击
# window.setCursor(cursor)
#
# window.unsetCursor()  # 恢复鼠标默认设置
#
# current_cursor = window.cursor()
# # print(current_cursor.pos())  # 查找位置
# current_cursor.setPos(500, 500)
# # window.setCursor(Qt.ForbiddenCursor)  # .setCursor() 就是用来设计控件的鼠标参数
#
# label = QLabel(window)
# label.setText("哎呦你干嘛")
# label.resize(100, 100)
# label.setStyleSheet("background-color: cyan")
# # label.setCursor(Qt.ForbiddenCursor)


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
