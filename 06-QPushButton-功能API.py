# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def contextMenuEvent(self, a0):  # 自定义右击展示菜单，需要重写一个方法
        print("展示菜单")
        # ******************菜单设置*******************开始
        menu = QMenu(self)  # 创建菜单
        # btn.setMenu(menu)  # 设置菜单
        btn = QPushButton(QIcon("ikun.jpg"), "ikun", window)  # 可以一步设置三个参数
        btn.setIconSize(QSize(100, 100))
        btn.resize(180, 110)
        # btn.move(50, 0)
        btn.setStyleSheet("background-color: green")
        btn.setFlat(True)

        # 设置子菜单  最近打开
        open_recent_menu = QMenu("最近打开", menu)
        # 设置行为动作  新建  打开  分割线  退出

        new_action = QAction(QIcon("ikun.jpg"), "新建ikun", menu)  # 一步化设置按钮行为
        new_action.triggered.connect(lambda: print("新建ikun"))  # 监听triggered信号

        open_action = QAction(QIcon("ikun.jpg"), "打开ikun", menu)
        open_action.triggered.connect(lambda: print("打开ikun"))

        exit_action = QAction(QIcon("ikun.jpg"), "退出ikun", menu)
        exit_action.triggered.connect(lambda: print("退出ikun"))

        file_action = QAction("只因你太美")
        open_recent_menu.addAction(file_action)

        menu.addAction(new_action)
        menu.addAction(open_action)
        menu.addMenu(open_recent_menu)
        menu.addSeparator()
        menu.addAction(exit_action)

        # poi  设置右击菜单展示位置
        menu.exec_(a0.globalPos())  # 将鼠标右击的全局位置传递给菜单
        pass
    pass


# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = Window()

# 2.2 设置控件
window.setWindowTitle("")
window.resize(500, 500)


# btn = QPushButton(window)
# btn.setText("xxx")
# btn.setIcon(QIcon("ikun.jpg"))  # 设置按钮图标

btn = QPushButton(QIcon("ikun.jpg"), "ikun", window)  # 可以一步设置三个参数
btn.setIconSize(QSize(100, 100))
btn.resize(180, 110)
# btn.move(50, 0)


# ******************菜单设置*******************开始

# menu = QMenu()  # 创建菜单
# btn.setMenu(menu)  # 设置菜单联系按钮
# btn.setStyleSheet("background-color: green")
# btn.setFlat(True)
# # print(btn.isFlat())
# # 设置子菜单  最近打开
#
# open_recent_menu = QMenu("最近打开", menu)
# # 设置行为动作  新建  打开  分割线  退出
#
# # new_action = QAction()
# # new_action.setText("新建ikun")
# # new_action.setIcon(QIcon("ikun.jpg"))
#
# new_action = QAction(QIcon("ikun.jpg"), "新建ikun", menu)  # 一步化设置按钮行为
# new_action.triggered.connect(lambda: print("新建ikun"))  # 监听triggered信号
#
# open_action = QAction(QIcon("ikun.jpg"), "打开ikun", menu)
# open_action.triggered.connect(lambda: print("打开ikun"))
#
# exit_action = QAction(QIcon("ikun.jpg"), "退出ikun", menu)
# exit_action.triggered.connect(lambda: print("退出ikun"))
#
# file_action = QAction("只因你太美")
# open_recent_menu.addAction(file_action)
#
# menu.addAction(new_action)
# menu.addAction(open_action)
# menu.addMenu(open_recent_menu)
# menu.addSeparator()
# menu.addAction(exit_action)


# ******************菜单设置*******************结束


def show_menu(poi):
    menu = QMenu()  # 创建菜单
    # btn.setMenu(menu)  # 设置菜单联系按钮

    btn.setStyleSheet("background-color: green")
    btn.setFlat(True)
    # print(btn.isFlat())
    # 设置子菜单  最近打开

    open_recent_menu = QMenu("最近打开", menu)
    # 设置行为动作  新建  打开  分割线  退出

    # new_action = QAction()
    # new_action.setText("新建ikun")
    # new_action.setIcon(QIcon("ikun.jpg"))

    new_action = QAction(QIcon("ikun.jpg"), "新建ikun", menu)  # 一步化设置按钮行为
    new_action.triggered.connect(lambda: print("新建ikun"))  # 监听triggered信号

    open_action = QAction(QIcon("ikun.jpg"), "打开ikun", menu)
    open_action.triggered.connect(lambda: print("打开ikun"))

    exit_action = QAction(QIcon("ikun.jpg"), "退出ikun", menu)
    exit_action.triggered.connect(lambda: print("退出ikun"))

    file_action = QAction("只因你太美")
    open_recent_menu.addAction(file_action)

    menu.addAction(new_action)
    menu.addAction(open_action)
    menu.addMenu(open_recent_menu)
    menu.addSeparator()
    menu.addAction(exit_action)

    # poi  设置右击菜单展示位置

    # 将poi（局部位置）映射为全局位置
    dest_poi = window.mapToGlobal(poi)
    menu.exec_(dest_poi)  # 将鼠标右击的全局位置传递给菜单


# 上下文菜单策略
window.setContextMenuPolicy(Qt.CustomContextMenu)  # 设置该策略后，右击会发射信号
window.customContextMenuRequested.connect(show_menu)  # 监听发射的信号

# 2.3 展示控件
window.show()

# btn.showMenu()  # 直接展开菜单，注意要在窗口展示之后
# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
