### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-08-25 | Alfred Jiang | - |

### 方案名称
NSString - 筛选出 NSString 中特定字符串

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
NSString \ 筛选 \ 字符串

### 需求场景
1. 需要在一个长串中筛选出特定的字串，比如一句中文中筛选出金额数字

### 参考链接
1. [Cocoa China](http://www.cocoachina.com/bbs/read.php?tid=84940)

### 详细内容

      NSString *aStr = @"这是一句测试，里面包含了19.23这个数字";
      NSCharacterSet* nonDigits = [[NSCharacterSet decimalDigitCharacterSet] invertedSet];
      NSString *aDigits = [aStr stringByTrimmingCharactersInSet:nonDigits];
      //aDigits = 19.23

### 效果图
（无）

### 备注
（无）
