# API 参考（API Reference）

**版本**：1.5.0 | **更新日期**：2025 年 12 月 16 日

面向 FTA/ETA 编辑器的编程调用（程序化使用）完整 API 文档。

## 概述（Overview）

本文档涵盖三个主要模块：

- **FTACore**：FTA/ETA 操作的核心业务逻辑
- **AIAgentHandler**：AI 助手集成（v1.5 新增）
- **FTAStructureAnalyzer**：FTA 数据转换工具

## FTACore 类（Class）

主要类，用于故障树和事件树分析操作。类（Class）是一种代码模板，用它创建的对象称为实例（Instance）。

### 构造函数（Constructor）

构造函数（Constructor）是创建类实例时自动调用的特殊方法（Method）。

```python
from src.FTA_Editor_core import FTACore

core = FTACore()
```

初始化后即带有默认根节点和元数据。

### 元数据方法（Metadata Methods）

元数据（Metadata）是描述分析本身的信息，如标题、日期、模式等。

#### `set_metadata(title=None, date=None, mode=None)`

设置分析元数据。

**参数（Parameters）**：
- `title`（str，可选）：分析标题
- `date`（str，可选）：分析日期
- `mode`（str，可选）："FTA" 或 "ETA"

**示例（Example）**：
```python
core.set_metadata(
    title="Server Reliability Analysis",
    date="2025-10-31",
    mode="FTA"
)
```

#### `get_metadata()`

获取当前元数据。

**返回值（Returns）**：包含键 `title`、`date`、`mode` 的字典

**示例（Example）**：
```python
metadata = core.get_metadata()
print(f"Mode: {metadata['mode']}")
```

### 数据管理方法（Data Management Methods）

#### `get_data()`

获取当前树数据结构。

**返回值（Returns）**：dict - 完整树结构

**示例（Example）**：
```python
tree = core.get_data()
print(f"Root: {tree['name']}")
```

#### `set_data(data)`

设置树数据结构。

**参数（Parameters）**：
- `data`（dict）：完整树结构

**示例（Example）**：
```python
tree_data = {
    "id": "root",
    "name": "System Failure",
    "type": "Root",
    "probability": 0.5,
    "logicGate": "OR",
    "children": [],
    "links": []
}
core.set_data(tree_data)
```

### 节点操作（Node Operations）

节点（Node）是树中的基本元素，表示事件、门或根节点。

#### `add_node(parent_id, node_data)`

添加一个节点作为指定父节点的子节点。

**参数（Parameters）**：
- `parent_id`（str）：父节点的 ID
- `node_data`（dict）：节点数据（name、type、probability 等）

**返回值（Returns）**：元组（tuple）(success: bool, error: str 或 None)

元组（Tuple）是 Python 中一个不可变的有序集合，可同时返回多个值。

**示例（Example）**：
```python
success, error = core.add_node("root", {
    "name": "Hardware Failure",
    "type": "Event",
    "probability": 0.1,
    "logicGate": "OR"
})
```

#### `update_node(node_id, updates)`

更新现有节点。

**参数（Parameters）**：
- `node_id`（str）：要更新的节点 ID
- `updates`（dict）：需要更新的字段

**返回值（Returns）**：元组（tuple）(success: bool, error: str 或 None)

**示例（Example）**：
```python
success, error = core.update_node("root_0", {
    "name": "Updated Name",
    "probability": 0.15
})
```

#### `delete_node(node_id)`

删除一个节点及其所有子节点。

**参数（Parameters）**：
- `node_id`（str）：要删除的节点 ID

**返回值（Returns）**：元组（tuple）(success: bool, error: str 或 None)

**示例（Example）**：
```python
success, error = core.delete_node("root_0_1")
```

#### `find_node_by_id(node_id)`

根据 ID 查找并返回节点。

**参数（Parameters）**：
- `node_id`（str）：要查找的节点 ID

**返回值（Returns）**：dict 或 None - 找到则返回节点数据，否则返回 None

**示例（Example）**：
```python
node = core.find_node_by_id("root_0")
if node:
    print(f"Found: {node['name']}")
```

### 概率计算（Probability Calculations）

概率（Probability）表示事件发生的可能性，取值范围在 0.0（必然不发生）到 1.0（必然发生）之间。

#### `recalculate_probabilities()`

根据当前模式重新计算所有节点的概率。

**注意（Note）**：加载数据后会自动调用。修改后请手动调用。

**示例（Example）**：
```python
core.recalculate_probabilities()
```

#### `get_zero_probability_nodes()`

