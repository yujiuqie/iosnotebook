### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-18 | Alfred Jiang | - |

### 方案名称
AppDelegate - IOS APP LAUNCH OPTION

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
ApplicationDelegate \ didFinishLaunchingWithOptions \ 应用启动 \ AppDelegate

### 需求场景
1. 需要对应用启动进行类别区分时

### 参考链接
1. [UIApplicationDelegate launch Options](http://nshipster.com/launch-options/)

### 详细内容

iOS 程序启动时总会调用application:didFinishLaunchingWithOptions:，其中第二个参数launchOptions为NSDictionary类型的对象，里面存储有此程序启动的原因。

launchOptions中的可能键值见UIApplication Class Reference的Launch Options Keys节 。

若用户直接启动，lauchOptions内无数据;

若由其他应用程序通过openURL:启动，则UIApplicationLaunchOptionsURLKey对应的对象为启动URL（NSURL）,UIApplicationLaunchOptionsSourceApplicationKey对应启动的源应用程序的bundle ID (NSString)；

若由本地通知启动，则UIApplicationLaunchOptionsLocalNotificationKey对应的是为启动应用程序的的本地通知对象(UILocalNotification)；

若由远程通知启动，则UIApplicationLaunchOptionsRemoteNotificationKey对应的是启动应用程序的的远程通知信息userInfo（NSDictionary）；

其他key还有UIApplicationLaunchOptionsAnnotationKey,UIApplicationLaunchOptionsLocationKey,
UIApplicationLaunchOptionsNewsstandDownloadsKey。

如果要在启动时，做出一些区分，那就需要在下面的代码做处理。
```
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    NSURL *url = [options objectForKey:UIApplicationLaunchOptionsURLKey];
    if(url)
    {
    }
    NSString *bundleId = [options objectForKey:UIApplicationLaunchOptionsSourceApplicationKey];
    if(bundleId)
    {
    }
    UILocalNotification * localNotify = [options objectForKey:UIApplicationLaunchOptionsLocalNotificationKey];
    if(localNotify)
    {
    }
    NSDictionary * userInfo = [options objectForKey:UIApplicationLaunchOptionsRemoteNotificationKey];
    if(userInfo)
    {
    }
}
```

### 效果图
（无）

### 备注
（无）
