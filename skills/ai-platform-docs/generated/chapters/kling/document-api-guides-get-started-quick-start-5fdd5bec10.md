<!-- Official source: https://klingai.com/document-api/guides/get-started/quick-start.md -->
<!-- Source SHA-256: 76dba4be31c5731d980d9b91fcee06f171e8410a2c841daaed316d54d4578e3b -->

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
| ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/home-zh.9f340aca6a28342c.png) |

## Step 2: 资源包购买&现金额度充值

您可根据实际调用需求进行采购：

**API 资源包：** 已全面开放视频生成与图像生成两类 API 资源包购买渠道，其中视频生成提供基础版、专业版、通用版、旗舰版四个版本，不同版本支持的模型与能力有所差异

- 视频生成 API 资源包购买入口：https://klingai.com/dev/pricing?scrollTo=video
- 图像生成 API 资源包购买入口：https://klingai.com/dev/pricing?scrollTo=image

**定制服务：** 若现有线上资源包无法满足您的业务需求，您有定制或大额采购需求，欢迎点击<a class="link-plain" href="#business-consult">【商务咨询】</a>填写问卷，我们将尽快与您联系，为您提供现金额度充值服务

**说明：** Kling API 支持积分和现金额度调用两种模式，相关报价信息可前往<a class="link-plain" href="/document-api/pricing/base/video">「价格」</a>查看

## Step 3: 登录开发者控制台

1. 访问 https://klingai.com/dev/api-key

|                                             开发者控制台                                             |
| :--------------------------------------------------------------------------------------------------: |
| ![](https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/console-login-zh.b2f8e02cdac691e6.webp) |

2. 使用您的手机号或快手扫码登录，控制台账号与可灵AI web端账号一致

## Step 4: 进行接口鉴权

获取 API Key

创建 API 密钥并命名管理，支持一键复制 API Key

| 新建 API 密钥名称                                                                                               | 一键复制API Key                                                                                               | 支持启用/禁用、编辑名称、删除                                                                                    |
| :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| ![](https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/api-key-create-zh.b7a919ff1e0c94de.png) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/api-key-copy-zh.e235d835373311b9.png) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/api-key-manage-zh.2767a8093c04055a.webp) |

1、打开可灵 AI 控制台并登录

2、点击「**+ 新建 API Key**」按钮

3、在弹窗中为 **API Key** 命名并确认，此时页面会显示 **API Key**

4、复制获取 **API Key**；API Key仅显示一次，请注意妥善保管

5、将 **API Key** 组装成 **Authorization**，填写到 **Request Header** 里

- 组装方式：**Authorization = "Bearer XXX"**，其中 XXX 填写第一步获取的 **API Key**（注意Bearer跟XXX之间有空格）

## Step 5: 调用 API 服务

> API 调用域名：`https://api-beijing.klingai.com`

## Step 6: 控制台查看信息

| 查看API 调用量&趋势                                                                                | 查看资源包消耗进度&趋势                                                                              | 查看资源包账单明细                                                                                        | 查看额度账单明细                                                                                        |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| ![](https://p2-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/usage-calls-zh.77423db3bde0218d.webp) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/usage-package-zh.10edccb5a6e51f5a.webp) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/usage-package-bill-zh.5c6c7517f3f9f063.webp) | ![](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/api-doc/usage-quota-bill-zh.add48e1f6fa41d20.webp) |
