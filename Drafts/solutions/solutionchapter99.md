### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-08-27 | Alfred Jiang | - |

### 方案名称
iOS 完全复制一个 UIView

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
UIView \ 复制 \ Duplicate

### 需求场景
1. 需要对一个 UIView 或其子类进行完整复制的操作

### 参考链接
1. [CSDN - iOS 完全复制UIView](http://blog.csdn.net/meegomeego/article/details/20375447)

### 详细内容

    // Duplicate UIView
    - (UIView*)duplicate:(UIView*)view
    {
        NSData * tempArchive = [NSKeyedArchiver archivedDataWithRootObject:view];
        return [NSKeyedUnarchiver unarchiveObjectWithData:tempArchive];
    }

### 效果图
（无）

### 备注
（无）