获取概率为零的节点 ID 列表。

**返回值（Returns）**：str 列表 - 节点 ID

**示例（Example）**：
```python
zero_nodes = core.get_zero_probability_nodes()
print(f"Zero probability nodes: {zero_nodes}")
```

### 文件读写方法（File I/O Methods）

#### `load_from_json(file_path)`

从 JSON 文件加载树数据。

**参数（Parameters）**：
- `file_path`（str）：JSON 文件路径

**返回值（Returns）**：元组（tuple）(success: bool, error: str 或 None)

**支持（Supports）**：同时支持新格式（含元数据）和旧格式

**示例（Example）**：
```python
success, error = core.load_from_json("data/analysis.json")
if not success:
    print(f"Error: {error}")
```

#### `save_to_json(file_path=None)`

将树数据连同元数据保存到 JSON 文件。

**参数（Parameters）**：
- `file_path`（str，可选）：保存路径。若为 None，则使用最后加载的文件。

**返回值（Returns）**：元组（tuple）(success: bool, error: str 或 None)

**示例（Example）**：
```python
success, error = core.save_to_json("output.json")
```

#### `export_to_xml(file_path)`

将树导出为 XML 格式。

**参数（Parameters）**：
- `file_path`（str）：XML 文件路径

**返回值（Returns）**：元组（tuple）(success: bool, error: str 或 None)

**示例（Example）**：
```python
success, error = core.export_to_xml("output.xml")
```

#### `export_to_excel(file_path)`

将树导出为层级结构的 Excel 格式。

**参数（Parameters）**：
- `file_path`（str）：Excel 文件路径

**返回值（Returns）**：元组（tuple）(success: bool, error: str 或 None)

**特性（Features）**：层级列、配色、自动列宽

**示例（Example）**：
```python
success, error = core.export_to_excel("output.xlsx")
```

## 完整使用示例（Complete Usage Example）

```python
from src.FTA_Editor_core import FTACore

# Initialize 初始化
core = FTACore()

# Set metadata 设置元数据
core.set_metadata(
    title="Nuclear Plant Safety Analysis",
    date="2025-10-31",
    mode="ETA"  # Event Tree Analysis 事件树分析
)

# Build tree structure 构建树结构
tree = {
    "id": "root",
    "name": "Loss of Coolant",
    "type": "Root",
    "probability": 0.001,  # Initiating event probability 初始事件概率
    "logicGate": "OR",
    "children": [
        {
            "id": "branch1",
            "name": "ECCS Activates",
            "type": "Event",
            "probability": 0.99,
            "logicGate": "OR",
            "children": [
                {
                    "id": "outcome1",
                    "name": "Core Cooled",
                    "type": "Event",
                    "probability": 0.98,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "outcome2",
                    "name": "Partial Cooling",
                    "type": "Event",
                    "probability": 0.02,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        },
        {
            "id": "branch2",
            "name": "ECCS Fails",
            "type": "Event",
            "probability": 0.01,
            "logicGate": "OR",
            "children": [
                {
                    "id": "outcome3",
                    "name": "Core Meltdown",
                    "type": "Event",
                    "probability": 1.0,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        }
    ],
    "links": []
}

core.set_data(tree)

# Calculate probabilities 计算概率
core.recalculate_probabilities()

# Access results 访问结果
root = core.get_data()
print(f"Root calculated probability: {root['calculatedProbability']}")

# Access specific outcome 访问特定结果
outcome1 = core.find_node_by_id("outcome1")
print(f"Core Cooled probability: {outcome1['calculatedProbability']}")
# In ETA mode: 0.001 × 0.99 × 0.98 = 0.00097
# 在 ETA 模式下：0.001 × 0.99 × 0.98 = 0.00097

# Export results 导出结果
core.save_to_json("analysis.json")
core.export_to_excel("analysis.xlsx")
core.export_to_xml("analysis.xml")

# Check for zero probability nodes 检查概率为零的节点
zero_nodes = core.get_zero_probability_nodes()
if zero_nodes:
    print(f"Warning: Zero probability nodes: {zero_nodes}")
```

## 数据结构参考（Data Structure Reference）

### 节点结构（Node Structure）

