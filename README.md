# FTA/ETA Editor 中文版

FTA/ETA 事故树编辑器（中文版）：一款功能完整的故障树分析（FTA）与事件树分析（ETA）桌面软件，支持概率计算、可视化树编辑、AI 分析助手与多种格式导出。本版内置 **DeepSeek、通义千问、智谱清言、Kimi** 等国内大模型与 **Ollama 本地**模型，开箱即可直连使用 AI 分析助手。

本仓库源于 [Gertrud-Violett/FTA_Editor](https://github.com/Gertrud-Violett/FTA_Editor)，在保留原版完整功能的基础上，新增 Windows / macOS / Linux 一键启动脚本与面向国内用户的 AI 服务商支持，界面与文档均为简体中文，方便中文用户直接下载使用。

## 项目缘起

本人工科专业出身，一直从事安全管理类工作，近几年岗位也由一线转向行政岗位。近期有一个临时任务需要绘制故障树 / 事件树，而这类图在工作中往往要么靠 **Visio 手工连线**，要么用**收费的专业风险分析软件**，对需要快速出图的工作场景既不够高效、成本也偏高。由于没有太多时间一张张手动拖拽节点、连线、标注概率，就一直想借助 AI 工具来直接生成这类图。

但目前主流的**办公类 AI 工具（例如 Trae、WorkBuddy 等）大多只能输出文本、Markdown 或普通图片，还无法直接绘制并导出 Visio（.vsdx）这类结构化绘图文件**。于是基于 [Gertrud-Violett/FTA_Editor](https://github.com/Gertrud-Violett/FTA_Editor) 做了这个编辑器，用来满足实际工作中的出图需求：

- 在图形界面里**所见即所得**地搭好故障树 / 事件树，省去手工连线；
- 自动按逻辑门**计算概率**，并对零概率节点高亮，方便快速定位问题；
- **AI 助手**可辅助分析与完善故障树；
- 支持导出 **JSON / XML / Excel** 等格式，方便归档与后续使用。

## 相对原版的改进

本版本在原作者 [Gertrud-Violett/FTA_Editor](https://github.com/Gertrud-Violett/FTA_Editor) 的基础上，主要做了以下几点增强：

1. **界面与文档全部为简体中文**：界面、菜单、按钮、提示与 AI 助手对话文案，以及 README、快速入门、用户手册、AI 配置、API 参考等全部文档均提供简体中文版本，方便中文用户直接上手。
2. **多平台一键启动脚本**：新增 Windows `启动FTA编辑器.bat` 与 macOS / Linux `启动FTA编辑器.sh`，安装依赖后即可一键运行，省去手动敲命令。
3. **扩展国内 AI 服务商支持**：在原有 OpenAI / Claude / Gemini 之外，新增 **DeepSeek、通义千问、智谱清言、Kimi** 与 **Ollama 本地** 5 家国内 / 本地服务商，均走 OpenAI 兼容接口、复用现有 `openai` SDK，无需新增依赖，开箱即用。
4. **面向国内用户做了适配**：端点（Endpoint）与默认模型均已内置并更新至各厂商最新版，通常无需手动填写；Ollama 本地可免密钥运行。
5. **精简服务商列表**：移除对国内用户实用性较低的 Microsoft / Azure / GitHub Copilot 支持，让设置更清晰聚焦。
6. **故障树渲染优化**：图形默认**竖向**布局（根事件在上、子事件向下展开，符合常见事故树图示习惯）；渲染时按系统**自动适配可用中文字体**（Windows 微软雅黑 / macOS 苹方 / Linux 文泉驿），不再因缺字体显示为方框（豆腐块）；渲染标签（概率、计算概率、日期、与门 / 或门等）全部为中文；并增加 **Graphviz 自动定位**与友好报错提示。
7. **新增 Mermaid 导出 / 复制**：把故障树一键转成 **Mermaid 流程图文本**，在 **WPS Office** 等软件里「导入流程图 → 粘贴 Mermaid 文本」即可得到可编辑图形，是最省事、兼容性最好的"可编辑"导出方式。

> 本项目为界面改良 + 功能扩展，未改动原版核心的 FTA / ETA 算法与逻辑，遵循 BSD-2-Clause 协议。

## 功能特性

[![License: BSD-2-Clause](https://img.shields.io/badge/License-BSD2-yellow.svg)](https://opensource.org/license/bsd-2-clause)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.5.1-green.svg)](CHANGELOG.md)

- **交互式树编辑器**：实时图形预览，所见即所得
- **双分析模式**：FTA（自下而上的故障树分析）与 ETA（自上而下的事件树分析）
- **AI 智能助手**：内置对话式界面，支持故障树分析与改进建议
- **精确概率计算**：支持与门（AND）/ 或门（OR）逻辑门
- **可视化图形生成**：基于 Graphviz，逻辑门直接显示在节点中；默认竖向布局并自动适配中文字体与中文标签
- **多种导出格式**：JSON、XML、Excel（带层级结构）
- **零概率节点高亮**：快速定位问题节点
- **安全凭据存储**：API 密钥仅保存在本地，绝不入库

## 快速开始

### 方式一：Windows 一键启动（推荐）

1. 安装 [Python 3.10+](https://www.python.org/downloads/)（国内可用镜像加速下载，如华为云、阿里云的 Python 镜像）与 [Graphviz](https://graphviz.org/download/)（安装时勾选"Add to PATH"）
2. 双击运行 `启动FTA编辑器.bat`
3. 首次使用前请先安装依赖：`pip install -r requirements.txt`

### 方式二：macOS / Linux 一键启动

1. 安装 [Python 3.10+](https://www.python.org/downloads/) 与 [Graphviz](https://graphviz.org/download/)：
   - macOS：`brew install graphviz`
   - Debian / Ubuntu：`sudo apt install graphviz python3-tk`
   - 确保已加入 PATH
2. 在终端运行：`bash 启动FTA编辑器.sh`（首次会自动创建虚拟环境并安装依赖，之后再运行可直接启动）

### 方式三：命令行启动

```bash
# 克隆本仓库
git clone https://github.com/<你的用户名>/FTA_Editor_Chinese.git
cd FTA_Editor_Chinese

# 安装依赖
pip install -r requirements.txt

# 运行程序
python src/FTA_Editor_UI.py
```

### 环境要求

- Python 3.10+
- Graphviz（从 [graphviz.org](https://graphviz.org/download/) 下载安装；安装时勾选"Add to PATH"，官网访问慢可稍后重试）
- Python 依赖见 `requirements.txt`

## AI 助手配置（可选）

内置 AI 助手已为国内用户优先适配 **DeepSeek、通义千问、智谱清言、Kimi** 与 **Ollama 本地**（免密钥）；端点与默认模型均已内置，通常无需改动。

| 服务商 | 推荐模型 | 开通地址 |
|--------|---------|---------|
| **DeepSeek** | `deepseek-v4-flash` / `deepseek-v4-pro` | https://platform.deepseek.com |
| **通义千问** | `qwen3.8-max` / `qwen3.8-flash` / `qwen3.7-plus` | https://dashscope.console.aliyun.com |
| **智谱清言** | `glm-5.3` / `glm-5.3-flash` / `glm-4.7-flash` | https://open.bigmodel.cn |
| **Kimi** | `kimi-k3` / `kimi-k2.7-code` | https://platform.moonshot.cn |
| **Ollama 本地** | `qwen3:8b` / `llama3.3:70b` / `qwen2.5` | 本机 `ollama pull`，免密钥 |

国际服务商（OpenAI / Claude / Gemini）同样可在设置中选用。

> **注意**：AI 设置窗口中，模型列表跟随最上方"AI 服务商"下拉框联动。服务商已按国内优先排序，默认停在第一个（DeepSeek）；切换到 DeepSeek / 通义千问 / 智谱清言 / Kimi / Ollama 本地，下方的模型下拉框即会自动填入上表对应的默认模型；若已填写该服务商 API 密钥，则实时拉取该账号可用的全部模型。

**配置**：打开 FTA Editor → AI 设置（⚙）→ 选择服务商、填入 API 密钥（本地模型可留空）→ 测试并保存。凭据仅保存在本地 `~/.fta_editor/ai_credentials.json`。

详细配置见 [docs/QUICK_AI_SETUP.md](docs/QUICK_AI_SETUP.md) 与 [docs/MULTI_PROVIDER_SETUP.md](docs/MULTI_PROVIDER_SETUP.md)。

### 快捷操作
- **分析故障树**：将评估与建议发送到对话窗口，不会修改你的树
- **更新故障树**：AI 生成完整 JSON 更新，经结构与安全性校验后替换当前故障树；已有节点保留，仅应用新增内容。AI 输出无效时会显示详细错误日志
- 可提问示例："这个失效模式可能缺少哪些根本原因？"、"请检查这棵树的概率"、"为选中节点建议更多失效模式"

## 使用说明

### 图形界面

```bash
python src/FTA_Editor_UI.py
```

**键盘快捷键：**
- `Ctrl+N`：新建分析
- `Ctrl+A`：添加节点
- `Ctrl+E`：编辑节点
- `Ctrl+D`：删除节点
- `Ctrl+S`：保存
- `Ctrl+R`：渲染图形

### 故障树图形渲染

- **默认竖向布局**：渲染出的故障树为自上而下（根事件在上、子事件向下展开），符合常见事故树图示习惯。
- **中文字体自动适配**：按系统自动选择可用中文字体（Windows 微软雅黑 / macOS 苹方 / Linux 文泉驿），无需手动配置，避免中文显示为方框（豆腐块）。
- **中文渲染标签**：节点内的概率、计算概率、日期、逻辑门（与门 / 或门）等标签均为中文；新建分析时根节点默认为"根事件"、标题默认为"未命名分析"。
- **Graphviz 自动定位**：若 `dot` 不在系统 PATH，会自动查找常见安装目录（如 Windows 的 `C:\Program Files\Graphviz\bin`），一般无需手动修改环境变量。
- **友好报错**：渲染失败或当前树为空时给出明确中文提示，不再出现 "cannot identify image file" 之类的隐藏错误。

### 编程接口

```python
from src.FTA_Editor_core import FTACore

core = FTACore()
core.set_metadata(title="分析", mode="FTA")
core.load_from_json("data/examples/sampleFTA.json")
core.recalculate_probabilities()
core.export_to_excel("output.xlsx")
```

## 项目结构

```
FTA_Editor_Chinese/
├── src/                          # 源代码
│   ├── FTA_Editor_UI.py         # 图形界面（含 AI 对话）
│   ├── FTA_Editor_core.py       # 核心业务逻辑
│   ├── AI_agent_handler.py      # AI 智能体与 API 处理
│   └── json_viewer.py           # 图形渲染器
├── tests/                        # 测试套件
├── data/examples/               # 示例数据
├── docs/                        # 文档
├── 启动FTA编辑器.bat             # Windows 一键启动脚本
├── 启动FTA编辑器.sh              # macOS / Linux 一键启动脚本
└── requirements.txt             # Python 依赖
```

## 测试

```bash
python -m pytest tests/
```

## 分析模式

**FTA（故障树分析）**：自下而上的可靠性分析
- 顶事件 = 系统失效事件
- 底事件 = 部件失效原因
- 由部件失效概率计算系统失效概率

**ETA（事件树分析）**：自上而下的后果分析
- 顶事件 = 初始事件
- 底事件 = 最终后果
- 由事件序列计算后果概率

## 导出格式

- **JSON**：完整树数据（含元数据）
- **XML**：标准故障树格式
- **Excel**：带颜色编码的层级表格
- **Mermaid(.mmd)**：导出 / 复制为 **Mermaid 流程图文本**；在 **WPS Office** 等软件中「导入流程图 → 粘贴 Mermaid 文本」即可生成可编辑的故障树图形（节点、与 / 或门、概率连线一应俱全），是免安装、最稳的"可编辑"导出方式

## 文档

- [快速入门指南](QUICKSTART.md) - 三步上手
- [用户手册](docs/USER_GUIDE.md) - 完整使用说明
- **AI 服务商配置：**
  - [多服务商配置](docs/MULTI_PROVIDER_SETUP.md)
- [ETA 模式](docs/ETA_MODE.md) - 事件树分析
- [API 参考](docs/API_REFERENCE.md) - 编程接口

## 常见问题

### AI 助手问题

**提示"AI 未配置"：**
- 点击 ⚙ 按钮，输入你的 API 凭据

**测试时"连接失败"：**
- 确认 API 密钥正确且有效
- 检查网络连接
- 确认 API 端点 URL 正确

**响应缓慢：**
- 可改用更快模型，如国际 `gpt-4o-mini`、国内 `qwen3.8-flash` 或 `glm-4.7-flash`
- 检查 API 调用限额

### 一般问题

**找不到 Graphviz：**
- 从 [graphviz.org](https://graphviz.org/download/) 安装
- 程序会先按系统 PATH 查找，找不到时自动查找常见安装目录（如 Windows 的 `C:\Program Files\Graphviz\bin`）；按默认路径安装即可，一般无需手动改环境变量
- 若为自定义安装目录且仍未识别，请将 `dot` 所在目录加入系统 PATH 后重启程序

**图形不显示：**
- 确认已安装 Pillow：`pip install Pillow`
- 确认 Graphviz 安装正确（见上）
- 若提示"当前树无可渲染内容"，说明当前树为空或暂无可渲染节点，请在画布中添加节点后重新渲染
- 若提示 "cannot identify image file"，通常是渲染未产出有效图片导致，重启程序后再试；仍出现可确认 `dot` 是否可用

## 开源协议与致谢

本项目基于 **BSD-2-Clause** 协议开源，版权归原作者 makkiblog.com 所有。

- 原仓库：[Gertrud-Violett/FTA_Editor](https://github.com/Gertrud-Violett/FTA_Editor)
- 本中文版在原版基础上将界面与文档调整为简体中文，并新增国内 / 本地 AI 服务商支持，未改动核心算法与功能逻辑
- 使用、修改、再分发请遵守 [LICENSE](LICENSE) 中的条款

## 支持

- 问题反馈：[GitHub Issues](https://github.com/Gertrud-Violett/FTA_editor/issues)
- 示例数据：[data/examples/](data/examples/)
