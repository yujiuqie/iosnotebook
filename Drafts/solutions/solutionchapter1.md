### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-02-27 | Alfred Jiang | - |

### 方案名称
NSString / NSData - Base64 编码

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
Base64 \ NSData \ NSString \ NSData <=> NSString

### 需求场景
1. 当需要将 NSData 类型数据 转为 NSString 类型数据进行传输时
2. 对 NSString 或 NSData 有编码需求时

### 参考链接
1. [GTMBase64 下载](https://code.google.com/p/google-toolbox-for-mac/source/browse/trunk/Foundation/?r=87)

### 详细内容
1. 首先下载 [GTMBase64](https://code.google.com/p/google-toolbox-for-mac/source/browse/trunk/Foundation/?r=87) 文件，在工程中加入以下三个文件

    GTMDefines.h

    GTMBase64.h

    GTMBase64.m

2. 代码实现如下

.h文件

    #pragma mark - base64
    + (NSString*)encodeBase64String:(NSString *)input;
    + (NSString*)decodeBase64String:(NSString *)input;
    + (NSString*)encodeBase64Data:(NSData *)data;
    + (NSString*)decodeBase64Data:(NSData *)data;

.m文件

    #pragma mark - base64
    + (NSString*)encodeBase64String:(NSString * )input {
        NSData *data = [input dataUsingEncoding:NSUTF8StringEncoding allowLossyConversion:YES];
        data = [GTMBase64 encodeData:data];
        NSString *base64String = [[[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding] autorelease];
        return base64String;
    }

    + (NSString*)decodeBase64String:(NSString * )input {
        NSData *data = [input dataUsingEncoding:NSUTF8StringEncoding allowLossyConversion:YES];
        data = [GTMBase64 decodeData:data];
        NSString *base64String = [[[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding] autorelease];
        return base64String;
    }

    + (NSString*)encodeBase64Data:(NSData *)data {
        data = [GTMBase64 encodeData:data];
        NSString *base64String = [[[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding] autorelease];
        return base64String;
    }

    + (NSString*)decodeBase64Data:(NSData *)data {
        data = [GTMBase64 decodeData:data];
        NSString *base64String = [[[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding] autorelease];
        return base64String;
    }

### 效果图
（无）

### 备注
（无）



