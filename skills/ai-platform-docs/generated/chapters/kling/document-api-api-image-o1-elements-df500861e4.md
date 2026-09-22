<!-- Official source: https://klingai.com/document-api/api/image/o1/elements.md -->
<!-- Source SHA-256: 7ca496c16292859a02b16476aef30aa6aa483843d1f2fed97972cd9004fd0a00 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 主体管理

> 来源: https://klingai.com/document-api/api/image/o1/elements
> 语言: zh
> 当前 Tab: 主体管理
> 同组 Tab: 图片生成 / 主体管理
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建主体

### 接口概览

- Method: `POST`
- Path: `/v1/general/advanced-custom-elements`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 创建主体相关服务已升级至全新版本，如需浏览旧版请移步[可灵AI【旧版】主体相关API文档](https://ksurl.cn/0DJoJIiX)

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `element_name` | string | 是 | - | - | 主体名称 |
| `element_description` | string | 是 | - | - | 主体描述 |
| `reference_type` | string | 是 | - | `video_refer`, `image_refer` | 主体参考方式 |
| `element_image_list` | object | 否 | `None` | - | 主体参考图，可通过多张图片设定主体及其细节 |
| `element_video_list` | object | 否 | `None` | - | 主体参考视频，可通过视频设定主体及其细节 |
| `element_voice_id` | string | 否 | `None` | - | 主体音色ID，可绑定音色库中已有音色 |
| `tag_list` | array | 否 | `None` | - | 为主体配置标签，一个主体可以配置多个标签 |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |
| `external_task_id` | string | 否 | - | - | 自定义任务ID。用户自定义任务ID，传入不会覆盖系统生成的任务ID，但支持通过该ID进行任务查询。请注意，单用户下需要保证唯一性 |

#### Request Body 字段补充说明

- `element_name`: 不能超过20个字符
- `element_description`: 不能超过100个字符
- `reference_type`: video_refer: 视频角色主体，此时将参考element_video_list定义主体外表
- `reference_type`: image_refer: 多图主体，此时将参考element_image_list定义主体外表
- `reference_type`: 通过视频定制的主体和通过图片定制的主体的可用范围不同，详见能力地图和参数说明。
- `element_image_list`: 包括正面参考图和其他角度或特写参考图，其中：至少包括1张正面参考图，由frontal_image参数定义；需包括1～3张其他参考图，需与正面参考图有差异，由image_url参数定义
- `element_image_list`: 用key:value承载，如下：
- `element_image_list`: ```json
  "element_image_list": {
  "frontal_image": "image_url_0", 
  "refer_images": [{ "image_url": "image_url_1" }, ...] 
  }
  ```
- `element_image_list`: 支持传入图片Base64编码或图片URL（确保可访问）
- `element_image_list`: 图片格式支持.jpg / .jpeg / .png。图片文件大小不能超过10MB，图片宽高尺寸不小于300px，图片宽高比要在1:2.5 ~ 2.5:1之间
- `element_image_list`: reference_type参数值为 image_refer 时，当前参数必填
- `element_video_list`: 可上传有声视频，有声视频包含人声则触发音色定制（定制+入音色库+与主体绑定）
- `element_video_list`: 暂时仅支持通过视频定制写实风格的人形形象
- `element_video_list`: 参考视频时当前参数必填，参考图片时当前参数无效
- `element_video_list`: 用key:value承载。视频格式仅支持MP4/MOV。仅支持时长介于3s～8s之间、宽高比例需为16:9或9:16的1080P视频。至多仅支持上传1段视频，视频大小不超过200MB。video_url参数值不得为空
- `element_video_list`: ```json
  "element_video_list": {
  "refer_videos": [{ "video_url": "video_url_1" }, ...] 
  }
  ```
- `element_video_list`: 视频定制的主体仅支持用于 kling-video-o3 及之后的模型
- `element_voice_id`: 当前参数为空时，当前主体不绑定音色
- `element_voice_id`: 为多图主体绑定音色时，仅支持人物形象主体或类人形象主体
- `element_voice_id`: 可通过音色相关API获取ID，详见[点此查看](https://klingai.com/document-api/api/video/3-0-omni/voice-customization)
- `tag_list`: 用key:value承载。tag的ID与名称：o_101 热梗, o_102 人物, o_103 动物, o_104 道具, o_105 服饰, o_106 场景, o_107 特效, o_108 其他
- `tag_list`: ```json
  "tag_list": [ { "tag_id": "o_101" }, { "tag_id": "o_102" } ]
  ```
- `tag_list`: tag和tag_id的对应关系如下：
   | tag_id | tag_name |
   | ------- | -------- |
   | o_101   | 热梗     |
   | o_102   | 人物     |
   | o_103   | 动物     |
   | o_104   | 道具     |
   | o_105   | 服饰     |
   | o_106   | 场景     |
   | o_107   | 特效     |
   | o_108   | 其他     |
- `callback_url`: 具体通知的消息schema见 [Callback协议](https://klingai.com/document-api/api/get-started/callbacks)

### Response Example

```json
{
  "code": 0, //错误码；具体定义见错误码
  "message": "string", //错误信息
  "request_id": "string", //请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", //任务ID，系统生成
    "task_info": { //任务创建时的参数信息
      "external_task_id": "string" //客户自定义任务ID
    },
    "task_status": "string", //任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "created_at": 1722769557708, //任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
  }
}
```

## 调用示例

### 创建图片定制主体

```Bash
curl --location 'https://xxx/v1/general/advanced-custom-elements/' \
--header 'Authorization: Bearer xxx' \
--header 'Content-Type: application/json\' \
--data '{
    "element_name": "xxx",
    "element_description": "xxx",
    "reference_type": "image_refer",
    "element_image_list": {
      "frontal_image": "xxx",
      "refer_images": [
        {"image_url": "xxx"},
        {"image_url": "xxx"}
      ]
    },
    "element_voice_id": string,
    "callback_url": "xxx",
    "external_task_id": "",
     "tag_list": [
        {
            "tag_id": "xxx"
        }
    ]
  }'
```

### 创建视频定制主体

```Bash
curl --location 'https://xxx/v1/general/advanced-custom-elements/' \
--header 'Authorization: Bearer xxx' \
--header 'Content-Type: application/json\' \
--data '{
    "element_name": "xxx",
    "element_description": "xxx",
    "reference_type": "video_refer",
    "element_video_list": {
        "refer_videos": [
            {
                "video_url": "xxx"
            }
        ]
    },
    "element_voice_id": string,
    "callback_url": "xxx",
    "external_task_id": "",
    "tag_list": [
        {
            "tag_id": "xxx"
        }
    ]
}'
```

---

## 查询自定义主体（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/general/advanced-custom-elements/{id}`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 创建主体相关服务已升级至全新版本，如需浏览旧版请移步[可灵AI【旧版】主体相关API文档](https://ksurl.cn/0DJoJIiX)

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Path Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_id` | string | 是 | - | - | 图片生成的任务ID。请求路径参数，直接将值填写在请求路径中 |
| `external_task_id` | string | 否 | - | - | 用户自定义任务 ID |

#### Path Params 字段补充说明

- `external_task_id`: 创建任务时填写的 external_task_id，与 task_id 两种查询方式二选一
  - 请注意，单用户下需要保证唯一性

### Response Example

```json
{
  "code": 0, //错误码；具体定义见错误码
  "message": "string", //错误信息
  "request_id": "string", //请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", //任务ID，系统生成
    "task_status": "string", //任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_status_msg": "string", //任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
    "task_info": { //任务创建时的参数信息
      "external_task_id": "string" //客户自定义任务ID
    },
    "task_result": {
      "elements": [
        {
          "element_id": 0, //主体ID
          "element_name": "string", //主体名称
          "element_description": "string", //主体描述
          "reference_type": "video_refer", //参考方式
          "element_image_list": {},
          "element_video_list": {},
          "element_voice_info": {
            "voice_id": "string", //定制的音色的ID；全局唯一
            "voice_name": "string", //定制的音色的名称
            "trial_url": "string", //定制的音色的试听音频下载URL
            "owned_by": "kling" //音色来源，kling为官方音色库，数字为创作者ID
          },
          "tag_list": [],
          "owned_by": "kling", //主体来源，kling为官方主体库，其他为创作者ID
          "status": "succeed" //主体状态，正常时为succeed，已被删除时为 deleted
        }
      ]
    },
    "final_unit_deduction": "string", //任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "created_at": 1722769557708, //任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询自定义主体（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/general/advanced-custom-elements`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 创建主体相关服务已升级至全新版本，如需浏览旧版请移步[可灵AI【旧版】主体相关API文档](https://ksurl.cn/0DJoJIiX)

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `pageNum` | int | 否 | `1` | - | 页码 |
| `pageSize` | int | 否 | `30` | - | 每页数据量 |

#### Query Params 字段补充说明

- `pageNum`: 取值范围：[1,1000]
- `pageSize`: 取值范围：[1,500]

### Response Example

```json
{
  "code": 0, //错误码；具体定义见错误码
  "message": "string", //错误信息
  "request_id": "string", //请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "task_id": "string", //任务ID，系统生成
      "task_status": "string", //任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "task_status_msg": "string", //任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "task_info": { //任务创建时的参数信息
        "external_task_id": "string" //客户自定义任务ID
      },
      "task_result": {
        "elements": [
          {
            "element_id": 0,
            "element_name": "string",
            "element_description": "string",
            "reference_type": "video_refer",
            "element_image_list": {},
            "element_video_list": {},
            "element_voice_info": {},
            "tag_list": [],
            "owned_by": "kling", //主体来源，kling为官方主体库，其他为创作者ID
            "status": "succeed" //主体状态，正常时为succeed，已被删除时为 deleted
          }
        ]
      },
      "final_unit_deduction": "string", //任务最终扣减积分数值
      "final_balance_deduction": { // 额度扣减信息
        "quota": "string", // 额度扣减折扣价
        "list_price": "string" // 额度扣减刊例价
      },
      "created_at": 1722769557708, //任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
    }
  ]
}
```

---

## 查询官方主体（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/general/advanced-presets-elements`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 创建主体相关服务已升级至全新版本，如需浏览旧版请移步[可灵AI【旧版】主体相关API文档](https://ksurl.cn/0DJoJIiX)

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Query Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `pageNum` | int | 否 | `1` | - | 页码 |
| `pageSize` | int | 否 | `30` | - | 每页数据量 |

#### Query Params 字段补充说明

- `pageNum`: 取值范围：[1,1000]
- `pageSize`: 取值范围：[1,500]

### Response Example

```json
{
  "code": 0, //错误码；具体定义见错误码
  "message": "string", //错误信息
  "request_id": "string", //请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "task_id": "string", //任务ID，系统生成
      "task_status": "string", //任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "task_status_msg": "string", //任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "task_info": { //任务创建时的参数信息
        "external_task_id": "string" //客户自定义任务ID
      },
      "task_result": {
        "elements": [
          {
            "element_id": 0,
            "element_name": "string",
            "element_description": "string",
            "reference_type": "video_refer",
            "element_image_list": {},
            "element_video_list": {},
            "element_voice_info": {},
            "tag_list": [],
            "owned_by": "kling", //主体来源，kling为官方主体库，其他为创作者ID
            "status": "succeed" //主体状态，正常时为succeed，已被删除时为 deleted
          }
        ]
      },
      "created_at": 1722769557708, //任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
    }
  ]
}
```

---

## 删除自定义主体

### 接口概览

- Method: `POST`
- Path: `/v1/general/delete-elements`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

> 删除自定义主体相关服务已原地升级，无需移步其他文档

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `element_id` | string | 是 | - | - | 要删除的主体ID，仅支持删除自定义主体 |

### Response Example

```json
{
  "code": 0, //错误码；具体定义见错误码
  "message": "string", //错误信息
  "request_id": "string", //请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", //任务ID，系统生成
    "task_status": "string" //任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
  }
}
```
