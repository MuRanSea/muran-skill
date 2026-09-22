<!-- Official source: https://klingai.com/document-api/api/effects/video-effects.md -->
<!-- Source SHA-256: af6b9ad1f3d3d69b4d95b366da4a79321f496b830bb6450526fd149d6587b46d -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://klingai.com/document-api/llms.txt
> Use this file to discover all available pages before exploring further.

# 视频特效

> 来源: https://klingai.com/document-api/api/effects/video-effects
> 语言: zh
> 当前 Tab: 视频特效
> 此内容为面向 LLM 优化的 Markdown，已展开页面内 Tab，并省略页面目录、复制按钮等 UI 控件。

---

## 创建任务

### 接口概览

- Method: `POST`
- Path: `/v1/videos/effects`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### 说明

当前一共支持 206 款特效，您可以根据调用 effect_scene 实现不同的效果，详细内容请见：[特效模版中心](https://klingai.com/document-api/quickStart/productIntroduction/effectsCenter)

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Request Body

| 字段路径 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `effect_scene` | string | 是 | - | `pet_working_daily`, `pet_roll_window`, `pet_crash_earth`, `makeup_style`, `hair_dressup`, `critter_paste`, `wiggle_faces_pets`, `paw_headbang`, `pet_fitness`, `disco_paws`, `pet_diving`, `dj_pet`, `african_sway`, `jealousy_sway`, `shrug_dance`, `soccer_star`, `bra_hot_dance`, `arg_hot_dance`, `fra_hot_dance`, `bra_goal`, `arg_goal`, `por_goal`, `victory_slide`, `samba_fever`, `bicycle_kick`, `football_dance_2`, `red_card_sent_off`, `football_dance`, `magic_world_vlog`, `magic_world_vlog_9_16`, `air_dunk`, `whirling_beverage_9_16`, `tennis_trend`, `tennis_trend_9_16`, `football_live_9_16`, `whirling_beverage`, `f1_live`, `football_live`, `spielberg_transition`, `korean_baseball_9_16`, `korean_baseball`, `pet_skateboard`, `daily_ootd`, `tiny_beast_printer`, `landmark_reveal`, `winter_charm`, `flash_ride`, `maestro_of_magic`, `magic_carpet_ride`, `good_luck_spirit`, `shooting_star`, `sparkler_wand`, `sovereign_scepter`, `dirt_rush`, `return_of_the_king`, `dance_with_dragon`, `minimalist_light`, `martial_meow`, `sassy_shake`, `knock_at_a_door_revenge`, `palm_sized_figure_pro`, `prank_box`, `perler_beads`, `spring_bloom`, `toss_run`, `switch_to_silk`, `get_rich_quick`, `make_it_rain`, `twist_shake`, `the_hip_sway`, `send_my_love`, `funky_martian`, `wealth_drive`, `the_high_kick`, `the_exercise`, `lucky_veggie`, `studio_look`, `flash_drive`, `shush_my_dreams`, `french_elegance`, `finger_swipe`, `advent_of_flora`, `smooth_transition`, `kiss_pro`, `raid_check`, `snow_night_kiss`, `eternal_kiss`, `fortune_in_motion`, `chinese_trend`, `sedan_chair_dance`, `good_luck_dance`, `laicai_dance`, `yangge_dance`, `color_mixing`, `lantern_festival_cuju`, `unique_firework`, `unique_spring_couplets`, `horse_mask`, `fortune_knocks_cartoon`, `tangyuan_to_animal`, `hot_feet_dance`, `swag_dance`, `pigeon_dance`, `bloodline_dance`, `chanel_dance`, `cute_dance`, `love_theme_song`, `pumpitup_dance`, `city_to_village`, `fortune_god_transform`, `new_year_feast`, `ring_in_new`, `horse_year_firework`, `crystal_horse`, `drunk_dance`, `drunk_dance_pet`, `daoma_dance`, `bouncy_dance`, `smooth_sailing_dance`, `new_year_greeting`, `lion_dance`, `prosperity`, `great_success`, `golden_horse_fortune`, `red_packet_box`, `lucky_horse_year`, `lucky_red_packet`, `lucky_money_come`, `lion_dance_pet`, `dumpling_making_pet`, `fish_making_pet`, `pet_red_packet`, `lantern_glow`, `expression_challenge`, `overdrive`, `heart_gesture_dance`, `poping`, `martial_arts`, `running`, `nezha`, `motorcycle_dance`, `subject_3_dance`, `ghost_step_dance`, `phantom_jewel`, `zoom_out`, `cheers_2026`, `fight_pro`, `hug_pro`, `heart_gesture_pro`, `dollar_rain_pro`, `pet_bee_pro`, `countdown_teleport`, `santa_random_surprise`, `magic_match_tree`, `bullet_time_360`, `happy_birthday`, `birthday_star`, `thumbs_up_pro`, `tiger_hug_pro`, `pet_lion_pro`, `surprise_bouquet`, `bouquet_drop`, `glamour_photo_shoot`, `box_of_joy`, `first_toast_of_the_year`, `my_santa_pic`, `santa_gift`, `steampunk_christmas`, `snowglobe`, `christmas_photo_shoot`, `ornament_crash`, `santa_express`, `instant_christmas`, `coronation_of_frost`, `building_sweater`, `spark_in_the_snow`, `scarlet_and_snow`, `bullet_time_lite`, `jumping_ginger_joy`, `pure_white_wings`, `black_wings`, `golden_wing`, `pink_pink_wings`, `venomous_spider`, `throne_of_king`, `luminous_elf`, `woodland_elf`, `guardian_spirit`, `swish_swish`, `snowboarding`, `witch_transform`, `vampire_transform`, `pumpkin_head_transform`, `demon_transform`, `mummy_transform`, `zombie_transform`, `cute_pumpkin_transform`, `halloween_escape`, `pet_moto_rider`, `running_man`, `3d_cartoon_2`, `pet_dance`, `swing_swing`, `day_to_night`, `surfsurf`, `skateskate` | 场景名称 |
| `input` | object | 是 | - | - | 支持不同任务输入的结构体。根据 scene 不同，结构体里传的字段不同。 |
| `input.image` | string | 否 | - | - | 参考图像（用于单图特效） |
| `input.images` | array | 否 | - | - | 参考图像组（用于双图特效） |
| `callback_url` | string | 否 | - | - | 本次任务结果回调通知地址，如果配置，服务端会在任务状态发生变更时主动通知 |
| `external_task_id` | string | 否 | - | - | 自定义任务 ID |

#### Request Body 字段补充说明

- `effect_scene`: 更多参数请见: [特效模版中心](https://klingai.com/document-api/api/effects/templates)
- `input`: **单图特效（191款）** 场景包括：pet_working_daily, pet_roll_window, pet_crash_earth, makeup_style, hair_dressup, critter_paste, wiggle_faces_pets, paw_headbang, pet_fitness, disco_paws, pet_diving, dj_pet, african_sway, jealousy_sway, shrug_dance, soccer_star, bra_hot_dance, arg_hot_dance, fra_hot_dance, bra_goal, arg_goal, por_goal, victory_slide, samba_fever, bicycle_kick, football_dance_2, red_card_sent_off, football_dance, magic_world_vlog, magic_world_vlog_9_16, air_dunk, whirling_beverage_9_16, tennis_trend, tennis_trend_9_16, football_live_9_16, whirling_beverage, f1_live, football_live, spielberg_transition, korean_baseball_9_16, korean_baseball, tiny_beast_printer, landmark_reveal, winter_charm, flash_ride, maestro_of_magic, magic_carpet_ride, good_luck_spirit, shooting_star, sparkler_wand, sovereign_scepter, dirt_rush, return_of_the_king, dance_with_dragon, minimalist_light, martial_meow, sassy_shake, knock_at_a_door_revenge, palm_sized_figure_pro, prank_box, perler_beads, spring_bloom, get_rich_quick, make_it_rain, twist_shake, the_hip_sway, send_my_love, funky_martian, wealth_drive, the_high_kick, the_exercise, lucky_veggie, flash_drive, shush_my_dreams, advent_of_flora, raid_check, fortune_in_motion, chinese_trend, sedan_chair_dance, good_luck_dance, laicai_dance, yangge_dance, color_mixing, lantern_festival_cuju, unique_firework, unique_spring_couplets, horse_mask, fortune_knocks_cartoon, tangyuan_to_animal, hot_feet_dance, swag_dance, pigeon_dance, bloodline_dance, chanel_dance, cute_dance, love_theme_song, pumpitup_dance, city_to_village, fortune_god_transform, new_year_feast, ring_in_new, horse_year_firework, crystal_horse, drunk_dance, drunk_dance_pet, daoma_dance, bouncy_dance, smooth_sailing_dance, new_year_greeting, lion_dance, prosperity, great_success, golden_horse_fortune, red_packet_box, lucky_horse_year, lucky_red_packet, lucky_money_come, lion_dance_pet, dumpling_making_pet, fish_making_pet, pet_red_packet, lantern_glow, expression_challenge, overdrive, heart_gesture_dance, poping, martial_arts, running, nezha, motorcycle_dance, subject_3_dance, ghost_step_dance, phantom_jewel, zoom_out, dollar_rain_pro, pet_bee_pro, countdown_teleport, santa_random_surprise, magic_match_tree, bullet_time_360, happy_birthday, birthday_star, thumbs_up_pro, tiger_hug_pro, pet_lion_pro, surprise_bouquet, bouquet_drop, glamour_photo_shoot, box_of_joy, first_toast_of_the_year, my_santa_pic, santa_gift, steampunk_christmas, snowglobe, christmas_photo_shoot, ornament_crash, santa_express, instant_christmas, coronation_of_frost, building_sweater, spark_in_the_snow, scarlet_and_snow, bullet_time_lite, jumping_ginger_joy, pure_white_wings, black_wings, golden_wing, pink_pink_wings, venomous_spider, throne_of_king, luminous_elf, woodland_elf, guardian_spirit, swish_swish, snowboarding, witch_transform, vampire_transform, pumpkin_head_transform, demon_transform, mummy_transform, zombie_transform, cute_pumpkin_transform, halloween_escape, pet_moto_rider, running_man, 3d_cartoon_2, pet_dance, swing_swing, day_to_night, surfsurf, skateskate
- `input`: **双图特效（15款）** 场景包括：pet_skateboard, daily_ootd, toss_run, switch_to_silk, studio_look, french_elegance, finger_swipe,  smooth_transition, snow_night_kiss, eternal_kiss, cheers_2026, kiss_pro, fight_pro, hug_pro, heart_gesture_pro
- `input.image`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `input.image`: 注意：若您使用 Base64 方式，请不要在 Base64 编码字符串前添加任何前缀（如 `data:image/png;base64,`），直接传递 Base64 编码后的字符串即可。
- `input.image`: 正确的 Base64 编码参数：
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `input.image`: 错误的 Base64 编码参数（包含 data: 前缀）：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `input.image`: 图片格式支持 .jpg / .jpeg / .png
- `input.image`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比介于 1:2.5 ~ 2.5:1 之间
- `input.images`: 数组的长度必须是 2，上传的第一张图在合照的左边，上传的第二张图在合照的右边
- `input.images`: 该服务包含合照功能，即用户上传两张人像图，可灵 AI 将自适应拼接为合照
  ![合照效果](https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/kling-api-document/video-effects-group-photo.jpeg)
- `input.images`: 支持传入图片 Base64 编码或图片 URL（确保可访问）
- `input.images`: 注意：若您使用 Base64 方式，请不要在 Base64 编码字符串前添加任何前缀（如 `data:image/png;base64,`），直接传递 Base64 编码后的字符串即可。
- `input.images`: **正确的 Base64 编码参数：**
  ```plaintext
  iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `input.images`: 错误的 Base64 编码参数（包含 data: 前缀）：
  ```plaintext
  data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...
  ```
- `input.images`: 图片格式支持 .jpg / .jpeg / .png
- `input.images`: 图片文件大小不能超过 10MB，图片宽高尺寸不小于 300px，图片宽高比介于 1:2.5 ~ 2.5:1 之间
- `callback_url`: 具体通知的消息 schema 见 [Callback 协议](https://klingai.com/document-api/api/get-started/callbacks)
- `external_task_id`: 用户自定义任务 ID，传入不会覆盖系统生成的任务 ID，但支持通过该 ID 进行任务查询
- `external_task_id`: 请注意，单用户下需要保证唯一性

### Request Example

```bash
curl --request POST \
  --url https://api-beijing.klingai.com/v1/videos/effects \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
    "effect_scene": "color_mixing",
    "input": {
      "image": "https://p4-kling.klingai.com/kcdn/cdn-kcdn112452/kling-op/effects_raw_pic/color_mixing.jpeg"
    }
  }'
```

### Response Example

```json
{
  "code": 0, //错误码；具体定义见错误码
  "message": "string", //错误信息
  "request_id": "string", //请求ID，系统生成，用于跟踪请求、排查问题
  "data":{
    "task_id": "string", //任务ID，系统生成
    "task_info":{ //任务创建时的参数信息
       "external_task_id": "string" //客户自定义任务ID
    },
    "task_status": "string", //任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "created_at": 1722769557708, //任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
  }
}
```

---

### 单图特效请求示例

```json
{
    "effect_scene": "pet_lion_pro",
    "input": {
        "image": "https://p4-kling.klingai.com/bs2/upload-ylab-stunt/c54e463c95816d959602f1f2541c62b2.png?x-kcdn-pid=112452"
    }
}
```

### 双图特效请求示例

```json
{
    "effect_scene": "hug_pro",
    "input": {
        "images": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
    }
}
```

---

## 查询任务（单个）

### 接口概览

- Method: `GET`
- Path: `/v1/videos/effects/{id}`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

### Headers

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `Content-Type` | string | 是 | `application/json` | - | 数据交换格式 |
| `Authorization` | string | 是 | - | - | 鉴权信息，参考接口鉴权 |

### Path Params

| 字段 | 类型 | 必填 | 默认值 | 可选值 | 说明 |
|---|---|---:|---|---|---|
| `task_id` | string | 否 | - | - | 视频特效的任务 ID |
| `external_task_id` | string | 否 | - | - | 视频特效的自定义任务 ID |

#### Path Params 字段补充说明

- `task_id`: 请求路径参数，直接将值填写在请求路径中
- `task_id`: 与 external_task_id 两种查询方式二选一
- `external_task_id`: 创建任务时填写的 external_task_id
- `external_task_id`: 与 task_id 两种查询方式二选一

### Request Example

```bash
curl --request GET \
  --url https://api-beijing.klingai.com/v1/videos/effects/{task_id} \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": {
    "task_id": "string", // 任务ID，系统生成
    "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
    "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
    "task_info": { //任务创建时的参数信息
      "external_task_id": "string" //客户自定义任务ID
    },
    "task_result": {
      "videos": [
        {
          "id": "string", // 生成的视频ID；全局唯一
          "url": "string", // 生成视频的URL，例如https://p1.a.kwimgs.com/bs2/upload-ylab-stunt/special-effect/output/HB1_PROD_ai_web_46554461/-2878350957757294165/output.mp4（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
          "watermark_url": "string", // 含水印视频下载URL，防盗链格式
        }
      ]
    },
    "watermark_info": {
      "enabled": boolean
    },
    "final_unit_deduction": "string", // 任务最终扣减积分数值
    "final_balance_deduction": { // 额度扣减信息
      "quota": "string", // 额度扣减折扣价
      "list_price": "string" // 额度扣减刊例价
    },
    "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
    "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
  }
}
```

---

## 查询任务（列表）

### 接口概览

- Method: `GET`
- Path: `/v1/videos/effects`
- Auth: `Authorization: Bearer <API_KEY>`
- Content-Type: `application/json`

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

- `pageNum`: 取值范围：[1, 1000]
- `pageSize`: 取值范围：[1, 500]

### Request Example

```bash
curl --request GET \
  --url 'https://api-beijing.klingai.com/v1/videos/effects?pageNum=1&pageSize=30' \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json'
