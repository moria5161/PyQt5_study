from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)#这里sys.argv就是将参数传递到我们创建的应用程序中

window=QWidget()
window.setWindowTitle("社会我楠哥，人狠话不多")
window.resize(500,500)
window.move(400,400)

label = QLabel(window)
label.setText("Hello World")
label.move(200,200)

window.show()

sys.exit(app.exec_())