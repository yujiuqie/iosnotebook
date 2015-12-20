### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-01 | Alfred Jiang | - |

### 方案名称
相册 - 从系统相册选择照片

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
相册 \ 拍照 \ 照片选取 \ ImagePickerController

### 需求场景
1. 需要从系统相册选择照片的一类需求

### 参考链接
1. [GitHub](https://github.com/jacobsieradzki/JSImagePickerController)
2. [Code4App](http://code4app.com/ios/JSImagePickerController/54ef0eb6933bf00d7a8b4e49)

### 详细内容

使用方法：

复制JSImagePickerViewController.h/m文件即可，导入头文件：

    #import "JSImagePickerViewController.h"

示例代码：

    JSImagePickerViewController *imagePicker = [[JSImagePickerViewController alloc] init];
    imagePicker.delegate = self;
    [imagePicker showImagePickerInController:self animated:YES];

通过delegate方法获取图像：

    - (void)imagePickerDidSelectImage:(UIImage *)image {
        self.imageView.image = image;
    }
多个delegate方法：

    - (void)imagePickerDidOpen;
    - (void)imagePickerWillOpen;
    - (void)imagePickerWillClose;
    - (void)imagePickerDidClose;
    - (void)imagePickerDidCancel;

另外以下公开属性支持自定义：

    @property (nonatomic) NSTimeInterval animationTime;
    @property (nonatomic, strong) UICollectionView *collectionView;
    @property (nonatomic, strong) UIButton *photoLibraryBtn;
    @property (nonatomic, strong) UIButton *cameraBtn;
    @property (nonatomic, strong) UIButton *cancelBtn;

### 效果图
（无）

### 备注
（无）
