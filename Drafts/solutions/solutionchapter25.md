### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-04 | Alfred Jiang | - |

### 方案名称
动画 - Core Animation 之 CABaseAnimation

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
动画 \ Core Animation \ CALayer \ CAAnimation \ CAPropertyAnimation \ CABaseAnimation \ CAKeyframeAnimation \ CATransition \ CAAnimationGroup

### 需求场景
1. 使用 Core Animation 实现动画需求

### 参考链接
1. [CABasicAnimation的基本使用方法（移动·旋转·放大·缩小）](http://blog.csdn.net/iosevanhuang/article/details/14488239)
2. [CABasicAnimation animationWithKeyPath 一些规定的值](http://www.cnblogs.com/pengyingh/articles/2379631.html)

### 详细内容
#####1.继承关系
@interface CAAnimation : NSObject &lt;NSCoding, NSCopying, CAMediaTiming, CAAction>

@interface CAPropertyAnimation : CAAnimation

@interface CABasicAnimation : CAPropertyAnimation

@interface CAKeyframeAnimation : CAPropertyAnimation

@interface CATransition : CAAnimation

@interface CAAnimationGroup : CAAnimation

#####2.使用说明
######1. 定义一个 CABasicAnimation
    // 指定position属性
    CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"position"];

######2. 设定动画属性


 | 属性 | 说明 |
 | -- | -- |
 | duration | 动画时长（秒为单位） |
 | repeatCount | 重复次数。永久重复的话设置为HUGE_VALF |
 | beginTime | 指定动画开始时间。从开始指定延迟几秒执行的话，请设置为「CACurrentMediaTime() + 秒数」的形式 |
 | timingFunction | 设定动画的速度变化 |
 | autoreverses | 动画结束时是否执行逆动画 |

    animation.duration = 2.5; // 动画持续时间
    animation.repeatCount = 1; // 不重复
    animation.beginTime = CACurrentMediaTime() + 2; // 2秒后执行
    animation.autoreverses = YES; // 结束后执行逆动画

    // 动画先加速后减速
    animation.timingFunction = [CAMediaTimingFunction functionWithName: kCAMediaTimingFunctionEaseInEaseOut];

######3. 设定动画的开始帧和结束帧

 设定动画开始和结束帧时的状态。设定的值会变为KeyPath所指定的属性的值。


 | 属性 | 说明 |
 | -- | -- |
 | fromValue | 开始值 |
 | toValue | 终了值（絶対値） |
 | byValue | 终了值（相对值） |

    // 指定position属性（移动）
    CABasicAnimation *animation =
        [CABasicAnimation animationWithKeyPath:@"position"];

    ・・・

    // 设定动画起始帧和结束帧
    animation.fromValue = [NSValue valueWithCGPoint:CGPointMake(0, 0)]; // 起始点
    animation.toValue = [NSValue valueWithCGPoint:CGPointMake(320, 480)]; // 终了点

######4. 添加动画
    [myView.layer addAnimation:animation forKey:@"move-layer"];

######5. 动画结束恢复初始状态（可选）
    // 动画终了后不返回初始状态
    animation.removedOnCompletion = NO;
    animation.fillMode = kCAFillModeForwards;

#####2.使用举例

######1. 移动动画
    /* 移动 */
    CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"position"];

    // 动画选项的设定
    animation.duration = 2.5; // 持续时间
    animation.repeatCount = 1; // 重复次数

    // 起始帧和终了帧的设定
    animation.fromValue = [NSValue valueWithCGPoint:myView.layer.position]; // 起始帧
    animation.toValue = [NSValue valueWithCGPoint:CGPointMake(320, 480)]; // 终了帧

    // 添加动画
    [myView.layer addAnimation:animation forKey:@"move-layer"];

######2. 旋转动画
    /* 旋转 */

    // 对Y轴进行旋转（指定Z轴的话，就和UIView的动画一样绕中心旋转）
    CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"transform.rotation.y"];

    // 设定动画选项
    animation.duration = 2.5; // 持续时间
    animation.repeatCount = 1; // 重复次数

    // 设定旋转角度
    animation.fromValue = [NSNumber numberWithFloat:0.0]; // 起始角度
    animation.toValue = [NSNumber numberWithFloat:2 * M_PI]; // 终止角度

    // 添加动画
    [myView.layer addAnimation:animation forKey:@"rotate-layer"];

######3. 缩放动画
    /* 放大缩小 */

    // 设定为缩放
    CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"transform.scale"];

    // 动画选项设定
    animation.duration = 2.5; // 动画持续时间
    animation.repeatCount = 1; // 重复次数
    animation.autoreverses = YES; // 动画结束时执行逆动画

    // 缩放倍数
    animation.fromValue = [NSNumber numberWithFloat:1.0]; // 开始时的倍率
    animation.toValue = [NSNumber numberWithFloat:2.0]; // 结束时的倍率

    // 添加动画
    [myView.layer addAnimation:animation forKey:@"scale-layer"];

######4. 组合动画
    /* 动画1（在X轴方向移动） */
    CABasicAnimation *animation1 =
        [CABasicAnimation animationWithKeyPath:@"transform.translation.x"];

    // 终点设定
    animation1.toValue = [NSNumber numberWithFloat:80];; // 終点


    /* 动画2（绕Z轴中心旋转） */
    CABasicAnimation *animation2 =
        [CABasicAnimation animationWithKeyPath:@"transform.rotation.z"];

    // 设定旋转角度
    animation2.fromValue = [NSNumber numberWithFloat:0.0]; // 开始时的角度
    animation2.toValue = [NSNumber numberWithFloat:4 * M_PI]; // 结束时的角度


    /* 动画组 */
    CAAnimationGroup *group = [CAAnimationGroup animation];

    // 动画选项设定
    group.duration = 3.0;
    group.repeatCount = 1;

    // 添加动画
    group.animations = [NSArray arrayWithObjects:animation1, animation2, nil];
    [myView.layer addAnimation:group forKey:@"move-rotate-layer"];

