# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

red = QWidget(window)
red.resize(200, 200)
red.setStyleSheet("background-color: red")
red.move(50, 50)

green = QWidget(window)
green.resize(200, 200)
green.setStyleSheet("background-color: green")
green.move(red.x() + red.width(), red.y() + red.height())

# 2.2 设置控件
window.setWindowTitle("QRadioButton-功能测试")
window.resize(500, 500)


rb_nan = QRadioButton("男", red)
rb_nan.setShortcut("Alt+M")
rb_nan.move(50, 50)
rb_nan.setChecked(True)  # 表示该按钮已经是选中状态
rb_nan.setIcon(QIcon("ikun.jpg"))
rb_nan.setIconSize(QSize(40, 40))

rb_nv = QRadioButton("女", red)
rb_nv.setShortcut("Alt+F")
rb_nv.move(50, 100)
rb_nv.toggled.connect(lambda isChecked: print(isChecked))  # 监听转换信号，并且判断是否为 isChecked

# rb_nv.setAutoExclusive(False)  # 表示设置非单选

rb_yes = QRadioButton("yes", green)
rb_yes.move(50, 50)  # 控件的移动参数是局部参数，根据其所在的父控件决定
rb_no = QRadioButton("no", green)
rb_no.move(50, 100)

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
