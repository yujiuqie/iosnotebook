### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-26 | Alfred Jiang | - |

### 方案名称
应用间通信 - 实现应用间互相调用与数据传递

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
调用其他应用 \ 应用间调用

### 需求场景
1. 需要调用非系统应用时

### 参考链接
1. [iOS开发长文--通讯录、蓝牙、内购、GameCenter、iCloud、Passbook系统服务开发汇总](http://www.cocoachina.com/ios/20150129/11068.html)

### 详细内容

假设你现在开发了一个应用A，如果用户机器上已经安装了此应用，并且在应用B中希望能够直接打开A。

1. 在plist文件中添加URL types节点并配置URL Schemas作为具体协议，配置URL identifier作为这个URL的唯一标识，确保应用A已经配置了Url Types;

![images/BundleTypeName.png](images/openURLSchemes.png)

2. 使用openURL方法打开应用B
        - (IBAction)thirdPartyApplicationClick:(UIButton *)sender {
            NSString *url=@"cmj://myparams";
            [self openUrl:url];
        }

        -(void)openUrl:(NSString *)urlStr{
            //注意url中包含协议名称，iOS根据协议确定调用哪个应用，例如发送邮件是“sms://”其中“//”可以省略写成“sms:”(其他协议也是如此)
            NSURL *url=[NSURL URLWithString:urlStr];
            UIApplication *application=[UIApplication sharedApplication];
            if(![application canOpenURL:url]){
                NSLog(@"无法打开\"%@\"，请确保此应用已经正确安装.",url);
                return;
            }
            [[UIApplication sharedApplication] openURL:url];
        }

3. 在应用B的 Appdelegate 中接受传递参数并打开
        -(BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation{
            NSString *str=[NSString stringWithFormat:@"url:%@,source application:%@,params:%@",url,sourceApplication,[url host]];
            NSLog(@"%@",str);
            return YES;//是否打开
        }

### 效果图
（无）

### 备注
