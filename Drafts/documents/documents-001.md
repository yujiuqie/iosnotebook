
##### API接口文档参考链接
1. [新浪微盘——API接口说明](http://vdisk.weibo.com/developers/index.php?module=api&action=apidoc#authorize)

##### API接口示例

###### 示例 1 （新浪微盘——API接口说明）:

* API : /oauth2/access_token
* 功能 : OAuth2 的 access_token 接口
* 请求方法
        POST https://auth.sina.com.cn/oauth2/access_token
* 参数说明

| 参数  | 必选  | 类型 | 说明 |
|:-------------: |:---------------:| :-------------:| :-------------:|
| client_id | Yes | string | 申请应用时分配的 AppKey。 |
| client_secret | Yes | string | 申请应用时分配的 AppSecret。 |
| grant_type | Yes | string | 请求的类型，可以为authorization_code、refresh_token。 |

* grant_type为authorization_code时：

| 参数  | 必选  | 类型 | 说明 |
|:-------------: |:---------------:| :-------------:| :-------------:|
| client_id | Yes | string | 申请应用时分配的 AppKey。 |
| client_secret | Yes | string | 申请应用时分配的 AppSecret。 |

* grant_type为refresh_token时：

| 参数  | 必选  | 类型 | 说明 |
|:-------------: |:---------------:| :-------------:| :-------------:|
| client_id | Yes | string | 申请应用时分配的 AppKey。 |

* 返回结果

    失败
        {
            "code": "1090",
            "msg": "error message"
        }

    成功
        {
            "access_token": "ACCESS_TOKEN",
            "expires_in": 1234,
            "refresh_token": "REFRESH_TOKEN",
            "time_left": 1234,
            "uid": "UID"
        }

##### 建议
1. 对于时间相关字段，统一使用时间戳
2. 建议字段类型统一使用字符串类型，空值使用 "" 形式，避免传递 null 字段
