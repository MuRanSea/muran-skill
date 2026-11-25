<!-- Official source: https://cloud.tencent.com/document/product/1823/141197 -->
<!-- Source SHA-256: 8f328d4e35e8b29cb31e48103c7cce3d4d3eb456bf43d8baf9835d03f8a0c46b -->

# 机密推理

官方来源：https://cloud.tencent.com/document/product/1823/141197
最近更新时间：2026-11-23 14:04:00

TokenHub 机密推理基于可信执行环境、远程证明和端到端加密，为包含敏感数据的模型调用提供受保护的推理链路。开启后，用户输入在客户端加密，以密文形式通过网络和服务接入链路，仅在经过验证的可信推理环境内解密并完成推理；模型响应在可信环境内重新加密，由客户端解密。

## 功能概述

机密推理从机密性、完整性和隔离性三个方面保护推理数据。

| 安全属性 | 主要机制 | 说明 |
| --- | --- | --- |
| 机密性 | 端到端加密、可信执行环境、会话密钥与请求级数据密钥 | 提示词和模型响应在客户端与可信推理边界之间保持密文；明文仅在客户端和经过验证的可信推理环境内短时出现。 |
| 完整性 | 可信启动、远程证明、握手完整性校验、运行时安全度量 | 客户端在建立安全会话时验证可信硬件身份、证明报告及其与当前会话的绑定关系；验证失败时不建立会话。 |
| 隔离性 | 安全镜像、访问控制、网络管控、磁盘与内存保护 | 限制非预期登录、调试和网络访问，缩小推理环境的暴露面，降低越权访问风险。 |

**说明：**

