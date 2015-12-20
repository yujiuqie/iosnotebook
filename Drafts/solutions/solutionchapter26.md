### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-04 | Alfred Jiang | - |

### 方案名称
动画 - Core Animation 之 Key Path

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
Core Animation \ CAAnimation \ CALayer

### 需求场景
1. CAAnimation 、 CALayer 实现动画需求时 setValue:forKeyPath: 和 valueForKeyPath: 支持的 Key Path 速查

### 参考链接
1. [Core Animation Programming Guide](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/CoreAnimation_guide/Key-ValueCodingExtensions/Key-ValueCodingExtensions.html#//apple_ref/doc/uid/TP40004514-CH12-SW2)

### 详细内容

表 1  支持的 Key Path 类型

| C type | Wrapping class |
| -- | -- |
| CGPoint | NSValue |
| CGSize | NSValue |
| CGRect | NSValue |
| CATransform3D | NSValue |
| CGAffineTransform | NSAffineTransform (OS X only) |

表 2  CATransform3D key paths

| Field Key Path | Description |
| -- | -- |
| rotation.x | The rotation, in radians, in the x axis. |
| rotation.y | The rotation, in radians, in the y axis. |
| rotation.z | The rotation, in radians, in the z axis. |
| rotation | The rotation, in radians, in the z axis. This is identical to setting the rotation.z field. |
| scale.x | Scale factor for the x axis. |
| scale.y | Scale factor for the y axis. |
| scale.z | Scale factor for the z axis. |
| scale | Average of all three scale factors. |
| translation.x | Translate in the x axis. |
| translation.y | Translate in the y axis. |
| translation.z | Translate in the z axis. |
| translation | Translate in the x and y axis. Value is an NSSize or CGSize. |
    [myLayer setValue:[NSNumber numberWithFloat:10.0] forKeyPath:@"transform.translation.x"];

表 3  CGPoint Key Paths

| Structure Field | Description |
| -- | -- |
| x | The x component of the point. |
| y | The y component of the point. |

表 4  CGSize Key Paths

| Structure Field | Description |
| -- | -- |
| width | The width component of the size. |
| height | The height component of the size. |

表 5  CGRect Key Paths

| Structure Field | Description |
| -- | -- |
| origin | The origin of the rectangle as a CGPoint. |
| origin.x | The x component of the rectangle origin. |
| origin.y | The y component of the rectangle origin. |
| size | The size of the rectangle as a CGSize. |
| size.width | The width component of the rectangle size. |
| size.height | The height component of the rectangle size. |

### 效果图
（无）

### 备注
（无）