```python
{
    "id": "unique_id",              # Unique identifier 唯一标识符
    "name": "Node Name",            # Display name 显示名称
    "type": "Event",                # Node type 节点类型
    "probability": 0.5,             # Base probability (0.0-1.0) 基础概率（0.0-1.0）
    "calculatedProbability": 0.3,   # Calculated (read-only) 计算得到（只读）
    "logicGate": "OR",              # "AND" or "OR" 逻辑门："AND" 或 "OR"
    "notes": "Description",         # Optional notes 可选备注
    "children": [],                 # List of child nodes 子节点列表
    "links": [                      # Links to other nodes 指向其他节点的链接
        {
            "target_id": "other_node",
            "relation": "AND"       # "AND" or "OR" 关系："AND" 或 "OR"
        }
    ]
}
```

### 元数据结构（Metadata Structure）

```python
{
    "title": "Analysis Title",
    "date": "2025-10-31",
    "mode": "ETA"  # "FTA" or "ETA" 模式："FTA" 或 "ETA"
}
```

### JSON 文件格式（JSON File Format）

```python
{
    "title": "Analysis Title",
    "date": "2025-10-31",
    "mode": "ETA",
    "tree": {
        # Node structure as above 节点结构如上所述
    }
}
```

## 错误处理（Error Handling）

所有方法均返回元组 `(success, error)`：

```python
success, error = core.save_to_json("output.json")
if not success:
    print(f"Error occurred: {error}")
else:
    print("Success!")
```

## 辅助函数（Helper Functions）

### `sanitize_name(s)`

去除字符串中多余的空格。

**参数（Parameters）**：
- `s`（str）：需要净化的字符串

**返回值（Returns）**：str - 净化后的字符串

**示例（Example）**：
```python
from src.FTA_Editor_core import sanitize_name

clean = sanitize_name("  Spaced   Text  ")
# Returns: "Spaced Text"
# 返回："Spaced Text"
```

## 常量（Constants）

无 - 所有配置均由数据驱动。

## 线程安全（Thread Safety）

FTACore **不是**线程安全的（Thread-safe）。并发的操作请使用各自独立的实例（Instance）。

## 性能说明（Performance Notes）

- 树的遍历是递归的（Recursive）——非常深的树可能触及递归深度上限
- 概率重算采用记忆化（Memoized）处理——对大树的求值高效
- 循环引用检测可防止无限循环

---

## AIAgentHandler 类（Class）

v1.5.0 新增。负责 AI 助手功能。

### 构造函数（Constructor）

```python
from src.AI_agent_handler import AIAgentHandler

handler = AIAgentHandler()
```

### 方法（Methods）

#### `is_configured()`

检查 AI 凭据（Credentials）是否已配置好。

凭据（Credentials）即 API 密钥（API Key），用于向 AI 服务商的接口进行身份认证。

**返回值（Returns）**：bool

```python
if handler.is_configured():
    print("AI is ready")
```

#### `configure(api_key, api_endpoint, model)`

配置 AI 凭据。

**参数（Parameters）**：
- `api_key`（str）：AI 服务商提供的 API 密钥（API Key）
- `api_endpoint`（str）：API 接口地址（默认：国际默认 "https://api.openai.com/v1"）
- `model`（str）：模型名称

**返回值（Returns）**：元组（tuple）(success, error_message)

**关于 API 密钥与模型选择**：国内用户应优先使用国内服务商。各服务商接口地址（endpoint）已由程序内置，**无需**在 `api_endpoint` 中手动填写；配置时只需填写你从服务商官网申请到的 `api_key` 和对应的 `model` 即可。推荐配置如下：

| 服务商 | 推荐模型（model） | 开通地址（申请密钥） |
| --- | --- | --- |
| **DeepSeek（深度求索）** | `deepseek-v4-flash` / `deepseek-v4-pro` | https://platform.deepseek.com |
| **通义千问（阿里云）** | `qwen3.8-max` / `qwen3.8-flash` / `qwen3.7-plus` | https://dashscope.console.aliyun.com |
| **智谱清言（智谱 AI）** | `glm-5.3` / `glm-5.3-flash` / `glm-4.7-flash` | https://open.bigmodel.cn |
| **Kimi（月之暗面）** | `kimi-k3` / `kimi-k2.7-code` | https://platform.moonshot.cn |
| **Ollama（本地部署）** | `qwen3:8b` / `llama3.3:70b` / `qwen2.5` | 无需密钥，需先执行 `ollama pull` | 

**说明**：国内用户优先使用国内服务商；OpenAI 等国际服务需自行前往官网申请密钥（作为备选方案）。Kimi 新版模型的 temperature 参数由程序自动适配，无需手动设置。

**示例 1：使用国内服务商（DeepSeek，推荐）**
```python
success, error = handler.configure(
    api_key="sk-你的DeepSeek密钥",
    api_endpoint="https://api.deepseek.com/v1",
    model="deepseek-v4-flash"
)
```

