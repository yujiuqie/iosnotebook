### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-02 | Alfred Jiang | - |
| 2 | 2015-09-09 | Alfred Jiang | - |

### 方案名称
Keychain - 使用 PDKeychainBindingsController 实现 Keychain 保存数据封装

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
Keychain \ 秘钥 \ 安全保存用户密码

### 需求场景
1. 需要保存秘钥串类字串，保证在应用被删除时亦不会消失的需求
2. 安全保存用户密码到 keychain 中的需求

### 参考链接
1. [GitHub - PDKeychainBindingsController](https://github.com/carlbrown/PDKeychainBindingsController)

### 详细内容

确保保存的信息在应用关闭甚至被删除时依然保存在本机

1. 将以下文件加入工程
        PDKeychainBindings.h
        PDKeychainBindings.m
        PDKeychainBindingsController.h
        PDKeychainBindingsController.m

2. 引入头文件
        #import "PDKeychainBindings.h"

2. 使用示例
        //保存
        PDKeychainBindings *bindings=[PDKeychainBindings sharedKeychainBindings];
        [bindings setObject:[textField.text stringByReplacingCharactersInRange:range withString:string] forKey:@"passwordString"];

        //读取
        [passwordField setText:[[PDKeychainBindings sharedKeychainBindings] objectForKey:@"passwordString"]]

### 效果图
（无）

### 备注
（无）

### 其他可选方案

1. [GitHub - SSKeychain](https://github.com/soffes/sskeychain)
2. [GitHub - STUtils](https://github.com/viktyz/STUtils)
