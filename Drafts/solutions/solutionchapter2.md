### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-02-27 | Alfred Jiang | - |

### 方案名称
NSString / NSData - AES 加密解密

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
加密 \ 解密 \ Aes

### 需求场景
1. 移动端与服务器敏感数据通讯加密需求

2. 移动端本地部分需要保存的敏感数据（NSUserDefaults、文件或数据库）

### 参考链接
1. [NSData+AES.h](https://gist.github.com/matsuda/9204276)

### 详细内容
代码实现如下

NSData+AES.h文件

     /**
     http://mythosil.hatenablog.com/entry/20111017/1318873155
     http://blog.dealforest.net/2012/03/ios-android-per-aes-crypt-connection/
     */

    @interface NSData (AES)

    - (NSData *)AES128EncryptedDataWithKey:(NSString *)key;
    - (NSData *)AES128DecryptedDataWithKey:(NSString *)key;
    - (NSData *)AES128EncryptedDataWithKey:(NSString *)key iv:(NSString *)iv;
    - (NSData *)AES128DecryptedDataWithKey:(NSString *)key iv:(NSString *)iv;

    @end


NSData+AES.m文件

    #import "NSData+AES.h"
    #import <CommonCrypto/CommonCryptor.h>

    @implementation NSData (AES)

    - (NSData *)AES128EncryptedDataWithKey:(NSString *)key
    {
        return [self AES128EncryptedDataWithKey:key iv:nil];
    }

    - (NSData *)AES128DecryptedDataWithKey:(NSString *)key
    {
        return [self AES128DecryptedDataWithKey:key iv:nil];
    }

    - (NSData *)AES128EncryptedDataWithKey:(NSString *)key iv:(NSString *)iv
    {
        return [self AES128Operation:kCCEncrypt key:key iv:iv];
    }

    - (NSData *)AES128DecryptedDataWithKey:(NSString *)key iv:(NSString *)iv
    {
        return [self AES128Operation:kCCDecrypt key:key iv:iv];
    }

    - (NSData *)AES128Operation:(CCOperation)operation key:(NSString *)key iv:(NSString *)iv
    {
        char keyPtr[kCCKeySizeAES128 + 1];
        bzero(keyPtr, sizeof(keyPtr));
        [key getCString:keyPtr maxLength:sizeof(keyPtr) encoding:NSUTF8StringEncoding];

        char ivPtr[kCCBlockSizeAES128 + 1];
        bzero(ivPtr, sizeof(ivPtr));
        if (iv) {
            [iv getCString:ivPtr maxLength:sizeof(ivPtr) encoding:NSUTF8StringEncoding];
        }

        NSUInteger dataLength = [self length];
        size_t bufferSize = dataLength + kCCBlockSizeAES128;
        void *buffer = malloc(bufferSize);

        size_t numBytesEncrypted = 0;
        CCCryptorStatus cryptStatus = CCCrypt(operation,
                                              kCCAlgorithmAES128,
                                              kCCOptionPKCS7Padding | kCCOptionECBMode,
                                              keyPtr,
                                              kCCBlockSizeAES128,
                                              ivPtr,
                                              [self bytes],
                                              dataLength,
                                              buffer,
                                              bufferSize,
                                              &numBytesEncrypted);
        if (cryptStatus == kCCSuccess) {
            return [NSData dataWithBytesNoCopy:buffer length:numBytesEncrypted];
        }
        free(buffer);
        return nil;
    }

    @end


### 效果图
（无）

### 备注
这里AES在iOS加过密以后以nsdata的形式存下来，如果想以NSString形式存储，那么对NSData进行base64位编码。


