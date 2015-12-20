### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-02-27 | Alfred Jiang | - |

### 方案名称
NSString / NSData - MD5 加密

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
加密 \ MD5

### 需求场景
1. 对信息有特殊的 MD5 摘要算法需求

### 参考链接
1. [stackoverflow](http://stackoverflow.com/questions/1524604/md5-algorithm-in-objective-c)

### 详细内容
MyAdditions.h

    @interface NSString (MyAdditions)
    - (NSString *)md5;
    @end

    @interface NSData (MyAdditions)
    - (NSString*)md5;
    @end

MyAdditions.m

    #import "MyAdditions.h"
    #import <CommonCrypto/CommonDigest.h> // Need to import for CC_MD5 access

    @implementation NSString (MyAdditions)
    - (NSString *)md5
    {
        const char *cStr = [self UTF8String];
        unsigned char result[CC_MD5_DIGEST_LENGTH];
        CC_MD5( cStr, strlen(cStr), result ); // This is the md5 call
        return [NSString stringWithFormat:
            @"%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x",
            result[0], result[1], result[2], result[3],
            result[4], result[5], result[6], result[7],
            result[8], result[9], result[10], result[11],
            result[12], result[13], result[14], result[15]
            ];
    }
    @end

    @implementation NSData (MyAdditions)
    - (NSString*)md5
    {
        unsigned char result[CC_MD5_DIGEST_LENGTH];
        CC_MD5( self.bytes, self.length, result ); // This is the md5 call
        return [NSString stringWithFormat:
            @"%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x",
            result[0], result[1], result[2], result[3],
            result[4], result[5], result[6], result[7],
            result[8], result[9], result[10], result[11],
            result[12], result[13], result[14], result[15]
            ];
    }
    @end

### 效果图
（无）

### 备注
（无）
