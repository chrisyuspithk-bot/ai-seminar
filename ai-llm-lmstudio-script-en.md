# From LLM Basics to LM Studio and Gemini — English Script

> Companion deck: `ai-llm-lmstudio-deck.html` (35 slides)
> Language: English (translated from the Cantonese script)
> How to use: one section per slide. The first block in each section is the script you read aloud. The "Ops note", "Aside" and "Likely question" blocks are speaker reminders and are not read out.
> Speaker note: keep sentences short, one idea per slide. The first time a technical term appears, give the English term and then explain it in plain words.

---

## How to use this script (read first)

1. This script maps page by page to the deck. Each page holds roughly two to three minutes of material. If you are short on time, read only the bolded sentences in each section.
2. "You" means the whole class. If you are teaching one to one, switch everything to the singular.
3. The first time a technical term appears, give the English term first and then the plain-language explanation.
4. If students are falling behind, do not stop to explain every word. The lesson has one throughline: **an LLM does probabilistic prediction; it does not query a database.** Everything else can be sacrificed.

---

# Part 1 · LLM fundamentals (25 min · 01–04)

## Slide 01 · Cover: from LLM basics to LM Studio and Gemini

Good morning, and welcome to this hundred-and-fifty-minute hands-on class. Today is structured a little differently: we are not going to sit and listen to three hours of theory. We will hear a short stretch of theory and then build something, over and over. The class is split into eight parts, starting from the most basic LLM concepts and going all the way to running a large language model on your own machine, and then to Gemini in the cloud.

Let me clear one thing up first: today is not about which model is strongest. That question gets a new answer every three months, so whatever you memorise today is out of date next quarter. What I want to teach you is a judgement — you have a task in front of you, you look at it, and you know whether it should go to a local model or to the cloud. That judgement does not go out of date.

On the cover you can see the eight parts and their timings. Keep a rough count in your head: parts 1 to 3 are concepts — twenty-five plus fifteen plus fifteen, about fifty-five minutes. Part 4 is hands-on, thirty minutes, and it is the heaviest section today. Parts 5 to 7 cover applications and limits. Part 8 is the Gemini ecosystem. If you want to be able to do this at home afterwards, do not drift during part 4.

**Today has one goal: by the end of the class you can go home, without asking anyone, install LM Studio, download a model, and hold a conversation with it.** It sounds simple, but I have watched a lot of people give up at the step where they have to pick which version to download. Today we take it apart, page by page.

> **Ops note** Before you start, confirm the classroom Wi-Fi can reach lmstudio.ai and huggingface.co. If you plan to download a model live, download it the night before and only demonstrate it in class.

## Slide 02 · What is ChatGPT actually doing?

Let's start with a slide that may overturn what you thought. When you use ChatGPT, you ask "when did Hong Kong return to China" and it answers "1997." Your instinct is that it went to some database, found 1997, and copied it out. **No. It has no database to look in.**

What it does is called predicting the next word. Having read your question, it computes: if I were to continue from here, what is the most likely next word? It computes, picks one, appends it, and then computes the next. It builds the answer one word at a time. So every time it answers you, it is continuing text — not verifying anything.

The flow is roughly three steps. Step one, take input: the text you typed is cut into tokens. Step two, compute probabilities: the model looks at that sequence of tokens and produces a probability distribution over the next token. Step three, generate one at a time: pick one, append it, recompute. Those three steps repeat until the answer is finished.

**So remember the first line of today: an LLM is a probability machine, not a knowledge base.** That line shapes every judgement you make afterwards. If it were a knowledge base, its answers should be accurate. Because it is a probability machine, its answers are the most plausible-sounding ones — not necessarily the most accurate. Once you know that, its confident errors stop being surprising.

Two practical numbers. In English, a token is roughly three-quarters of a word. Chinese is different: one Chinese character is roughly one to two tokens. Why does that matter? Because everything you do later — local or cloud — is billed and limited in tokens, not in characters.

> **Aside** Someone will ask how it can have knowledge at all. The answer: its knowledge is not stored in a table; it is compressed into billions of parameters. Think of it as having read the entire internet and then compressed the statistical regularities of all that text into its own mathematical structure. So it can convey the gist, but the details distort easily.

> **Likely question** "So it cannot answer anything?" It can, and better than many people. But it answers in a statistically plausible way, not a verified way. That distinction is exactly why we cover RAG and verification later.

## Slide 03 · Transformer and self-attention

The last slide said it continues text one word at a time. So here is the question: how does it know what the next word should be? This slide is the answer, and it is the most central mechanism in all of modern AI: self-attention.

Let me use a sentence to make it click: "Ming gave the apple to Wah because he was hungry." You look at the final "he" and you immediately know it means Ming, not Wah. How do you know? Because you looked at the whole sentence at once and judged which name "he" relates to most. Self-attention does exactly the same thing.

When the model generates each word, it looks back over every word in the sequence and computes a relevance score for each. High scores influence the output more; low scores influence it less. In that sentence, the information "was hungry" causes the model to weight "Ming" more heavily, so it resolves "he" to Ming.

Three things worth taking away. First, attention is fundamentally relevance scoring — it is not understanding meaning, it is computing which words relate to which. Second, it was a breakthrough because it parallelises: older models had to read word by word, so by the tenth word the memory of the first had faded. Self-attention sees the whole sequence at once, so it can train in parallel and handle much longer context. Third, without that breakthrough, today's LLMs would not exist.

**One line to remember: self-attention lets the model re-judge, for every word it generates, which information is most relevant.** You do not need to memorise it. Just remember that it looks back.

> **Aside** To make it more everyday: it is like someone in a meeting who does not just listen to whoever spoke last, but re-scans the room on every sentence to see whose point matters most right now.

## Slide 04 · Parameter scale: what 4B, 7B and 70B mean

This slide is the practical basis for choosing models later. The model names you see online usually carry a number: Qwen 7B, Llama 70B, Gemma 4B. That B is billion. 7B means seven billion parameters.

Think of parameters as the model's brain capacity. More parameters means it can represent more complex patterns, but it also needs more memory and compute. That is a very real trade-off — there is no free lunch.

Let me split it into three levels. 4B is the light tier. If your machine has 8GB of RAM there is a decent chance it runs, and the speed is acceptable. But its reasoning is shallow, so it suits simple rewriting, translation and classification. 7B is the sweet spot and the mainstream choice for local deployment. A machine with 16GB of RAM handles it comfortably, and the quality-to-speed balance is good. This is the tier I will demonstrate today. 70B is the flagship tier. It needs a high-end GPU and is not worth considering on an ordinary home machine.

**The practical conclusion: if this is your first time with local models, aim for the 7B to 13B range.** Do not chase 70B straight away, because your hardware cannot keep up, it will not load, and you will conclude that local models are no good and give up. The first question when choosing a model is not "which is strongest" — it is "which will run."

> **Teaching note** You can ask here: "whose machine has under 8GB of RAM?" Note who raises a hand, because in part 4 they will need a 3B or smaller model. That is not their fault; it is a hardware limit.

---

# Part 2 · Open vs closed, and model types (15 min · 05–06)

## Slide 05 · Open-source vs closed models

Let's move to another dimension: who gives you the model, and how. This split decides where your data goes, so it is not purely technical — it is a question of responsibility.

