<!-- Official source: https://cloud.tencent.com/document/product/1823/130072 -->
<!-- Source SHA-256: 0414ef4f6ad890c238622ba88ced19fc3e026370ae460c5e13cb826c29a0affa -->

# Cline

官方来源：https://cloud.tencent.com/document/product/1823/130072
最近更新时间：2026-10-22 10:29:00

Cline 是一款内置于编辑器和终端的 AI 编码助手。它可以读写文件、运行终端命令、使用浏览器，并通过自然对话帮助您构建功能。本文介绍如何在 Cline 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。

## 安装 Cline

打开 VSCode，在扩展市场搜索并安装 Cline，详情可参考 [Cline 官方安装指引](https://docs.cline.bot/getting-started/installing-cline)。

## 配置 Token Plan

1. Cline 插件安装完成后，单击右上角的设置按钮。

2. 配置以下信息：

API Provider：选择 **OpenAI Compatible**（Token Plan 接口兼容 OpenAI 标准）。

Base URL：`https://tokenhub.tencentmaas.com/plan/v3`。

API Key：填写 Token Plan 专属的 API Key。

Model ID：根据您购买的套餐，填入 [套餐支持的模型 ID](https://cloud.tencent.com/document/product/1823/130119)。

如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。

如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。

## 使用 Cline

配置完成后，您可以看到对话框下方显示对应的模型配置，并可以通过对话框与模型进行交互。

![](https://qcloudimg.tencent-cloud.cn/image/document/771e51a01247a1ed6084c26afaf5589e.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/771e51a01247a1ed6084c26afaf5589e.png)
