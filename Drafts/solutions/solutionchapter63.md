### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-31 | Alfred Jiang | - |

### 方案名称
UILabel - 通过字符串长度计算显示框大小的方法

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
UILabel \ Size \ UITextView \ CGSize \ CGFrame

### 需求场景
1. 根据一段文字动态计算出用于显示的 UILabel 或 UITextView 等控件的显示大小

### 参考链接
（无）

### 详细内容

#### Swift 版本

#### Objective-C 版本

    + (CGSize)string:(NSString *)string rectSize:(CGSize)upperSize font:(UIFont *)aFont
    {
        NSDictionary *dic = [NSDictionary dictionaryWithObjectsAndKeys:aFont, NSFontAttributeName, nil];

        CGSize size = [string boundingRectWithSize:upperSize
                                                   options:\
                            NSStringDrawingTruncatesLastVisibleLine |
                            NSStringDrawingUsesLineFragmentOrigin |
                            NSStringDrawingUsesFontLeading
                                                attributes:dic
                                                   context:nil].size;

        return size;
    }

### 效果图
（无）

### 备注
（无）
