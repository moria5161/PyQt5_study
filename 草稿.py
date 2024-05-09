# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("按钮功能测试")
window.resize(500, 500)

btn = QPushButton(window)
# ***************文本**********************开始

btn.setText("1")
def plus_one():
    print("加一")
    num = int(btn.text()) + 1
    btn.setText(str(num))

def cao():
    push_button.toggle()
    pass

btn.pressed.connect(plus_one)  # 因为不是调用，所以函数的()不用加上去
btn.pressed.connect(cao)  # 因为不是调用，所以函数的()不用加上去

# ****************文本*********************结束

# ****************图标*********************开始

icon = QIcon("ikun.jpg")
btn.setIcon(icon)

size = QSize(50, 50)
btn.setIconSize(size)
# ****************图标*********************结束

# ****************快捷键*********************开始

# btn.setText("哈哈哈哈")
# btn.pressed.connect(lambda: print("点击"))
# btn.setShortcut("Alt+Q")  # 设置快捷键点击按钮

# ****************快捷键*********************结束

# ****************自动重复*********************开始
# btn.setAutoRepeat(True)  # 设置重复
# btn.setAutoRepeatDelay(2000)  # 代表延迟2秒后进行重复操作
# btn.setAutoRepeatInterval(100)  # 代表重复时间间隔1秒
# ****************自动重复*********************结束
#
push_button = QPushButton(window)
# push_button.setText("这是QPushButton")
# push_button.move(100,100)
#
# radio_button = QRadioButton(window)
# radio_button.setText("这是一个radio")
# radio_button.move(100,150)
#
# # 设置按压的时候执行某种样式
# push_button.setStyleSheet("QPushButton:pressed {background-color: red;}")
#
# push_button.setCheckable(True)  # 设置按钮为可选中性
# push_button.setChecked(True)  # 设置按钮为选中状态
#
# checkbox = QCheckBox(window)
# checkbox.setText("这是checkbox")
# checkbox.move(100, 200)


# ****************排他性设置*********************开始


# for i in range(0, 3):
#     btn = QPushButton(window)
#     btn.setText("btn" + str(i))
#     btn.move(50*i, 50*i)
#     btn.setAutoExclusive(True)  # 设置按钮具有排他性
#     btn.setCheckable(True)
#     pass

# ****************排他性设置*********************结束

# *****************按钮模拟点击********************开始
# btn = QPushButton(window)
# btn.setText("哎呦你干嘛")
# btn.move(200, 200)
# btn.pressed.connect(lambda: print("点击了这个按钮"))

# btn.click()  # 模拟点击按钮
# btn.animateClick(1000)  # 模拟按住按钮一秒

# btn2 = QPushButton(window)
# btn2.setText("哎呦你弄么")
#
#
# def test():
#     btn.animateClick(1000)
#     pass


# 通过监听点击按钮2的操作实现模拟点击按钮1

# btn2.pressed.connect(test)

# *****************按钮模拟点击********************结束


# 自定义点击的有效区域


# 设置按下状态
# push_button.setDown(True)

# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
