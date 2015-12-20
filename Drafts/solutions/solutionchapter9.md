### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-02 | Alfred Jiang | - |

### 方案名称
设计模式 - 单例模式

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
单例 \ GCD \ dispatch_once \ 设计模式

### 需求场景
1. 单例场景，如某个全局使用的管理类

### 参考链接
（无）

### 详细内容
1. Swift 解决方案
        class var sharedInstance : SettingManager {
            struct Static {
                static var onceToken : dispatch_once_t = 0
                static var instance : SettingManager? = nil
            }
            dispatch_once(&Static.onceToken) {
                Static.instance = SettingManager()
            }
            return Static.instance!
        }

2. Objective-C 解决方案
        +(DBManager *)sharedManager
        {
            static DBManager *sharedManager;

            static dispatch_once_t onceToken;
            dispatch_once(&onceToken, ^{
                sharedManager = [[DBManager alloc] init];
            });

            return sharedManager;
        }

### 效果图
（无）

### 备注
更多设计模式介绍请参考专题[《iOS App 开发常用设计模式有哪些》](questions/questionchapter1.md)
