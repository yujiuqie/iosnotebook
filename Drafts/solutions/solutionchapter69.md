### 变更记录
| 序号 | 录入时间 | 录入人 | 备注 |
| -- | -- | -- | -- |
| 1 | 2015-04-03 | Alfred Jiang | - |

### 方案名称
文件 - 使用 SSZipArchive 实现文件的压缩和解压缩

### 方案类型（推荐 or 参考）
推荐方案

### 关键字
压缩 \ 解压缩 \ zip \ unzip

### 需求场景
1. 需要对文件进行压缩和解压缩操作时

### 参考链接
1. [SSZipArchive](https://github.com/soffes/ssziparchive)

### 详细内容

1. 将 SSZipArchive 文件加入工程
2. 引入 SSZipArchive.h 头文件
3. 添加 libz.dylib 库
4. 用法
        // Unzipping
        NSString *zipPath = @"path_to_your_zip_file";
        NSString *destinationPath = @"path_to_the_folder_where_you_want_it_unzipped";
        [SSZipArchive unzipFileAtPath:zipPath toDestination:destinationPath];

        // Zipping
        NSString *zippedPath = @"path_where_you_want_the_file_created";
        NSArray *inputPaths = [NSArray arrayWithObjects:
                               [[NSBundle mainBundle] pathForResource:@"photo1" ofType:@"jpg"],
                               [[NSBundle mainBundle] pathForResource:@"photo2" ofType:@"jpg"]
                               nil];
        [SSZipArchive createZipFileAtPath:zippedPath withFilesAtPaths:inputPaths];

##### Swift 使用实例

    var zipPath = NSBundle.mainBundle().pathForResource("TestArchive", ofType: "zip")
    var outputPath = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)[0] as String
    SSZipArchive.unzipFileAtPath(zipPath, toDestination: outputPath)

##### Objective-C 使用实例

    NSString *zipPath = [[NSBundle bundleForClass:[self class]] pathForResource:@"TestArchive" ofType:@"zip"];
    	NSString *outputPath = [self _cachesPath:@"Regular"];
    [SSZipArchive unzipFileAtPath:zipPath toDestination:outputPath delegate:self];


### 效果图
（无）

### 备注
