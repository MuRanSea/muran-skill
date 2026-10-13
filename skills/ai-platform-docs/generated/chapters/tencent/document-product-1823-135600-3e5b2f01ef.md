<!-- Official source: https://cloud.tencent.com/document/product/1823/135600 -->
<!-- Source SHA-256: 0f5bb5904af6a3454ca7360acb78acdbf4849d4ba002bffddab13d76723324f5 -->

# 旧版本视觉模型下线迁移指引

官方来源：https://cloud.tencent.com/document/product/1823/135600
最近更新时间：2026-08-21 15:43:10

随着腾讯云 TokenHub 视觉模型的计费调整，后续视觉模型将陆续调整为按 Token 计费方式。我们将上线按 Token 计费的新版本模型，并逐步对旧版本模型进行下线。

根据调整规划，[大模型服务平台 TokenHub](https://cloud.tencent.com/document/product/1823/130050) 内 Kling 系视频生成模型、Vidu 系视频生成模型、HY 系图片生成模型已上线按 Token 计费的新版本模型，旧版本模型将于 **北京时间2026年9月15日00:00起**停止发起任务调用，HY 系列视频生成模型将于**北京时间2026年9月21日00:00起**停止发起任务调用，请各位用户提前完成业务迁移。

建议根据迁移指引选择对应的新版本模型，不同模型版本的功能、调用参数、输出效果及适用范围可能存在差异，具体以迁移映射表和产品文档为准，详见下方模型列表：

**计费说明：**

模型完成切换后，相关调用将按照切换后的新计费规则执行。请您在切换前通过控制台或计费文档确认新模型价格、额度消耗和适用范围。计费文档详情请参考 [计费方式](https://cloud.tencent.com/document/product/1823/130054)、[模型价格](https://cloud.tencent.com/document/product/1823/130055)。

## 下线模型列表

| 下线模型 model 参数 | 建议迁移模型 model 参数 |
| --- | --- |
| kl-video-v3 | kling-video-v3 |
| kl-video-v2-6 | kling-video-v2.6 |
| kl-video-v2-5-turbo | kling-video-v2.5-turbo |
| kl-video-v2-1 | kling-video-v3 |
| kl-video-v2-1-master | kling-video-v3 |
| kl-video-v2-master | kling-video-v3 |
| kl-video-v1-6 | kling-video-v3 |
| kl-video-v1-5 | kling-video-v3 |
| kl-video-v1 | kling-video-v3 |
| vd-video-q3-pro | vidu-video-q3-pro |
| vd-video-q3-turbo | vidu-video-q3-turbo |
| vd-video-q2 | vidu-video-q2 |
| vd-video-q2-pro | vidu-video-q2-pro |
| vd-video-q2-pro-fast | vidu-video-q2-pro |
| vd-video-q2-turbo | vidu-video-q2-turbo |
| hy-image-v3.0 | hy-image-v3 |
| hy-image-lite | hy-image-v3 |
| hy-video-1.5 | hy-video-v1.5 |

## 典型场景费用对照

<table><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td><div><b>模型名称</b></div></td><td><div><b>旧计费方式积分单价</b></div><div><b>（元/积分）</b></div></td><td><div><b>参数</b></div></td><td><div><b>旧计费方式参考费用</b></div><div><b>（按积分计费）</b></div></td><td><div><b>新计费方式参考费用</b></div><div><b>（按 Token 计费）</b></div></td></tr><tr><td colspan="1" rowspan="5"><div>Kling-Video-v3</div></td><td colspan="1" rowspan="5"><div>1.0 元/积分</div></td><td><div>720P 无声</div></td><td><div>0.6 积分/秒（折合 0.6元/秒）</div></td><td colspan="1" rowspan="1"><div>60,000 tokens/秒（折合 0.6元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>720P 有声</div></td><td><div>0.9 积分/秒（折合 0.9元/秒）</div></td><td colspan="1" rowspan="1"><div>90,000 tokens/秒（折合 0.9元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>1080P 无声</div></td><td><div>0.8 积分/秒（折合 0.8元/秒）</div></td><td colspan="1" rowspan="1"><div>80,000 tokens/秒（折合 0.8元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>1080P 有声</div></td><td><div>1.2 积分/秒（折合 1.2元/秒）</div></td><td colspan="1" rowspan="1"><div>120,000 tokens/秒（折合 1.2元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>4K 无声&amp;有声</div></td><td><div>3 积分/秒（折合 3元/秒）</div></td><td colspan="1" rowspan="1"><div>300,000 tokens/秒（折合 3元/秒）</div></td></tr><tr><td colspan="1" rowspan="4"><div>Kling-Video-v2.6</div></td><td colspan="1" rowspan="4"><div>1.0 元/积分</div></td><td><div>720P 无声</div></td><td><div>0.3 积分/秒（折合 0.3 元/秒）</div></td><td colspan="1" rowspan="1"><div>30,000 tokens/秒（折合 0.3元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>1080P 无声</div></td><td><div>0.5 积分/秒（折合 0.5 元/秒）</div></td><td colspan="1" rowspan="1"><div>50,000 tokens/秒（折合 0.5元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>1080P 有声</div></td><td><div>1.0 积分/秒（折合 1 元/秒）</div></td><td colspan="1" rowspan="1"><div>100,000 tokens/秒（折合 1元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>1080P 有声-指定音色</div></td><td><div>1.2 积分/秒（折合 1.2 元/秒）</div></td><td colspan="1" rowspan="1"><div>120,000 tokens/秒（折合 1.2元/秒）</div></td></tr><tr><td colspan="1" rowspan="2"><div>Kling-Video-v2.5-turbo</div></td><td colspan="1" rowspan="2"><div>1.0 元/积分</div></td><td><div>720P</div></td><td><div>0.3 积分/秒（折合 0.3 元/秒）</div></td><td colspan="1" rowspan="1"><div>30,000 tokens/秒（折合 0.3元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>1080P</div></td><td><div>0.5 积分/秒（折合 0.5 元/秒）</div></td><td colspan="1" rowspan="1"><div>50,000 tokens/秒（折合 0.5元/秒）</div></td></tr><tr><td colspan="1" rowspan="3"><div>Vidu-Video-q3-pro</div></td><td colspan="1" rowspan="3"><div>0.3125 元/积分</div></td><td><div>540P</div></td><td><div>0.9 积分/秒（折合 0.28125元/秒）</div></td><td colspan="1" rowspan="1"><div>28,125 tokens/秒（折合 0.28125元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>720P</div></td><td><div>2 积分/秒（折合 0.625 元/秒）</div></td><td colspan="1" rowspan="1"><div>62,500 tokens/秒（折合 0.625 元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td><div>1080P</div></td><td><div>2.4 积分/秒（折合 0.75元/秒）</div></td><td colspan="1" rowspan="1"><div>75,000 tokens/秒（折合 0.75元/秒）</div></td></tr><tr><td colspan="1" rowspan="3"><div>Vidu-Video-q3-turbo</div></td><td colspan="1" rowspan="3"><div>0.3125 元/积分</div></td><td colspan="1" rowspan="1"><div>540P</div></td><td><div>0.7 积分/秒（折合 0.21875元/秒）</div></td><td colspan="1" rowspan="1"><div>21,875 tokens/秒（折合 0.21875元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="1" rowspan="1"><div>720P</div></td><td><div>1.2 积分/秒（折合 0.375元/秒）</div></td><td colspan="1" rowspan="1"><div>37,500 tokens/秒（折合 0.375元/秒）</div></td></tr><tr><td colspan="0" rowspan="0"><div></div></td><td colspan="0" rowspan="0"><div></div></td><td colspan="1" rowspan="1"><div>1080P</div></td><td><div>1.3 积分/秒（折合 0.40625元/秒）</div></td><td colspan="1" rowspan="1"><div>40,625 tokens/秒（折合 0.40625元/秒）</div></td></tr></tbody></table>

**说明：**

示例仅供参考，实际费用以控制台展示、实际 Token 消耗和账单为准。

## 迁移方式

**第一步：**登录 [TokenHub](https://console.cloud.tencent.com/tokenhub/models) 控制台，前往 [在线推理](https://console.cloud.tencent.com/tokenhub/inference) 页面，选择您需要的模型，启用后付费，开启之后将按 Token 用量后付费，模型后付费价格请参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055)。

![](https://qcloudimg.tencent-cloud.cn/image/document/b68388d9545cc6dd83dc69550bc628ed.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/b68388d9545cc6dd83dc69550bc628ed.png)

**第二步：**参考**模型详情页**中的调用示例，为您的业务更换新的模型调用地址和请求参数，以 kling-video-v3 为例：

![](https://qcloudimg.tencent-cloud.cn/image/document/21906a9021807eb749e6899cfee02ff3.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/21906a9021807eb749e6899cfee02ff3.png)

更多 API 调用示例请参见 [API 使用说明](https://cloud.tencent.com/document/product/1823/130078)。

**说明：**

模型完成切换后，相关调用将按照切换后的新计费规则执行；请您在切换前通过控制台或计费文档确认新模型价格、额度消耗和适用范围；计费文档详见 [计费方式](https://cloud.tencent.com/document/product/1823/130054)、[模型价格](https://cloud.tencent.com/document/product/1823/130055)。

旧版模型下线后，历史用量数据的保存时效与导出方式保持不变，详见 [用量统计](https://cloud.tencent.com/document/product/1823/130088)。

## 联系我们

如果您在迁移过程中遇到任何问题或需要帮助，您可以咨询 [在线客服](https://cloud.tencent.com/act/event/Online_service) 或 [提交工单](https://console.cloud.tencent.com/workorder/category) 来与我们联系。

﻿
