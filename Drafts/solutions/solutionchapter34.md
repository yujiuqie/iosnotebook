### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-18 | Alfred Jiang | - |

### 方案名称
授权 - 使用 ClusterPrePermissions 更加友好的提示授权操作

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
通讯录 \ 相册 \ 地址 \ 授权

### 需求场景
1. 需要用户授权通讯录、相册、地址等信息时提前增加提示

### 参考链接
1. [GitHub](https://github.com/clusterinc/ClusterPrePermissions)

### 详细内容

使用方法

    ClusterPrePermissions *permissions = [ClusterPrePermissions sharedPermissions];
    [permissions showPhotoPermissionsWithTitle:@"Access your photos?"
                                       message:@"Your message here"
                               denyButtonTitle:@"Not Now"
                              grantButtonTitle:@"Give Access"
                             completionHandler:^(BOOL hasPermission,
                                                 ClusterDialogResult userDialogResult,
                                                 ClusterDialogResult systemDialogResult) {
                                 if (hasPermission) {
                                     // Continue with your code here
                                 } else {
                                      // Handle access not being available
                                 }
                             }];

### 效果图
（无）

### 备注
（无）