Closed models first. Closed means you can only use it through an API, and you never see the weights. GPT-4o and Claude are in this group. The advantages are obvious: the strongest performance, works out of the box, no hardware to worry about, a few lines of code and you are calling it. The disadvantages are equally obvious: your data is uploaded to their servers; you pay, and heavy use gets expensive; you cannot modify it or fine-tune it on your company's terminology.

Now open models. Open means you can download the weights and run it on your own machine. Llama 4, DeepSeek V3 and Qwen 3 are in this group. The advantages: your data never leaves your machine, it is free, and you can fine-tune it yourself. The disadvantages: hardware is a barrier, setup is more involved, and quality is usually a little behind.

One technical detail, so you do not get caught out later: strictly speaking, "open source" and "open weights" are different things. Open source means the training code and data are also released. Open weights means only the final model file is released, with the training details kept back. When the industry says "open model", ninety-nine times out of a hundred it means open weights.

**How to choose? Here is a two-question framework. First, is your data sensitive?** If it is a customer list, medical records or unreleased financials, you should not upload it to any cloud. Choose open. **Second, do you need the strongest performance and want to ignore hardware?** Then choose closed. Answer those two and you have your answer.

> **Likely question** "Are open models always worse?" Not necessarily. On many specialised tasks, a fine-tuned 7B open model beats a general-purpose giant closed model. The difference is that you have to put in the tuning time.

## Slide 06 · Text, multimodal, embedding, omni

This slide covers a classification that confuses a lot of people. I will not give you definitions — I will split them by what goes in and what comes out. Learn that format and you will not get muddled.

First, text models. Text in, text out. You type Chinese, it answers in Chinese. This is the most common kind, and the chatbot you normally use is this.

Second, multimodal models. Text plus image in, text out. You take a photo and ask what it is, and it tells you. Note that the output is still text — it will not draw you a picture back.

Third, embedding models. Text in, a vector out. This is the least glamorous and the most important. It will not chat with you. It turns a piece of text into a string of numbers, a coordinate. Why? Because once it is a coordinate, "similar meaning" becomes something you can compute — the closer two vectors, the closer their meaning. When you meet RAG later you will see how powerful that is.

Fourth, omni models. Any modality in, any modality out. Text in, speech out. Image in, video out. Jina v5-omni is one example. This is the newest direction and the most expensive one.

**One line: text models read and write words, multimodal models can see images, embedding models turn meaning into coordinates, and omni does everything.** When you pick a model on Hugging Face in future, the first thing to check is which of these it is. Do not pick the wrong kind.

> **Aside** Embeddings click with an everyday example: when you look for a book in a library, you do not need the title to match exactly. You need it to be close to your subject. The coordinate is how you measure "close".

---

# Part 3 · Quantisation and Hugging Face (15 min · 07–08)

## Slide 07 · What is quantisation?

This slide is the make-or-break point of local deployment. A lot of my students get stuck right here: they downloaded a model, so why will it not load? The answer is usually that they downloaded a version that is too fat.

First, some background. An original model is stored in FP16, meaning sixteen bits per parameter. Do the arithmetic: seven billion parameters at sixteen bits is two bytes each, so seven billion times two is about fourteen gigabytes. A normal laptop cannot spare that. Hence quantisation.

Quantisation means compressing those numbers from sixteen bits down to eight, four, or lower. **Here is an analogy that will land: it is like a photo on your phone. The original is a RAW file, tens of megabytes. You save it as JPEG and it is maybe two or three megabytes, but it still looks about the same.** That is what quantisation does.

But compression has a cost, so you need to know the levels. Q8 is closest to the original quality, but the file is still large, so it does not help much on a home machine. Q4_K_M is the one I want you to remember — **Q4_K_M is the recommended balance point**, using roughly forty percent less VRAM than FP16 while losing under one percent of quality. When you are faced with a dozen versions and cannot choose, Q4_K_M is right about ninety percent of the time. Q2 is extreme compression: the smallest file, but with a noticeable quality loss. You will feel it start to ramble.

**So remember: the key to local deployment is not choosing the biggest model. It is choosing a quantised version that suits your machine.** That is why the same 7B model gets described as smooth by one person and laggy by another — they downloaded different quantisations.

> **Ops note** After this slide you can open Hugging Face, search a model, click the Files tab, and show students that one model has dozens of files. The visual shock is worth more than saying it ten times.

## Slide 08 · Hugging Face and the GGUF format

Having covered quantisation, you will ask: where do I download from? The answer is Hugging Face. **Think of Hugging Face as the GitHub of AI.** Researchers and companies around the world upload their trained models, and a free account lets you download them. Whatever you are looking for, ninety-nine percent of the time it is on there.

So which file do you download? Here you need one format: GGUF. GGUF is the model file format from the llama.cpp ecosystem, optimised specifically for local inference. You do not need the full name. You need one practical trick: **when searching Hugging Face, type the model name plus GGUF, and you will find versions LM Studio can use directly.**

How do you choose once you have found it? Open the page, scroll to the Files section, and you will see a long list. All you do is find the files ending in `.gguf`, and within those pick the quantisation level you learned on the last slide. You will usually see a dozen files for the same model, from Q2 up to Q8. Pick Q4_K_M.

> **Ops note** This is the step where most people get stuck, so do one complete demonstration: search, open the page, Files, pick the file. Use the big screen, not your laptop screen, because students need to read the filename format clearly.

> **Likely question** "Why does one model have so many files?" Because the quantisation methods differ, and so do file size and quality. The uploader usually notes on the page which version suits which hardware. You can follow that, but you do not have to.

---

# Part 4 · Installing and configuring LM Studio (30 min · 09–14)

## Slide 09 · What is LM Studio?

Now the most important section of the day. From this slide you switch from listening to doing. First, what is LM Studio?

LM Studio is a free desktop application that lets you run large language models locally through a graphical interface, without writing any code. That is its main value: **running a local model used to mean opening a terminal and typing a pile of commands. Now it is a few clicks.**

Let me give you four advantages so you see why I chose it as today's teaching tool. First, graphical, no coding. Second, built-in model search, so you can find and download models inside the app without going to a browser. Third, fully offline — once the model is downloaded you can unplug the network cable and it still works. Fourth, it provides an OpenAI-compatible API, which means code you have already written works with a local model by changing one URL, with no change to the logic.

**That fourth point deserves emphasis.** A lot of people assume local models are just for playing around. But when your code can call cloud today and local tomorrow through the same interface, you genuinely have a choice. That is the technical basis for the judgement I mentioned at the start.

## Slide 10 · Download and install

Let's get our hands dirty. Step one: go to `lmstudio.ai` and click Download. Remember that address; do not go to third-party download sites, because if someone has modified that file you will never know.

Step two: pick your operating system — Windows, macOS or Linux — and install. The installer is unremarkable, keep clicking Next. One warning: **check your hardware.** Apple Silicon Macs have a specifically optimised build, and on Windows you should confirm your GPU driver is current.

Step three: after the first launch, go to Settings, General, Language, and pick your language. You do not have to, but you will be more comfortable if you do.

One honest caveat: **the non-English language packs are still beta**, so parts of the interface will stay in English. That is not an installation error; it is expected and it does not affect functionality. Do not think you have done something wrong when you see a mix.

> **Ops note** If the network is unreliable, you do not need to re-download the installer in class. Install it before the session and only demonstrate Settings → Language.

## Slide 11 · Searching for and downloading a model (live)

