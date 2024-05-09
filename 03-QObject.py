from PyQt5.Qt import *

class Window(QWidget): #这里Window继承了父类QWidget的所有方法，但是子类中自动调用__init__时并没有用上父类的方法。
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qobject学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.QObject继承结构测试()
        # self.QObject对象名称和属性的操作()
        # self.QObject对象的父子关系操作()
        # self.QObject信号的操作()
        # self.QObject类型判定()
        self.QObject对象删除()


    def QObject继承结构测试(self):
        #QObject.__subclasses__()
        mros = QObject.mro()
        for mro in mros:
            print(mro)
        pass

    def QObject对象名称和属性的操作(self):
        # 测试API
        # obj = QObject()  # 创建一个object对象
        # obj.setObjectName("notice") # 设置名字
        # print(obj.objectName())
        #
        # obj.setProperty("notice_level","error") # 设置属性
        # obj.setProperty("notice_level2","warning")

        # 案例
        with open("QObject.qss","r") as f: # 读取设置好的qss文件（字体格式文件）
            qApp.setStyleSheet(f.read()) # 将上述的字体格式应用到全局对象当中，qApp指的是全局应用程序

        label = QLabel(self) # 创建标签
        label.setText("练习两年半")  # 设置标签名字
        label.setObjectName("notice")
        label.setProperty("notice_level","warning") # 设置标签的属性
        label2 = QLabel(self) # 创建标签
        label2.move(100,100) # 将两个标签分开
        label2.setText("个人练习生") # 设置标签名字
        label2.setObjectName("notice")
        label2.setProperty("notice_level", "error")
        label3 = QLabel(self)
        label3.move(150, 150)
        label3.setText("唱跳rap篮球") # 这里我想让标签3不是红色，标签1和2仍然为红色，就需要引入object名字作为一种标签标记对象

        btn = QPushButton(self)
        btn.setText("你干嘛")
        btn.move(50,50)


        # label.setStyleSheet("font-size:20px;color:red") # 字体格式

    def QObject对象的父子关系操作(self):
        #测试API
        obj1 = QObject() # 创建对象
        obj2 = QObject() # 创建对象
        obj1.setParent(obj2) # 把obj2设置为obj1的父对象
        pass

    def QObject信号的操作(self):
        # self.obj = QObject() # self.obj指的是传参对象，就是后面的window
        # def destroy_cao():
        #     print("对象被释放了")
        #
        #
        # self.obj.destroyed.connect(destroy_cao)

        # del self.obj

        # def obj_name_cao(name):
        #     print("对象名称发生了改变", name)
        #
        # self.obj.objectNameChanged.connect(obj_name_cao)
        #
        # self.obj.setObjectName("hhhhh")

        # btn = QPushButton(self)
        # btn.setText("点击我") # 为了使点击后有响应，要建立信号与槽机制。
        # def cao(): #定义一个槽
        #     print("哎呦，你干嘛")
        #
        #
        # btn.clicked.connect(cao) # 点击操作执行后，会产生一个点击信号，传递给cao，然后cao开始执行
        def cao(title):
            print("窗口名字变化了",title)
            # self.windowTitleChanged.disconnect() # 收到信号后断开链接，执行下面一行代码
            self.blockSignals(True)
            self.setWindowTitle("坤坤出击-" + title)
            self.blockSignals(False)
            # self.windowTitleChanged.connect(cao) # 执行完上面一行代码后再链接信号与cao

        self.windowTitleChanged.connect(cao)

        # self.setWindowTitle("不想学习")
        # self.setWindowTitle("想学习")
        self.setWindowTitle("学你妈啊")

    def QObject类型判定(self):
        # obj = QObject()
        # w = QWidget()
        # btn = QPushButton()
        # label = QLabel()
        #直接上案例
        label1 = QLabel(self)
        label1.setText("你干嘛")
        label1.move(100,100)



        label2 = QLabel(self)
        label2.setText("what are you doing")
        label2.move(200, 100)


        btn = QPushButton(self)
        btn.setText("点击我")
        btn.move(200,200)

        # for widget in self.findChildren(QLabel): #只找widget中的QLabel
        for widget in self.children(): # 找所有子控件
            if widget.inherits("QLabel"):
                widget.setStyleSheet("background-color: cyan;")

            # print(widget)


        pass

    def QObject对象删除(self):

        obj1 = QObject()
        obj2 = QObject()
        obj3 = QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda : print("obj1被释放了"))
        obj2.destroyed.connect(lambda : print("obj2被释放了"))
        obj3.destroyed.connect(lambda : print("obj3被释放了"))
        
        pass













if __name__ == '__main__':
    import sys
    # 1.创建一个应用对象
    app = QApplication(sys.argv)  # 这里sys.argv就是将参数传递到我们创建的应用程序中

    window =Window()

    # 2.3 展示控件
    window.show()
    # 3.应用程序的执行，进入到消息循环
    sys.exit(app.exec_())