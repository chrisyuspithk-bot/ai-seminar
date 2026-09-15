# 《從 LLM 到 Agentic AI：原理、框架與實戰》課程大綱

> 120 分鐘實戰課 · 七個 PART · 對應簡報 `agentic-ai-deck.html`（共 34 頁）

從「會說話」到「會做事」的完整路徑：先看懂 AI 如何從 LLM 走向 Agentic AI，再看多代理協作的兩個真實案例（中國 Kimi、日本 Sakana AI），接著盤點業界框架與工具，最後在 Mac 上親手用 OpenWorkers 生成 PPT、用 OpenHands Cloud 一句 Prompt 做出一個 App。

---

## 課程目標

下課後，學員能帶走這六件事：

1. 用自己的話說出 LLM、RAG、AI Agent、Agentic AI 四層躍遷的差別。
2. 理解 Agentic AI 的五大核心架構，並說出「多代理協作」為何是關鍵。
3. 比較 Kimi Agent Swarm 與 Sakana Fugu 兩種多代理策略的差異與戰略意義。
4. 分辨框架層（Google ADK、LangGraph）與工具層（OpenHands、OpenWorkers）的定位。
5. 在 Mac 上實際操作 OpenWorkers，從素材到交付完成一份 PPT 檔案。
6. 在 OpenHands Cloud 用一句 Prompt 完成一個可運行的待辦事項 App。

---

## 時間分配（總計 120 分鐘）

| 段落 | 主題 | 投影片 | 建議時間 |
| --- | --- | --- | --- |
| Part 1 | 開場與課程導覽 | 01–03 | 10 分 |
| Part 2 | Agentic AI 與 LLM 的根本差異 | 04–08 | 15 分 |
| Part 3 | Agent Swarm 多代理協作 | 09–16 | 20 分 |
| Part 4 | 從框架到工具 | 17–21 | 15 分 |
| BREAK | 中場休息 | 22 | 15 分 |
| Part 5 | Mac 實戰 Demo：OpenWorkers | 23–26 | 20 分 |
| Part 6 | OpenHands Cloud 教學 | 27–31 | 20 分 |
| Part 7 | 總結與 Q&A | 32–34 | 5 分 |
| **總計** | **七個 PART ＋ 中場休息** | **34 頁** | **120 分** |

---

## Part 1 · 開場與課程導覽（10 分鐘 · 投影片 01–03）

### 一、封面與今天要回答的四個問題（01–02）

- **01 封面** — 標題《從 LLM 到 Agentic AI》，封面即列出七個 PART 與中場休息的各自分鐘數。
- **02 今天要回答的四個問題** — 問題一：Agentic AI 到底是什麼？問題二：多個 Agent 協同會發生什麼？問題三：業界有哪些框架與工具？問題四：怎麼真的動手做？

### 二、開場數據（03）

- **03 這已經不是實驗室裡的概念** — 引用 MIT 史隆管理學院與波士頓顧問集團 2025 年 11 月報告：**35%** 受訪企業已部署 AI 代理、**44%** 計劃很快跟進。
- 教學提示：把課程拆成「原理 → 案例 → 框架 → 實戰」四段，先給學員一張地圖。

---

## Part 2 · Agentic AI 與 LLM 的根本差異（15 分鐘 · 投影片 04–08）

### 三、從會說話到會做事（04）

- **04 從「會說話」到「會做事」** — 生成式 AI 產出的是「內容」；Agentic AI 是會在世界中採取行動的 AI，行動可以是物理的（機器人），也可以是數位的（訂機票）。

### 四、四層智能躍遷（05–06）

- **05 四層智能躍遷：像四級台階** — LAYER 1 LLM（會不會說）、LAYER 2 RAG（有沒有依據）、LAYER 3 AI Agent（能不能做事）、LAYER 4 Agentic AI（能不能協同）。
- **06 一句話記住** — LLM 是智能的**語言引擎**、RAG 是**知識底座**、AI Agent 是**任務執行單元**、Agentic AI 是**組織協同系統**；每一層都是疊加，無法跳過。

### 五、五大架構與關鍵比喻（07–08）

- **07 Agentic AI 的五大核心技術架構** — ① LLM 當大腦、② 工具整合、③ 記憶機制、④ 規劃與反思、⑤ 多代理協作。前四項讓單一 Agent 變強，第五項是這一輪最關鍵的發展。
- **08 聰明的秘書 vs 全權代理人** — 傳統生成式 AI 像秘書（你交代什麼做什麼）；Agentic AI 像全權代理人（一句「幫我計劃下個月去日本，預算兩萬元」，自己查機票、酒店、天氣與行程）。提醒：能力越強，**信任與監督機制**越重要（人在迴路）。