Model download is the most critical hands-on step today. First the interface: the left sidebar has four buttons — Chat, Developer, My Models, Discover.

We will use three of them today. Chat is where you talk to the model. Developer is where you start the API server, which we return to on slide 14. My Models holds what you have already downloaded. Discover is where you find new models.

The flow is this. Click Discover, type `Qwen2.5-7B-Instruct-GGUF` in the search bar. You will get many results from different uploaders. **Here is a judgement to learn: pick a reliable uploader.** For example bartowski, or the official Qwen account. Why does the uploader matter? Because model files can be tampered with, and using an official or well-known uploader carries much less risk.

Once you have picked the uploader, click through, choose the Q4_K_M version, and press Download. The file is roughly four to five gigabytes, so depending on your connection you will wait a few minutes.

**One warning: do not download a Q8 version and then tell me it is slow.** The Q8 file is about twice the size and your machine may not cope. Remember the conclusion from the last slide: Q4_K_M.

> **Ops note** When demonstrating live, use an already-downloaded model as the comparison. Start the download, then say "this will take a few minutes, so let's continue with the one I downloaded earlier", and you will not waste the class staring at a progress bar.

> **Likely question** "Can I download more than one model?" Yes, and I would suggest two: a 7B for real work and a 3B for quick tests. But remember every model takes disk space, and your machine is not infinite.

## Slide 12 · Loading a model and basic conversation

Once the download finishes, go back to the Chat tab. At the top there is a dropdown — select the model you just downloaded and it will start loading. The first load takes a few seconds to a few tens of seconds, depending on your hardware and the model size.

Once it is loaded you can start talking. But do not ask random things. I suggest your first test is a fixed sentence: "Introduce yourself in one paragraph." That sentence does three things: it tells you immediately whether it handles your language, it shows you its tone and length, and it lets you measure speed — how many words per second, or how long you wait.

**That speed test matters, because it decides how you will use the model.** If it produces a dozen words a second, you can use it as a writing assistant. If it manages two or three, do not expect it to write your thesis. Short classification tasks suit it better.

> **Teaching note** This is the moment students feel most successful — watching a model run on their own machine. Have everyone do it, then ask "whose model answered fastest?" The comparison teaches them about hardware differences naturally.

## Slide 13 · GPU, context length and temperature

Once the model is running, let's look at the settings. Three parameters you need to know, because they directly affect your experience and your cost.

First, GPU offload, which controls how many layers run on the GPU. The default is one hundred percent. **If you drop it below fifty percent, speed falls sharply**, because the remaining layers fall back to the CPU, and the CPU is far slower at this kind of arithmetic. So unless your GPU memory really is insufficient, leave it alone.

Second, context length. The default is four thousand and ninety-six tokens, and you can raise it. But remember an iron rule: **double the context and the VRAM requirement doubles too.** It is not a simple linear relationship, but the model must keep intermediate state for every token. So check how much GPU memory you have spare before raising it.

Third, temperature. Low, roughly zero point one to zero point three, suits factual questions, because you want it stable rather than creative. High, roughly zero point seven to one point zero, suits creative writing, because you want variety and experimentation. The same question at different temperatures gives completely different answers.

One newer feature: n_parallel. Added after LM Studio zero point four point zero, it handles multiple inference requests at once, with four parallel slots by default. That is useful once you are serving an API.

> **Likely question** "So what should I set?" If you do not know, do not change anything. The defaults are the best answer for most people. Tuning is something you do after you notice a problem, not before you start.

## Slide 14 · The built-in OpenAI-compatible API

This closes part four and is one of the most valuable features today. LM Studio ships with an OpenAI-compatible API.

How to use it: go to the Developer tab and press Start Server. It starts at `http://localhost:1234`. Any library that supports the OpenAI API can then connect to it.

Here is a Python example. You originally write:

```
from openai import OpenAI
client = OpenAI(api_key="sk-xxx", base_url="https://api.openai.com/v1")
```

You only change `base_url` to `http://localhost:1234/v1`. The `api_key` can be anything, because you are talking to your own machine. Not one other line of code changes.

**What does that mean? It means you have a free local API.** No monthly fee, no usage anxiety, no worry about data leaving. That is the real value of local deployment — not that it is cool, but that it can genuinely be used in production.

> **Ops note** Run the Python example live if you can. If time is short, at minimum start the server and open `localhost:1234` in a browser so students see it is a real running service.

> **Likely question** "Can I expose this API to the internet?" Technically yes, but I would not. There is no authentication at all, so opening it up means anyone in the world can run models on your machine.

---

# Part 5 · Prompt engineering and core concepts (20 min · 15–20)

## Slide 15 · The prompt is your only interface

From here we move to a different topic: prompting. Getting the model running does not mean using it well. And the prompt is the **only** interface between you and the model.

Why do I stress "only"? Because there is no other way to influence it. You cannot open up its head. You cannot say "be smarter." The text you type is all you control.

So the same model, used by two different people, can produce wildly different results. Not because the model plays favourites, but because the prompts differ in quality. Today I will give you a framework so you can write them systematically.

First, the most basic principle and the most common mistake: **the model does not know what is in your head.** You are assuming a pile of context — "this is for secondary students", "make it formal", "keep it under three hundred words." But you did not write any of it down, so it does not know. The key to prompting is writing out everything you assume is obvious.

Here is a contrast. You write "write me a resignation letter." It will write one. But addressed to whom? Polite or blunt? Long or short? Did you mention you are leaving immediately or in a month? If you do not say, it guesses. And its guess is probably not what you wanted.

> **Teaching note** You can do a live demonstration here: ask a student to write a one-line prompt, run it on the spot, and see whether the result matches what they wanted. That demonstration is worth more than ten minutes of theory.

## Slide 16 · COSTAR: six elements

So how do you write one? Here is a framework called COSTAR. Six elements.

C is context: the background — who you are, where this came from, what the assumptions are. O is objective: what you want it to do, as specifically as possible. S is style: academic, journalistic, conversational. T is tone: professional, warm, serious. A is audience: who will read this — this is the most commonly omitted and most influential element. R is response: the output format — a table, bullet points, JSON.

Here is a complete example. "C: I am a tutor at a learning centre and next week I have to explain probability to Form 4 students. O: Write me a five-minute opening script. S: Everyday language, use plenty of local examples. T: Relaxed but professional. A: Form 4 students with average maths ability. R: Three paragraphs, none over a hundred and fifty words."

Compare that with "write me an intro to probability." See the difference? This is not magic. It is whether you stated your requirements clearly.

One practical piece of advice: **you do not need all six every time.** But two are non-negotiable: C and O. Context and objective. Without them the model is guessing blind. When time is short, at minimum write down who you are and what you want.

> **Aside** COSTAR is not the only framework; there are plenty about. The point of a framework is to remind you what to cover, not to dictate how you say it. Once you are fluent you can simplify it yourself.

## Slide 17 · Tokens and the context window

Back to technical matters. This slide explains something many people hit without understanding: after a long conversation, why does the model "forget" what I said earlier?

The answer is the context window. We covered tokens on slide 2 — the smallest unit the model processes. The context window is the maximum number of tokens it can see at once. That window contains three things: your prompt, its response, and the entire conversation history so far.

**Here is the key: the history occupies the window too.** So with the same window size, the longer you talk, the less room is left.

What happens when you exceed it? The oldest content is pushed out. Your opening background information gets dropped. That is why it seems to lose its memory. It is not broken; the window is full.

