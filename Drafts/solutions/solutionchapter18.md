### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-03-03 | Alfred Jiang | - |

### 方案名称
语法 - 使用字面量

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
字面量 \ 字面值

### 需求场景
1. 代码可读性更强，看着简洁，减少代码冗余

### 参考链接
1. [IOS使用字面值](http://kingxl.cn/2015/01/11/ios-literal/)
2. [字面量转换](http://swifter.tips/literal/)
3. [GitHub](https://github.com/mattt/Literally)

### 详细内容
#####1. Swift 解决方案

#####NSString

    let aString = "Hello"

#####Number

    let aNumber : NSNumber = 3
    let aBool : NSNumber = true

#####NSArray

    let anArray = [1,2,3]

#####Dictionary

    let aDictionary = ["key1": "value1", "key2": "value2"]

Swift 为我们提供了一组非常有意思的接口，用来将字面量转换为特定的类型。对于那些实现了字面量转换接口的类型，在提供字面量赋值的时候，就可以简单地按照接口方法中定义的规则“无缝对应”地转换为这些类型。这些接口包括了各个原生的字面量，它们是：

ArrayLiteralConvertible

BooleanLiteralConvertible

CharacterLiteralConvertible

DictionaryLiteralConvertible

ExtendedGraphemeClusterLiteralConvertible

FloatLiteralConvertible

NilLiteralConvertible

IntegerLiteralConvertible

StringLiteralConvertible

StringInterpolationConvertible

用法举例：

通常通过 NSString 定义一个 NSURL 的方法如下

    let url = NSURL(string: "http://swifter.tips")

使用 StringLiteralConvertible 构造一个 NSURL 的 extension

    extension NSURL: StringLiteralConvertible {
        public class func
            convertFromStringLiteral(value: String) -> Self
        {
            return self(string: value)
        }

        public class func
            convertFromExtendedGraphemeClusterLiteral(value: String) -> Self
        {
            return self(string: value)
        }
    }

那么我们现在可以直接使用如下方式直接赋值 NSString 生成 NSURL

    let url: NSURL = "http://swifter.tips"

#####2. Objective-C 解决方案

#####NSString

    NSString *str = [[NSString alloc] initWithFormat:@"%@",@"Hello World"];

    //---->字面值如下

    NSString *str = @"Hello World";

#####Number

    NSNumber *someNumber = [NSNumber numberWithInt:1];

    //---->字面值如下

    NSNumber *intNumber = @1;
    NSNumber *floatNumber = @2.5f;
    NSNumber *doubleNumber = @3.14159;
    NSNumber *boolNumber = @YES;
    NSNumber *charNumber = @'a';

#####NSArray
    NSArray *animals =[NSArray arrayWithObjects:@"cat", @"dog", @"mouse", @"badger", nil];

    //---->字面值如下

    NSArray *animals = @[@"cat", @"dog", @"mouse", @"badger"];

    NSString *dog = [animals objectAtIndex:1];

    //---->通过字面值取数据

    NSString *dog = animals[1];

    //可变的话可以直接设置新值
    [mutableArray replaceObjectAtIndex:1 withObject:@"dog"];

    //---->字面值设置值

    mutableArray[1] = @"dog";


    NSString *str1;
    NSString *str2 = @"1";
    NSString *str3 = @"1";

    //插入空数据会抛出异常
    NSArray *arr = @[str1,str2,str3];

    //reason: '*** -[__NSPlaceholderArray initWithObjects:count:]: attempt to insert nil object from objects[0]'

    //这种方式不会抛异常，但是数组会收到第一个nil就终止了。所以采用字面值形式会得到错误提示。
    NSArray *arr = [NSArray arrayWithObjects:str1,str2,str3, nil];
    NSLog(@"arr.count=%d",arr.count); //0
    NSLog(@"arr.first=%@",arr.firstObject);  //null

#####Dictionary
    NSDictionary *personData =[NSDictionary dictionaryWithObjectsAndKeys:@"Kevin", @"firstName",@"Jin", @"lastName",[NSNumber numberWithInt:25], @"age", nil];

    //---->字面值如下

    NSDictionary *personData = @{@"firstName" : @"Kevin",@"lastName" : @"Jin", @"age" : @25};


    NSString *str1;
    NSString *str2 = @"1";
    NSString *str3 = @"1";
    //和数组一样，value不能有nil ，否则就会抛出异常。
    NSDictionary *dic =@{@"str1":str1,@"str2":str2,@"str3":str3};

    //reason: '*** -[__NSPlaceholderDictionary initWithObjects:forKeys:count:]: attempt to insert nil object from objects[0]'

    //不会提示你错误
    NSDictionary *dic = [NSDictionary dictionaryWithObjectsAndKeys:str1,@"str2",str2,@"str2",str3,@"str3", nil];
    NSLog(@"dic.count=%d",dic.count); //0

    //取值
    NSString *lastName = [personData objectForKey:@"lastName"];

    //---->字面值取值

    NSString *lastName = personData[@"lastName"];

    //可变的话可以这样设置新值
    [mutableDictionary setObject:@"Galloway" forKey:@"lastName"];

    //---->字面值设置值

    mutableDictionary[@"lastName"] = @"Galloway";


### 效果图
（无）

### 备注
访问的时候数组采用下标方式，字典直接通过Key来取值，需要注意的就是数组和字典中不能插入nil，否则会抛出异常。

以下为Github上的常用 Swift 字面量转换例子

    // Literally.swift
    //
    // Copyright (c) 2014 Mattt Thompson (http://mattt.me)
    //
    // Permission is hereby granted, free of charge, to any person obtaining a copy
    // of this software and associated documentation files (the "Software"), to deal
    // in the Software without restriction, including without limitation the rights
    // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    // copies of the Software, and to permit persons to whom the Software is
    // furnished to do so, subject to the following conditions:
    //
    // The above copyright notice and this permission notice shall be included in
    // all copies or substantial portions of the Software.
    //
    // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    // THE SOFTWARE.

    // MARK: - Foundation -

    import Foundation

    // MARK: NSCharacterSet

    extension NSCharacterSet: ArrayLiteralConvertible {
        public class func convertFromArrayLiteral(characters: Character...) -> Self {
            return self(charactersInString: join("", characters.map({String($0)})))
        }
    }

    extension NSCharacterSet: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(charactersInString: value)
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(charactersInString: value)
        }
    }

    // MARK: NSExpression

    extension NSExpression: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(format: value, argumentArray: [])
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(format: value, argumentArray: [])
        }
    }

    // MARK: NSIndexPath

    extension NSIndexPath: ArrayLiteralConvertible {
        public class func convertFromArrayLiteral(indexes: Int...) -> Self {
            return self(indexes: indexes, length: indexes.count)
        }
    }

    // MARK: NSIndexSet

    extension NSIndexSet: ArrayLiteralConvertible {
        public class func convertFromArrayLiteral(indexes: Int...) -> Self {
            var mutableIndexSet = NSMutableIndexSet()
            for index in indexes {
                mutableIndexSet.addIndex(index)
            }

            return self(indexSet: mutableIndexSet)
        }
    }

    // MARK: NSNull

    extension NSNull: NilLiteralConvertible {
        public class func convertFromNilLiteral() -> Self {
            return self()
        }
    }

    // MARK: NSOrderedSet

    extension NSOrderedSet: ArrayLiteralConvertible {
        public class func convertFromArrayLiteral(elements: AnyObject...) -> Self {
            return self(array: elements)
        }
    }

    // MARK: NSPredicate

    extension NSPredicate: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(format: value, argumentArray: [])
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(format: value, argumentArray: [])
        }
    }

    // MARK: NSRegularExpression

    extension NSRegularExpression: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(pattern: value, options: nil, error: nil)
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(pattern: value, options: nil, error: nil)
        }
    }

    // MARK: NSScanner

    extension NSScanner: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(string: value)
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(string: value)
        }
    }

    // MARK: NSSet

    extension NSSet: ArrayLiteralConvertible {
        public class func convertFromArrayLiteral(elements: AnyObject...) -> Self {
            return self(array: elements)
        }
    }

    // MARK: NSTimeZone

    extension NSTimeZone: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(name: value)
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(name: value)
        }
    }

    // MARK: NSURL

    extension NSURL: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(string: value)
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(string: value)
        }
    }

    // MARK: - UIKit -

    #if os(iOS)

    import UIKit

    // MARK: UIColor

    extension UIColor: IntegerLiteralConvertible {
        public class func convertFromIntegerLiteral(value: IntegerLiteralType) -> Self {
            let red = CGFloat((value & 0xFF0000) >> 16) / 255.0
            let green = CGFloat((value & 0x00FF00) >> 8) / 255.0
            let blue = CGFloat(value & 0x0000FF) / 255.0
            let alpha = CGFloat(1.0)

            return self(red: red, green: green, blue: blue, alpha: alpha)
        }
    }

    // MARK: UIImage

    extension UIImage: StringLiteralConvertible {
        typealias ExtendedGraphemeClusterLiteralType = StringLiteralType

        public class func convertFromExtendedGraphemeClusterLiteral(value: StringLiteralType) -> Self {
            return self(named: value)
        }

        public class func convertFromStringLiteral(value: StringLiteralType) -> Self {
            return self(named: value)
        }
    }

    #endif

    // MARK: - AppKit -

    #if os(OSX)

    import Cocoa

    extension NSColor: IntegerLiteralConvertible {
        public class func convertFromIntegerLiteral(value: IntegerLiteralType) -> Self {
            let red = CGFloat((value & 0xFF0000) >> 16) / 255.0
            let green = CGFloat((value & 0x00FF00) >> 8) / 255.0
            let blue = CGFloat(value & 0x0000FF) / 255.0
            let alpha = CGFloat(1.0)

            return self(red: red, green: green, blue: blue, alpha: alpha)
        }
    }

    #endif
