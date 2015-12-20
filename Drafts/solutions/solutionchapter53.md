### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-26 | Alfred Jiang | - |

### 方案名称
语法 - ID类字段生成实现

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
唯一ID \ ID \ 不重复ID

### 需求场景
1. 需要生成不重复的ID类字段时

### 参考链接
（无）

### 详细内容
    + (NSString *)randomId
    {
        NSString *strId = [[NSString stringWithFormat:@"%f",[[NSDate date] timeIntervalSince1970]] stringByReplacingOccurrencesOfString:@"." withString:@""];
        return [strId stringByAppendingString:[NSString stringWithFormat:@"%u",arc4random_uniform(10000)]];
    }

### 效果图
（无）

### 备注
（无）