This has practical consequences. If you want it to work on a long document, do not expect it to remember every detail. What you do instead is paste the relevant passage back in with each question. That is exactly what RAG, on the next slide, is for.

> **Likely question** "Why not just make the window infinite?" Cost. The larger the window, the more memory and compute it needs, and attention scales with the square of the length. So the window is a balance between cost and capability.

## Slide 18 · RAG and embeddings

The last slide said the model cannot remember much. So what do you do? The industry answer is RAG: retrieval-augmented generation.

RAG works in five steps. Step one, chunk: cut your documents into passages. Step two, use an embedding model to turn each chunk into a vector. Step three, store those vectors in a vector database. Step four, when the user asks something, turn the question into a vector and find the most similar chunks in the database. Step five, feed those chunks and the question to the LLM together.

**The embedding step is what makes this work: it turns "semantic similarity" into a computable mathematical problem.** The closer two vectors, the closer their meaning. You do not need the keywords to match — you only need the meaning to be close.

An example. You ask "how do I cancel my account?" The document says "account termination procedure." You never used the word "cancel", but the embedding knows the two mean the same thing, so it finds it.

**That is the value of RAG: it fixes two problems — the knowledge cut-off and hallucination.** Because the answer is grounded in real documents you supplied, not in what the model made up.

> **Ops note** This slide is concept-dense, so use a physical analogy: RAG is like being allowed one reference book in an exam, but the invigilator only lets you open three pages — so you need to find the three most relevant pages fast.

## Slide 19 · Hallucination: why it lies with a straight face

Now hallucination. This is the most common question: why does it state something wrong so confidently?

Three reasons. First, a mismatch in the training objective. It is trained to produce the most plausible text, not the most correct text. Those two usually overlap, but not always. Second, contaminated training data. It learned from the internet, and the internet contains a great deal of wrong and outdated information. Third, randomness in the decoding strategy. There is a random element in choosing each word, so the same question asked twice can get different answers.

**Notice that none of these three reasons is "it wants to deceive you."** Hallucination is a by-product of how it works, not malice.

So how do you reduce it? Four measures. First, explicitly require in the prompt that it say "I don't know" when unsure. Second, use RAG and feed it real documents. Third, lower the temperature so it invents less. Fourth, cross-check — ask again with another model or another phrasing.

**Of those four, RAG is the most effective, because it addresses the root cause: having no grounding.**

> **Teaching note** Do a live demonstration here: ask the model an obscure question you know it will get wrong, and show how confident it sounds. Seeing it beats being told ten times not to trust it.

## Slide 20 · From talking to doing

Last slide of part five, and a turning point: tool use.

Everything the model has done so far is talk. You ask about the weather and it gives you weather — but it does not know today's weather. It generated text that sounds like a weather report. That is what slide 2 said: it is a probability machine.

So how do you get it to actually know today's weather? Tool use. You give it a tool, say a weather lookup function. When you ask "what's the weather today", it does not answer immediately. It first judges: this question needs a tool. Then it generates a call request saying "I want to call the weather function with the argument Hong Kong." Your program receives that, actually calls the API, gets real data, and hands it back. Only then does the model generate an answer from the real data.

**That is the step from talking to doing.** It is no longer answering from memory; it is actually fetching.

But a new problem appears: every tool needs a piece of adapter code. Ten tools means ten pieces. That is tedious and non-standard. The next stop, MCP, exists to solve exactly that.

> **Aside** This sets up part six. You can say: "if tool use is being able to use tools, MCP is a universal socket standard, so every tool can plug in."

---

# Part 6 · MCP and tool use in practice (15 min · 21–24)

## Slide 21 · What is MCP?

The last slide gave tool use a pain point: every new tool needs adapter code. This slide is the solution: MCP.

MCP stands for Model Context Protocol, proposed by Anthropic in 2024. Here is the most memorable analogy: **MCP is the USB-C port of AI.**

Think about the world before USB-C. A charger plug for the phone, another for the camera, another for the laptop — you left the house with a bag of cables. After USB-C, one cable charges everything. MCP does the same thing. Every tool used to need bespoke connection code; now, with a standard protocol, any tool written to the standard plugs into any application that supports MCP.

There are three roles to know. First, the host — your LLM application, such as LM Studio or Claude Desktop. Second, the client — the MCP SDK, which manages connections. Third, the server — the service providing the tools, communicating over stdio or HTTP.

One widespread misunderstanding to clear up: **MCP and function calling are complementary, not alternatives.** Function calling solves "how does a model call its own API." MCP solves "how do we standardise tool interfaces so multiple agents can share multiple tools." You can think of function calling as how to make the phone call, and MCP as the standard format for phone numbers.

> **Aside** MCP can package resources and prompt templates too. But at the introductory stage, just remember it as a standard interface for tools.

## Slide 22 · Setting up MCP in LM Studio

Now the practical setup. LM Studio supports two methods.

Method one, through the interface: switch to the Program tab on the right, find Install, then Edit mcp.json. This suits you if you do not want to hunt for the file manually.

Method two, edit the file directly. On macOS the path is `~/.lmstudio/mcp.json`; on Windows it is `%USERPROFILE%\.lmstudio\mcp.json`. Open it in any text editor.

The structure is roughly: an `mcpServers` object, where each key is a server name, and each server needs command, args and env fields. You do not need to memorise the format. Copy an example from the MCP documentation or GitHub, change the name and arguments, and you are done.

**The step you must not skip: save the file and then restart LM Studio, or press Reload MCP servers.** A lot of people edit the file, see nothing happen, and ask why. Nine times out of ten it is an un-reloaded config. This is the most common mistake.

> **Ops note** Set up one server before the session and only demonstrate Edit mcp.json and Reload in class. Typing JSON from scratch live has a high chance of error and will wreck your pacing.

> **Likely question** "Do I have to use an Anthropic model for MCP?" No. MCP is an open protocol and not tied to a vendor. But your model must support tool calling, otherwise it cannot issue the tool request.

## Slide 23 · Practising: getting the model to use a tool

This is the most dramatic step today. We are going to make the model genuinely use a tool.

Two things to prepare. First, load a model that supports tool calling, such as the Qwen series — not all models do, so check before you choose. Second, configure a filesystem MCP server, a tool that can read and write files on your machine.

Once configured, we ask it: "read test.txt on my desktop." Note that we have not told it what is in the file. We gave it a path.

It will do four things. Step one, judge the intent: it analyses your question and decides "I cannot answer this, because I do not know the file contents — I need a tool." Step two, generate the tool call: it outputs a structured request saying "I want to call read_file on the filesystem, with the desktop test.txt as the argument." Step three, the MCP client executes it: your application reads the file and returns the contents. Step four, the model produces the final answer: it responds in natural language based on the real content it just received.

**Where is the power here? In going from only being able to talk to being able to do.** It is no longer answering from memorised training data; it is actually touching your file system.

> **Teaching note** This is the climax of the lesson. Prepare a `test.txt` in advance containing something interesting, such as a riddle you wrote. The moment the model reads it out, the whole class understands that it really can do things.

## Slide 24 · Web search MCP

Last demo, and the most practical: web search MCP.

The setup is the same as the last slide, just a different server. Once configured you can ask for live information: "what is the weather in Taipei today?" or "what is in the news today?"

