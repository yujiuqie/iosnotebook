### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-18 | Alfred Jiang | - |

### 方案名称
UIImageView - 使用 LBBlurredImage 实现图像模糊效果

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
图像模糊 \ LBBlurredImage \ UIImageView \ UIImage

### 需求场景
1. 需要实现图像模糊的场景

### 参考链接
1. [GitHub](https://github.com/lukabernardi/LBBlurredImage)

### 详细内容
#####1. 在工程中添加UIImageView+LBBlurredImage.{h,m} 和 UIImageImage+ImageEffects.{h,m} 文件

#####2. 在需要实现图像模糊的类中引入 UIImageView+LBBlurredImage.h 文件

#####3. 使用下面的代码实现图像模糊

    [self.imageView setImageToBlur:[UIImage imageNamed:@"example"]
                    blurRadius:kLBBlurredImageDefaultBlurRadius
               completionBlock:^(){
                   NSLog(@"The blurred image has been set");
               }];

### 效果图
（无）

### 备注
（无）
