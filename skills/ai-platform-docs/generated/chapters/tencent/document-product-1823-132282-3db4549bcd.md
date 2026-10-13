<!-- Official source: https://cloud.tencent.com/document/product/1823/132282 -->
<!-- Source SHA-256: 7b9b4e9e41dd830864638b93401d9a3df41560b71c016cd1f542695471caeed3 -->

# 请求结构

官方来源：https://cloud.tencent.com/document/product/1823/132282
最近更新时间：2026-05-29 10:58:22

## 1. 服务地址

API 支持就近地域接入，本产品就近地域接入域名为 tokenhub.tencentcloudapi.com ，也支持指定地域域名访问，例如广州地域的域名为 tokenhub.ap-guangzhou.tencentcloudapi.com 。

推荐使用就近地域接入域名。根据调用接口时客户端所在位置，会自动解析到**最近的**某个具体地域的服务器。例如在广州发起请求，会自动解析到广州的服务器，效果和指定 tokenhub.ap-guangzhou.tencentcloudapi.com 是一致的。

**注意：对时延敏感的业务，建议指定带地域的域名。**

**注意：域名是 API 的接入点，并不代表产品或者接口实际提供服务的地域。产品支持的地域列表请在调用方式/公共参数文档中查阅，接口支持的地域请在接口文档输入参数中查阅。**

目前支持的域名列表为：

| 接入地域 | 域名 |
|----------|------|
| 就近地域接入（推荐，只支持非金融区）| tokenhub.tencentcloudapi.com |
| 华南地区（广州） | tokenhub.ap-guangzhou.tencentcloudapi.com |
| 华东地区（上海） | tokenhub.ap-shanghai.tencentcloudapi.com |
| 华东地区（南京） | tokenhub.ap-nanjing.tencentcloudapi.com |
| 华北地区（北京） | tokenhub.ap-beijing.tencentcloudapi.com |
| 西南地区（成都） | tokenhub.ap-chengdu.tencentcloudapi.com |
| 西南地区（重庆） | tokenhub.ap-chongqing.tencentcloudapi.com |
| 港澳台地区（中国香港） | tokenhub.ap-hongkong.tencentcloudapi.com |
| 亚太东南（新加坡） | tokenhub.ap-singapore.tencentcloudapi.com |
| 亚太东南（雅加达） | tokenhub.ap-jakarta.tencentcloudapi.com |
| 亚太东南（曼谷） | tokenhub.ap-bangkok.tencentcloudapi.com |
| 亚太东北（首尔） | tokenhub.ap-seoul.tencentcloudapi.com |
| 亚太东北（东京） | tokenhub.ap-tokyo.tencentcloudapi.com |
| 美国东部（弗吉尼亚） | tokenhub.na-ashburn.tencentcloudapi.com |
| 美国西部（硅谷） | tokenhub.na-siliconvalley.tencentcloudapi.com |
| 南美地区（圣保罗） | tokenhub.sa-saopaulo.tencentcloudapi.com |
| 欧洲地区（法兰克福） | tokenhub.eu-frankfurt.tencentcloudapi.com |

**注意：由于[金融区](https://cloud.tencent.com/document/product/304/2766)和非金融区是隔离不互通的，因此当访问金融区服务时（公共参数 Region 为金融区地域），需要同时指定带金融区地域的域名，最好和 Region 的地域保持一致。**

| 金融区接入地域 | 金融区域名 |
|----------|------|
| 华东地区（上海金融）| tokenhub.ap-shanghai-fsi.tencentcloudapi.com |
| 华南地区（深圳金融）| tokenhub.ap-shenzhen-fsi.tencentcloudapi.com |

## 2. 通信协议

腾讯云 API 的所有接口均通过 HTTPS 进行通信，提供高安全性的通信通道。

## 3. 请求方法

支持的 HTTP 请求方法:

* POST（推荐）
* GET

POST 请求支持的 Content-Type 类型：

* application/json（推荐），必须使用签名方法 v3（TC3-HMAC-SHA256）。
* application/x-www-form-urlencoded，必须使用签名方法 v1（HmacSHA1 或 HmacSHA256）。
* multipart/form-data（仅部分接口支持），必须使用签名方法 v3（TC3-HMAC-SHA256）。

GET 请求的请求包大小不得超过32KB。POST 请求使用签名方法 v1（HmacSHA1、HmacSHA256）时不得超过1MB。POST 请求使用签名方法 v3（TC3-HMAC-SHA256）时支持10MB。

## 4. 字符编码

均使用`UTF-8`编码。