**This demo fixes a fundamental limit of LLMs: the training data has a cut-off date.** Think about it — once a model is trained, its knowledge is frozen at that moment. Anything that happens afterwards, it simply does not know. But with a search tool it can fetch the latest information and use its language ability to organise it for you.

There is an important shift in framing here: **it is not "knowing" this; it is "going and finding" it.** That is a big difference. Knowing relies on memory; finding relies on action. And an answer obtained through action has a source and can be verified — you can ask it for the links.

**So the thread I laid from part 1 closes here: I said an LLM is a probability machine, not a knowledge base. But when you give it tools, it becomes a probability machine that can look things up.** Its nature has not changed, but the boundary of what it can do has expanded enormously.

> **Likely question** "Does that solve hallucination?" Partly. It can still misread or mis-summarise what it finds. The habit of verifying is still required.

---

# Part 7 · The limits of local models and the need for cloud (10 min · 25–26)

## Slide 25 · Three hard limits of local models

We have spent a lot of time on the advantages of local models, so I owe you a clear statement of the limits. And these are not limits that will disappear in two years — they are architectural.

**The first limit: a physical ceiling on context length.** We said on slide 17 that the window is finite. But the problem is not simply that there is a cap. Research found that when you extend the window from a thousand tokens to sixty-five thousand, performance on extraction tasks drops by around thirteen percent. So a bigger window is not automatically more usable — in long contexts the model's effective attention spreads out. And the KV cache grows linearly with context: a model that normally occupies twenty-one gigabytes can balloon to twenty-five or thirty gigabytes in operation. Once your VRAM overflows, it does not slow down — it dies.

**The second limit: a fundamental gap in compute.** You may be running an RTX 4090 with twenty-four gigabytes. The cloud runs H100s with eighty gigabytes, and lots of them. Local inference lags by one point four to seven point four times. You cannot tune your way past that gap; it is the hardware itself.

**The third limit: the cost of compressing the model's intelligence.** Local models are almost all quantised — remember Q4_K_M? It saved you forty percent of the memory, and the price is precision. Frontier models such as GPT-4o, Claude and Gemini have tens of times more parameters, and they are uncompressed.

**One line: local is good enough, cloud is good — and the gap is architectural, not a matter of how hard you try.**

> **Teaching note** This slide can make students wonder why they bothered learning local models. Immediately add: the value of a local model is not that it is strongest, it is that you control it. Those are different dimensions and neither replaces the other.

## Slide 26 · Why cloud is necessary, and the hybrid strategy

So what is the conclusion? Not "cloud replaces local", but "the two divide the work."

First, the nature of cloud: **it puts the compute and storage in someone else's data centre.** You do not own the hardware; you rent it. State that clearly and the pros and cons follow.

Local covers four cases: private or confidential data, working offline, limited budget, and experimental projects. Cloud covers another four: complex reasoning, long document analysis, needing current knowledge, and production-critical work.

Cloud has three advantages: context up to a million tokens, always the latest models, and pay-as-you-go — if you do not use it, you do not pay. It has three costs: data leaves your device, there is network latency, and long-term use accumulates.

**The most pragmatic approach is a hybrid architecture.** Everyday tasks and anything involving privacy go to LM Studio. Tasks needing strong reasoning or deep ecosystem integration go to Gemini.

A concrete example. You are an accountant. You have to work with a client's unreleased financial statements — that must be local, because the data cannot leave your machine. But you also need to write an industry trend analysis, which needs the latest market data and deep reasoning, so that goes to the cloud. Same person, same day, two tools. **That is the judgement I mentioned at the start.**

> **Aside** You can give yourself a simple rule: if this data leaking would be a problem, use local. If getting this task wrong would be a problem, use the strongest cloud model. The rule is not perfect, but it covers about ninety percent of cases.

---

# Part 8 · The Gemini ecosystem (20 min · 27–33)

## Slide 27 · What is Gemini? More than a chatbot

Let's move from local to cloud. Many people assume Gemini is just Google's ChatGPT — you type a line, it answers a line. That impression is not wrong exactly, but it is far short.

Gemini is an ecosystem. Two layers. The first is the model family: a fast tier for quick simple tasks, a thinking tier that reasons slowly before answering hard problems, and a top Pro model for the hardest work. The second layer, and the one that really makes Gemini different: **it is embedded deeply in your workflow.** Gmail, Docs, Sheets, Slides, Drive, Meet and Calendar all have it inside.

**That is the concrete content of the "cloud territory" I mentioned at the start.** When your AI is inside your email and your documents, it is no longer a separate tool you open. It is part of your workflow.

An example makes it clear. On Monday you have to write a quarterly report. Your old flow: open Drive to find last quarter's file, open Sheets to copy the numbers, open Docs to write, then go to ChatGPT to proofread. With Gemini you can sit in Docs and say "using these three files in Drive, draft this for me." No switching apps, no copy-paste back and forth.

This is not slightly more convenient. It is a restructuring of the process. **When a tool is absorbed into the process, the way you work changes.**

> **Aside** This is also the hardest thing for local models to match right now. A local model can be strong, but it does not have your Gmail or your Drive. That is not a model capability problem; it is an ecosystem problem.

## Slide 28 · Comparing Gemini plans

Now money. This slide is reference material, so let me give you a table.

The free tier, zero cost, fifteen gigabytes of cloud storage. Good for everyday queries and light use. If you only ask things occasionally, the free tier is enough.

Google AI Plus, a low monthly fee, two hundred gigabytes. For people who want to try paid features on a limited budget.

Google AI Pro, a moderate monthly fee, two terabytes. For students, researchers and heavy users. **This is usually where I suggest most people start.** The feature set is generous and the price is not outrageous.

Google AI Ultra, a high monthly fee, thirty terabytes. For enterprise use and extreme performance needs. That price is not for individuals; it is for companies.

But the real difference between the paid tiers is not storage. It is two things: **context jumps from thirty-two thousand tokens on the free tier to a million; and the thinking model gets a daily allowance of three hundred to fifteen hundred prompts.**

Consider that gap. Thirty-two thousand tokens is a short report. A million tokens is several books. This is not "a bit more" — it is the difference between possible and impossible.

> **Likely question** "So which should I buy?" My answer: do not buy at the start. Use the free tier for two or three weeks and see whether you actually hit the limits. Buy when you actually hit them, because by then you know what you need.

## Slide 29 · Gems: your own AI specialist

This is, I think, the most underrated feature today: Gems.

What is a Gem? **It is a Gemini you configure, with pre-set instructions and knowledge.** You do not have to re-explain what you want each time. You build it once and use the same configuration thereafter.

The steps: go to `gemini.google.com`, find Gems, create one, give it a name, write the instructions, optionally upload documents, and save.

Here is an example so you feel what it is like. Suppose you do financial analysis. You write a Gem with the instruction: "You are a financial analysis assistant. When I upload a financial report, output in this format: one, revenue structure analysis; two, gross margin changes and causes; three, the three risk points that most need attention. Professional tone."

Once built, every future time you only upload the report and press send, and it answers to the same standard. You never rewrite the requirements.

**That is the power of configure once, reuse forever.** And the power is not only time saved — it standardises your output. You and a colleague using the same Gem produce reports in the same format. That matters a great deal for teamwork.

> **Ops note** Demonstrate this live with a very concrete example, such as a CV screening assistant or a meeting-notes assistant. Once students see the effect, they will immediately think of uses in their own work.

## Slide 30 · Gems × Google Drive: no-code RAG

