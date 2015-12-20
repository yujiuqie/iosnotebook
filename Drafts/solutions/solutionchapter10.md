### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-02 | Alfred Jiang | - |

### 方案名称
时间- 延时执行解决方案

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
延时执行 / 时间

### 需求场景
1. 部分需要等待的操作

### 参考链接
1. [iOS延时执行的几种方法](http://www.cnblogs.com/hanyis/p/3660051.html)

### 详细内容
1. 直接使用 performSelector

        - (void)checkRefreshCatalogViewData
        {
            [catalogView performSelector:@selector(refreshDataAfterFiveMinute) withObject:nil afterDelay:kRefreshCatalogViewDelayTime];
        }

        //对于代码中调用performSelector产生延时操作的代码，如果不是通过category方式定义，要在dealloc函数里面用cancelPreviousPerformRequestsWithTarget取消。因为不取消的话，如果页面在延时的时间内退出，将因为找不到执行函数而崩溃。

        - (void)dealloc
        {
            [NSObject cancelPreviousPerformRequestsWithTarget:self selector:@selector(refreshDataAfterFiveMinute) object:nil];
            [super dealloc];
        }

2. Block + performSelector
        @implementation NSObject (PerformBlockAfterDelay)

        - (void)performBlock:(void (^)(void))block
                  afterDelay:(NSTimeInterval)delay
        {
            block = [block copy];
            [self performSelector:@selector(fireBlockAfterDelay:)
                       withObject:block
                       afterDelay:delay];
        }

        - (void)fireBlockAfterDelay:(void (^)(void))block {
            block();
        }

        @end

3. GCD
        //Swift 解决方案
        func delay(delay:Double, closure:()->()) {
            dispatch_after(
                dispatch_time(
                    DISPATCH_TIME_NOW,
                    Int64(delay * Double(NSEC_PER_SEC))
                ),
                dispatch_get_main_queue(), closure)
        }

        //Objective-C 解决方案
        - void RunBlockAfterDelay(NSTimeInterval delay, void (^block)(void))
        {
            dispatch_after(dispatch_time(DISPATCH_TIME_NOW, NSEC_PER_SEC*delay),
                           dispatch_get_main_queue(), block);
        }

4. 用animation的completion参数 (不推荐)

5. 使用NSOperationQueue，在应用程序的下一个主循环执行 (不推荐)


### 效果图
（无）

### 备注
（无）
