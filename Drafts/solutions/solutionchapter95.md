### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-08-17 | Alfred Jiang | - |

### 方案名称
UIImage - 页面模糊效果的实现

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
模糊 \ 半透明 \ 毛玻璃 \ 高斯模糊

### 需求场景
1. 实现页面或图片的模糊效果

### 参考链接
1. [知乎 - iOS 7 的实时毛玻璃模糊 (live blur) 效果渲染需要多大的系统开销？](http://www.zhihu.com/question/21260575/answer/18401841)
2. [三石·道 - iOS开发使用半透明模糊效果](http://www.molotang.com/articles/1921.html)

### 详细内容

* 真实时高斯模糊貌似是不可能了（流畅的）；
对于局部动态的高斯模糊：
* CoreImage 的帧数会随着模糊大小而降低，cpu也蛮高;
* Accelerate 的模糊是最靠谱的，速度和效果都非常完美，同时会占用更高的cpu；
* GPUImage 的速度和效果都不好,但是cpu占用更少（我想一定是哪里用错了才得出这个结论的，因为所有人都说GPUImage碉堡了，秒杀CoreImage）；
所以真要在项目里使用毛玻璃效果的话好像就只能在局部做个伪实时的效果吧。
Accelerate的模糊方法


    - (UIImage *)accelerateBlurWithImage:(UIImage *)image
    {
        NSInteger boxSize = (NSInteger)(10 * 5);
        boxSize = boxSize - (boxSize % 2) + 1;

        CGImageRef img = image.CGImage;

        vImage_Buffer inBuffer, outBuffer, rgbOutBuffer;
        vImage_Error error;

        void *pixelBuffer, *convertBuffer;

        CGDataProviderRef inProvider = CGImageGetDataProvider(img);
        CFDataRef inBitmapData = CGDataProviderCopyData(inProvider);

        convertBuffer = malloc( CGImageGetBytesPerRow(img) * CGImageGetHeight(img) );
        rgbOutBuffer.width = CGImageGetWidth(img);
        rgbOutBuffer.height = CGImageGetHeight(img);
        rgbOutBuffer.rowBytes = CGImageGetBytesPerRow(img);
        rgbOutBuffer.data = convertBuffer;

        inBuffer.width = CGImageGetWidth(img);
        inBuffer.height = CGImageGetHeight(img);
        inBuffer.rowBytes = CGImageGetBytesPerRow(img);
        inBuffer.data = (void *)CFDataGetBytePtr(inBitmapData);

        pixelBuffer = malloc( CGImageGetBytesPerRow(img) * CGImageGetHeight(img) );

        if (pixelBuffer == NULL) {
            NSLog(@"No pixelbuffer");
        }

        outBuffer.data = pixelBuffer;
        outBuffer.width = CGImageGetWidth(img);
        outBuffer.height = CGImageGetHeight(img);
        outBuffer.rowBytes = CGImageGetBytesPerRow(img);

        void *rgbConvertBuffer = malloc( CGImageGetBytesPerRow(img) * CGImageGetHeight(img) );
        vImage_Buffer outRGBBuffer;
        outRGBBuffer.width = CGImageGetWidth(img);
        outRGBBuffer.height = CGImageGetHeight(img);
        outRGBBuffer.rowBytes = 3;
        outRGBBuffer.data = rgbConvertBuffer;

        error = vImageBoxConvolve_ARGB8888(&inBuffer, &outBuffer, NULL, 0, 0, boxSize, boxSize, NULL, kvImageEdgeExtend);

        if (error) {
            NSLog(@"error from convolution %ld", error);
        }
        const uint8_t mask[] = {2, 1, 0, 3};

        vImagePermuteChannels_ARGB8888(&outBuffer, &rgbOutBuffer, mask, kvImageNoFlags);

        CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
        CGContextRef ctx = CGBitmapContextCreate(rgbOutBuffer.data,
                                                 rgbOutBuffer.width,
                                                 rgbOutBuffer.height,
                                                 8,
                                                 rgbOutBuffer.rowBytes,
                                                 colorSpace,
                                                 kCGImageAlphaNoneSkipLast);
        CGImageRef imageRef = CGBitmapContextCreateImage(ctx);
        UIImage *returnImage = [UIImage imageWithCGImage:imageRef];

        //clean up
        CGContextRelease(ctx);

        free(pixelBuffer);
        free(convertBuffer);
        free(rgbConvertBuffer);
        CFRelease(inBitmapData);

        CGColorSpaceRelease(colorSpace);
        CGImageRelease(imageRef);

        return returnImage;
    }

### 效果图
（无）

### 备注
（无）
