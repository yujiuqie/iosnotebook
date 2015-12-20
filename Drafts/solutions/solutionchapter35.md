### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-18 | Alfred Jiang | - |
| 2 | 2015-12-07 | Alfred Jiang | 更新约束警告调试 |

### 方案名称
Xcode - 调试相关

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
Debug \ Xcode \ Crash

### 需求场景
1. 调试常见问题收集

### 参考链接
1. [Debugging iOS AutoLayout Issues](http://staxmanade.com/2015/06/debugging-ios-autolayout-issues/)

### 详细内容

#####1. unrecognized selector sent to instance 问题快速定位的方法

方法一：在Debug菜单中选择 Breakpoints -> Create Symbolic Breakpoint，在Symbol中填写如下方法签名：-[NSObject(NSObject) doesNotRecognizeSelector:]，然后再运行，错误时断点会停在真正导致崩溃的地方。

方法二：添加 Exception 类断点（推荐方案）

    打开Xcode
    打开断点导航栏 cmd+7
    点击左下角 **+** 号按钮
    选择 Add Exception Breakpoint...

![](images/Breakpoint01.png)

#####2. Swift Delegate Error show "use of undeclared type in swift project"

在 Swift 中，Delegate 名称不能和函数命相同

#####3. Make a symbolic breakpoint at UIViewAlertForUnsatisfiableConstraints to catch this in the debugger.

    打开Xcode
    打开断点导航栏 cmd+7
    点击左下角 **+** 号按钮
    选择 Add Symbolic Breakpoint...
    右键 Edit Breakpoint...
    在 Symbol 中输入 UIViewAlertForUnsatisfiableConstraints

![](images/Breakpoint02.png)

    通过 打印内存地址信息可以查看控件信息
    (lldb) po 0x7fc82aba1210

    通过 recursiveDescription 方法可以查看全部页面层级关系
    (lldb) po [[0x7fc82aba1210 superview] recursiveDescription]

### 效果图
（无）

### 备注
（无）
