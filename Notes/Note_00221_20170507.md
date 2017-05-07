### 变更记录

| 序号 | 录入时间 | 录入人 | 备注 |
|:--------:|:--------:|:--------:|:--------:|
| 1 | 2017-05-07 | [Alfred Jiang](https://github.com/viktyz) | - |

### 方案名称

工具 - Sublime Text 3 - 禁用启动时打开上次文件

### 关键字

工具 \ Sublime Text 3 \ 关闭记住上次打开文件

### 需求场景

1. Sublime Text 3 中关闭记住上次打开的文件
2. 解决部分默认打开上次打开文件导致的无限保存 bug

### 参考链接

1. [博客园 - Sublime Text 3 中关闭记住上次打开的文件](http://www.cnblogs.com/harxingxing/articles/4595967.html)(推荐)

### 详细内容

进入 **Preferences  -> Settings -> Preferences.sublime-settings** ,添加如下两行

```shell
    "hot_exit": false,
    "remember_open_files": false,
```

说明：

* **hot_exit**：关闭时是否出现保存提示的关键。
* **remember_open_files**：打开上一次打开的文件。

### 效果图
（无）

### 备注
（无）