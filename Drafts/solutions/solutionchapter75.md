### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-22 | Alfred Jiang | - |
| 2 | 2015-05-11 | Alfred Jiang | 增加 RKNotificationHub|

### 方案名称
UIButton - badge 显示的实现(使用 UIBarButtonItem-Badge)

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
badge \ UIButton \ UIBarButtonItem

### 需求场景
1. 需要在按钮左上角显示未读数目

### 参考链接
1. [CocoaControls Badges](https://www.cocoacontrols.com/search?utf8=%E2%9C%93&q=badge)
2. [GitHub - UIBarButtonItem-Badge](https://github.com/mikeMTOL/UIBarButtonItem-Badge)
3. [GitHub - RKNotificationHub](https://github.com/cwRichardKim/RKNotificationHub)

### 详细内容

###### 1. 引入头文件
    #import "UIBarButtonItem+Badge.h"

###### 2. 添加 UIBarButtonItem

    UIImage *image = [UIImage imageNamed:@"someImage"];
    UIBarButtonItem *navLeftButton = [[UIBarButtonItem alloc] initWithImage:image
                                                                      style:UIBarButtonItemStylePlain
                                                                     target:self
                                                                     action:@selector(buttonPress:)];
    self.navigationItem.leftBarButtonItem = navLeftButton;
    self.navigationItem.leftBarButtonItem.badgeValue = @"1";

###### 3. 有用的属性
    // Each time you change one of properties, the badge will refresh with your changes

    // Badge value to be display
    @property (nonatomic) NSString *badgeValue;
    // Badge background color
    @property (nonatomic) UIColor *badgeBGColor;
    // Badge text color
    @property (nonatomic) UIColor *badgeTextColor;
    // Badge font
    @property (nonatomic) UIFont *badgeFont;

    // Padding value for the badge
    @property (nonatomic) CGFloat badgePadding;
    // Minimum size badge to small
    @property (nonatomic) CGFloat badgeMinSize;
    // Values for offseting the badge over the BarButtonItem you picked
    @property (nonatomic) CGFloat badgeOriginX;
    @property (nonatomic) CGFloat badgeOriginY;

    // In case of numbers, remove the badge when reaching zero
    @property BOOL shouldHideBadgeAtZero;
    // Badge has a bounce animation when value changes
    @property BOOL shouldAnimateBadge;

### 效果图
![screenshotbadge](images/screenshotbadge.png)

### 备注

当嵌套 SlideNavigationController 等控件时，需要注意 leftBarButtonItem 的对象究竟属于哪个 UIViewController

    func badgeValue(aValue : NSString)
    {
        var aNewValue = aValue.integerValue > 99 ? "99+" : aValue
        self.navigationItem.leftBarButtonItem?.badgeValue = aNewValue
    }

### 其他可选方案

* [RKNotificationHub](https://github.com/viktyz/RKNotificationHub)
