<!-- Official source: https://cloud.tencent.com/document/product/1823/130665 -->
<!-- Source SHA-256: 96042f34c2d92bacae31160ba805709107811b443495fd3823697f913b23f87a -->

# Claude Code

官方来源：https://cloud.tencent.com/document/product/1823/130665
最近更新时间：2026-09-03 14:36:30

Claude Code 是一款 AI 编程助手，支持通过 Anthropic API 接入模型，帮助开发者快速编写、调试和管理代码。

Token Plan 企业版中的模型支持 Anthropic API 兼容接口，可以通过 Claude Code 调用。

## 前置条件

在开始配置前，确保您已完成以下准备工作：

1. [订阅 Token Plan 企业版套餐](https://cloud.tencent.com/document/product/1823/130660#9bad146b-59b9-463a-b9d9-4c21a823f8a5)。

2. 获取模型配置：

2.1 [专业套餐模型配置](https://cloud.tencent.com/document/product/1823/130659#cde5404a-a7bb-4d53-acba-6e3b1b6b8264)；

2.2 [轻享套餐模型配置](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19)。

3. [获取 API Key](https://cloud.tencent.com/document/product/1823/130660#c517dcb2-4a6d-4fbc-9793-a6fc05467143)。

## 安装 Claude Code

**注意：**

在 Windows 上使用 Claude Code，需要提前安装 [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) 或 [Git for Windows](https://git-scm.com/install/windows)。

Claude Code 通过 npm 安装，需先安装 Node.js（建议 ≥ 18）。如未安装，请访问 [Node.js 官网](https://nodejs.org/) 下载 LTS 版本。

执行如下命令安装 Claude Code，更多操作可参考 [Claude Code 安装指引](https://code.claude.com/docs/zh-CN/quickstart#%E6%AD%A5%E9%AA%A4-1%EF%BC%9A%E5%AE%89%E8%A3%85-claude-code)。

```bash
npm install -g @anthropic-ai/claude-code
```

安装结束后，执行以下命令查看安装结果，若显示版本号则安装成功。

```bash
claude --version
```

## 配置 Token Plan 企业版

在 Claude Code 中接入 Token Plan 企业版，需要配置以下信息：

ANTHROPIC\_BASE\_URL：设置为 `https://tokenhub.tencentmaas.com/plan/anthropic`。

ANTHROPIC\_AUTH\_TOKEN：设置为套餐专属 API Key。

ANTHROPIC\_MODEL：设置为套餐支持的模型。

**配置步骤如下：**

1. 编辑或新增 settings.json 文件，需要修改或添加的配置信息如下：

<USER\_API\_KEY>：替换为您自己的 API Key。

<Model\_ID>：根据您购买的套餐，填入套餐支持的模型 ID。

专业套餐：具体模型请参考 [Token Plan 企业版专业套餐](https://cloud.tencent.com/document/product/1823/130659) 中的可用模型列表。

轻享套餐：具体模型请参考 [Token Plan 企业版轻享套餐](https://cloud.tencent.com/document/product/1823/131173#b18f9f4d-fad3-49a9-a38e-2ef38854fa19) 中的可用模型列表。

**注意：**

不同系统配置文件路径不同，具体如下：

MacOS / Linux：`~/.claude/settings.json`。

Windows：`C:\\Users\\<用户名>\\.claude\\settings.json`。

```json
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "<USER_API_KEY>",
        "ANTHROPIC_BASE_URL": "https://tokenhub.tencentmaas.com/plan/anthropic",
        "ANTHROPIC_MODEL": "<Model_ID>"
    }
}
```

2. 编辑或新增 .claude.json 文件，修改或新增 hasCompletedOnboarding 字段值为 `true`。

**注意：**

不同系统配置文件路径不同，具体如下：

MacOS / Linux：`~/.claude.json`

Windows：`C:\\Users\\<用户名>\\.claude.json`

```json
{
  "hasCompletedOnboarding": true
}
```

3. 保存配置文件后，在新的终端窗口执行后续命令。

## 在命令行中使用 Claude Code

通过命令行进入项目目录后，执行 `claude` 命令启动 Claude Code 即可开始使用。

```bash
cd my-project
claude
```

选择 **Yes, I trust this folder** 信任当前目录。

![](https://qcloudimg.tencent-cloud.cn/image/document/181060abf5d6b059a18e79d2c26b94c2.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/181060abf5d6b059a18e79d2c26b94c2.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/c84f9763488f361a5bf4d692e68d0072.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/c84f9763488f361a5bf4d692e68d0072.png)

## （可选）配置 Claude Code 子代理模型

Claude Code 在代码检索、任务规划等部分场景中，可能自动调用 Explore、Plan 等内置子代理。一般对话和基础代码任务无需额外配置。

若您需要使用子代理，或执行任务时出现以下错误，可在 settings.json 的 env 中补充 CLAUDE\_CODE\_SUBAGENT\_MODEL：

```json
Model <模型名称> is not supported by TokenPlan
API Error: 403
API Error: 500
```

**配置示例：**

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "<USER_API_KEY>",
    "ANTHROPIC_BASE_URL": "https://tokenhub.tencentmaas.com/plan/anthropic",
    "ANTHROPIC_MODEL": "<MODEL_ID>",
    "CLAUDE_CODE_SUBAGENT_MODEL": "<MODEL_ID>"
  }
}
```

CLAUDE\_CODE\_SUBAGENT\_MODEL 请填写当前 Token Plan 企业版套餐支持的模型 ID，建议与 ANTHROPIC\_MODEL 保持一致。修改配置后，请重新打开终端或重启 Claude Code，使配置生效。配置完成后，Claude Code 不会单独显示子代理模型配置成功提示。可通过触发 Explore、Plan 等子代理任务进行验证；若子代理能够正常完成任务，说明配置已生效。

## 在 IDE 中使用 Claude Code

**注意：**

Claude Code IDE 插件依赖 Claude Code CLI 工具，需先完成 Claude Code 的安装及配置。

VS Code

JetBrains

1. 在扩展市场搜索 Claude Code 进行安装。

![](https://qcloudimg.tencent-cloud.cn/image/document/14c30807bcef6ceb80be4ef94557ab72.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/14c30807bcef6ceb80be4ef94557ab72.png)

2. 安装成功后，单击 VS Code 右上角的 Claude Code 图标，进入 Claude Code 页面。

![](https://qcloudimg.tencent-cloud.cn/image/document/1df3f3b731adce5d45f9eadb93a9b7a8.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/1df3f3b731adce5d45f9eadb93a9b7a8.png)

3. 切换模型：在对话框中输入`/`，选择 **General config** 进入设置页面，在 **Selected Model** 中选择支持的模型，新建一个新窗口开始对话。

1. 在扩展市场中搜索 Claude Code 并安装。

![](https://qcloudimg.tencent-cloud.cn/image/document/8caa3cc75758215fb9977159bb715c3d.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/8caa3cc75758215fb9977159bb715c3d.png)

2. 安装后重启 IDE，单击右上角图标即可使用，您可以通过`/model <模型名称>`命令切换模型。

![](https://qcloudimg.tencent-cloud.cn/image/document/0bfcfc3d6eef72ad1537521b5b12da85.png)

![](https://qcloudimg.tencent-cloud.cn/image/document/0bfcfc3d6eef72ad1537521b5b12da85.png)

## 更多信息

如需进一步了解 Claude Code 的更多功能，请参考 [Claude Code 官方文档](https://code.claude.com/docs/)。
