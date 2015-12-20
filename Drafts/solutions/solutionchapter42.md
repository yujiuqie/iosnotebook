### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-20 | Alfred Jiang | - |

### 方案名称
音视频 - 使用 POVoiceHUD 实现语音录制

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
Voice \ 语音录制 \ POVoiceHUD \ 音频

### 需求场景
1. 需要实现语音录制需求时

### 参考链接
1. [GitHub](https://github.com/polatolu/POVoiceHUD)

### 详细内容

#####1. 引入以下 framework

    AVFoundation.framework
    AudioToolbox.framework
    CoreGraphics.framework
    QartzCore.framework

#####2. 在 ViewDidLoad 中实例化

    self.voiceHud = [[POVoiceHUD alloc] initWithParentView:self.view];
    self.voiceHud.title = @"Speak Now";

    [self.voiceHud setDelegate:self];
    [self.view addSubview:self.voiceHud];

#####3. 在需要录制的地方调用下面的代码

    [self.voiceHud startForFilePath:[NSString stringWithFormat:@"%@/Documents/MySound.caf", NSHomeDirectory()]];

### 效果图
（无）

### 备注
（无）
