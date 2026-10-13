<!-- Official source: https://cloud.tencent.com/document/product/1823/130090 -->
<!-- Source SHA-256: a6673626cc98f9dc2a02f8991a278e2566736fa60a73147c7d4611fdfa17fd9b -->

# API Key 管理

官方来源：https://cloud.tencent.com/document/product/1823/130090
最近更新时间：2026-09-28 18:59:30

API Key 是调用大模型服务平台 TokenHub 服务的身份凭证，长期有效。您可以在 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey?regionId=1) 页面创建、编辑、启停和删除，并为每个 API Key 设置精细的访问范围。

**注意：**

API Key 长期有效，请在请求时通过请求头携带，并妥善保管，定期更新。请勿在公开环境中分享或泄露，以防未授权访问造成安全隐患或资金损失。

单个主账号 API Key 默认创建个数上限为 50 个，如您有更多使用需求，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请。

API Key 中暂不包含 Coding plan、Token plan 生成的 Key，二者的 Key 创建个数也不受此处默认值限制。

## API Key 列表

<table><colgroup><col/><col/></colgroup><tbody><tr><td><div>字段</div></td><td><div>说明</div></td></tr><tr><td><div><b>名称 / Key ID</b></div></td><td><div>自定义的 API Key 名称，Key ID 用于分账账单查询 Key 的对应标识，详情参考 <a href="https://cloud.tencent.com/document/product/1823/131726">账单分账</a>。</div></td></tr><tr><td><div><b>说明</b></div></td><td><div>自定义的 API Key 说明，方便识别用途。</div></td></tr><tr><td><div><b>Key</b></div></td><td><div>调用 TokenHub 服务的身份凭证，脱敏显示（前 5 位 + *** + 后 4 位），支持一键复制完整 API Key。</div></td></tr><tr><td colspan="1" rowspan="1"><div><b>状态</b></div></td><td colspan="1" rowspan="1"><div>启用/禁用。</div><div>您可以通过状态开关切换 API Key 的启用、禁用状态。禁用状态下，被禁用 API Key 的所有 API 请求将被拒绝。</div></td></tr><tr><td><div><b>用量监控</b></div></td><td><div>查看当前 APIKey 的 token 消耗走势、模型消耗排行、 请求调用量统计。</div></td></tr><tr><td><div><b>访问范围</b></div></td><td><div>全部（可访问所有模型和服务）。</div><div>限定范围（包含模型对应的默认和自定义推理服务接入点）。</div></td></tr><tr><td><div><b>额度限制</b></div></td><td><div>限制 API Key 的使用用量，默认状态不开启。若已经超过您配置的周期内上限，超过后则调用失败。</div></td></tr><tr><td><div><b>创建时间</b></div></td><td><div>API Key 首次创建时间。</div></td></tr><tr><td><div><b>操作</b></div></td><td><div>编辑：修改 API Key 的访问范围及关联的模型/服务。</div><div>删除：永久删除 API Key，需二次确认。删除后使用该 API Key 的所有请求将立即失败。</div></td></tr></tbody></table>

## 创建 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey?regionId=1) 页面。

2. 在页面上方选择地域后，单击**创建 API Key。**

3. 在**创建 API Key** 对话框进行配置：

![](https://qcloudimg.tencent-cloud.cn/image/document/8e8e5d3391af00d4e066921f2b98ca19.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/8e8e5d3391af00d4e066921f2b98ca19.png)

**Key 名称**：例如 “生产环境-文本服务”、“测试用 Key”。

**说明（选填）**：为 API Key 设置说明，方便识别和区分用途。

**IP 白名单：**设置允许访问此 Key 的 IP 范围，支持设置 IP 网段，最多允许设置 200 个。

**额度限制：开启后该 API Key 的 token 用量达到配额上限将停止服务**，用量统计不区分模型与推理服务接入点（免费包不计算入内）。

限额策略：支持日/月/总额度三种限额周期，**切换限额策略（如 日 → 月）或修改月度生效日后，历史用量将清零**，并按新规则重新累积。

生效范围：根据您选择的策略周期配置。

日：按自然日统计，每日 00:00 重置用量重新累积。

月：按所选生效日统计，周期结束自动重置。如选每月 3 日则统计本月 3 日 00:00 至次月 2 日 23:59。

总额度：开启后持续累积用量，不自动重置。

额度上限：单位为 tokens。

**可访问范围**：

**全选**：可访问您账号下的所有模型和推理服务。

**限定范围**：您可以在**可访问范围**区域勾选可访问的推理服务，实现访问范围控制。**平台为每个模型创建一个默认在线推理服务，勾选效果等同于授权模型级的访问，支持基于“模型品牌”和“类型”细粒度筛选。**

4. 单击**确定**，完成创建。

创建完成后，请您务必**复制并妥善保管 API Key**，在后续调用 API 流程中将会使用该信息。

**注意：**

API Key 名称和 API Key 值创建后不可修改。

## 编辑 API Key

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey?regionId=1) 页面。

2. 在页面上方选择目标 API Key 所属地域，找到 API Key。

3. 在 API Key 右侧的**操作**列单击**编辑。**

4. 您可以在**编辑 API Key** 对话框修改 API Key 说明或 API Key 的访问范围。

**注意：**

切换为新的指定范围后，上次选择的访问范围将失效，以本次切换后的范围为准。

5. 单击**确定**，保存更改。

## 删除 API Key

**注意：**

删除 API Key 后将无法恢复，使用该 API Key 的所有服务调用将立即失效。删除时，会触发账号身份校验，请知悉。

1. 进入 [API Key 管理](https://console.cloud.tencent.com/tokenhub/apikey?regionId=1) 页面。

2. 在页面上方选择目标 API Key 所属地域，找到 API Key。

3. 在 API Key 右侧的**操作**列单击**删除**。

4. 在**确认删除 API Key** 对话框确认删除信息无误后，单击**确认**，完成删除。

![](https://qcloudimg.tencent-cloud.cn/image/document/748443c1258c234ec8851511ba450caa.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/748443c1258c234ec8851511ba450caa.png)

## 使用建议

| 建议 | 说明 |
| --- | --- |
| **按用途分配 API Key** | 为不同应用或环境（开发/测试/生产）创建独立的 API Key。 |
| **最小权限原则** | 使用**指定范围**限制 API Key 仅能访问所需的模型和服务。 |
| **及时轮换 API Key** | 定期更换 API Key，降低泄露风险。 |
| **禁用不用的 API Key** | 不再使用的 API Key 应及时禁用或删除。 |
| **妥善保管 API Key** | API Key 创建后，请立即保存到安全位置。 |
