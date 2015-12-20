### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-22 | Alfred Jiang | - |

### 方案名称
使用 Scp 命令上传下载文件

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
Scp \ 上传下载文件

### 需求场景
1. 上传本地文件至 Linux 服务器或者从 Linux 服务器下载文件

### 参考链接
1. [Linux SSH远程文件/目录传输命令scp](http://www.vpser.net/manage/scp.html)

### 详细内容

#####1. 使用如下的命令上传本地文件至服务器

    scp -P 22 -r /Users/ajiang048/Documents/Alfred_Document/asvn/svn/Trunk/iOS-Git-Book/_book/* viktyz@120.27.34.52:/var/www/html/iOSBook

#####2. 使用如下的命令下载服务器文件至本地

    scp -P 22 -r viktyz@120.27.34.52:/var/www/html/iOSBook /Users/ajiang048/Documents/

### 效果图
（无）

### 备注
（无）
