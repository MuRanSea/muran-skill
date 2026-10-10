<!-- Official source: https://klingai.com/document-api/guides/get-started/quick-start.md -->
<!-- Source SHA-256: 316c5bea49aa08341a60fdcd9dfa40e9a8776346058818045058f96fd390f7d2 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速入门

> 来源: https://klingai.com/document-api/guides/get-started/quick-start
> 语言: zh
> 当前 Tab: 快速入门
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

以下为新系统 API 服务的详细使用指引，建议您参考步骤快速完成接入。若有疑问，可随时联系技术支持团队。

## Step 1: 进入可灵AI 开发者平台

- 访问 https://klingai.com/dev

|                                     可灵AI 开发者平台                                      |
| :----------------------------------------------------------------------------------------: |
| ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/home-zh.70df5415e1a4cdc2.png) |

## Step 2: 资源包购买

我们现已全面开放视频生成和图像生成两种 API 资源包的购买渠道。您可以根据实际调用需求选择不同的套餐。此外，为了方便您快速接入，我们还提供了【试用资源包】以供联调测试。详情请访问下单页面进行查看。

- 视频生成 API 购买入口：https://klingai.com/dev/pricing?scrollTo=video
- 图像生成 API 购买入口：https://klingai.com/dev/pricing?scrollTo=image

|                                       视频生成 API 资源包                                        |                                       图像生成 API 资源包                                        |
| :----------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------: |
| ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/home-video-zh.a2986bbf57d22eca.png) | ![](https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/home-image-zh.db68ae2f858ad76a.png) |

## Step 3: 登录开发者控制台

1. 访问 https://klingai.com/dev/api-key

|                                        开发者控制台                                        |
| :----------------------------------------------------------------------------------------: |
| ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/list-zh.906efffb6f70bc0d.png) |

2. 使用您的手机号或快手扫码登录，控制台账号与可灵AI web端账号一致

## Step 4: 进行接口鉴权

获取 API Key

创建 API 密钥并命名管理，支持一键复制 API Key

| 新建 API 密钥名称                                                                                       | 一键复制API Key                                                                                              | 支持启用/禁用、编辑名称、删除                                                                         |
| :------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| ![](https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/rename-zh.e6bd11d32ac78cb5.png) | ![](https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/images/copy-zh.98938e404cfe67ab.png) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/list-zh.906efffb6f70bc0d.png) |

1、打开可灵 AI 控制台并登录

2、点击「**+ 新建 API Key**」按钮

3、在弹窗中为 **API Key** 命名并确认，此时页面会显示 **API Key**

4、复制获取 **API Key**；API Key仅显示一次，请注意妥善保管

5、将 **API Key** 组装成 **Authorization**，填写到 **Request Header** 里

- 组装方式：**Authorization = "Bearer XXX"**，其中 XXX 填写第一步获取的 **API Key**（注意Bearer跟XXX之间有空格）

## Step 5: 调用 API 服务

> API 调用域名：`https://api-beijing.klingai.com`

## Step 6: 控制台查看信息

| 查看API 调用量&趋势                                                                     | 查看资源包消耗进度&趋势                                                                 | 查看资源包账单明细                                                                      | 查看额度账单明细                                                                        |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| ![](https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/1-zh.0797d1a83ea443ba.png) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/2-zh.25a93ef0bbeb8ab6.png) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/3-zh.63d730eac98a7e66.png) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/4-zh.9d8dbf54f5220af7.png) |