```

### Response Example

```json
{
  "code": 0, // 错误码；具体定义见错误码
  "message": "string", // 错误信息
  "request_id": "string", // 请求ID，系统生成，用于跟踪请求、排查问题
  "data": [
    {
      "task_id": "string", // 任务ID，系统生成
      "task_status": "string", // 任务状态，枚举值：submitted（已提交）、processing（处理中）、succeed（成功）、failed（失败）
      "task_status_msg": "string", // 任务状态信息，当任务失败时展示失败原因（如触发平台的内容风控等）
      "task_info": { //任务创建时的参数信息
        "external_task_id": "string" //客户自定义任务ID
      },
      "task_result": {
        "videos": [
          {
            "id": "string", // 生成的视频ID；全局唯一
            "url": "string", // 生成视频的URL，例如https://p1.a.kwimgs.com/bs2/upload-ylab-stunt/special-effect/output/HB1_PROD_ai_web_46554461/-2878350957757294165/output.mp4（请注意，为保障信息安全，生成的图片/视频会在30天后被清理，请及时转存）
            "watermark_url": "string", // 含水印视频下载URL，防盗链格式
          }
        ]
      },

      "final_unit_deduction": "string", // 任务最终扣减积分数值
      "final_balance_deduction": { // 额度扣减信息
        "quota": "string", // 额度扣减折扣价
        "list_price": "string" // 额度扣减刊例价
      },
      "created_at": 1722769557708, // 任务创建时间，Unix时间戳、单位ms
      "updated_at": 1722769557708 //任务更新时间，Unix时间戳、单位ms
    }
  ]
}
```