The last slide was about a configured assistant. This slide is about what happens when you connect Gems to Drive: you get a no-code RAG system.

The steps: go to `drive.google.com`, find Ask Gemini in the top right, choose Gems in the sidebar, pick the Gem you built, and just ask. It retrieves answers from the files in your Drive.

Why do I call it no-code RAG? Recall slide 18. The RAG steps were: chunk, vectorise, store, retrieve, feed to the LLM. In the Drive setting you do none of those five steps. Google has done them for you.

Three practical uses. First, contract review: put a batch of contracts in Drive and ask "which of these have auto-renewal clauses?" Second, project status: ask "where did each project get to last month?" Third, research: put your references together and ask "which paper mentions this method and has experimental results?"

**This is an important shift: RAG is no longer the preserve of engineers.** It used to need code, a database, and maintenance. Now all you need is documents in Drive. That moves the capability from technical teams out to every knowledge worker.

> **Teaching note** This is the most practical slide in the lesson. If students take away only one thing, I would want it to be this: **wherever your documents live, you can ask AI there.**

## Slide 31 · Gemini inside Workspace

Let's look at what it actually does inside each application.

Google Docs has two features worth mentioning. First, Help me create: you can have it pull content from relevant Drive files and produce a first draft. Second, Match writing style: you can have it harmonise the tone across collaborators. **That second one is especially useful for teams.** Picture a report written by three people, each with a different voice, and it reads like a mess. You ask it to unify, and it does.

Google Sheets works like this: you describe the project you want to manage in one sentence, and it builds a multi-sheet spreadsheet. You do not build headers or write formulas; you state the requirement.

The most useful Drive feature is cross-file question answering. An example: you ask "in last month's correspondence with client A, was there any mention of a budget adjustment?" That used to mean searching, opening each message, and comparing. Now it is one question.

**You will notice a common thread: the value of Gemini is not how cleverly it answers. It is that it knows your business.** However strong a general model is, it does not know your correspondence with a client last month. A system integrated into your workflow does. That is the power of an ecosystem.

> **Likely question** "Will Google use my data?" That is a very reasonable question. Enterprise and personal data policies differ, and if you are handling company data you should ask your IT department first. There is no universal answer, but you must ask.

## Slide 32 · Gemini Live and voice interaction

This slide covers a feature that is both cool and genuinely useful: Gemini Live.

Gemini Live is real-time voice conversation. You can operate Gmail by voice — search, summarise, star, archive, delete. There is also a daily briefing feature that reads out a summary of your important mail, calendar and to-dos.

Here is a situation that shows its value. On your morning commute you used to be unable to deal with anything, because your hands were busy. Now you can put in earphones and hear: "you have three meetings today, the first email is a client chasing a quote, and there is one from accounts asking you to confirm an invoice." Before you reach the office you already know how the day looks.

**This is the ultimate version of AI absorbed into the process: you no longer need to be sitting at a computer to use it.**

One limit to be clear about: this is currently mainly for Google AI Pro and Ultra users. The free tier does not get it. So if you are considering upgrading for this, confirm your plan includes it.

> **Aside** Voice interaction has a very practical problem: privacy. If you talk in a public place, everyone around you hears it. Be aware of that.

## Slide 33 · When to use local, when to use Gemini

This closes part 8 and it is the slide I most want you to take away. Here is a decision list.

**Choose local (LM Studio) if:** you are handling sensitive or confidential data; you need to work offline; your budget is limited; your task is simple generation, summarisation or translation.

**Choose cloud (Gemini) if:** you are handling very long documents, in the million-token range; you need deep integration with Gmail, Drive and Docs; you need the newest model capabilities; your task is complex multi-step reasoning.

**And the most pragmatic answer is: use both.** Everyday tasks and anything involving privacy go to LM Studio. Tasks needing strong reasoning and ecosystem integration go to Gemini.

Let me stress it once more: this list is not a ranking of which is better. It is a matching of situations to tools. The most valuable thing you learn today is not the operation of any specific tool. It is this ability to match. Because tools change, and your framework for judging does not.

> **Teaching note** Run a quick vote here. Offer five concrete tasks — analyse a client's unreleased financials, write an industry trend report, translate an English letter, summarise a hundred-page PDF, tidy up the contracts in my Drive — and have students vote local or cloud for each. Then explain each one. The interaction sticks.

---

# Summary (34–35)

## Slide 34 · From principles, to practice, to ecosystem

Let's wrap up. Here are eight conclusions to take away, and you can map each back to what we covered.

First, an LLM is a probabilistic prediction machine. That is the basis of all its behaviour. When you see it get something wrong or forget something, you will know why.

Second, open models let you run locally, and LM Studio is the lowest-barrier entry point. No coding, just clicking.

Third, quantisation is the key to running locally, and Q4_K_M is the best balance. You will use this every time you download a model from now on.

Fourth, the COSTAR framework makes your prompts more effective. Remember that C and O are essential.

Fifth, MCP lets models use tools, upgrading them from talking to doing.

Sixth, local models have hard limits: context, compute, and the cost of compression. These are architectural, not something effort can overcome.

Seventh, cloud AI is a necessary complement, and Gemini shows what workflow integration makes possible.

Eighth, Gems plus Drive is no-code RAG, and you can use it at work tomorrow.

**So here are five things to do next.** One, run a 7B model — ignore the quality, just get the experience. Two, write a prompt using COSTAR and feel the difference. Three, build your own Gem. Four, use a Gem in Drive to analyse a document. Five, look at your own workflow and decide which tasks go local and which go to the cloud.

Those five are achievable this week. Once you have done them, you are no longer someone who has heard of AI. You are someone using it.

## Slide 35 · Closing

Last slide.

I said at the start that this lesson is not about which tool is better. By now I hope you see why.

Because "which tool is better" has no permanent answer. The strongest model today may be mid-tier in six months. A model that will not run today may run on your phone in two years. If your knowledge is built on remembering which tool is strongest, it will keep expiring.

But if your knowledge is built on the framework of **which situation calls for which tool**, it will not expire. Because the situations do not change: sensitive data should never be uploaded, complex reasoning always needs a stronger model, and needing current information can never rely on memory.

**That judgement is worth more than any single technology.**

I started today with "an LLM is a probability machine" and ended with "hybrid architecture." On the surface those look like many separate topics, but they are one line: **the better you understand its nature, the better you know where its boundaries are; and the better you know its boundaries, the more precisely you can use it.**

Thank you. Questions — let's talk.

---

# Appendix A · One line to take away from each part

| Part | One line |
| --- | --- |
| 1 | An LLM is a probability machine, not a knowledge base. |
| 2 | The value of open models is that you control them, not that they are strongest. |
| 3 | Quantisation is the key to running locally; Q4_K_M is the balance point. |
| 4 | LM Studio lowers the barrier to running a model locally to a few clicks. |
| 5 | The prompt is your only interface; C and O are mandatory. |
| 6 | MCP is the USB-C of AI tooling. |
| 7 | Local is control, cloud is capability. They are different dimensions. |
| 8 | Wherever your documents live, you can ask AI there. |

---

# Appendix B · Speaker notes

## 1. Timing

