# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("QCommandLinkButton使用")
window.resize(500, 500)

btn = QCommandLinkButton("标题", "描述", window)
btn.setText("哎呦你干嘛")
btn.setDescription("ikun")
btn.setIcon(QIcon("ikun.jpg"))


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
