# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def paintEvent(self, a0):  # 重新写绘制方法
        print("窗口被绘制了")
        return super().paintEvent(a0)  # 让父类进行绘制
    pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("交互状态[*]")
window.resize(500, 500)

# window.setWindowModified(True)

btn = QPushButton(window)
btn.setText("哎呦你干嘛")
btn.pressed.connect(lambda: print("进行了一次重拳出坤"))
btn.setEnabled(False)  # 设置按钮为不可使用
btn.destroyed.connect(lambda: print("按钮消失了"))

# btn.deleteLater()

btn.setAttribute(Qt.WA_DeleteOnClose, True)  # 关闭按钮就释放掉
btn.close()  # 关闭不代表消失
# 2.3 展示控件
# window.show()

window.setVisible(True)

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
