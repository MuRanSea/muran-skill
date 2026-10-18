<!-- Official source: https://cloud.tencent.com/document/product/1823/131701 -->
<!-- Source SHA-256: 629264100c9f0d2b0a19babcac357499a1cd445f0d233712a5f09a08acbac8de -->

# 网络配置

官方来源：https://cloud.tencent.com/document/product/1823/131701
最近更新时间：2026-10-17 13:11:21

通过网络配置，您可以创建一条提供用户 VPC 到 TokenHub 的内网连接通道，实现内网访问 TokenHub 接口域名，提升网络安全。

## 使用前提

已开通大模型服务平台 TokenHub 服务。

## 操作步骤

1. 登录大模型服务平台 TokenHub 控制台，进入 [网络配置](https://console.cloud.tencent.com/tokenhub/network) 页面。

![](https://qcloudimg.tencent-cloud.cn/image/document/5e6933b6e6c8642f222ebc895c0a1813.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/5e6933b6e6c8642f222ebc895c0a1813.png)

2. 单击**新建连接**，并开通 VPC 内网访问。

2.1 内网访问依托 [终端节点服务](https://console.cloud.tencent.com/vpc/vpce)、[PrivateDNS 服务](https://console.cloud.tencent.com/cns/privatedns)，首次创建连接时，系统会检测上述服务的开通状态，您可以单击控制台中的**开通 PrivateLink 服务**一键完成两项服务的开通。

![](https://qcloudimg.tencent-cloud.cn/image/document/4fcecd4209655a0a13fcf9909adf211b.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/4fcecd4209655a0a13fcf9909adf211b.png)

2.2 开通 PrivateLink 服务后，选择需要打通内网访问的 VPC，以及终端节点服务所属子网后，单击**立即开通**：

**选择 VPC**：需要建立内网连接的 VPC，成功建立连接后，此 VPC 内所有子网均可内网访问 TokenHub 服务。

**选择子网**：终端节点服务所在子网，将决定内网访问 IP 所属网段。

![](https://qcloudimg.tencent-cloud.cn/image/document/9aa5cb1c1f23758a253f611658b10cca.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/9aa5cb1c1f23758a253f611658b10cca.png)

3. 首次使用服务需完成服务授权，授权 TokenHub 创建网络连接：

![](https://qcloudimg.tencent-cloud.cn/image/document/9b2be9097233f10a82f7c64e6d464da2.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/9b2be9097233f10a82f7c64e6d464da2.png)

单击**同意授权**后，等待连接创建完成，当状态显示为**已连接**时，表示创建完成。用户**在此 VPC 内无需修改调用配置，访问 TokenHub 接口域名时会自动切换为内网**，更多关于接口域名信息，请参见 [API 使用说明](https://cloud.tencent.com/document/product/1823/130078)。

![](https://qcloudimg.tencent-cloud.cn/image/document/12e7d80123de20e392e9645e37222f4b.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/12e7d80123de20e392e9645e37222f4b.png)

## 其他操作

### 1. 创建多个 VPC 的内网连接

在网络配置页面单击**新建连接**，可创建多条网络连接，打通多个 VPC 的内网访问。

![](https://qcloudimg.tencent-cloud.cn/image/document/ca8fc47a899df531610d5fe016eae841.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/ca8fc47a899df531610d5fe016eae841.png)

### 2. 跨 VPC 网络内网访问

默认情况下，打通网络连接后仅支持已创建连接的 VPC 内网访问 TokenHub 接口域名，当其他网络也需要内网访问时（如：跨 region VPC、跨云网络、混合云网络等），您需要确保该网络与已创建连接的 VPC 内网互通（更多关于私有网络连接的创建，请参见 [云联网](https://console.cloud.tencent.com/vpc/ccn)）。在内网互通的前提下，如果该网络无法自动解析已创建连接的 VPC DNS，则可通过手动添加域名解析的方式，将 TokenHub 接口域名解析到相应网络连接的终端节点 IP 即可实现内网域名访问。

### 3. 使用 HTTP 协议或自定义域名

网络连接创建后，默认情况下在创建链接的 VPC 中，平台已自动通过 PrivateDNS 为您配置了解析规则，将 TokenHub 公网域名解析到终端节点 IP，您无需修改任何调用配置即可通过内网访问模型服务。内网链接支持 HTTP 协议访问，如果您的访问节点不在此 VPC 中，但该节点与 VPC 内网互通，您可以通过使用 HTTP 协议访问终端节点 IP 的形式访问模型服务。例如：在下图所示的环境中，将`https://tokenhub.tencentmaas.com/v1/chat/completions` 替换为 `http://10.0.10.3/v1/chat/completions` 可正常访问模型服务。您也可以为终端节点 IP 添加自定义域名解析，通过自定义域名访问模型服务。

![](https://qcloudimg.tencent-cloud.cn/image/document/c978d4c221a587bd509146141cb513bc.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/c978d4c221a587bd509146141cb513bc.png)

###
