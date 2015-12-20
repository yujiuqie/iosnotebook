### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-02 | Alfred Jiang | - |

### 方案名称
语法函数 - 类似 NSError 的引用传值实现

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
NSError \ 引用传值 \ Objective-C 多值返回

### 需求场景
1. 需要实现类似 NSError 的返回时

### 参考链接
（无）

### 详细内容
1. 定义
        - (BOOL)validatePassword:(NSString *)password
                    failingRules:(out NSArray *__autoreleasing *)rules
        {
            NSArray *failingRules = [self.rules filteredArrayUsingPredicate:[NSPredicate predicateWithBlock:^BOOL(id <NJOPasswordRule> rule, NSDictionary *bindings) {
                return [rule evaluateWithString:password];
            }]];

            if (rules) {
                *rules = failingRules;
            }

            return [failingRules count] == 0;

        }

2. 调用
        NSArray *failingRules = nil;
        if ([self.validator validatePassword:password failingRules:&failingRules]) {
            //
        }

### 效果图
（无）

### 备注
（无）