| Section | Slides | Planned | Trim to |
| --- | --- | --- | --- |
| Part 1 | 01–04 | 25 min | 18 min |
| Part 2 | 05–06 | 15 min | 10 min |
| Part 3 | 07–08 | 15 min | 10 min |
| Part 4 | 09–14 | 30 min | 30 min |
| Part 5 | 15–20 | 20 min | 14 min |
| Part 6 | 21–24 | 15 min | 12 min |
| Part 7 | 25–26 | 10 min | 8 min |
| Part 8 | 27–33 | 20 min | 15 min |
| Summary | 34–35 | 10 min | 5 min |

**Protect part 4.** It is the only section students cannot get from reading. If you must trim, trim parts 2 and 3.

## 2. Live-demo fallbacks

**If the download fails:** switch to an already-downloaded model and say "the download is running in the background; let's keep going." Do not let the class watch a progress bar.

**If the model will not load:** check quantisation first — that is the cause nine times out of ten. Then check GPU offload.

**If MCP will not connect:** reload MCP servers before you debug anything else.

## 3. The five questions students ask most

1. Why local rather than cloud? — Control over data.
2. My machine cannot run 7B. Am I in the wrong class? — No. Drop to 3B and follow along.
3. If AI gets things wrong, should I trust it at all? — Trust it as a first draft, verify before you act.
4. How long until I am competent? — A week to run a model; a month to develop judgement.
5. Will this still matter in three years? — The tools will change; the framework will not.

## 4. Currency warning

Model names, plan prices and quantisation defaults change quickly. Verify the free-tier limits and current model names before you teach this again.

---

# Appendix C · Common misconceptions

## Misconception 1: "AI goes to a database to find answers."

There is no database. It predicts the next token from compressed statistical patterns. Confident wrong answers follow directly from this.

## Misconception 2: "Bigger models are always better."

Bigger means more capacity, more memory and more cost. A 70B model you cannot run is worse than a 7B model you can.

## Misconception 3: "Open models are always worse."

On specialised tasks a fine-tuned 7B open model often beats a general giant. It costs you tuning time.

## Misconception 4: "Quantisation makes the model stupid."

At Q4_K_M quality loss is under one percent while memory drops around forty percent. Below Q4 the loss becomes visible.

## Misconception 5: "Local models are free."

The software is free. The hardware, electricity and your time are not. A machine that runs 7B well costs real money.

## Misconception 6: "Lower temperature means more accurate answers."

It means more consistent and less varied. Consistency is not correctness.

## Misconception 7: "Longer prompts are better."

Longer prompts consume the context window and dilute attention. Be specific, not long.

## Misconception 8: "RAG completely solves hallucination."

It reduces it. The model can still misread or mis-summarise what it retrieves.

## Misconception 9: "MCP is Anthropic-only."

MCP is an open protocol. Any vendor can implement it. Your model must support tool calling.

## Misconception 10: "Tool calling equals MCP."

Tool calling is the mechanism by which a model requests an action. MCP standardises how tools are exposed. Complementary, not identical.

## Misconception 11: "A bigger context window means I can feed it everything at once."

Effective attention degrades in long contexts, and the KV cache grows linearly. A million-token window does not mean a million tokens of reliable attention.

## Misconception 12: "Local models can fully replace cloud."

Different dimensions. Local is control and privacy; cloud is capability and currency of knowledge.

## Misconception 13: "Gemini is just Google's ChatGPT."

Gemini is an ecosystem embedded in Gmail, Docs, Sheets, Drive, Meet and Calendar.

## Misconception 14: "Gems are just custom prompts."

Gems carry instructions, reusable configuration and document grounding, and they standardise output across a team.

## Misconception 15: "Learning AI means learning which tool is strongest."

Tool rankings expire. The situation-to-tool framework does not.

---

# Appendix D · Classroom activities

## Activity one · Opening (before part 1, five minutes)

Ask everyone to name the task they most want AI to take off their plate. Write the answers on the board and refer back to them in part 8 when you match situations to tools.

## Activity two · Choosing a quantisation (after slide 07, eight minutes)

Give students three hardware profiles — 8GB RAM laptop, 16GB, and a machine with a discrete GPU — and have them pick a quantisation level for each. The point is that the answer depends on the machine, not on preference.

## Activity three · Local or cloud (before slide 33, ten minutes)

Five scenarios, a show of hands for each, then your explanation. This is the single highest-value activity in the lesson because it exercises the judgement the lesson is about.

## Activity four · Prompt rewrite (after slide 16, ten minutes)

Everyone writes a one-line prompt, then rewrites it with COSTAR. Run two or three live and compare. The before-and-after contrast is the whole lesson in miniature.

---

# Appendix E · Glossary

| Term | Plain reading |
| --- | --- |
| Token | The smallest unit of text the model processes |
| Context window | The maximum tokens visible at once, including history |
| Parameter | Loosely, an internal connection; the "capacity" number |
| Quantisation | Compressing parameters to fewer bits; FP16 down to Q4 etc. |
| GGUF | The local-inference model file format from llama.cpp |
| FP16 | Sixteen bits per parameter — the uncompressed original |
| Q4_K_M | The recommended quantisation: good balance of size and quality |
| Self-attention | Scoring how relevant each word is to each other word |
| Transformer | The 2017 architecture behind modern LLMs |
| Embedding | Turning text into a vector so meaning becomes computable |
| RAG | Retrieval-augmented generation — grounding answers in documents |
| Hallucination | Confident output that is not true |
| Temperature | Randomness of generation; low is stable, high is varied |
| GPU offload | How many layers run on the GPU rather than the CPU |
| KV cache | Intermediate state stored per token; grows with context |
| Tool calling | A model requesting that code perform an action |
| MCP | Model Context Protocol — a standard interface for tools |
| Gems | Configurable Gemini assistants with instructions and documents |

**Speaker tip:** "agent", "token" and "embedding" are the three terms students most often nod along to without understanding. Check comprehension on those three specifically rather than asking "any questions?"

---

# Appendix F · Rehearsal: likely questions and answers

## Scene one · "Why would I use a local model? Isn't cloud better?"

**You could answer:**

"Cloud is more capable. That is true and I will not pretend otherwise.

But capability is not the only dimension. Ask instead: **what can I do with this data that I cannot do with cloud?**

If you are handling a client's unreleased accounts, or medical records, or anything covered by an NDA, uploading it is not a trade-off. It is simply not an option. Local is the only way to use AI on that data at all.

So the question is not 'which is better.' It is 'which do I actually have the right to use.'"

**Why answer this way:** the student is assuming capability is the only axis. Reframing to permission and control is the actual lesson.

## Scene two · "My machine cannot run 7B. Am I in the wrong class?"

**You could answer:**

"No — you are in exactly the right class, and you just found out something useful about your hardware.

Drop to a 3B model at Q4. It will run. It will be slower and less capable, but every concept today still applies: quantisation, loading, prompting, tool use.

The people with the fastest machines will finish their demos first. That does not mean they understood more. Your constraint is a hardware fact, not a statement about you."

**Why answer this way:** this is an anxiety question. Naming the hardware limit explicitly defuses it.

## Scene three · "If AI gets things wrong, should I trust it?"

**You could answer:**

"Trust it the way you would trust a fast, confident intern who has read a lot but never worked in your field.

You would not send that intern's work out unread. But you would absolutely use them to get a first draft in ten minutes instead of two hours.

The rule I would give you: **use it to get a draft, verify before you act.** The verification is the part you cannot delegate."

**Why answer this way:** a blanket "do not trust it" fails, because they will use it anyway. A calibrated rule will actually be followed.

## Scene four · "How long until I am competent?"