---

## Part 3 · Agent Swarm 多代理協作（20 分鐘 · 投影片 09–16）

### 六、為什麼需要多代理（09）

- **09 如果一個 Agent 不夠強，為什麼不訓練一個更強的？** — 複雜任務需要的專業知識遠超單一模型邊界；與其訓練「全能模型」，不如讓多個專責模型協同。核心思想：**智能不在節點，而在關係**。

### 七、中國案例：Kimi Agent Swarm（10–12）

- **10 月之暗面與 Kimi K3** — 2.8 兆參數、200 萬 token 上下文、896 路由專家（每次激活 16 個）；真正的重點是 Agent Swarm 產品支援**最多 100 個並發子智能體**。
- **11 代理群怎麼運作？** — 動態生成最多 100 個子代理、最多 1,500 次工具呼叫、執行時間最多縮短 **4.5 倍**；整個代理群由模型自動建立與調度，無需事先定義角色。
- **12 不只是「向上擴展」，還要「向外擴展」** — 月之暗面的方向：更大的模型 ＋ 更多的 Agent；引用明斯基《心智社會》(1986)——智能存在於組件的**組織方式**之中。

### 八、日本案例：Sakana AI（13–15）

- **13 Sakana Fugu：AI 的「總指揮」** — 2023 年成立的日本獨角獸，由 Transformer 論文第五作者 Llion Jones 共同創辦；Fugu 是 2026 年 6 月的編排器模型，自己**不回答問題**，而是調用世界上各種模型。
- **14 Fugu 的四個基礎機制** — ① 識別問題類型、② 選擇 worker 模型、③ 拆解任務、④ 校驗與綜合；答案品質超過多個單一模型獨立作答的結果。
- **15 性能表現與「AI 主權」** — Terminal Bench 峰值集中在 GPT-5.5、GPQA Diamond 圍繞 Gemini 展開；戰略上從 Anthropic 出口管制吸取教訓，底層模型池完全可替換。**編排能力本身正成為一種獨立的競爭力。**

### 九、兩個案例對比（16）

- **16 Kimi Agent Swarm vs Sakana Fugu** — 對比核心策略、Agent 數量、角色定義、戰略定位、獨特價值：Kimi 靠 100 個並發子代理縮短 4.5 倍時間；Fugu 靠編排器打破單一供應商依賴。

---

## Part 4 · 從框架到工具（15 分鐘 · 投影片 17–21）

### 十、框架層：開發者如何構建 Agent（17–18）

- **17 Google ADK（Agent Development Kit）** — 2025 年 4 月 Cloud NEXT 發布的開源框架；四大特色：Multi-Agent by Design、豐富模型生態（LiteLLM 整合）、豐富工具生態（含 MCP）、內建評估。Google 自家 Agentspace 與 Customer Engagement Suite 即採用此框架。
- **18 LangGraph：把工作流畫成一張圖** — LangChain 團隊開發，用於**有狀態的、多參與者的** LLM 應用；四個概念：StateGraph、Node、Edge、Persistence（支援記憶、中斷恢復、人工參與）。實際用戶：LinkedIn、Uber、Klarna、GitLab。

### 十一、框架選擇的思考（19）

- **19 兩種設計哲學** — Google ADK 屬「企業整合派」（GCP 整合、企業級部署與評估）；LangGraph 屬「精細控制派」（流程控制、狀態管理與中斷恢復）。選擇取決於技術棧、部署環境與團隊熟悉度。

### 十二、工具層與層次關係（20–21）

- **20 不用自己寫框架，直接拿來用** — OpenHands（原名 OpenDevin，GitHub Star 超過 7.4 萬；Cloud／CLI／Local GUI／Software Agent SDK）；OpenWorkers（吳恩達團隊開源；交付成品、本地優先＋任意模型、每個重要動作都有審批）。
- **21 四個層次，由上而下** — Agentic AI 應用層 → 框架層 → Agent 運行時層 → 模型層；界線正在模糊（OpenHands 同時提供 SDK 與 Cloud GUI）。

---

## BREAK · 中場休息（15 分鐘 · 投影片 22）

- **22 休息 15 分鐘** — 上半場講完原理與案例；下半場兩種實戰：先讓 Agent 生出一份 PPT，再用一句 Prompt 做出一個 App。

