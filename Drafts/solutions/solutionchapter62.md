### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-31 | Alfred Jiang | - |

### 方案名称
UDID - 解决方案介绍与比较

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
UUID \ UDID \ 设备唯一标识符

### 需求场景
1. 需要设备唯一标识符的场景

### 参考链接
1. [IOS7开发～UDID解决方法](http://blog.csdn.net/lizhongfu2013/article/details/11982851)
2. [现有IOS设备唯一标示符的方案比较](http://kensou.blog.51cto.com/3495587/1249734)

### 详细内容

#####1. UDID
    [[UIDevice currentDevice] uniqueIdentfier]

iOS官方最早提供的UDID方案，根据某一公式，使用设备序列号、网卡地址等信息作为参数计算而来，iOS6之后该计算公式发生了改变。

该方法返回的结果在所有应用中都相同，并且卸载应用、刷机、还原设备均不会发生改变，是最为准确的设备唯一标示符。

iOS5之后，该方法被标记为废弃！最终，在2013年5月1号之后，AppStore禁止任何使用该方法的应用上架。

iOS7中对外公开的API中已经移除了该方法！

#####2. 网卡地址
通过Unix级别的API去获取Wifi的网卡地址。

该方法属于UDID替代方案中最为准确的一种，因为网卡地址不会因为刷机、还原设备而发生改变。故追求唯一性的厂商多选择此种方案！

在iOS7之后，应用已经无法获取网卡地址，所以该方案在iOS7中也已经被废弃。

#####3. OpenUDID
开源的一个UDID替代方案，原理是利用应用间的剪贴板共享和本地一些必要的缓存信息，让多个应用间共享一个UUID。

OpenUDID在官方废弃UDID接口之后，受到广泛的欢迎！可以说是现在大多数应用的UDID替代方法。

OpenUDID在刷机、还原设备后就会产生新的UDID，事实上，由于剪贴板的特殊性，如果所有使用了OpenUDID的应用被全部卸载之后，再次安装的应用取到的OpenUDID将会是一个全新的值！

iOS7中，不同组的应用（即不同厂商）的应用之间不再能共享剪贴板间的数据！

同组（即同一厂商）应用的定义为：Info.plist中关于软件唯一标示符的字段CFBundleIdentifier中的前两段标识符（例如com.mycompany）相同。

固在iOS7中，OpenUDID也将慢慢失去它的意义。

#####4. 保存在NSUserDefault中的UUID
在iOS5将UDID标为废弃之后，官方提供的替代方案。即使用CFUUIDCreate生成一个UUID，并将之保存在NSUserDefault中，用它作为设备标识符。在iOS6之后，苹果更推出NSUUID来替代CFUUIDCreate，但本质是一样的。

UUID每次都会生成一个新的字符串，也就是说应用被卸载之后，就会被认为是一个新的设备，更不用提刷机、还原设备了。

故基本无人采用UUID的方案。

#####5. 厂商唯一标识符identifierForVender
    [[UIDevice currentDevice] identifierForVender]

iOS6中推出的UDID替代方案，该方法对于同一厂商的应用返回相同的值，不同厂商所得到的值不同。

该方案刷机、还原设备后，获得值将会改变。同样注意的是：如果同一厂商安装的所有应用都被卸载后，新安装的同一厂商的应用同样也将获得新的值，而不是原来的值！

由于不能跨厂商，并且软件卸载后再安装有改变的可能性，该方案也并没有被广大开发商接受。

#####6. 广告标识符advertisingIdentifier <font color="red">(推荐方案)</font>
    [[ASIdentifierManager sharedManager] advertisingIdentifier];

iOS6中推出的另一款UDID替代方案，该方法对所有厂商的应用返回相同的值。同样提供的是另一个API，advertisingTrackingEnabled，该参数表示用户是否希望广告追踪被限定，但该参数仅仅是个布尔值，用于表示用户意愿，不影响advertisingIdentifier的读取。

该方法由于是官方提供的，并且所有厂商的应用取到的值相同，所以相对接受度好些，但是由于仅在iOS6上适用，所以更多人还是选择了OpenUDID的方案。

该方法刷机、还原设备后，获得的值将会改变。此外，用户如果通过设置->关于本机->广告->还原广告标识符，就可以重新生成一个新的值。

该方法是iOS7上目前官方允许的范畴内最为可接受的方案。

#####7. IMEI
iOS官方API无法获得IMEI，或者说禁止获取。故很少有人在iOS上去读取IMEI。但IMEI作为设备唯一标识符是最为准确的方法之一！不会随着刷机、还原设备而改变！

读取IMEI的应用将会被AppStore拒绝！

同样类似的方案有蓝牙地址、iOS设备序列号（SerialNumbedr）等等。

### 效果图
（无）

### 备注
（无）


