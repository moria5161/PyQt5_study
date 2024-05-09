# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("QToolButton-使用")
window.resize(500, 500)

tb = QToolButton(window)  # 工具按钮一般显示图标的话默认不显示内容，这样在工具栏更加整洁
tb.setText("哎呦")  # 一般内容文本不显示
tb.setIcon(QIcon("ikun.jpg"))
tb.setIconSize(QSize(50, 50))
tb.setToolTip("你干嘛")  # 设置文本提示语
# tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置图标和文本内容同时显示
# tb.setArrowType(Qt.LeftArrow)
tb.setAutoRaise(True)  # 设置扁平化处理，并且鼠标放上去的时候会有边框显示

menu = QMenu(tb)
sub_menu = QMenu(menu)
sub_menu.setTitle("新建")
sub_menu.setIcon(QIcon("ikun.jpg"))

action1 = QAction(QIcon("ikun.jpg"), "kunkun1", menu)
action1.setData("练习时长两年半")  # 给不同行为给予数据传递
action2 = QAction(QIcon("ikun.jpg"), "kunkun2", menu)
action2.setData("唱跳rap篮球")

# 监听菜单行为的方法triggered
# action.triggered.connect(lambda: print("点击了kunkun"))

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)

tb.clicked.connect(lambda: print("点击了工具按钮图标"))  # 与QToolButton.InstantPopup唤出菜单的模式有冲突

tb.setMenu(menu)
# 默认情况下需要鼠标按住一小会儿才能唤出菜单，可以作如下修改
# tb.setPopupMode(QToolButton.MenuButtonPopup)  # 在图标右侧设置一个箭头，点击一下就能唤出菜单
tb.setPopupMode(QToolButton.InstantPopup)  # 直接点击图标，就能唤出菜单


def do_action(action):  # action是行为的形参
    print("点击了kunkun", action.data())


tb.triggered.connect(do_action)  # 是不是可以理解triggered只是监听action而，点击菜单或者唤出菜单不属于action

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
