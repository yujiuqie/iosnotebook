### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-25 | Alfred Jiang | - |

### 方案名称
时间 - 倒计时器的实现

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
倒计时 \ 计时器

### 需求场景
1. 倒计时

### 参考链接
（无）

### 详细内容

#####1. 方法定义
    + (void)countdownTime:(int32_t)startCount
            countHandler:(void(^)(int32_t currentCount,dispatch_source_t timer))handler
       completionHandler:(void(^)(void))endHandler
    {
        __block int timeout = startCount; //倒计时时间

        dispatch_queue_t queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
        dispatch_source_t _timer = dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER, 0, 0,queue);
        dispatch_source_set_timer(_timer,dispatch_walltime(NULL, 0),1.0*NSEC_PER_SEC, 0); //每秒执行

        dispatch_source_set_event_handler(_timer, ^{
            if(timeout<=0){ //倒计时结束，关闭
                dispatch_source_cancel(_timer);
                dispatch_async(dispatch_get_main_queue(), ^{
                    endHandler();
                });
            }else{

    //            var hours : Int32 = currentTime / (60 * 60)
    //            var minutes : Int32 = currentTime % 3600 / 60
    //            var seconds : Int32 = currentTime % 60

                dispatch_async(dispatch_get_main_queue(), ^{
                    //设置界面的按钮显示 根据自己需求设置
                    handler(timeout,_timer);

                });
                timeout--;

            }
        });

        dispatch_resume(_timer);
    }

#####2. 示例
    private var timer : dispatch_source_t?

    private func countTime(aTime : Int32)
    {
        if self.timer != nil
        {
            dispatch_source_cancel(self.timer)
        }

        REXOCTools.countdownTime(aTime, countHandler: { (currentTime : Int32, timer : dispatch_source_t?) -> Void in

            self.timer = timer

            var hours : Int32 = currentTime / (60 * 60)
            var minutes : Int32 = currentTime % 3600 / 60
            var seconds : Int32 = currentTime % 60

            self.endLabel.text = "\(hours) h \(minutes) m \(seconds) s"

            }) { () -> Void in
                self.endLabel.text = "End"
        }
    }


### 效果图
（无）

### 备注
（无）
