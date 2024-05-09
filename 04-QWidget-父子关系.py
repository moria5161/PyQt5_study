# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用对象
app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

# 2.控件操作
# 2.1 创建控件
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("父子关系学习")
window.resize(500, 500)

label1 = QLabel(window)
# label1.setParent()
label1.setText("标签一")

label2 = QLabel(window)
# label2.setParent()
label2.setText("标签二")
label2.move(50, 50)

label3 = QLabel(window)
# label3.setParent()
label3.setText("标签三")
label3.move(100, 100)

print(window.childrenRect())  # 所有子控件组成的边界矩形


# 2.3 展示控件
window.show()

# 3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())
