### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-13 | Alfred Jiang | - |
| 2 | 2015-08-28 | Alfred Jiang | - |

### 方案名称
UILabel - 显示多格式文本

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
NSMutableAttributedString \ attributedText \ UILabel

### 需求场景
1. 需要显示一段多格式的文本

### 参考链接


### 详细内容

#####1. Objective-C 示例
        NSString *plainText = [NSString stringWithFormat:@"%@ test", @"click"];
        NSMutableAttributedString *styleText = [[NSMutableAttributedString alloc] initWithString:plainText];
        NSDictionary *attr = @{NSFontAttributeName: [UIFont systemFontOfSize:15],NSForegroundColorAttributeName : [UIColor redColor]};
        NSRange nameRange = [plainText rangeOfString:aInfo.title];
        [styleText setAttributes:attr range:nameRange];
        self.labelInfo.attributedText = styleText;

#####2. Swift 示例

示例1

    var plainText = title! + " button pressed";
    var styleText = NSMutableAttributedString(string: plainText);
    var attributes : NSDictionary = [NSFontAttributeName : UIFont.boldSystemFontOfSize( statusLabel.font.pointSize )]
    let nameRange : NSRange  = (plainText as NSString).rangeOfString(title!);
    //styleText.setAttributes(attributes, ))
    styleText.setAttributes(attributes, range: nameRange);
    statusLabel.attributedText = styleText;

示例2

    func attributedString(plainText : NSString, sString : NSString) -> NSMutableAttributedString
    {
        var styleText = NSMutableAttributedString(string: plainText)
        var font : UIFont = UIFont(name: "Helvetica-BoldOblique", size: 13.0)!
        var color : UIColor = COLOR_ORANGE
        var attrs = [NSFontAttributeName : font, NSForegroundColorAttributeName : color]
        let nameRange : NSRange  = (plainText as NSString).rangeOfString(sString)
        styleText.setAttributes(attrs, range: nameRange)
        return styleText
    }

### 效果图
（无）

### 备注
