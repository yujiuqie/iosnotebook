### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-02 | Alfred Jiang | - |

### 方案名称
UIButton - 使用 RNLoadingButton 实现等待按钮

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
UIButton \ 等待 \ 按钮

### 需求场景
1. 实现一个显示等待状态的按钮

### 参考链接
1. [RNLoadingButton-Swift](https://github.com/souzainf3/RNLoadingButton-Swift)
2. [RNLoadingButton](https://github.com/souzainf3/RNLoadingButton)

### 详细内容

用法示例

    //Mark: Can usage with Nib
    // Configure State
    btn1.hideTextWhenLoading = false
    btn1.loading = false
    btn1.activityIndicatorAlignment = RNActivityIndicatorAlignment.Right
    btn1.activityIndicatorEdgeInsets = UIEdgeInsetsMake(0, 50, 0, 10)
    btn1.setTitle("connecting", forState: UIControlState.Disabled)

    //等待完成
    //(sender: RNLoadingButton)

    sender.enabled = false
    sender.loading = true;

### 效果图
（无）

### 备注