> 提示：接口地址 `api_endpoint` 已由程序内置，一般可省略。若省略，程序会根据所选服务商自动切换到对应的国内接口（如 DeepSeek、通义千问、智谱清言、Kimi 等）。

**示例 2：使用国内服务商（通义千问）**
```python
success, error = handler.configure(
    api_key="sk-你的通义千问密钥",
    model="qwen3.8-flash"
)
```

**示例 3：使用国内服务商（智谱清言）**
```python
success, error = handler.configure(
    api_key="你的智谱清言密钥",
    model="glm-4.7-flash"
)
```

**示例 4：使用国内服务商（Kimi）**
```python
success, error = handler.configure(
    api_key="sk-你的Kimi密钥",
    model="kimi-k3"
)
```

**示例 5：使用本地模型（Ollama，免密钥）**
```python
# 先在本机拉取模型：ollama pull qwen3:8b
success, error = handler.configure(
    api_key="ollama",
    model="qwen3:8b"
)
```

**示例 6：使用国际服务商（OpenAI，作为备选）**
```python
success, error = handler.configure(
    api_key="sk-...",
    api_endpoint="https://api.openai.com/v1",
    model="gpt-4o"
)
```

#### `set_fta_context(fta_data, mode, title)`

为 AI 分析设置 FTA 上下文。

**参数（Parameters）**：
- `fta_data`（dict）：当前 FTA 数据结构
- `mode`（str）："FTA" 或 "ETA"
- `title`（str）：分析标题

```python
handler.set_fta_context(
    core.get_data(),
    core.mode,
    core.title
)
```

#### `send_message(user_message, include_fta_context=True)`

向 AI 发送消息并获取响应。

**参数（Parameters）**：
- `user_message`（str）：用户的消息
- `include_fta_context`（bool）：是否在第一条消息中包含 FTA 上下文

**返回值（Returns）**：元组（tuple）(response_text, AIProposedChange 列表)

```python
response, changes = handler.send_message(
    "What root causes might be missing?"
)
print(response)
for change in changes:
    print(f"Proposed: {change.description}")
```

#### `get_quick_analysis(fta_data, mode, title)`

获取当前 FTA 的快速 AI 分析。

**返回值（Returns）**：元组（tuple）(analysis_text, proposed_changes)

```python
analysis, changes = handler.get_quick_analysis(
    core.get_data(), "FTA", "My Analysis"
)
```

#### `clear_conversation()`

重置对话历史。

```python
handler.clear_conversation()
```

---

## AICredentialManager 类（Class）

管理 API 凭据的存储。

### 凭据存放位置（Credential Location）

凭据保存在如下位置（`.fta_editor/ai_credentials.json` 是本地的凭据配置文件文件）：

- Windows：`C:\Users\<username>\.fta_editor\ai_credentials.json`
- macOS/Linux：`~/.fta_editor/ai_credentials.json`

### 方法（Methods）

#### `save_credentials(api_key, api_endpoint, model)`

将凭据保存到本地存储。

**返回值（Returns）**：元组（tuple）(success, error_message)

#### `load_credentials()`

从本地存储加载凭据。

**返回值（Returns）**：元组（tuple）(credentials_dict 或 None, error_message 或 None)

#### `delete_credentials()`

删除已保存的凭据。

**返回值（Returns）**：元组（tuple）(success, error_message)

#### `has_credentials()`

检查凭据文件是否存在。

**返回值（Returns）**：bool

---

## FTAStructureAnalyzer 类（Class）

用于将 FTA 数据转换为可供 AI 使用的文本格式的工具。

### 静态方法（Static Methods）

静态方法（Static Method）是不依赖于某个实例、可直接通过类名调用的方法。

#### `fta_to_text(fta_data, mode, title, indent=0)`

将 FTA 数据转换为人类可读的文本。

**参数（Parameters）**：
- `fta_data`（dict）：FTA 数据结构
- `mode`（str）："FTA" 或 "ETA"
- `title`（str）：分析标题
- `indent`（int）：当前缩进层级

**返回值（Returns）**：str - 格式化后的文本表示

```python
from src.AI_agent_handler import FTAStructureAnalyzer

text = FTAStructureAnalyzer.fta_to_text(
    core.get_data(), "FTA", "My Analysis"
)
print(text)
```

#### `get_summary(fta_data, mode)`

获取 FTA 的简要摘要。

**返回值（Returns）**：str - 摘要文本

---

如需更多示例，请查看 `tests/` 目录与 `data/examples/`。