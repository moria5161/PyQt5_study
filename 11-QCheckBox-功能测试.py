# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("QCheckBox-功能测试")  # 复选框
window.resize(500, 500)


cb = QCheckBox("Python", window)
cb.setIcon(QIcon("ikun.jpg"))
cb.setIconSize(QSize(50, 50))
cb.setTristate(True)  # 支持三态的复选框
# cb.setCheckState(Qt.PartiallyChecked)  # 设置初始状态为中间态

# cb.stateChanged.connect(lambda state: print(state))  # 监听三态
cb.toggled.connect(lambda isChecked: print(isChecked))  # 监听双态


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
