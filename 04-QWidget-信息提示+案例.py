# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
# window = QWidget()  # 没有状态栏

# 设置一个组合控件
window = QMainWindow()  # 懒加载
window.statusBar()  # 加载状态栏

# 2.2 设置控件
window.setWindowTitle("信息提示案例")
window.resize(500, 500)

# 当鼠标停留在窗口控件上面时,在状态栏提示一段文本
window.setStatusTip("这是窗口")  # 状态提示

label = QLabel(window)
label.setText("哎呦你干嘛")
label.setStatusTip("这是一个标签")

# 鼠标停留在控件一小会儿显示提示
label.setToolTip("这是一个提示标签")
# 控制显示时间 默认单位毫秒
label.setToolTipDuration(2000)

# label.setWhatsThis("这是什么?这是标签")

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
