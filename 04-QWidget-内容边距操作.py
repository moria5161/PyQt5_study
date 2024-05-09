# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("内容边距设定")
window.resize(500, 500)

label = QLabel(window)
label.setText("哎呦你干嘛")
label.resize(300, 300)
label.setStyleSheet("background-color: cyan")

label.setContentsMargins(100, 200, 0, 0)  # 设置标签内容边距，左上右下
print(label.getContentsMargins())  # 显示内容边距大小

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
