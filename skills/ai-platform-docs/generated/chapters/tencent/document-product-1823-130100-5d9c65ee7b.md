<!-- Official source: https://cloud.tencent.com/document/product/1823/130100 -->
<!-- Source SHA-256: e676178b148c023e0cd942ac24b255a7ebafdfa2f24a39f0ceaa2f2823eb796d -->

# Cursor

官方来源：https://cloud.tencent.com/document/product/1823/130100
最近更新时间：2026-04-03 16:27:22

Cursor 是基于 VS Code 深度改造、AI 原生的代码编辑器，内置 GPT-4/Claude 等模型，支持自然语言生成、代码理解、跨文件重构、智能调试与自主代理（Agent）。本文介绍如何在 Cursor 中配置与使用 Coding Plan。

## 前置条件

在开始配置前，请确保您已订阅 Coding Plan 套餐并获取 API Key，可参见 [Coding Plan 概述](https://cloud.tencent.com/document/product/1823/130092)。

## 安装 Cursor

官网下载安装包：通过 [Cursor 官网](https://cursor.com/) 下载并安装 Cursor。

**注意：**

由于 Cursor 的限制，只有订阅了 Cursor Pro 及以上套餐的用户才支持自定义配置模型。

## 配置 Coding Plan

Cursor 安装完成后，在 Cursor 中，点击右上角的 **Cursor Settings**，选择 **Models** 页面。Models 模块的具体配置如下：

OpenAI API Key：填写 Coding Plan 的专属 API Key。

Override OpenAI Base URL：`https://api.lkeap.cloud.tencent.com/coding/v3`。

Add Custom Model：填写 Coding Plan 支持的 [Model Name](https://cloud.tencent.com/document/product/1823/130092#540d21b1-f168-4435-8784-2e8d26331f65)。

## 使用 Cursor

配置完成后，即可在聊天面板中选择配置的模型进行交互。