---

## Part 5 · Mac 實戰 Demo：OpenWorkers（20 分鐘 · 投影片 23–26）

### 十三、環境準備與下達指令（23–24）

- **23 環境準備** — macOS 13+、至少 8GB RAM（建議 16GB）、Node.js v20+、一組 LLM API Key；從 GitHub 下載安裝檔並設定 API Key（教學建議 DeepSeek 或 Kimi，成本較低）。
- **24 準備素材，然後下達指令** — 桌面 `ProductLaunch` 資料夾含 product_features.md、market_data.csv、competitor_analysis.md；在對話框輸入一段要求產出 6 部分、`.pptx` 格式、檔名 `ProductLaunch_Presentation` 的指令。

### 十四、觀察工作流程與設計哲學（25–26）

- **25 Agent 自己拆解、自己交付** — 五步驟：規劃階段 → 讀取檔案 → 生成內容 → 創建簡報 → 檢查與交付；交付的是**可直接打開、可分享的簡報檔案**。
- **26 它提議，你拍板** — 不理想就直接說，OpenWorkers 會記住上下文修改對應頁面；三大設計哲學：**本地優先**、**審批門控**、**連接器生態**（HubSpot、GitHub、Slack 等 25+ 服務）。

---

## Part 6 · OpenHands Cloud 教學（20 分鐘 · 投影片 27–31）

### 十五、架構解析與快速上手（27–28）

- **27 OpenHands 的架構解析** — 核心（LLM · Agent）、環境（Runtime · Sandbox）、服務（Server）、骨幹（EventStream）；它給 LLM 配備完整開發環境，是**閉環回饋系統**。
- **28 三個步驟開始** — 註冊帳號（app.all-hands.dev，GitHub／GitLab 登入）→ 設定模型（OpenHands 模型無關，支援 OpenAI／Anthropic／Google／LiteLLM）→ 開始新任務（Launch from Scratch）。初學者建議先選 Claude 或 GPT 系列。

### 十六、一句 Prompt 做出一個 App（29–31）

- **29 我們只給它這一段話** — Prompt 要求用 Python Flask 建待辦事項 Web App：新增／編輯／刪除、標記完成、SQLite、原生 HTML+CSS、README、測試，並啟動伺服器驗證。
- **30 從規劃到交付，六個階段** — 規劃 → 環境準備 → 程式碼編寫 → 測試與除錯（自我迭代）→ 啟動與驗證 → 交付。
- **31 這不只是生成程式碼，而是完成一整個開發任務** — 四大設計原則：Sandbox 隔離、EventStream 驅動、模型無關、原生沙盒化。

---

## Part 7 · 總結與 Q&A（5 分鐘 · 投影片 32–34）

### 十七、四個層次的總結（32）

- **32 我們從四個層次理解了這個轉變** — 概念層（四個階梯）、案例層（Kimi／Sakana 兩案例）、框架層（ADK／LangGraph）、工具層（OpenWorkers／OpenHands）。一句話：**Agentic AI 是 AI 從「輔助工具」進化為「生產力主體」的關鍵轉折。**

### 十八、三個 takeaway 與結語（33–34）

- **33 帶走三句話** — ① 價值不在模型，而在系統；② 編排能力是獨立競爭力；③ 安全與信任是前提。下一步：下載 OpenWorkers 跑真實任務、申請 OpenHands Cloud 免費額度、用一句 Prompt 做出小工具。
- **34 結語** — 未來 AI 的競爭，未必只屬於擁有最強單體模型的公司，也可能屬於最擅長設計**關係**的公司。開放提問。

---

## 講者備忘與這份大綱的範圍

- **操作備案**：Part 5 與 Part 6 為兩個實戰環節；網路不穩時，Part 5 可改用預先準備的截圖與成品檔，Part 6 可先錄好操作影片。
- **環境提醒**：Part 5 需 macOS 與 LLM API Key，建議課前請學員完成安裝與 Key 設定；Part 6 只需瀏覽器，適合所有人同步操作。
- **時間控制**：Part 1–4 可依聽眾反應適度壓縮，把時間留給 Part 5、Part 6 的現場演示與提問。
- **資訊時效**：Kimi 與 Sakana 的規格、OpenHands／OpenWorkers 的功能更新頻繁，講座前一週請確認最新資訊。
- 本大綱對應簡報 **agentic-ai-deck.html**，共 **34 頁**、七個 PART、一個中場休息，總時長約 **120 分鐘**。
