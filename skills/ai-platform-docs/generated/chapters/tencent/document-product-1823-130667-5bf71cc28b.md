<!-- Official source: https://cloud.tencent.com/document/product/1823/130667 -->
<!-- Source SHA-256: 30e14bd81aaffed3e2120e6715495ffbc1e58b3c47a335241de0159f0e5521e8 -->

# Cline

官方来源：https://cloud.tencent.com/document/product/1823/130667
最近更新时间：2026-09-03 14:36:30

Cline 是一款内置于编辑器和终端的 AI 编码助手。它可以读写文件、运行终端命令、使用浏览器，并通过自然对话帮助您构建功能。本文介绍如何在 Cline 中配置与使用腾讯云大模型 Token Plan 企业版。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. 获取模型配置：

2.1 [专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)；

2.2 [轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 安装 Cline

打开 VSCode，在扩展市场搜索并安装 Cline，详情可参考 [Cline 官方安装指引](https://docs.cline.bot/getting-started/installing-cline)。

## 配置 Token Plan 企业版

Cline 插件安装完成后，单击右上角的设置按钮，配置以下信息：

API Provider：选择 **OpenAI Compatible**（Token Plan 接口兼容 OpenAI 标准）。

Base URL：

新加坡：`https://tokenhub-intl.tencentmaas.com/plan/v3`

广州：`https://tokenhub.tencentmaas.com/plan/v3`

API Key：填写您的 API Key。

Model ID：根据您购买的套餐，填入套餐支持的模型 ID。

专业套餐：具体模型请参考 [Token Plan 企业版专业套餐](https://cloud.tencent.com/document/product/1823/130659) 中的可用模型列表。

轻享套餐：具体模型请参考 [Token Plan 企业版轻享套餐](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19) 中的可用模型列表。

## 使用 Cline

配置完成后，您可以看到对话框下方显示对应的模型配置，并可以通过对话框与模型进行交互。
