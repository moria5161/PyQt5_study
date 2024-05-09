# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("按钮组的使用")
window.resize(500, 500)


# 创建四个按钮
r_male = QRadioButton("男", window)
r_male.move(100, 100)
r_female = QRadioButton("女", window)
r_female.move(100, 150)


sex_group = QButtonGroup(window)  # 创建一个group
sex_group.addButton(r_male, 1)
sex_group.addButton(r_female, 2)

# sex_group.setExclusive(False)  # 设置组内子控件取消互斥


r_yes = QRadioButton("真爱粉", window)
r_yes.move(200, 100)
r_no = QRadioButton("小黑子", window)
r_no.move(200, 150)


def test(val):
    print(sex_group.id(val))  # 得到按钮组的id
    
sex_group.buttonToggled.connect(test)  # buttonToggled 按钮转换信号监听


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
