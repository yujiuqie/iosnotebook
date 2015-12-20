### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-02 | Alfred Jiang | - |

### 方案名称
密码 - 使用 NAVAJO 进行密码安全强度检测

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
密码强度 \ 输入检测 \ 安全检测 \ NAVAJO

### 需求场景
1. 对用户注册密码进行安全强度检测

### 参考链接
1. [GitHub](https://github.com/mattt/Navajo)

### 详细内容
    NSString *password = @"abc123"
    NJOPasswordValidator *validator = [NJOPasswordValidator standardValidator];

    NSArray *failingRules = nil;
    BOOL isValid = [validator validatePassword:password
                                  failingRules:&failingRules];

    if (!isValid) {
        for (id <NJOPasswordRule> rule in failingRules) {
            NSLog(@"- %@", [rule localizedErrorDescription]);
        }
    }

### 效果图
（无）

### 备注
（无）
