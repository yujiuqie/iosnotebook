### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-02 | Alfred Jiang | - |

### 方案名称
修改 Mac OS X root 密码

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
MAC OS \ Root \ 权限

### 需求场景
1. 需要系统 root 权限安装工具时

### 参考链接
1. [John Liu Thinks](http://johnliu.info/mac/xiao_xiao_de_hei_yi_ba_macosx-_xiu_gai_root_mi_ma/)

### 详细内容

方案1：修改root密码

sudo passwd，回车后输入两次想要给root的密码，done……

表打我。。

想要root的shell时候直接su，给密码，完事，exit返回正常

Mac:~ john$ sudo passwd

Password:

Changing password for root.

New password:

Retype new password:

Mac:~ john$ whoami

cxlyx

Mac:~ john$ su

Password:

sh-3.2# whoami

root

方案2：不修改root密码

需要root权限的terminal时候，sudo bash，回车，给自己当前用户密码，完事……唯一缺点就是不能启动root权限的图形界面

### 效果图
（无）

### 备注
（无）
