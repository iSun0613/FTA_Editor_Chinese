# 多服务商 AI 配置指南

FTA Editor 现支持**国内外多家 AI 服务商**：国内/本地服务商（DeepSeek、通义千问、智谱清言、Kimi、Ollama 本地）与国际服务商（OpenAI、Anthropic Claude、Google Gemini）。本指南帮助你选择并配置最适合自己的方案。

> **国内用户建议优先使用下方的国内 / 本地服务商**：端点与默认模型已由程序内置，开箱即可直连使用。

---

## 国内服务商（推荐优先）

国内服务商均走 OpenAI 兼容接口（复用现有 `openai` SDK，无需新增依赖），端点已由程序内置，通常无需改动，只需填入各自的 API 密钥。Kimi 新模型的 temperature（温度参数，控制输出随机性）由程序自动适配。

> 说明：以下「开通地址」为各服务商申请 API 密钥（API Key，调用接口所需的鉴权令牌）的官方平台。

### 1. DeepSeek（深度求索）

**推荐模型：** `deepseek-v4-flash` / `deepseek-v4-pro`

**开通地址：** https://platform.deepseek.com

**配置步骤：**

1. 访问上面开通地址，注册 / 登录你的账号
2. 在控制台创建并复制 API 密钥
3. 在 FTA Editor 的 AI 设置中：
   - **服务商（Provider）**：选择 "DeepSeek"
   - **API 密钥**：粘贴你的 DeepSeek API 密钥
   - **端点（Endpoint）**：程序已内置，一般无需改动
   - **模型（Model）**：选择 `deepseek-v4-flash`（推荐，速度快）或 `deepseek-v4-pro`（更高能力）
4. 点击 **测试并保存（Test & Save）**

**适用场景：** 性价比高，适合日常 FTA 推理分析与批量分析。

---

### 2. 通义千问（Aliyun DashScope）

**推荐模型：** `qwen3.8-max`（最强）/ `qwen3.8-flash`（快速）/ `qwen3.7-plus`（均衡）

**开通地址：** https://dashscope.console.aliyun.com

**配置步骤：**

1. 访问上面开通地址（阿里云百炼平台），注册 / 登录
2. 开通模型服务并获取 API 密钥
3. 在 FTA Editor 的 AI 设置中：
   - **服务商**：选择 "通义千问"（或对应 DashScope 选项）
   - **API 密钥**：粘贴你的密钥
   - **端点（Endpoint）**：程序已内置，一般无需改动
   - **模型（Model）**：选择 `qwen3.8-max`、`qwen3.8-flash` 或 `qwen3.7-plus`（按需）
4. 点击 **测试并保存**

**适用场景：** 中文理解能力强，兼顾能力与速度，适合中文故障树分析与改进建议。

---

### 3. 智谱清言（Zhipu AI / BigModel）

**推荐模型：** `glm-5.3` / `glm-5.3-flash` / `glm-4.7-flash`

**开通地址：** https://open.bigmodel.cn

**配置步骤：**

1. 访问上面开通地址，注册 / 登录
2. 在控制台创建 API 密钥
3. 在 FTA Editor 的 AI 设置中：
   - **服务商**：选择 "智谱清言"
   - **API 密钥**：粘贴你的密钥
   - **端点（Endpoint）**：程序已内置，一般无需改动
   - **模型（Model）**：选择 `glm-5.3`（最强）、`glm-5.3-flash`（快速）或 `glm-4.7-flash`（轻量）
4. 点击 **测试并保存**

**适用场景：** 通用能力出色，flash 系列适合对响应速度要求高的场景。

---

### 4. Kimi（Moonshot，月之暗面）

**推荐模型：** `kimi-k3` / `kimi-k2.7-code`

**开通地址：** https://platform.moonshot.cn

**配置步骤：**