机密推理能力**受邀开放，**计费方式为增值服务（参见 [模型价格](https://cloud.tencent.com/document/product/1823/130055#fe64a45e-7f1e-4442-9abf-191dbdb5475d)）需搭配模型单元共同使用。支持的地域为国内站广州，模型为 GLM 5.3、DeepSeek-V4.1-Flash-1017。

## 适用业务场景

### 金融业务分析与智能风控

银行、证券、保险等机构使用大模型处理客户资料、交易信息、授信材料或风控特征时，提示词中可能包含个人信息和内部业务数据。机密推理对纳入策略的字段加密，使其从 SDK 或客户侧 Proxy 到推理处理边界之间保持密文，降低数据在传输与服务接入环节的暴露风险。

### 企业知识、代码与敏感文档处理

企业知识库问答、研发 Copilot、代码审查、合同审阅、医疗材料摘要和内部制度检索等场景，会使用内部文档、源代码、配置、日志或敏感文档片段作为模型上下文。这些内容通常不能以明文暴露给中间网络、平台运维人员或非授权系统。

### 智能终端与个人数据处理

手机助手、智能座舱和个人智能体可能需要处理图片描述、日程、联系人、位置或用户指令等个人数据。此类调用通常由大量终端发起，既需要云端模型能力，也需要降低数据离开终端后的泄露风险。

## 基础知识

| 概念 | 通俗说明 | 在机密推理中的作用 |
| --- | --- | --- |
| 可信执行环境 | 由硬件提供隔离保护的计算区域。外部系统即使具备较高权限，也不能直接读取其中正在处理的数据。 | 承载模型推理和业务明文处理。 |
| 远程证明 | 客户端在调用前检查服务端提供的硬件证明，确认对端处于预期的可信环境。 | 回答“数据将由什么环境处理”。 |
| 端到端加密 | 数据在发送端加密，到达可信推理环境后才解密；响应在可信环境内加密，再由客户端解密。 | 回答“数据在传输途中是否可读”。 |
| 安全会话 | 客户端与可信服务在验证身份后建立的临时加密关系。 | 绑定远程证明、会话密钥和有效期。 |
| 安全报告 | 平台汇总可信硬件、启动度量和运行时状态形成的记录。 | 帮助用户查看服务在指定时刻的可信状态。 |

三项核心机制的关系是：**远程证明先确认环境可信，安全会话再协商密钥，端到端加密最后保护每次模型请求和响应。**

### 安全架构

机密推理由客户可信域、服务接入链路和腾讯云安全推理区组成。

| 区域 | 主要组件 | 作用 |
| --- | --- | --- |
| 客户可信域 | 业务应用、AICC SDK 或安全代理 | 验证远程证明，建立安全会话，加密请求并解密响应。 |
| 服务接入链路 | TokenHub 接入网关 | 完成身份鉴权、协议接入和请求路由；业务内容以密文通过。 |
| 安全推理区 | AICC 安全会话服务、可信推理节点、安全网关 | 完成可信身份验证、密钥协商、密文解密、模型推理和响应加密。 |
| 密钥与证明体系 | KMS、硬件信任根、运行时度量组件 | 保护密钥，生成或验证证明材料，控制可信节点准入。 |

用户可采用两种接入方式：

**SDK 接入**：在业务代码中调用 AICC SDK，适合需要自行管理会话、加解密和错误处理的应用。

**安全代理接入（Proxy 模式）**：在企业网关或应用侧部署安全代理，适合已使用 OpenAI 兼容接口、希望降低业务改造量的系统。

### 端到端加密流程

端到端加密由客户端 SDK 或客户侧安全代理完成，保护客户端与推理处理边界之间的提示词、响应等受支持字段。端到端加密采用 X25519 与 ML-KEM-768 进行混合密钥协商，通过 HKDF-SHA256 派生会话及请求、响应密钥，并使用 AES-256-GCM 提供加密和完整性保护。业务可直接集成 SDK，也可在本地部署安全代理自动管理安全会话和加解密流程。

1. **发起安全会话**：客户端通过 SDK 或客户侧安全代理向 AICC 安全服务发起握手。

2. **验证并协商密钥**：客户端侧通过 SDK 或本地安全代理校验远程证明及其与当前握手的绑定关系，完成密钥协商与双向确认后建立安全会话。会话密钥不以明文传输。

3. **加密请求**：客户端可通过 SDK 或本地部署的安全代理为每次请求派生独立的数据密钥，对提示词等指定业务字段加密后，通过 HTTPS 发送请求。

4. **执行推理**：密文请求进入安全推理区，在经过验证的可信推理环境内解密并调用模型。

5. **加密响应**：模型生成结果后，在可信推理环境内使用响应方向的数据密钥加密。

6. **本地解密**：客户端收到密文响应并完成完整性校验，随后在本地解密。流式响应按顺序逐段校验和解密。

### 远程证明流程

远程证明用于在发送敏感数据前，验证服务端的硬件可信身份，并确认该身份与本次安全会话的绑定关系。客户端可通过 SDK 或安全代理校验硬件证书链、证明报告签名，以及报告、短期证书与当前握手之间的关联；只有验证通过并完成密钥确认后，客户端才接受安全会话并发送加密请求。对于推理节点的启动度量和运行状态，平台通过采集与策略评估形成安全报告，供用户在控制台查看和审计。

1. **发起验证**：客户端可通过 SDK 或本地部署的安全代理向 AICC 安全服务发送会话请求，提交随机数和密钥协商材料。

2. **返回证明材料**：服务端返回由硬件证明密钥签名的报告、可追溯至硬件信任根的证书链，以及短期证明证书和本次握手的校验信息。

3. **客户端本地验证**：客户端可通过 SDK 或本地部署的安全代理校验证书链、报告签名，以及报告、短期证书与当前握手之间的绑定关系。

4. **双向密钥确认**：双方通过密钥确认消息，校验会话密钥和握手上下文的一致性。

5. **接受安全会话**：全部校验通过后，SDK 或 Proxy 接受安全会话，用于后续加密调用；任一校验失败则终止本次握手，不自动降级为普通调用。

## 创建机密推理服务

1. 登录 [TokenHub 控制台](https://console.cloud.tencent.com/tokenhub)。

2. 在左侧导航栏选择**推理服务 > 自定义在线推理服务**。

3. 单击**新建**，选择支持部署的模型，在计费方式中选择**模型单元，**在资源规格区域勾选**机密推理版**。

4. 确认其他服务参数后完成服务创建。

## 使用 Python SDK 调用

### 环境要求

Python 3.10 或更高版本。

已创建并运行机密推理服务。

已获取该服务的安全会话地址、模型调用地址和可用的 TokenHub API Key。

客户端能够通过 HTTPS 访问上述地址。

### 安装 SDK

```bash
pip install "tcaicc==1.4.1" httpx
```

本示例基于 tcaicc 1.4.1。SDK 负责远程证明、安全会话和字段加解密；模型请求由 HTTP 客户端发送。模型调用的超时、重试和取消由业务侧管理。

### 配置接入信息

建议通过环境变量或密钥管理系统传入敏感参数，不要将真实 API Key 写入源码、命令行参数、日志或版本库。

```bash
export TOKENHUB_AICC_SESSION_URL='https://tokenhub.tencentmaas.com/v1/aicc'
export TOKENHUB_AICC_CHAT_URL='https://tokenhub.tencentmaas.com/v1/chat/completions'
export TOKENHUB_API_KEY='<API_KEY>'

export TOKENHUB_MODEL='ep-xxxxxxxx'
export TOKENHUB_AICC_ENDPOINT='ep-xxxxxxxx'
```

具体地址和模型 ID 以服务详情提供的信息为准。

### 非流式调用示例

```python

import json
import os
from urllib.parse import urlsplit

import httpx
from tcaicc import Protocol, SessionFactory, SessionPool, default_policy

session_url = os.environ["TOKENHUB_AICC_SESSION_URL"]
chat_url = os.environ["TOKENHUB_AICC_CHAT_URL"]
api_key = os.environ["TOKENHUB_API_KEY"]
model = os.environ["TOKENHUB_MODEL"]
endpoint = os.environ["TOKENHUB_AICC_ENDPOINT"]

if any(urlsplit(url).scheme != "https" for url in (session_url, chat_url)):
    raise ValueError("生产环境必须使用 HTTPS 地址")

policy = default_policy(Protocol.OPENAI)

# 长期运行时复用工厂、会话池和 HTTP 客户端；每次请求新建 Request。
with SessionFactory(session_url, api_key, ttl=600) as factory:
    factory.set_endpoint(endpoint)

    with SessionPool(factory, 1) as sessions, httpx.Client(timeout=600) as client:
        with sessions.new_request() as request:
            body = {
                "model": model,
                "messages": [{"role": "user", "content": "你好，请介绍机密推理。"}],
                "stream": False,
            }
            response = client.post(
                chat_url,
                content=request.encrypt_request(json.dumps(body).encode(), policy),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                    "X-AICC-Mode": "1",
                    "X-AICC-Endpoint": request.endpoint,
                },
            )
            response.raise_for_status()

            result = json.loads(request.decrypt_response(response.content, policy))
            if "error" in result:
                raise RuntimeError("模型调用返回错误，未获得正常响应")
            print(result["choices"][0]["message"].get("content") or "")
```

示例包含两部分：

1. `SessionFactory` 与 `SessionPool` 管理安全会话的建立、复用和临期换新。

2. 每次模型请求通过 `sessions.new_request()` 创建独立的 `Request`，按 OpenAI 协议策略加密请求并解密响应。

### 流式调用

流式调用向服务详情提供的模型调用地址发送 HTTPS POST，请求体设置 `"stream": true`。将完整 SSE 数据事件按返回顺序交给同一个 `StreamDecryptor.decrypt_event()` 处理，再读取解密后的正文。

以下示例可独立运行，使用与非流式示例相同的环境变量。默认 Compatible 模式不要求加密尾片，因此不使用 `decryptor.finished` 判断完成。

```python

import json
import os
from urllib.parse import urlsplit

import httpx
from tcaicc import Protocol, SessionFactory, SessionPool, default_policy

session_url = os.environ["TOKENHUB_AICC_SESSION_URL"]
chat_url = os.environ["TOKENHUB_AICC_CHAT_URL"]
api_key = os.environ["TOKENHUB_API_KEY"]
model = os.environ["TOKENHUB_MODEL"]
endpoint = os.environ["TOKENHUB_AICC_ENDPOINT"]

if any(urlsplit(url).scheme != "https" for url in (session_url, chat_url)):
    raise ValueError("生产环境必须使用 HTTPS 地址")

policy = default_policy(Protocol.OPENAI)
# read=600 是读取等待超时，不是整个生成过程的总时限。
timeout = httpx.Timeout(600, read=600)

with SessionFactory(session_url, api_key, ttl=600) as factory:
    factory.set_endpoint(endpoint)

    with SessionPool(factory, 1) as sessions, httpx.Client(timeout=timeout) as client:
        with sessions.new_request() as request:
            body = {
                "model": model,
                "messages": [{"role": "user", "content": "讲一个简短的故事。"}],
                "stream": True,
            }
            decryptor = request.new_stream_decryptor()
            seen_done = False
            finish_reason = None
            data_lines = []

            with client.stream(
                "POST",
                chat_url,
                content=request.encrypt_request(json.dumps(body).encode(), policy),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                    "X-AICC-Mode": "1",
                    "X-AICC-Endpoint": request.endpoint,
                },
            ) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    # SSE 事件以空行分隔；同一事件的多个 data 行合并后处理。
                    if line != "":
                        field, _, value = line.partition(":")
                        if field == "data":
                            data_lines.append(value[1:] if value.startswith(" ") else value)
                        continue
                    if not data_lines:
                        continue
                    data = "\\n".join(data_lines)
                    data_lines = []

                    if data.strip() == "[DONE]":
                        seen_done = True
                        break
                    plain, _ = decryptor.decrypt_event(data.encode(), policy)
                    if plain is None:
                        continue
                    event = json.loads(plain)
                    if "error" in event:
                        raise RuntimeError("流式调用返回错误，已显示内容可能不完整")

                    for choice in event.get("choices") or []:
                        if choice.get("finish_reason") is not None:
                            finish_reason = choice["finish_reason"]
                        content = (choice.get("delta") or {}).get("content")
                        if content:
                            print(content, end="", flush=True)
                    # finish_reason 后继续读取后续 usage / [DONE] 事件。

            # 默认 Compatible 模式不要求加密尾片；这里只检查应用层结束信息。
            if not seen_done and finish_reason is None:
                raise RuntimeError("流式响应没有结束信息，响应可能不完整")
            print()
```

流式调用需遵循以下规则：

每轮 HTTP 请求都通过 `sessions.new_request()` 新建 `Request`；同一请求使用同一个请求上下文和流式解密器。

完整 SSE 事件必须按返回顺序解密；当前加密流式调用不支持 `n>1`。

请求重试时重新创建 `Request`；会话池管理会话换新，不自动重试模型调用。

示例在既未收到 `[DONE]`、也没有 `finish_reason` 就结束时报告可能不完整。这是应用层检查，不等同于整条响应的密码学截断检测。

`finish_reason=length` 表示达到生成限制；读取超时 600 秒是一次读取等待上限，不是整个生成过程的总时限。

## 查看安全报告

安全报告展示平台已采集的节点状态、证明材料及评估结果，供用户检查和审计。查看时应区分会话证明、节点证明与运行状态记录，并结合采集时间、验证状态和覆盖范围理解结果。

| 验证内容 | 说明 |
| --- | --- |
| 硬件身份 | 推理服务是否运行在受支持的可信硬件环境中。 |
| 证明真实性 | 证明报告是否由对应硬件信任根签名，证书链是否有效。 |
| 证明新鲜性 | 报告是否绑定随机挑战或当前会话，避免历史证明被重放。 |
| 环境状态 | 启动度量、运行时状态和平台安全基线是否满足可信准入要求。 |
| 会话绑定 | 证明材料、临时证书和当前安全会话是否一致。 |

## 限制条件

安全会话建立会增加额外网络往返；加解密和可信环境会产生一定性能开销，建议在上线前按实际请求长度、并发量和流式模式进行压测。

安全会话的有效期由客户端申请值和服务端策略共同决定，会话到期后需重新建立。

第二阶段密钥派生或导入为一次性操作；失败后需重新调用 `create_session`，不能复用已消费的握手状态。

生产环境不得设置 `verify_sev=False`，否则客户端无法证明对端运行在可信执行环境中。

生产环境不得使用跳过 TLS 证书校验的配置。使用私有 CA 时，应向 SDK 显式提供 CA 证书；使用公信 CA 时，仍需校验证书链和域名。

SDK 默认验证硬件证明、证书链、签名和会话绑定，不替代业务侧对自定义镜像度量值或安全策略字段的校验。

机密推理不提供内容合规判断，内容风险识别需使用内容安全防护。

## 常见问题

### 机密推理与普通 HTTPS 有什么区别？

HTTPS 保护客户端到接入地址的传输链路，并验证域名身份。机密推理在此基础上，通过远程证明验证安全会话服务，并对指定业务字段加密，使其从 SDK 或客户侧 Proxy 到推理处理边界之间保持密文。

### 开启机密推理后，现有调用代码是否需要修改？

取决于接入方式：

**SDK 接入**：业务代码需集成 `tcaicc`，增加安全会话建立、请求加密和响应解密处理。本文示例使用 OpenAI Chat Completions 请求与响应结构。

**安全代理接入（Proxy 模式）**：在客户可信域内部署代理，业务侧调整调用地址与鉴权配置，由代理负责安全会话和加解密。

### 远程证明失败后是否会自动转为普通调用？

不会。远程证明或握手校验失败时，SDK 终止安全会话，不自动降级为明文调用。请根据错误码和 RequestId 排查服务状态、证书链、网络和 SDK 版本。

### API Key、会话密钥和请求密钥分别有什么作用？

**API Key**：用于 TokenHub 调用身份鉴权，不作为业务数据加密密钥。

**会话密钥**：由安全会话协商产生，绑定会话和有效期。

**请求级数据密钥对**：由会话密钥结合请求上下文派生，分别用于单次请求方向和响应方向的数据加解密。

### 是否可以复用会话？

可以。长期运行时复用 `SessionFactory`、`SessionPool` 和 HTTP 客户端，每轮 HTTP 请求通过 `sessions.new_request()` 创建独立的 `Request`。会话池管理换新；模型请求的重试由业务侧决定。会话过期、证明失败或第二阶段握手失败后，需要重新建立安全会话。

### 机密推理是否等同于内容安全防护？

不等同。机密推理保护提示词、响应和推理环境的机密性、完整性与隔离性；内容安全防护负责识别提示词攻击、违规内容和敏感数据。两者解决的问题不同。