######5. 捕获动画开始时和终了时的事件
    /* 移动 */
    CABasicAnimation *animation = [CABasicAnimation animationWithKeyPath:@"transform.translation.y"];
    animation.delegate = self; // 指定委托对象

    // 设定动画选项
    animation.duration = 2.5; // 动画时长
    animation.repeatCount = 1; // 重复次数

    // 终点设定
    animation.toValue = [NSNumber numberWithFloat:100];; // 终点

    // 添加动画
    [myView.layer addAnimation:animation forKey:@"move-layer"];

    ・・・

    /**
     * 动画开始时
     */
    - (void)animationDidStart:(CAAnimation *)theAnimation
    {
        NSLog(@"begin");
    }

    /**
     * 动画结束时
     */
    - (void)animationDidStop:(CAAnimation *)theAnimation finished:(BOOL)flag
    {
        NSLog(@"end");
    }

######6. 几个可以用来实现热门APP应用PATH中menu效果的几个方法

    +(CABasicAnimation *)opacityForever_Animation:(float)time ／／永久闪烁的动画
    {
        CABasicAnimation *animation=[CABasicAnimation animationWithKeyPath:@"opacity"];
        animation.fromValue=[NSNumber numberWithFloat:1.0];
        animation.toValue=[NSNumber numberWithFloat:0.0];
        animation.autoreverses=YES;
        animation.duration=time;
        animation.repeatCount=FLT_MAX;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        return animation;
    }

    +(CABasicAnimation *)opacityTimes_Animation:(float)repeatTimes durTimes:(float)time; ／／有闪烁次数的动画
    {
        CABasicAnimation *animation=[CABasicAnimation animationWithKeyPath:@"opacity"];
        animation.fromValue=[NSNumber numberWithFloat:1.0];
        animation.toValue=[NSNumber numberWithFloat:0.4];
        animation.repeatCount=repeatTimes;
        animation.duration=time;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        animation.timingFunction=[CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseIn];
        animation.autoreverses=YES;
        return  animation;
    }

    +(CABasicAnimation *)moveX:(float)time X:(NSNumber *)x ／／横向移动
    {
        CABasicAnimation *animation=[CABasicAnimation animationWithKeyPath:@"transform.translation.x"];
        animation.toValue=x;
        animation.duration=time;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        return animation;
    }

    +(CABasicAnimation *)moveY:(float)time Y:(NSNumber *)y ／／纵向移动
    {
        CABasicAnimation *animation=[CABasicAnimation animationWithKeyPath:@"transform.translation.y"];
        animation.toValue=y;
        animation.duration=time;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        return animation;
    }

    +(CABasicAnimation *)scale:(NSNumber *)Multiple
                         orgin:(NSNumber *)orginMultiple
                      durTimes:(float)time
                           Rep:(float)repeatTimes ／／缩放
    {
        CABasicAnimation *animation=[CABasicAnimation animationWithKeyPath:@"transform.scale"];
        animation.fromValue=orginMultiple;
        animation.toValue=Multiple;
        animation.duration=time;
        animation.autoreverses=YES;
        animation.repeatCount=repeatTimes;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        return animation;
    }

    +(CAAnimationGroup *)groupAnimation:(NSArray *)animationAry
                               durTimes:(float)time
                                    Rep:(float)repeatTimes ／／组合动画
    {
        CAAnimationGroup *animation=[CAAnimationGroup animation];
        animation.animations=animationAry;
        animation.duration=time;
        animation.repeatCount=repeatTimes;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        return animation;
    }

    +(CAKeyframeAnimation *)keyframeAniamtion:(CGMutablePathRef)path
                                     durTimes:(float)time
                                          Rep:(float)repeatTimes ／／路径动画
    {
        CAKeyframeAnimation *animation=[CAKeyframeAnimation animationWithKeyPath:@"position"];
        animation.path=path;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        animation.timingFunction=[CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseIn];
        animation.autoreverses=NO;
        animation.duration=time;
        animation.repeatCount=repeatTimes;
        return animation;
    }

    +(CABasicAnimation *)movepoint:(CGPoint )point ／／点移动
    {
        CABasicAnimation *animation=[CABasicAnimation animationWithKeyPath:@"transform.translation"];
        animation.toValue=[NSValue valueWithCGPoint:point];
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        return animation;
    }

    +(CABasicAnimation *)rotation:(float)dur
                           degree:(float)degree
                        direction:(int)direction
                      repeatCount:(int)repeatCount ／／旋转
    {
        CATransform3D rotationTransform  = CATransform3DMakeRotation(degree, 0, 0,direction);
        CABasicAnimation* animation;
        animation = [CABasicAnimation animationWithKeyPath:@"transform"];
        animation.toValue= [NSValue valueWithCATransform3D:rotationTransform];
        animation.duration= dur;
        animation.autoreverses= NO;
        animation.cumulative= YES;
        animation.removedOnCompletion=NO;
        animation.fillMode=kCAFillModeForwards;
        animation.repeatCount= repeatCount;
        animation.delegate= self;
        return animation;
    }

### 效果图
（无）

### 备注
（无）
