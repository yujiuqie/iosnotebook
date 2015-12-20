### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-02 | Alfred Jiang | - |

### 方案名称
语法 - 弧度（radians）和角度转换（degree）

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
radians \ degree

### 需求场景
1. 弧度（radians）和角度转换（degree）相互转换

### 参考链接
（无）

### 详细内容

1. Swift 解决方案
        CGFloat DegreesToRadians(CGFloat degrees) {return degrees * M_PI / 180;};
        CGFloat RadiansToDegrees(CGFloat radians) {return radians * 180 / M_PI;};

2. Objective-C 解决方案
        /** Degrees to Radian **/
        #define degreesToRadians( degrees ) ( ( degrees ) / 180.0 * M_PI )

        /** Radians to Degrees **/
        #define radiansToDegrees( radians ) ( ( radians ) * ( 180.0 / M_PI ) )

### 效果图
（无）

### 备注
（无）
