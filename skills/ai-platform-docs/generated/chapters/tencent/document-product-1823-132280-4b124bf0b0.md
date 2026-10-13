<!-- Official source: https://cloud.tencent.com/document/product/1823/132280 -->
<!-- Source SHA-256: 56770a590c2e8dc75b335733e7de3bcc0b0f3b95ffec0fc8acbb3906efba3268 -->

# 简介

官方来源：https://cloud.tencent.com/document/product/1823/132280
最近更新时间：2026-07-15 03:29:10

## 概述
大模型服务平台 TokenHub 致力于为企业和开发者提供统一的大模型服务入口，整合腾讯自研的混元大模型能力，并引入优质第三方模型，覆盖通用对话、深度推理、代码生成、视觉理解、图像生成、视频生成等多类场景。平台支持按量调用、保障型资源、专属部署等多种服务模式，帮助企业简单、高效地获取 AI 算力。
本章节介绍 TokenHub 控制面操作相关云 API  ，例如 服务创建、Key管理、用量统计数据获取、Token Plan 企业版套餐管理、Token Plan 企业版 API Key 管理。注意管控面 API 暂不支持模型调用，如有需求，请查看[模型调用概览](https://cloud.tencent.com/document/product/1823/130078)。

## 术语表
TokenHub API 接口的常见术语请参见下表：

| 术语 | 描述 | 
|---------|---------|
| EndpointId | 推理服务的服务 ID |
| TeamId | Token Plan 企业版套餐 ID。 | 
| PrepayResourceID | Token Plan 企业版套餐绑定的云计费预付费资源包 ID。 | 

> **注意**
> TokenPlan Key、用量等信息在套餐中单独管理，有独立的接口控制，无法通过 TokenHub 全局接口查询和使用。

## API 快速入门
您可以使用 API Explorer 工具在线调用 API。
本文以查询 Token Plan 套餐详情为例，通过 API Explorer 工具调用 API 接口的步骤如下：
1.进入 [API Explorer](https://console.cloud.tencent.com/api/explorer) 工具页面。更多 API Explorer 工具使用信息，请参见 [使用 API Explorer](https://cloud.tencent.com/document/product/1278/46697)。
2.调用 DescribeTokenPlan，查询 Token Plan 套餐详情的。
3.选择 Region: 华南地区（广州）。
4.输入要查询的套餐 ID（TeamId）。
5.发起调用即可。