1. 访问上面开通地址，注册 / 登录
2. 在平台创建并复制 API 密钥
3. 在 FTA Editor 的 AI 设置中：
   - **服务商**：选择 "Kimi"
   - **API 密钥**：粘贴你的密钥
   - **端点（Endpoint）**：程序已内置，一般无需改动
   - **模型（Model）**：选择 `kimi-k3`（最新）或 `kimi-k2.7-code`
4. 点击 **测试并保存**

> 提示：Kimi 新模型的 temperature 由程序自动适应，无需手动调整。

**适用场景：** 长文本理解与复杂分析，适合需要深入推理的故障树评估。

---

### 5. Ollama 本地（本地部署，免密钥）

**推荐模型：** `qwen3:8b` / `llama3.3:70b` / `qwen2.5`

**特点：**
- 完全本地运行，数据不出本地，**无需 API 密钥**
- 免费使用，无调用限额（限额与本地硬件资源相关）

**配置步骤：**

1. 安装 [Ollama](https://ollama.com/) 并在本机启动服务
2. 拉取（pull）所需的本地模型，例如：
   ```
   ollama pull qwen3:8b
   ```
3. 在 FTA Editor 的 AI 设置中：
   - **服务商**：选择 "Ollama 本地"
   - **API 密钥**：留空即可
   - **模型（Model）**：选择已拉取的模型（`qwen3:8b`、`llama3.3:70b` 或 `qwen2.5`，按需）
4. 点击 **测试并保存**

**适用场景：** 对数据隐私要求高、希望离线使用或避免云端费用的用户。

---

## 国际服务商（备选）

> 国内用户可优先使用上方国内服务商；下方国际服务商可按需选用。

### 1. Google Gemini（适合预算敏感用户）

**Pros（优点）：**
- 提供免费额度（limits 一般为每分钟 15 次请求）
- 超出免费额度后按量付费
- 响应速度快
- 对 FTA 分析而言质量不错

**Cons（缺点）：**
- 免费额度有速率限制
- 不适合高并发自动化分析

**配置步骤：**

1. 前往 [Google AI Studio](https://aistudio.google.com/apikey)
2. 点击 **Create API Key（创建 API 密钥）**
3. 选择或新建你的 Google Cloud 项目
4. 复制生成的 API 密钥
5. 在 FTA Editor 的 AI 设置中：
   - **服务商**：选择 "Google Gemini"
   - **API 密钥**：粘贴你的 Gemini API 密钥
   - **端点（Endpoint）**：自动填充为 `https://generativelanguage.googleapis.com/v1beta`
   - **模型（Model）**：在下拉列表中选择可用的 Gemini 模型
6. 点击 **测试并保存**

**成本估算：**
- 免费：每分钟 15 次请求
- 付费：约 $0.075 / 1M（百万）输入 token（约为每次 FTA 分析 $0.001）

**参考文档**：https://ai.google.dev

---

### 2. Anthropic Claude（适合复杂推理）

**Pros（优点）：**
- 出色的推理与分析能力
- 适合复杂的 FTA 逻辑评估
- 定价透明
- 文档完善

**Cons（缺点）：**
- 无免费额度
- 单 token 成本高于 Gemini
- 需要绑定境外支付方式

**配置步骤：**

1. 前往 [Anthropic Console](https://console.anthropic.com/)
2. 注册或登录账号
3. 在侧边栏进入 **API Keys**
4. 点击 **Create Key**
5. 复制 API 密钥
6. 添加计费信息（需要信用卡 / 借记卡）
7. 在 FTA Editor 的 AI 设置中：
   - **服务商**：选择 "Anthropic Claude"
   - **API 密钥**：粘贴你的 Claude API 密钥
   - **端点（Endpoint）**：自动填充为 `https://api.anthropic.com`
   - **模型（Model）**：在下拉列表中选择可用的 Claude 模型
8. 点击 **测试并保存**

**成本估算：**
- 约 $3 / 1M 输入 token，约 $15 / 1M 输出 token（约为每次 FTA 分析 $0.02-0.05）

**参考文档**：https://docs.anthropic.com/

---

### 3. OpenAI（适合通用用途）

**Pros（优点）：**
- 最可靠、使用最广泛
- 质量优秀
- 速度快
- 文档完善

**Cons（缺点）：**
- 无免费额度
- 成本高于 Gemini
- 需要境外账号与支付方式

**配置步骤：**

1. 前往 [OpenAI Platform](https://platform.openai.com/)
2. 注册或登录
3. 进入 **Dashboard**（控制台）→ **API keys**
4. 点击 **Create new secret key（创建新的密钥）**
5. 复制密钥（仅显示一次，请妥善保存）
6. 设置计费：
   - 进入 **Settings** → **Billing**
   - 添加支付方式
   - 按需设置用量上限（建议每月 $10-50）
7. 在 FTA Editor 的 AI 设置中：
   - **服务商**：选择 "OpenAI"
   - **API 密钥**：粘贴你的 OpenAI API 密钥
   - **端点（Endpoint）**：自动填充为 `https://api.openai.com/v1`
   - **模型（Model）**：在下拉列表中选择可用的 GPT 模型
8. 点击 **测试并保存**

**成本控制建议：**
```
1. 在 OpenAI 设置中设定用量上限（如每月 $10）
2. 优先选择性价比更高的模型
3. 常规 FTA 分析每月费用通常在 $2-10
```

**参考文档**：https://platform.openai.com/docs/

## 服务商快速对比

| 服务商 | 类型 | 免费额度 | 推荐模型 | 备注 |
|--------|------|---------|---------|------|
| **DeepSeek** | 国内 | 按官方政策 | `deepseek-v4-flash` / `deepseek-v4-pro` | 性价比高 |
| **通义千问** | 国内 | 按官方政策 | `qwen3.8-max` / `qwen3.8-flash` | 中文能力强 |
| **智谱清言** | 国内 | 按官方政策 | `glm-5.3` / `glm-5.3-flash` | 均衡通用 |
| **Kimi** | 国内 | 按官方政策 | `kimi-k3` / `kimi-k2.7-code` | 长文本 / 推理强 |
| **Ollama 本地** | 本地 | 免费（免密钥） | `qwen3:8b` / `llama3.3:70b` | 离线 / 隐私 |
| Google Gemini | 国际 | ✅ 免费额度 | 下拉选择 | 有免费额度 |
| Anthropic Claude | 国际 | ❌ | 下拉选择 | 境外支付 |
| OpenAI | 国际 | ❌ | 下拉选择 | 境外支付 |

---

## 切换服务商

你可以随时在多个服务商之间切换：

1. 在 AI 助手面板中点击 **⚙（设置）** 按钮
2. 从下拉列表选择不同服务商
3. 端点与模型选项会自动更新
4. 输入新服务商的 API 密钥
5. 点击 **测试并保存**

你的凭据安全地保存在本地电脑上（`~/.fta_editor/ai_credentials.json`），可同时维护多套服务商配置。

---

## 故障排查

### 提示"Cannot connect / 连接失败"

**针对国内服务商（DeepSeek / 通义千问 / 智谱 / Kimi）：**
- 确认 API 密钥格式与开通状态是否正确
- 确认账号已开通对应模型
- 检查本机能否正常访问该服务商官网

**针对 Gemini：**
- 确认使用了正确的密钥格式（形如 `AIzaSy...`）
- 确认在 Google Cloud 项目中已启用相关 API
- 确认网络可连通 `generativelanguage.googleapis.com`（可能需要代理）

**针对 Claude：**
- 确认密钥以 `sk-ant-` 开头
- 确认已设置计费且账号状态正常
- 确认网络可连通 `api.anthropic.com`

**针对 OpenAI：**
- 确认密钥以 `sk-` 开头
- 确认有有效计费与用量限额
- 确认网络可连通 `api.openai.com`

### 提示模型不存在（Model not found）

- 部分模型可能未在所选区域/账号下开放
- 从下拉列表换用其他模型
- 查阅服务商文档确认当前账号可用的模型

### 触发速率限制（Rate limiting）

- **国内服务商**：查看各平台免费额度的调用限额
- 国际服务商可参考原文对比（如 Gemini 免费额度为每分钟 15 次）

### API 密钥泄露（安全）

如果你不小心泄露了 API 密钥：

1. **立即在服务商控制台吊销（Revoke）该密钥**
2. 在 FTA Editor 设置中点击 **清除（Clear）** 删除已保存的凭据
3. 生成新的 API 密钥
4. 在 FTA Editor 中重新配置

---

## 成本优化建议

### 1. 优先使用本地 / 免费方案
- 先用 Ollama 本地模型或各国内服务商的免费额度做验证
- 测试好 FTA 分析流程后，再按需升级付费

### 2. 选择合适的模型
- 简单分析：使用轻量模型（如 `qwen3.8-flash`、`glm-4.7-flash`、`deepseek-v4-flash`）
- 复杂分析：使用更强模型（如 `qwen3.8-max`、`deepseek-v4-pro`）

### 3. 设置用量上限
- 国内服务商与 OpenAI 等平台均可在控制台设置月度预算 / 限额

### 4. 批量分析
- 在同一个对话会话中合并多个问题
- 减少重复开销与 token（令牌，接口计费单位）消耗

### 5. 监控用量
- 定期查看服务商控制台的用量统计

---

## 推荐配置方案

### 方案 1：低成本（学习 / 测试）
```
服务商：Ollama 本地 或 任选一家国内服务商免费额度
模型：qwen3:8b 或 qwen3.8-flash
成本：免费（有额度 / 硬件限制）
适用：学习、测试、简单分析
```

### 方案 2：常规使用（个人 / 小团队）
```
服务商：DeepSeek（主） + 通义千问（备）
模型：deepseek-v4-flash → qwen3.8-flash
成本：低
适用：常规 FTA 分析、小型工程团队
```

### 方案 3：专业使用（复杂分析）
```
服务商：DeepSeek 或 通义千问 或 智谱清言
模型：deepseek-v4-pro 或 qwen3.8-max 或 glm-5.3
成本：中
适用：复杂分析、专业工程工作
```

### 方案 4：高隐私 / 离线分析
```
服务商：Ollama 本地
模型：qwen3:8b 或 llama3.3:70b
成本：仅消耗本机资源
适用：数据敏感、需要离线使用
```

---

## API 密钥安全最佳实践

1. **切勿把密钥提交到仓库**：密钥保存在 `~/.fta_editor/ai_credentials.json`
2. **泄露后立即重建**：在服务商控制台删除旧密钥并创建新密钥
3. **使用最小权限**：只授予必要权限（如 GitHub 的 `read:user`）
4. **设置用量上限**：在服务商控制台开启计费告警与限额
5. **定期轮换**：建议每 6 个月轮换一次密钥以保障安全

---

## 参考资源

**国内 / 本地服务商：**
- **DeepSeek**：https://platform.deepseek.com
- **通义千问**：https://dashscope.console.aliyun.com
- **智谱清言**：https://open.bigmodel.cn
- **Kimi**：https://platform.moonshot.cn
- **Ollama**：https://ollama.com/

**国际服务商：**
- **Google Gemini**：https://ai.google.dev
- **Anthropic Claude**：https://www.anthropic.com/
- **OpenAI**：https://openai.com/

**项目相关：**
- **FTA Editor 原仓库**：https://github.com/Gertrud-Violett/FTA_Editor

---

## 支持

遇到问题了？

1. 先查阅本指南（上方有常见问题解答）
2. 查看你所使用服务商的官方文档
3. 在本项目 GitHub 提交 issue：https://github.com/Gertrud-Violett/FTA_Editor/issues
4. 提交时请包含：
   - 你使用的服务商
   - 具体的错误信息
   - 你在尝试做什么操作