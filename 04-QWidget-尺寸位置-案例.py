# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("哎呦你干嘛")
window.resize(500, 500)
window.move(300, 300)
window.show()

# 设置控件个数
widget_count = 100

# 一行有多少列
column_count = 10

# 计算一个控件的宽度
widget_width = window.width() / column_count

# 总共有多少行（编号//一行有多少列+1）
row_count = (widget_count - 1) // column_count + 1  # 因为编号i是从0开始的，所以控件个数要减去1

widget_height = window.height() / row_count

for i in range(0, widget_count):
    w = QWidget(window)
    w.resize(int(widget_width), int(widget_height))
    widget_x = i % column_count * widget_width
    widget_y = i // column_count * widget_height
    w.move(int(widget_x), int(widget_y))
    w.setStyleSheet("background-color: red; border: 1px solid yellow;")
    w.show()


# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
