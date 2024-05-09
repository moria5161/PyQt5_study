# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件

window.resize(500, 500)
window.setWindowTitle("哎呦你干嘛")
# icon = QIcon("666.jpg")
# window.setWindowIcon(icon)  # 设置顶层窗口图标也就是软件图标
#
# window.setWindowOpacity(0.6)

# print(window.windowState() == Qt.WindowNoState)
# window.setWindowState(Qt.WindowMaximized)
# window.setWindowState(Qt.WindowFullScreen)

# w2 = QWidget()
# w2.setWindowTitle("hhhhhh")

# 2.3 展示控件
window.show()

# w2.show()

window.setWindowState(Qt.WindowActive)  # 设置活跃状态可以让该窗口调到最前面显示
# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
