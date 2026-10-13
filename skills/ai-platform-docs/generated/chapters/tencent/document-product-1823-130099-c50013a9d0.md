<!-- Official source: https://cloud.tencent.com/document/product/1823/130099 -->
<!-- Source SHA-256: c0cfddc9216d3bb21f0d36496fbd08eb23846621d511f6b38e1b63d2e7b38f7a -->

# Cline

官方来源：https://cloud.tencent.com/document/product/1823/130099
最近更新时间：2026-08-24 18:29:31

Cline 是一款内置于编辑器和终端的 AI 编码助手。它可以读写文件、运行终端命令、使用浏览器，并通过自然对话帮助您构建功能。本文介绍如何在 Cline 中配置与使用腾讯云大模型 Coding Plan。

## 前置条件

在开始配置前，请确保您已订阅 Coding Plan 套餐并获取 API Key，可参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

## 安装 Cline

打开 VSCode，在扩展市场搜索并安装 Cline，详情可参考 [Cline 官方安装指引](https://docs.cline.bot/getting-started/installing-cline)。

## 配置 Coding Plan

Cline 插件安装完成后，单击右上角的设置按钮，点击 **Bring my own API key**，配置以下信息：

API Provider：选择 **OpenAI Compatible**（Coding Plan 接口兼容 OpenAI 标准）。

Base URL：`https://api.lkeap.cloud.tencent.com/coding/v3`。

API Key：填写 Coding Plan 专属的 API Key。

Model ID：填写 Coding Plan 支持的 [Model Name](https://cloud.tencent.com/document/product/1823/130092#540d21b1-f168-4435-8784-2e8d26331f65)。

![](https://qcloudimg.tencent-cloud.cn/image/document/20b905c833e6ae7aecd66180eef365f6.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/20b905c833e6ae7aecd66180eef365f6.png)

## 使用 Cline

配置完成后，您可以看到对话框下方显示对应的模型配置，并可以通过对话框与模型进行交互。

![](https://qcloudimg.tencent-cloud.cn/image/document/771e51a01247a1ed6084c26afaf5589e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/771e51a01247a1ed6084c26afaf5589e.png)
