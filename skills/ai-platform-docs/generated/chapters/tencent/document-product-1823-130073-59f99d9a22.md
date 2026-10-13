<!-- Official source: https://cloud.tencent.com/document/product/1823/130073 -->
<!-- Source SHA-256: 76f22532a4d2e300a806b1f6a02ad92d7d9153182476828db977cbccc44f0003 -->

# Cursor

官方来源：https://cloud.tencent.com/document/product/1823/130073
最近更新时间：2026-09-03 14:36:31

Cursor 是基于 VSCode 深度改造、AI 原生的代码编辑器，内置 GPT-4/Claude 等模型，支持自然语言生成、代码理解、跨文件重构、智能调试与自主代理（Agent）。本文介绍如何在 Cursor 中配置与使用腾讯云大模型 Token Plan。

## 前置条件

在开始配置前，请确保您已完成以下准备工作：

1. [订阅 Token Plan 套餐](https://cloud.tencent.com/document/product/1823/130119#bdc49d9b-f68d-4b79-bb5a-0aa694f2624a)。

2. [获取 API Key](https://cloud.tencent.com/document/product/1823/130119#ac6f544e-6de6-46b7-8709-36d777248b34)。

3. 安装 Cursor。您可以通过 [Cursor 官网](https://cursor.com/) 下载并安装 Cursor。

**注意：**

由于 Cursor 的限制，只有订阅了 Cursor Pro 及以上版本套餐的用户才支持自定义配置模型。

## 配置 Token Plan

Cursor 安装完成后，在 Cursor 中，单击右上角的 **Cursor Settings**，选择 **Models** 模块并进行配置。**Models** 模块的具体配置如下：

OpenAI API Key：填写 Token Plan 的专属 API Key。

Override OpenAI Base URL：`https://api.lkeap.cloud.tencent.com/plan/v3`。

Add Custom Model：根据您购买的套餐，填入 [套餐支持的模型 ID](https://cloud.tencent.com/document/product/1823/130119)。

如果您购买通用 Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b6fdbed0-897c-475d-a9a1-f9af922027c4)，选择具体的 **Model ID** 配置。

如果您购买 Hy Token Plan 套餐：请参见 [可用模型](https://cloud.tencent.com/document/product/1823/130060#b145766a-c747-42eb-89c2-a04463d20cc5)，选择具体的 **Model ID** 配置。

## 使用 Cursor

配置完成后，即可在聊天面板中选择配置的模型进行交互。
