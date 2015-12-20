### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-13 | Alfred Jiang | - |

### 方案名称
语法 - If not let - in Swift

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
optional \ ? \ ! \ if let

### 需求场景
1. 判断 optional 字段是否有效\无效时

### 参考链接
1. [Stacckoverflow - If not let in Swift](http://stackoverflow.com/questions/27412735/if-not-let-in-swift)

### 详细内容

正常的 if let 用法

    if let type = json.type  {

    } else {
        //There is no type in the root element
    }

if not let 实现

    func ifNotLet<T>(optional: T?, closure: @autoclosure () -> ()) -> T {
        switch optional {
        case .None:
            closure()
        case let .Some(value)
            return value
        }
    }

    let type = ifNotLet(json.type) {
        XCTFail("There is no type in the root element")
    }

### 效果图
（无）

### 备注
