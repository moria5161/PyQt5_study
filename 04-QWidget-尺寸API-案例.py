# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("最小尺寸与最大尺寸")
# window.setFixedSize(500, 500)  # 固定尺寸
# window.setMinimumSize(200, 200)  # 最小尺寸限制
# window.setMinimumWidth()  # 最小宽度
# window.setMinimumHeight()  # 最小高度
# 同理可设置最大尺寸，以及最大高度宽度

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