**You could answer:**

"Two different timelines.

**A week to run a model.** Install LM Studio, download a Q4_K_M model, have a conversation. That is genuinely a week of casual evenings.

**A month to develop judgement.** Judgement means looking at a task and knowing whether it should go local or cloud, and knowing what to hand over and what to check. That is practice, not information.

Do not confuse the two. Getting the tool running is quick. Getting the judgement is the actual work."

**Why answer this way:** separating the mechanical skill from the judgement names what the lesson is really about.

## Scene five · "Will any of this still matter in three years?"

**You could answer:**

"Some of it will be obsolete. Probably the specific model names and the plan prices.

But here is what will not change: sensitive data should not be uploaded; complex reasoning needs a bigger model; current information cannot come from memory; and running something locally gives you control that renting does not.

**Those are properties of situations, not of tools.** Situations outlive tools. That is precisely why I teach the framework rather than the ranking."

**Why answer this way:** it is honest that specifics age, while making the case for the durable part.

## Scene six · "Why not just hand everything to AI?"

**You could answer:**

"Because you would be handing over the part that is actually yours.

The AI can produce a draft. It cannot know whether the draft is appropriate for this client, this week, in this negotiation. It was not in the room. It does not know what your manager is worried about.

**Handing over the output is fine. Handing over the judgement is not**, because the judgement is the part nobody can check for you."

**Why answer this way:** it draws the line at judgement, matching the whole session's throughline.

---

# Appendix G · Speaker self-check

## An hour before

- Wi-Fi reaches lmstudio.ai, huggingface.co and the model download mirror.
- A 7B Q4_K_M model is already downloaded and verified to load.
- A 3B model is downloaded for students on weak hardware.
- The MCP filesystem server is configured and tested.
- `test.txt` exists on the desktop with a riddle in it.
- The API server has been started once and confirmed on port 1234.

## Ten minutes before

- LM Studio opens to the Chat tab, model already loaded.
- Browser tabs ready: Hugging Face search, a Gem, Drive Ask Gemini.
- Screen resolution suits the projector, not your laptop.

## Content check

- Can you say in one sentence why an LLM is not a database?
- Can you explain quantisation without jargon?
- Can you demo tool use without reading from the script?
- Can you justify a local-versus-cloud choice for a task you did not prepare?

## Mindset

- Some students will not get their model running. That is expected. Have them pair up.
- Live demos fail. Have the fallback ready and move on calmly.
- You will not cover everything. Protect part 4.

---

# Appendix H · Per-slide timing

| Slide | Topic | Minutes |
| --- | --- | --- |
| 01 | Cover | 3 |
| 02 | What ChatGPT does | 7 |
| 03 | Transformer and self-attention | 8 |
| 04 | Parameter scale | 7 |
| 05 | Open vs closed | 8 |
| 06 | Model types | 7 |
| 07 | Quantisation | 8 |
| 08 | Hugging Face and GGUF | 7 |
| 09 | What LM Studio is | 4 |
| 10 | Install | 4 |
| 11 | Download a model | 6 |
| 12 | Load and chat | 6 |
| 13 | GPU, context, temperature | 5 |
| 14 | OpenAI-compatible API | 5 |
| 15 | Prompt as interface | 4 |
| 16 | COSTAR | 6 |
| 17 | Tokens and context window | 4 |
| 18 | RAG and embeddings | 4 |
| 19 | Hallucination | 4 |
| 20 | Tool use | 4 |
| 21 | What MCP is | 4 |
| 22 | MCP setup | 4 |
| 23 | Tool use demo | 5 |
| 24 | Web search MCP | 4 |
| 25 | Three local limits | 5 |
| 26 | Cloud and hybrid | 5 |
| 27 | What Gemini is | 3 |
| 28 | Plan comparison | 3 |
| 29 | Gems | 3 |
| 30 | Gems × Drive | 3 |
| 31 | Workspace integration | 3 |
| 32 | Gemini Live | 2 |
| 33 | Local vs cloud | 3 |
| 34 | Summary | 5 |
| 35 | Closing | 5 |

---

# Appendix I · Homework and assessment

## 1. Homework (to complete within a week)

**Task one · Run a model (required).** Install LM Studio, download a 7B Q4_K_M model and hold a conversation. Submit a screenshot and one sentence on how it felt.

**Task two · COSTAR rewrite (required).** Take a prompt you have actually used and rewrite it with COSTAR. Submit both and note what changed in the output.

**Task three · One Gem (required).** Build a Gem for a task you repeat. Submit its instructions.

**Task four · A local-or-cloud call (required).** Pick three tasks from your own work and justify local or cloud for each, in two sentences each.

**Task five · Optional.** Connect one MCP server and get the model to use it. Write down what broke and how you fixed it.

## 2. Assessment criteria

| Criterion | What good looks like |
| --- | --- |
| Conceptual grasp | Explains the next-token prediction in their own words |
| Practical skill | A model runs locally and answers coherently |
| Judgement | Local-or-cloud calls are justified by data sensitivity and task complexity |
| Prompt quality | C and O are always present; the rest used as needed |
| Verification habit | Distinguishes a draft from a verified output |

## 3. Self-check questions

1. Why is an LLM not a database?
2. What does self-attention compute?
3. What is the trade-off in parameter count?
4. What problem does quantisation solve?
5. Why Q4_K_M rather than Q8 or Q2?
6. Who gives you an open model, and what does "open weights" mean?
7. What is the difference between a text model, a multimodal model and an embedding model?
8. What are the five RAG steps?
9. Why does hallucination happen? Give three causes.
10. What problem does tool use solve?
11. What does MCP standardise?
12. Why can a large context window still perform poorly?
13. When should you choose local, and when cloud?

**Questions 1, 9 and 13 matter most.**

## 4. Further reading

**Documentation.** The LM Studio docs on quantisation and the OpenAI-compatible server.

**Spec.** The Model Context Protocol specification — the concepts section, not the full API reference.

**Practice.** Pick one repetitive task from your own work and build a Gem for it this week. Building one teaches more than reading about ten.

---

# Appendix J · Classroom situations

## Situation one · The network drops

**What to do:** do not debug the network in front of the class. Switch to an already-downloaded model, say the download is running in the background, and continue. Mention that this is exactly why we cache models locally.

## Situation two · A student's machine will not run the model

**What to do:** move them to a 3B or lower model, pairing with a neighbour if needed. Say explicitly that this is a hardware limit, not a comprehension problem. It matters that they are not left feeling behind.

## Situation three · A question you cannot answer

**What to do:** say so plainly: "I don't know — let's look it up." Then either search or note it to answer next session. Students trust "I don't know" far more than a confident guess, and you are modelling exactly the verification habit you are teaching.

## Situation four · Running badly over time

**What to do:** cut parts 2 and 3 to their summary tables, keep part 4 intact, and deliver part 8 as a checklist rather than a walkthrough.

## Situation five · Very mixed ability in the room

**What to do:** give the fast group an extension — for example, have them compare Q4_K_M against Q8 output on the same prompt — while you help the slower half get a model loaded.

## Situation six · Nobody answers your questions

**What to do:** switch to directed questions or a show of hands. Ask "who has used ChatGPT for work this week?" rather than the open "any questions?" The specific question always gets more response.

---

*This script accompanies `ai-llm-lmstudio-deck.html` — 35 slides, eight parts, roughly 150 minutes.*
