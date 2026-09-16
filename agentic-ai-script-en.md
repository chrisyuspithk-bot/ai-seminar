# From LLM to Agentic AI: Principles, Frameworks and Practice — English Script

> Companion deck: `agentic-ai-deck.html` (34 slides)
> Language: English (translated from the Cantonese script)
> How to use: one section per slide. The first block in each section is the script you read aloud. The "Ops note", "Aside" and "Likely question" blocks are speaker reminders and are not read out.
> Speaker note: keep sentences short, one idea per slide. The first time a technical term appears, give the English term and then explain it in plain words.

---

## How to use this script (read first)

1. This script maps page by page to the deck. Each page holds roughly two to three minutes of material. If you are short on time, read only the bolded sentences in each section.
2. "You" means the whole class. If you are teaching one to one, switch everything to the singular.
3. The first time a technical term appears, give the English term first and then the plain-language explanation.
4. Part 5 is the highest-risk section because it depends on a Mac and a network. Part 6 only needs a browser. **If you can only do one live demo, do part 6.**
5. The lesson has one throughline: **intelligence lies in the relationships between components, not in any single component.** Everything else supports that.

---

# Part 1 · Opening and course overview (10 min · 01–03)

## Slide 01 · Cover: from LLM to Agentic AI

Hello everyone, and welcome to this hundred-and-twenty-minute hands-on class.

Let me start with a scene. You open an AI tool and type: "plan my trip to Japan next month, budget twenty thousand." What did AI used to do? It wrote you a lovely paragraph — "I suggest Tokyo on day one and Kyoto on day two." It sounded plausible, but you had no idea where it came from, and you could not press a button to book a flight.

Today's agentic AI does something completely different. It opens a browser itself, checks flights, compares prices, looks at hotels, checks the weather, works out whether twenty thousand is enough, produces an itinerary, and may even book it. **That is the shift we cover today: from talking to doing.**

There are seven parts. Part 1 is the overview. Part 2 covers the fundamental difference between agentic AI and an LLM. Part 3 is the most interesting section — we look at two real cases, Kimi in China and Sakana AI in Japan, to see what "multiple AIs working together" actually means. Part 4 covers industry frameworks. After the break, parts 5 and 6 are hands-on: we generate a slide deck on a Mac using OpenWorkers, and then build an app from a single prompt on OpenHands Cloud.

**Today's goal is concrete: not that you can write code, but that you see with your own eyes how an agent goes from one sentence from you to a finished deliverable.**

> **Ops note** Before you start, confirm the classroom network can reach GitHub and app.all-hands.dev. Part 5 needs macOS; part 6 only needs a browser. If the network is unreliable, have a pre-recorded demo video ready.

## Slide 02 · Four questions we will answer today

Instead of "here is what we will cover", let me open with four questions. Once you have heard them, you will know what to take away.

Question one: what exactly is agentic AI? Note that I am not asking what AI is. I am asking what changes when you add the word agentic. That is part 2.

Question two: what happens when multiple agents work together? If one agent is not strong enough, should we not just train a stronger one? Why bring in several? That is part 3, and it is the most interesting part today.

Question three: what frameworks and tools exist? You may have heard of LangChain, AutoGen, CrewAI. What do they do, and which should you use? That is part 4.

Question four: how do you actually do it? This one matters most, because you can look up the first three online, but actually doing it yourself cannot be replaced. That is parts 5 and 6.

**Notice the order: concept, cases, tools, hands-on.** That is not arbitrary. It is a learning path. You cannot skip ahead to part 6, because if you do not know why you are doing something, you will copy steps without being able to use them.

> **Teaching note** You can do one thing on this slide: give students thirty seconds to write down which of the four questions they most want answered. Then, before each part, say "this part answers question two for you." It makes the whole session much more coherent.

## Slide 03 · This is no longer a lab concept

Slide three, and I want to deal with a common reaction: students think this is big-company stuff that has nothing to do with them.

I will cite a report. A survey published in November 2025 by MIT Sloan and the Boston Consulting Group found that **thirty-five percent of the firms surveyed had already deployed AI agents, and another forty-four percent planned to follow shortly.**

Do the arithmetic: thirty-five plus forty-four is nearly eighty percent. Nearly eighty percent of firms are not merely aware — they have done it, or they are about to. What does that number mean? That this is no longer future tense. It is present continuous.

**But one warning: that number does not mean they are doing it well.** Deployment and success are different things. Plenty of firms say "we use AI" when what they actually did was open some accounts. So the meaning of that number is not "you should worry about falling behind." It is "you should know this is a real trend, not hype."

What I want you to take away today is not panic. It is a map. **We have split the course into four stages: principles, cases, frameworks, practice.** By the end you will know where this came from, what is happening, what tools exist, and how to start.

> **Aside** If your audience is students, reframe this slide: not "will your company use it" but "how will you work after you graduate." That version lands much harder with them.

---

# Part 2 · The fundamental difference between agentic AI and an LLM (15 min · 04–08)

## Slide 04 · From talking to doing

Now to the substance. This is the most important contrast in the lesson and I want you to remember it.

Generative AI — the ChatGPT and Gemini you use — produces content. You ask a question, it gives you text. You ask for a poem, it writes a poem. You ask for a summary, it summarises. **Its output is text, and you have to do something with that text yourself.**

Agentic AI is different. It is AI that takes action in the world. Note the word action.

Action comes in two kinds. The first is physical: a robot moving boxes, an arm welding. The second is digital: booking a flight, editing a file, sending an email, writing code and then running it. Today we focus on the second, because it affects most people's work most directly.

**One line to make the difference clear: generative AI tells you how to do it. Agentic AI does it for you.**

You might ask: is this just automation? Not quite. Traditional automation means you write the process and it follows it, like an Excel macro. Agentic AI is different — you do not write the process. You state a goal, and it works out how many steps are needed and what each step is. That flexibility is the new part.

> **Teaching note** Ask students: "of the AI tools you used today, which are talking and which are doing?" Most will find that ninety-nine percent of what they use is the former. That discovery makes everything after this feel more relevant.

## Slide 05 · Four levels of intelligence: four steps

The last slide covered talking to doing. But there are actually four levels, not two. Picture four steps.

**Level one: the LLM.** The question it answers is "can you speak." It has language ability, but no ability to act and no reliable source of knowledge.

**Level two: RAG.** The question it answers is "are you grounded." You give it documents and it answers from those documents rather than from memory.

**Level three: the AI agent.** The question it answers is "can you do things." It has tools, memory and planning, and can complete a task.

**Level four: agentic AI.** The question it answers is "can you coordinate." Multiple agents work on one thing, each with a role.

Why steps rather than a list? Because steps have an important property: **you have to climb them in order, and you cannot skip.** Without an LLM's language ability there is no RAG. Without RAG's grounding, an agent acts on nonsense. Without a solid single agent, multi-agent coordination is empty talk.

**That image will be useful when someone tells you their company uses multi-agent systems. You can ask: "so is your single agent reliable?" If they cannot answer, their multi-agent story is probably marketing.**

> **Likely question** "Do I have to follow this order?" In product terms, yes. When learning, you can look at level four first to have a target, then come back — the difference is that you know you are learning, not building.

## Slide 06 · One line each

The last slide gave you four steps. Here are four lines, one each. Learn them.

**An LLM is the language engine of intelligence.** It handles understanding and generating language, and it underlies everything.

**RAG is the knowledge foundation.** It makes the AI's answers grounded rather than guesses.

**An AI agent is a task execution unit.** It can take one concrete thing from start to finish.

**Agentic AI is an organisational coordination system.** It is not a unit but a system, with many units operating together.

I especially want you to notice the word system in the last line. That word matters, because it represents a shift in thinking: **when you move from using a tool to designing a system, your role changes.**

Using ChatGPT, you are a user. You think of the question, write the prompt, and judge the answer. Designing an agentic system, you are a designer. You think: how many steps does this task need? Which agent does each step? How do they communicate? What happens when something fails?

**That role change is the core value of today's session.** Not one more tool, but a different identity.

> **Aside** This "from user to designer" shift connects to the framework choices in part 4, because once you are a designer you need frameworks, not just tools.

## Slide 07 · Five core technical components

This is the technical core. Agentic AI has five components; let me go through them.

**First, the LLM as the brain.** It handles understanding, judgement and decisions. That is level one.

**Second, tool integration.** That is the tool calling and MCP from the previous lesson. It lets the agent actually touch the outside world rather than just talk.

**Third, memory.** The agent has to remember what it did, otherwise it restarts every time. Memory can be short-term, within this conversation, or long-term, across conversations.

**Fourth, planning and reflection.** This is the most interesting one. The agent must not only execute but also decompose the task, and then check its own work afterwards. If it is wrong, it has to go back and fix it.

**Fifth, multi-agent coordination.** Several agents dividing the work.

Why do I stress that the first four make a single agent stronger while the fifth is the key one? Because the first four are one person getting better. The fifth is a group working together. **And historically, the big leaps in human civilisation came not from individuals getting smarter but from finding ways for many people to collaborate.**

One honest caveat: the fifth is also the hardest. Every additional agent doubles the communication cost, the chance of error, and the coordination difficulty. That is the theme of part 3.

> **Teaching note** An analogy works here: the first four are one very capable employee, the fifth is a team. One capable person can do a great deal, but some things require a team — one person cannot simultaneously do marketing, engineering and finance. That lands immediately.

## Slide 08 · The clever secretary vs the plenipotentiary

Last slide of part two. Let me sum up with an analogy.

Traditional generative AI is like a very clever secretary. You tell them what to do and they do it well. You ask for a letter and it is beautifully written. But they will not decide for you whether to send it, who to send it to, or when. **They wait for your instruction.**

Agentic AI is like a plenipotentiary — an agent with full authority. You do not give step-by-step instructions; you state a goal. "Plan my trip to Japan next month, budget twenty thousand." It researches flights, finds hotels, checks the weather, builds an itinerary, and decides the steps itself.

**That is an enormous increase in capability — and here is the important warning: the stronger the capability, the more the trust and oversight mechanisms matter.**

Think about it. If a secretary only drafts your letters and gets something wrong, you fix it. If an agent with booking authority gets it wrong, your money is gone. So the industry has a term for this: human in the loop — a human keeps approval rights at the key decision points.

Both tools I will demonstrate today, OpenWorkers and OpenHands, have this design. **OpenWorkers describes it as approval on every important action: it proposes, you decide.** That is not a restriction; it is a necessary design.

> **Aside** The theme of trust returns in part 7. You can plant the seed here: "we will come back to this question, because it decides whether agentic AI can actually be deployed."

---

# Part 3 · Agent swarms and multi-agent coordination (20 min · 09–16)

## Slide 09 · If one agent is not strong enough, why not train a stronger one?

Part 3, the most interesting section, because we have two real cases. Before we start, one question — the title of this slide.

**If one agent is not strong enough, why not simply train a stronger one?**

It is a natural thought. Your computer is slow, you buy a faster one. Your model is not clever enough, you train a bigger one. That approach works in many settings — the 4B, 7B and 70B we discussed follow exactly that logic: bigger is stronger.

But that path has a limit. **The expertise a complex task requires vastly exceeds the boundary of any single model.**

An example. Suppose the task is "open a restaurant for me." You need market research, site selection, financial planning, menu design, hiring, licensing and marketing. Seven different things, each needing different expertise. Train one generalist model and it might do all seven at sixty percent, none of them professionally. Seven specialist agents each at ninety percent, with their outputs integrated, will beat one generalist at sixty.

**So the core idea is: intelligence lies not in the nodes but in the relationships.**

That is abstract, so here is an example. Think of a football team. You would not ask one player to be goalkeeper, defender and striker. You put eleven players in different roles, and the coordination between them — the relationships — is what makes the team strong. Put eleven of the best strikers on the pitch and they will not win.

So the right question is not "how do we train a stronger node" but "how do we arrange for them to work together."

> **Teaching note** A live activity works here: split students into groups and give them five minutes to design a multi-agent system for "open a restaurant", listing how many agents are needed and what each does. The activity makes them feel how hard task decomposition actually is.

## Slide 10 · Moonshot and Kimi K3

First real case, from China: Moonshot AI, whose product is called Kimi.

Specifications first, so you feel the scale. **Kimi K3 has two-point-eight trillion parameters.** Recall that 7B from last lesson was seven billion — two-point-eight trillion is seven hundred billion, several thousand times 7B. **Its context is two million tokens**, twice Gemini's paid million. **It uses eight hundred and ninety-six routed experts, activating only sixteen at a time.** That is a mixture-of-experts architecture: inside it there are eight hundred and ninety-six specialists, but only sixteen relevant ones are called for any given case, so it does not use all its capacity every time.

But let me be clear: **these specifications are not the most important part today.**

You can look the numbers up online, and they will be beaten in three months. What is genuinely worth noticing is this: **its agent swarm product supports up to a hundred concurrent sub-agents.**

A hundred. Running at the same time. This is not "our model is big." It is "we can put a hundred workers on the job at once." Feel the difference: the former is a cleverer person, the latter is a crew working in parallel.

**That is the "relationships" idea from the last slide.** And this direction is the most important change in this round of AI development. We are moving from training bigger models to organising more models.

> **Aside** These numbers age fast. If a newer version exists when you teach, do not avoid it — say "see, the numbers I quoted three months ago are already out of date, but the direction has not changed." That is itself a good teaching moment.

## Slide 11 · How does a swarm operate?

The last slide mentioned a hundred sub-agents. How do they actually work? Three numbers, then one key point.

**First, it dynamically generates up to a hundred sub-agents.** Note the word dynamically. It does not pre-define "number one does marketing, number two does finance." After receiving your task, the model decides how many to open and what each should do.

**Second, up to one thousand five hundred tool calls.** Those hundred agents can collectively invoke tools fifteen hundred times. That is a very large number — if each call is a web lookup or a file read, fifteen hundred calls means it can process an enormous amount of material.

**Third, execution time reduced by up to four point five times.** That is the most practical number. The same task, done by the swarm, in four and a half times less time.

**And now the key point: the entire swarm is created and orchestrated automatically by the model, with no pre-defined roles.**

That sentence is the heart of the case. Recall the activity from the last slide: you designed a restaurant system and you wrote "market agent, finance agent, site agent." That is pre-defining roles. Kimi does something different — you state the task and it decides how many and what kind.

**Why does that matter? Because pre-defining roles means you must know in advance what will be needed. But many real tasks are discovered as you go.** While doing market research you might find a region with unusually many competitors, which calls for an extra competitor-analysis agent. If your roles are fixed in advance, you cannot make that adjustment.

> **Likely question** "Is dynamic generation always better? Doesn't it get chaotic?" It does get chaotic. That is the price — you give up predictability for flexibility. So the hard part of such systems is not "how many to open" but "how to guarantee it does not go off the rails."

## Slide 12 · Not only scale up, but scale out

Here are two terms to remember.

**Scale up** means making one model bigger. From 7B to 70B, and from 70B to two-point-eight trillion. That has been the mainstream direction for a decade.

**Scale out** means organising multiple models. Not making one bigger, but opening several.

Moonshot's direction is both at once: **a bigger model plus more agents.** That is their strategy.

Let me cite a book. Marvin Minsky's "The Society of Mind", 1986. His claim: **intelligence exists in how components are organised, not in any single component.**

Think about what that means. Minsky was one of the pioneers of AI, and what he said forty years ago is what Kimi has now implemented. He said you should not ask which brain cell holds the intelligence, because it is not in any cell — it is in how they are connected.

**That is the original source of the idea that intelligence lies in relationships.**

I think the citation has a deeper lesson: **it reminds us that when we meet a new technology, we should not only ask how many parameters it has. We should ask how it organises itself.** Because the organisation is where the real breakthrough is.

> **Aside** You can link this back to your audience's field. If they manage people, the point is familiar: a company's capability is not how many clever people it has but how they collaborate. That makes it click immediately.

## Slide 13 · Sakana Fugu: AI's orchestrator

Second case, from Japan.

Sakana AI is a Japanese unicorn founded in 2023. It has one unusual detail: **it was co-founded by Llion Jones, the fifth author on the Transformer paper.** Remember the Transformer? I mentioned it when covering self-attention last lesson — one of the authors of that landmark paper went and started a company.

That is a good story in itself: **the people who wrote the Transformer paper are now working on what comes after the Transformer.**

Their product is called Fugu. What is Fugu? **It is an orchestrator model from June 2026.** In one line: **it does not answer questions itself. It calls on models from around the world.**

That idea is counter-intuitive. Everyone else is competing on how clever their model is. Sakana's approach is: I will not compete with you. I am the orchestrator. I assign the work to whoever is best suited.

**That is like a project manager in a company.** A good PM is not necessarily the best engineer or the best designer. They know who suits which job, and they coordinate. Fugu is the PM of the AI world.

Where is the cleverness? **In that it does not need to win any single race.** It does not need to build the strongest model. It only needs the best ability to choose models. The former is a money-burning arms race; the latter is a game of intelligence.

> **Teaching note** This contrasts with the last slide: Kimi's direction is "train a huge model yourself and coordinate a hundred agents", Sakana's is "train no model, only orchestrate." Two paths, two philosophies. We formalise the contrast on slide 16.

## Slide 14 · Fugu's four mechanisms

How does Fugu actually work? Four mechanisms.

**First, identify the problem type.** When it receives your question, the first step is not to answer but to judge: what kind of problem is this? Maths? Writing? Code? Analysis?

**Second, select a worker model.** Having judged the type, it picks the best-suited model. The key point: **it can pick models from different companies.** Your maths goes to one, your writing to another.

**Third, decompose the task.** If the problem is complex enough, it splits it into sub-tasks and assigns them to different models.

**Fourth, verify and synthesise.** Having received answers from several models, it does two things: verification, to spot which answer has problems, and synthesis, to integrate them into one complete response.

Those four steps make a complete orchestration pipeline. And the effect is this: **answer quality exceeds what any single model produces on its own.**

That line deserves a pause. It is not saying it is stronger than the strongest model. It is saying it is better than what each model achieves alone. That means **orchestration itself creates value, and that value is not supplied by any single model.**

> **Aside** This also explains how Sakana can be so valuable without training a model. What it sells is not model capability but orchestration capability.

## Slide 15 · Performance and "AI sovereignty"

Two parts to this slide, one technical and one strategic. Technical first.

**Terminal Bench performance peaks with GPT-5.5, and GPQA Diamond performance centres on Gemini.** Those are benchmarks; you do not need the numbers. You need one fact: **the strongest model differs by task.** On some tasks GPT is best, on others Gemini.

**That fact is the reason orchestration exists.** If one model were always strongest, you would not need an orchestrator — you would just use that one. But reality is that no single model wins everything, so knowing how to choose becomes a skill.

Now the strategic part, which is more important than the technical.

Sakana's strategy: **learning from Anthropic export controls, the underlying model pool is fully replaceable.** Unpack that. What happened? The United States imposed export controls on AI models, meaning certain countries cannot use certain models. If your entire company is built on "we use model X", a change in the rules can finish you.

Sakana's approach: **I am not tied to any single model.** Block model A and I switch to B. Block B and I switch to C. Because my core value is not in the model. It is in the orchestration.

**That is what AI sovereignty means: not "I own the strongest model", but "I am not controlled by any single model."**

**And the conclusion is one line: orchestration capability is itself becoming an independent source of competitiveness.**

You used to think of orchestration as a supporting role and the model as the value. Sakana shows that once models become commodities — once everyone can buy them — orchestration becomes the differentiator.

> **Teaching note** The strategic part suits a discussion. You can ask: "if you were a company's CTO, would you commit to one model or keep the pool replaceable?" There is no standard answer, but the discussion shows students the trade-off.

## Slide 16 · Kimi Agent Swarm vs Sakana Fugu

This closes part 3. Here is a comparison.

| Dimension | Kimi Agent Swarm | Sakana Fugu |
| --- | --- | --- |
| Core strategy | Trains a huge model plus large-scale concurrency | Trains no model, orchestrates only |
| Number of agents | Up to 100 concurrent sub-agents | Not fixed; delegated per task |
| Role definition | Model generates roles; none pre-defined | Orchestrator identifies type then selects |
| Strategic position | Scale up plus scale out | Breaks single-vendor dependence |
| Distinct value | Execution time cut by 4.5× | Underlying model pool fully replaceable |

I do not want you to memorise the table. I want you to remember one question: **is this company's value inside the model, or outside it?**

Kimi's answer is both — it trains a huge model and also orchestrates. Sakana's answer is purely outside — it owns no model, it owns orchestration.

Which path wins? I do not know, and I do not think there is an answer today. But the fact that both exist is itself a signal: **competition in AI has expanded from which model is strongest to which system is cleverest.**

**And that shift is the best evidence for the "intelligence lies in relationships" idea from part 2.**

---

# Part 4 · From frameworks to tools (15 min · 17–21)

## Slide 17 · Google ADK (Agent Development Kit)

Now from cases to tools. You might ask: I am not a big company, how do I build an agentic system myself? The answer is frameworks.

The first is Google ADK, Agent Development Kit. It is an open-source framework released at Cloud NEXT in April 2025.

Four features.

**First, multi-agent by design.** It was built around multi-agent from the start, rather than a single-agent framework with multi-agent bolted on. That matters, because the difficulty of multi-agent systems is coordination, and if the framework fights you, you will suffer later.

**Second, a rich model ecosystem.** It integrates LiteLLM, so you can use models from different vendors without being locked to one.

**Third, a rich tool ecosystem, including MCP.** Remember MCP from last lesson, the USB-C analogy? ADK supports MCP, so you can use ready-made tools from the ecosystem directly.

**Fourth, built-in evaluation.** Many people overlook this and it matters. An agent's output is not as easy to test as a conventional program — it is not "A in, B out", it is a system with judgement. So how do you know whether it is doing well? You need evaluation tooling, and ADK includes it.

**The strongest evidence is that Google's own Agentspace and Customer Engagement Suite use this framework.** It is not a developer toy; it is something Google runs in production.

> **Aside** For enterprise users, ADK's advantage is its integration with GCP. If you already use Google Cloud, this framework makes deployment and monitoring much smoother.

## Slide 18 · LangGraph: drawing your workflow as a graph

The second framework is LangGraph, from the LangChain team.

Its positioning: for **stateful, multi-actor** LLM applications. Note those two adjectives. Stateful means it remembers what happened before. Multi-actor means more than one agent.

It has four core concepts, and here is an analogy. **Think of LangGraph as drawing a flowchart.**

**First, StateGraph.** The graph itself. You define a state — the data that flows through the process.

**Second, Node.** The points on the graph. Each node is a processing step.

**Third, Edge.** The lines connecting nodes, defining where the flow goes.

**Fourth, persistence.** This is LangGraph's most valuable feature. It supports three things: memory, resuming after an interruption, and human-in-the-loop — inserting a manual approval mid-flow.

**Human-in-the-loop is the same idea as the human in the loop from part 2.** I said earlier that the stronger the capability, the more oversight matters. LangGraph provides that mechanism at the framework level.

Actual users include LinkedIn, Uber, Klarna and GitLab — companies with complex workflow requirements.

> **Teaching note** Use a drawing here. Put three circles and two lines on the whiteboard and say "that is a StateGraph." Students immediately see that frameworks are not that abstract.

## Slide 19 · Two design philosophies

So which framework should you choose? I will not give you an answer. I will give you a way of thinking.

**Google ADK is the enterprise integration school.** Its focus is GCP integration, enterprise deployment and built-in evaluation. If you are a company already on Google Cloud and you want to ship quickly with monitoring and evaluation included, ADK is smoother.

**LangGraph is the fine-grained control school.** Its focus is flow control, state management and resumption. If you need precise control over what happens at each step, need to pause for human approval, and need complex state transitions, LangGraph suits you.

**So the choice depends on three things: your stack, your deployment environment, and your team's familiarity.**

I especially want to stress the third. Very often a technology choice is not about picking the best but about picking what your team can actually use. A theoretically superior framework your team does not know is a liability.

**One practical piece of advice: if you are unsure, choose the one your team already knows.** Frameworks can be swapped; the team's learning cost is real.

> **Likely question** "Do I have to use a framework? Can I write my own?" You can. But ask yourself whether you want to reinvent state management, error handling and retry logic — the things a framework has already solved.

## Slide 20 · Don't write a framework, use one

Now from the framework layer to the tool layer. The distinction matters: a framework is something you write code in to build a system. A tool is something you use directly.

Two tools.

**First, OpenHands.** Formerly OpenDevin, with over seventy-four thousand GitHub stars, which indicates an active community. Four ways to use it: Cloud, CLI, local GUI, and the Software Agent SDK. **That is the "boundaries are blurring" example from earlier — the same product is both a tool for ordinary people and a framework for developers.**

**Second, OpenWorkers.** Open-sourced by Andrew Ng's team. Three features: it delivers finished artefacts rather than text; local-first with any model, so you can use your own API key without vendor lock-in; and approval on every important action, which is the human-in-the-loop idea.

**Why did I choose these two for the live demos?** Because they represent two scenarios: OpenWorkers represents "I do not write code but I want a finished artefact", and OpenHands represents "I want a complete development task done." Between them they cover most people's needs.

> **Ops note** This slide previews parts 5 and 6. You can say: "over the next forty minutes we will do two things with these tools. You do not need to follow along, but watch how they decompose the task."

## Slide 21 · Four layers, top down

Last slide of part 4. Let me arrange everything so far into a four-layer architecture.

**Top layer: the agentic AI application layer.** The product you finally use, such as a customer service system.

**Second layer: the framework layer.** Google ADK, LangGraph. This is where you build your system.

**Third layer: the agent runtime layer.** OpenHands, OpenWorkers. This layer does the actual execution.

**Fourth layer: the model layer.** GPT, Claude, Gemini, Qwen.

**Why lay it out like this? Because it tells you which layer you work at.**

If you are a user, you only see the top layer. If you are a developer you work at layers two and three, but you do not need to touch layer four, because models are replaceable.

**And the most notable thing is that the boundaries between these layers are blurring.** OpenHands is a good example — it offers both an SDK at the framework layer and a Cloud GUI at the application layer. That means the industry is still evolving fast and has not settled.

**The practical implication: do not lock yourself into one choice at one layer too early.** Keeping your architecture able to swap layers is an important design principle.

> **Aside** This four-layer view also helps you judge marketing claims. If a company says "we are an agentic AI platform", you can ask which layer they are at. Often they have built a wrapper at the top layer with everything underneath rented.

---

# Break · Intermission (15 min · 22)

## Slide 22 · Fifteen-minute break

Let's take fifteen minutes.

In the first half we covered principles and cases: the four steps from talking to doing, the five components, the Kimi and Sakana cases, and the four-layer relationship between frameworks and tools.

The second half is two live demos. **Part 5: on a Mac, using OpenWorkers, we go from a pile of source material to a generated slide deck. Part 6: on OpenHands Cloud, we build a working to-do app from a single prompt.**

**Neither requires you to write code.** What you should watch is how it decomposes the task, how it decides the next step, and how it hands you a finished artefact.

Before the break, here is a question to sit with: **if you had an agent that could do anything, what is the first thing you would hand over?** You do not need to tell me, but have an answer in mind. After the second half, look at that answer again — it may have changed.

See you in fifteen minutes.

> **Ops note** Use the break to do two things. One: check the demo environment for the second half — terminal, browser tabs, API keys. Two: talk to any students who are struggling and gauge the room. Those fifteen minutes are not only a break; they are your buffer.

---

# Part 5 · Mac live demo: OpenWorkers (20 min · 23–26)

## Slide 23 · Environment setup

Now the hands-on part. In this section we generate a slide deck on a Mac using OpenWorkers.

First the requirements. You do not need to follow along, but you should know what is needed. **One, macOS thirteen or later. Two, at least 8GB of RAM, 16GB recommended. Three, Node.js version twenty or later. Four, an LLM API key.**

That fourth point deserves more. OpenWorkers works with any model, so you can use any vendor's API key. **For teaching I suggest DeepSeek or Kimi, because the cost is lower.** That is very practical — if you use the most expensive model on a task with twenty tool calls, the cost will put you off experimenting.

The install flow: download the installer from GitHub, then configure your API key. Configuration is simple — usually paste it into the settings interface or a config file.

**One warning: an API key is something to guard carefully.** Do not paste it somewhere public, do not commit it to git, do not share it in a group chat. If it does leak, go to the vendor's console and revoke it immediately.

> **Ops note** Run the full install flow yourself the day before. This tool updates frequently, so the steps from three months ago may no longer apply. If the network is unreliable, have a screen recording ready.

> **Likely question** "I am not a Mac user — can I not use this?" OpenWorkers may work cross-platform, but today's demo is macOS-based. If you are on Windows, watch the flow; the concepts are identical, only the install steps differ.

## Slide 24 · Prepare material, then give the instruction

Once the environment is ready, prepare the source material.

We create a folder on the desktop called `ProductLaunch` containing three files: **`product_features.md` (the feature list), `market_data.csv` (market data), and `competitor_analysis.md` (competitor analysis).**

Why three different formats? Because I want you to see something: **the agent has to handle different kinds of material.** It is not just reading text. It has to read the numbers in a CSV and understand the structure in the markdown.

With the material ready, we type the instruction into the chat box. Roughly this:

"Using the three files in the `ProductLaunch` folder on my desktop, produce a product launch presentation. Requirements: one, six sections. Two, output as `.pptx`. Three, filename `ProductLaunch_Presentation`."

Notice several features of that instruction. **It has a clear input source** — I said exactly which folder. **It has a clear output format** — not "write me some things" but `.pptx`. **It has a clear structure** — six sections. **It has a clear filename.**

**Those four points are the COSTAR framework from last lesson applied in practice.** You have an objective and a response format, which are the two that matter most.

> **Teaching note** Prepare the source material with real content before the session, for example a fictional smartwatch product. Real data makes the finished artefact land. Lorem Ipsum is much weaker.

## Slide 25 · The agent decomposes and delivers

Once you press send, watch what it does. This is the slide most worth your attention today.

Five steps.

**Step one, planning.** It first thinks: how should this be done? What steps are involved? Note that it does nothing here — it is purely thinking. This is the planning and reflection from part 2.

**Step two, reading files.** It opens the three files on your desktop and reads the contents. This is the tool calling from last lesson — it is genuinely touching your file system.

**Step three, generating content.** Based on what it read, it produces the six sections. This is where its language ability comes in.

**Step four, creating the presentation.** It converts the content into `.pptx`. This step is not writing text; it is creating a file — the taking action from part 2.

**Step five, checking and delivering.** It verifies the file is sound and hands it to you.

**And the most important line: what it delivers is a presentation file you can open and share directly.**

Feel the difference. If I gave you text saying "a product launch deck should have five points", you would open PowerPoint, lay it out yourself, build six pages. Now it gives you a `.pptx` and you just open it.

**That is the difference between delivering an artefact and providing content.** And everything I am saying today revolves around that difference.

> **Teaching note** Open the `.pptx` live here. Point out the filename, the six sections, and that the numbers came from your CSV. Those details convince them it really read the files rather than generating something random.

## Slide 26 · It proposes, you decide

Last slide of part 5, and an important idea.

**If the artefact is not ideal, you do not start over. You tell it what is wrong, and it keeps the context and revises the relevant pages.**

Many people do not know this. They assume they have to rewrite the instruction. You do not. Just say "the numbers on page three are wrong, use the second-quarter figures", and it changes only that page.

**Now three design philosophies, the core of OpenWorkers.**

**First, local-first.** It does as much as possible on your machine, which protects privacy.

**Second, approval gating.** Every important action needs approval. It proposes, you decide. This is the human-in-the-loop idea from part 2 made concrete.

**Third, the connector ecosystem.** It supports more than twenty-five services including HubSpot, GitHub and Slack. **This is the most strategically significant point.** When an agent can connect to your CRM, your version control and your messaging, it stops being a standalone tool and becomes part of your workflow.

**These three answer one question: how trustworthy does an agent have to be before you let it act?** The answer: local-first so your data does not leave; approval gating so you keep control; a connector ecosystem so it can genuinely do things. All three are needed.

> **Aside** You can ask the class: "if this agent had no approval mechanism, would you still let it touch your files?" Most will say no. That is why approval gating is not a feature but a precondition.

---

# Part 6 · OpenHands Cloud walkthrough (20 min · 27–31)

## Slide 27 · OpenHands architecture

Part 6. Here we build an app from a single prompt on OpenHands Cloud. First, the architecture.

Four parts.

**First, the core: LLM and agent.** The LLM is the brain; the agent is the decision logic.

**Second, the environment: runtime and sandbox.** This matters. **It does not work on your computer. It works inside a sandbox.** A sandbox is an isolated environment where it can install things, run things and break things without affecting your machine. That is a key safety design.

**Third, the service: server.** The backend that receives your instructions and coordinates resources.

**Fourth, the backbone: EventStream.** It records everything that happens, forming a complete timeline.

**And the line most worth noting: it gives the LLM a complete development environment and forms a closed feedback loop.**

Why closed loop? Because it is not "you say something, it gives an answer." It is "you say something, it acts, it looks at the result, it finds a problem, it fixes it, it acts again." **That cycle — act, inspect, correct — is the most fundamental difference from ordinary AI.**

Think about it. An ordinary AI writes code and does not know whether it runs. OpenHands can genuinely run it, see the error, and fix it. That is the closed loop.

> **Teaching note** For the sandbox concept, use an analogy: a sandbox is like a laboratory where you can run dangerous experiments without affecting the outside. That is the precondition for letting it act.

## Slide 28 · Start in three steps

How do you begin? Three steps.

**Step one, sign up.** Go to `app.all-hands.dev` and sign in with GitHub or GitLab.

**Step two, configure a model.** OpenHands is model-agnostic — it supports OpenAI, Anthropic, Google, LiteLLM and others. Use whichever you already have a key for.

**Step three, start a task.** Choose Launch from Scratch.

**Advice for beginners: if you do not know which model to pick, start with Claude or the GPT series.** Why? Because those two are more stable on coding-related tasks and make fewer mistakes. On your first attempt you should not be worrying about whether you chose the wrong model. You should be watching how it decomposes the task. Once you are comfortable, try others.

Those three steps take under five minutes. **Let me stress that: the barrier to entry is far lower than you expect.** No environment to install, no Docker to configure, no dependencies to resolve. That is the value of the cloud version.

> **Ops note** Demonstrate the signup live using a spare account. When students see it takes five minutes, they are immediately motivated to try. Mention that they can sign up with their own GitHub account afterwards.

## Slide 29 · This is all we give it

This is the most striking slide today. Our input is one prompt.

We will say: "Build me a to-do web app in Python Flask. It needs create, edit and delete, and the ability to mark items complete. Store data in SQLite. Use plain HTML and CSS on the front end, no frameworks. Include a README. Include tests. When you are done, start the server and verify it works."

Look at the features of that prompt.

**First, we specified the stack.** Python Flask, SQLite, plain HTML and CSS. Why specify? Because if you do not, it chooses, and its choice may not be what you wanted. Specifying is a form of control.

**Second, we listed the features.** Create, edit, delete, mark complete. All four.

**Third, we asked for extras.** A README and tests. Those are not features, but a professional deliverable should have them.

**Fourth, and most critical: when you are done, start the server and verify it works.** That sentence is the closed loop from the last slide. I do not just want it written. I want it run and confirmed.

**Without that last sentence, it writes the code and hands it to you — and then you discover it does not run.** With it, it finds the problem itself and fixes it.

**That is the clearest example of instruction quality determining delivery quality.** The same "build me an app", with and without that last sentence, gives very different results.

> **Aside** Link back to COSTAR: this prompt has an objective and a response format — Flask, SQLite, HTML — and "start the server and verify" is a constraint you added yourself.

## Slide 30 · From planning to delivery, six stages

Once you press send, it does six things.

**First, planning.** It works out what to do and how many steps.

**Second, environment setup.** It installs Flask and the SQLite driver inside the sandbox and creates the project structure.

**Third, writing code.** It writes the code. This is the step most people expect.

**Fourth, testing and debugging, with self-iteration.** This is the key step. It runs the tests, sees errors, fixes them, and runs again. The cycle may repeat several times.

**Fifth, starting and verifying.** It starts the server and confirms it actually works.

**Sixth, delivery.** It hands you the artefact.

**Let me stress again: step three is only one of six.** Most people imagine AI coding as step three — it writes the code. But what makes this work is the cycle in step four.

**That cycle is the fundamental difference between OpenHands and a code generator.** A generator does step three. OpenHands does six.

> **Teaching note** Watch the six steps live. Students will see it installing, see it error, see it fix. When it finds its own error, pause and say: "look, I did not tell it to fix that — it knew it had to." That moment is more persuasive than any explanation.

## Slide 31 · Not just generating code, but completing a development task

Last slide of part 6. Four design principles.

**First, sandbox isolation.** It works in an isolated environment and cannot affect your system. This is the precondition for letting it act.

**Second, EventStream-driven.** Everything is an event and everything is recorded. That makes the process traceable, replayable and auditable.

**Third, model-agnostic.** You can swap models. This is the same thinking as Sakana's strategy from part 3 — no vendor lock-in.

**Fourth, native sandboxing.** Its sandbox capability is native, not bolted on.

**And the most important conclusion: this is not just generating code. It is completing an entire development task.**

Where is the difference?

Generating code: I give you a chunk of code. You install it, run it, debug it.

Completing a development task: I give you a running system, with a README and tests, and I have already verified it.

**That difference is the difference between content and a finished artefact.** And that is what I have been talking about since part 2.

Listening from part 1 to here, I hope you see one thing: **this is not a change in technology. It is a change in how work is delivered.** From "I write it for you" to "I finish it for you."

> **Aside** That change affects how you work. In future you should not ask "what did the AI write for me" but "what did the AI deliver to me." That shift in question marks the shift in your thinking from using a tool to designing a system.

---

# Part 7 · Summary and Q&A (5 min · 32–34)

## Slide 32 · We understood this shift at four levels

Let's wrap up. I want to lay out everything today at four levels.

**First, the conceptual level.** Four steps: LLM, RAG, AI agent, agentic AI. The image is four stairs you cannot skip. And the line running through all four is from talking to doing.

**Second, the case level.** Two cases. Kimi Agent Swarm, the Chinese approach: train a huge model, support up to a hundred concurrent sub-agents, organise dynamically. Sakana Fugu, the Japanese approach: train no model, orchestrate only, with a fully replaceable model pool. Together they teach one thing: **intelligence lies in relationships, not in nodes.**

**Third, the framework level.** Google ADK and LangGraph, two design philosophies — enterprise integration and fine-grained control. The choice depends on your stack, your deployment environment and your team's familiarity.

**Fourth, the tool level.** We generated a deck with OpenWorkers and built an app with OpenHands. Those two prove one thing: **these are not concepts. They are things you can use today.**

**And the one line I most want you to take away: agentic AI is the key turning point where AI evolves from an assistive tool into a productive agent.**

What is the difference between an assistive tool and a productive agent? An assistive tool means you do the work and it helps you correct it. A productive agent means you state a goal and it hands you a finished artefact. That turn is not gradual. It is a jump.

> **Teaching note** Draw the four levels on the whiteboard. On the left, concept → cases → frameworks → tools. On the right, abstract → concrete. The visualisation makes the session feel like one structure rather than scattered information.

## Slide 33 · Three lines to take away

Three lines.

**First: the value is not in the model, it is in the system.** Of everything you saw today — Kimi, Sakana, OpenWorkers, OpenHands — not one wins by having the strongest model. They win on system design: how they organise, coordinate and deliver.

**Second: orchestration capability is an independent source of competitiveness.** This is Sakana's lesson. Once models become commodities everyone can buy, your differentiation is not the model but how you use it.

**Third: safety and trust are preconditions.** This is the lesson from OpenWorkers and OpenHands. Local-first, approval gating, sandbox isolation — these are not features, they are preconditions. Without them you would not dare let an agent do real work.

**So here are three things to do next.**

First, download OpenWorkers and run a real task. Not a toy task — use something from your actual work, such as a report you really need. **Because only a real task throws up real problems.**

Second, get the free tier on OpenHands Cloud and try building a small tool from one prompt. Start simple, such as a web page that does a calculation, or a script that tidies a CSV.

Third, once you are comfortable, use the "build a small tool from one prompt" pattern to solve one small pain point in your daily work. **Do not start with a big project. Start small.**

> **Aside** The three are ordered: experience with OpenWorkers, experiment with OpenHands Cloud, then apply it to your own problem. It is a learning path, not three separate tasks.

## Slide 34 · Closing

Last slide.

Let me finish with an observation.

The two cases today were one Chinese, one Japanese. Kimi's approach is "I must have the strongest model." Sakana's approach is "I do not need the strongest model; I only need to use the best models well."

**Those two paths represent two understandings of competitiveness.**

The first believes in ownership. To win, you must own the best resources.

The second believes in organisation. To win, you must be able to organise different resources.

**And I would say this: the future of AI competition may not belong only to the companies with the strongest single model. It may also belong to the companies best at designing relationships.**

Why do I say that? Because as model capability converges — anything you have, I can buy — the difference stops coming from what you own and starts coming from how you combine it.

**That principle is not limited to AI.** Think of any industry: the most successful companies are not always those with the best resources. They are the ones best at organising resources.

So what I really want to teach today is not what tools exist in AI. It is what questions you should ask when a new capability appears. You should ask how to organise it, not only how to obtain it.

That is all from me. Now for Q&A — ask anything.

> **Teaching note** Prepare three self-answered questions in case the room is quiet: "I cannot write code, can I still use this?", "are these tools safe, will they steal my data?", and "which tool should I learn first?" Those are the three most commonly asked.

---

# Appendix A · One line to take away from each part

| Part | One line |
| --- | --- |
| 1 | This is happening now, not a lab concept. |
| 2 | From talking to doing — four steps you cannot skip. |
| 3 | Intelligence lies in relationships, not in nodes. |
| 4 | The boundary between the framework layer and the tool layer is blurring. |
| 5 | The agent delivers an artefact, not content. |
| 6 | Closed-loop feedback: act, inspect, correct. |
| 7 | The value is not in the model, it is in the system. |

---

# Appendix B · Speaker notes

## 1. Timing

**Parts 1 to 3 are ten plus fifteen plus twenty, forty-five minutes.** That is concepts and cases. If the room is engaged, part 3 can run long — the two cases are the most interesting material, and five extra minutes is worth it.

**Part 4 is fifteen minutes.** If time is tight, compress it to ten by merging slides 17 and 18 and covering only the core difference.

**Protect the fifteen-minute break.** Do not cut it to five, because the second half needs the room alert.

**Parts 5 and 6 are forty minutes and should not be compressed.** If you genuinely run short, shorten part 4, or deliver the comparison table on slide 16 more quickly.

**Part 7 is five minutes, but leave at least ten for Q&A.**

## 2. Fallbacks for the two live sections

**Part 5 (OpenWorkers):**
- Unreliable network: use a pre-recorded screen capture.
- Install fails: use a pre-made `.pptx` and explain the flow in reverse.
- Not enough time: demonstrate up to "generating content" and skip checking and delivery.

**Part 6 (OpenHands Cloud):**
- This only needs a browser, so it is far more reliable.
- If the sandbox is slow to start: cover the architecture on slide 27 while it starts.
- If generation takes too long: open a new tab, continue with part 7, then come back.

**One line: part 5 is high risk, part 6 is low risk. If you can only do one, do part 6.**

## 3. The five questions students ask most

**"I cannot write code — can I still use this?"**
Neither part 5 nor part 6 requires you to write code. You need to be able to describe what you want. That is a different skill, and a much easier one to learn.

**"Will these tools steal my data?"**
Read the policy. OpenWorkers is local-first, so data does not leave. OpenHands works in a sandbox. But do not paste confidential material into a cloud tool without checking your organisation's rules.

**"Which tool should I learn first?"**
OpenWorkers, because the barrier is lowest and you get a finished artefact. Then OpenHands.

**"Do I need to understand the frameworks to use the tools?"**
No. But you need the four-level picture to know where each sits.

**"Will this replace me?"**
It replaces execution, not judgement. The person who decides what to build and whether the output is right is still you.

## 4. Currency warning

The Kimi specifications, Sakana's product details and the framework comparisons change quickly. Verify the current versions before teaching again. If they have changed, use that as a teaching point: the numbers move, the direction does not.

---

# Appendix C · Common misconceptions

## Misconception 1: "Agentic AI is just a better chatbot."

A chatbot produces content; an agent takes action and delivers artefacts. The distinction is in the output, not the model.

## Misconception 2: "If one agent is weak, train a bigger one."

Complex tasks need expertise beyond any single model's boundary. That is why organisation matters.

## Misconception 3: "More agents are always better."

Every agent adds communication cost, error surface and coordination difficulty. Multi-agent is not automatically superior.

## Misconception 4: "Multi-agent systems can define roles in advance."

Pre-defining roles requires knowing the task in advance. Real tasks are often discovered as you go, which is why dynamic generation exists.

## Misconception 5: "Orchestration is a supporting role, not the value."

When models become commodities, orchestration becomes the differentiator. That is Sakana's whole thesis.

## Misconception 6: "The strongest model wins."

No model wins every benchmark. Knowing which model suits which task is the skill.

## Misconception 7: "Frameworks and tools are the same thing."

A framework is what you build in; a tool is what you use directly. They sit at different layers.

## Misconception 8: "AI coding is just code generation."

Code generation is one of six stages. The loop of testing, debugging and verifying is what makes it work.

## Misconception 9: "Sandboxes are a limitation."

Isolation is what makes it safe to let an agent act. It is a precondition, not a restriction.

## Misconception 10: "Approval gates slow things down."

They are what make it trustworthy enough to use at all. Without them you would not delegate.

## Misconception 11: "Our company uses AI, so we are ready."

Deployment and success are different. Many firms opened accounts and called it adoption.

## Misconception 12: "You have to climb the four levels in order to build anything."

For products, yes. For learning, you can look ahead to have a target. The difference is knowing you are learning, not building.

## Misconception 13: "Vendor lock-in is a technical detail."

It is a strategic risk. A replaceable model pool is a form of sovereignty.

## Misconception 14: "Learning AI means learning which tool is strongest."

Tool rankings expire. Designing systems does not.

## Misconception 15: "This is only for big companies."

Both live demos today were done by one person on a laptop or a browser.

---

# Appendix D · Classroom activities

## Activity one · Opening (before part 1, five minutes)

Ask each student to name the task they would most want an agent to take over. Write them up and return to the list in part 7.

## Activity two · Design a swarm (after slide 09, five minutes)

In groups, design a multi-agent system for "open a restaurant." List the agents and their roles. The point is to feel how hard decomposition is — and then to see, on slide 11, that Kimi does this automatically.

## Activity three · Local or cloud (before slide 33, not applicable here — see lesson 2)

This lesson focuses instead on the agent-versus-chatbot distinction. Ask: "which of the tools you used today would you hand a real task to?"

## Activity four · Ordering the four levels (after slide 05, five minutes)

Give students the four level names shuffled and have them order them, then justify why the order cannot be skipped.

---

# Appendix E · Glossary

| Term | Plain reading |
| --- | --- |
| LLM | Language model; the language engine, level one |
| RAG | Retrieval-augmented generation; grounding answers in documents |
| AI agent | A unit that can complete one task using tools, memory and planning |
| Agentic AI | A system of coordinated agents |
| Scale up | Making one model bigger |
| Scale out | Organising more models |
| Agent swarm | Many agents working in parallel |
| Mixture of experts | Many specialised sub-networks, only some active per input |
| Orchestrator | A model that routes work to other models rather than answering |
| Multi-agent by design | Built around multi-agent coordination from the start |
| StateGraph | LangGraph's representation of a workflow as nodes and edges |
| Human in the loop | A human retaining approval at key decision points |
| Sandbox | An isolated environment where actions cannot affect the host |
| Closed loop | Act, inspect the result, correct, act again |
| EventStream | The recorded timeline of everything that happened |
| Approval gating | Requiring human approval before important actions |
| Local-first | Doing as much as possible on the user's machine |

**Speaker tip:** "agent" and "orchestration" are the two terms students nod along to without understanding. Check those two specifically rather than asking "any questions?"

---

# Appendix F · Rehearsal: likely questions and answers

## Scene one · "I cannot write code. Can I use any of this?"

**You could answer:**

"For parts 5 and 6 today, you did not need to. Notice what I actually did: I described what I wanted.

Writing code is one way to tell a computer what to do. **Describing the outcome in plain language is another, and it is the newer one.** It is a different skill, and I would argue it is easier to learn than syntax.

What you do need is the ability to say precisely what you want and to recognise when the result is wrong. That is judgement, and it is the part that does not automate."

**Why answer this way:** the fear is about a missing technical skill. Reframe to what the skill actually is.

## Scene two · "Will these tools take over my job?"

**You could answer:**

"They take over execution. They do not take over judgement.

Think about the six stages in part 6. The agent did planning, setup, coding, testing, verifying and delivery. What it did not do was decide **whether this app was the right thing to build, and whether the finished app was good enough to ship.** I did that.

**The jobs that go are the ones that are only execution.** If your work is entirely "someone tells me exactly what to do and I do it", you are exposed. If your work involves deciding what should be built, you are the one directing the agent."

**Why answer this way:** acknowledge the real part rather than denying it, then locate the durable role.

## Scene three · "Is multi-agent always better than a single agent?"

**You could answer:**

"No, and I want to be careful here because multi-agent is heavily marketed.

Every extra agent adds communication cost, another place to fail, and more coordination work. If a single agent can do the task reliably, use one.

**Multi-agent pays off when the task needs genuinely different expertise**, or when the work can be done in parallel. If the task is "summarise this document", one agent. If it is "run a market analysis, a financial model and a legal review", several."

**Why answer this way:** students will meet a lot of multi-agent hype. Giving them the condition under which it pays off is more useful than enthusiasm.

## Scene four · "Why doesn't Sakana just train its own model?"

**You could answer:**

"Because that would put it in the same race as everyone else, and it would need to win.

By orchestrating instead, it only needs to be good at choosing. **And critically, it cannot be locked out.** If a vendor blocks access to a model, Sakana swaps in another, because its value was never in the model.

That is a strategic choice about where to compete, not a technical limitation."

**Why answer this way:** it teaches the strategic reasoning, which is the real point of the case.

## Scene five · "Which tool should I start with?"

**You could answer:**

"Start with OpenWorkers, because the barrier is lowest and you get something finished on the first attempt. Nothing motivates like a real artefact.

Then OpenHands, because that is where you see the closed loop — the agent finding and fixing its own errors. That is the moment the whole idea clicks.

The frameworks come later, when you have a system to build rather than a task to finish."

**Why answer this way:** it gives an actual order, which is what the question is asking for.

## Scene six · "Isn't the approval process annoying?"

**You could answer:**

"It is slower, and that is the point.

Ask yourself: **would you let an agent book flights with your card without asking?** Probably not. The approval gate is not friction for its own sake. It is the thing that makes delegation possible at all.

And in practice you tune it. Low-risk actions run automatically; high-risk ones stop and ask. That is exactly how the tools we saw are designed."

**Why answer this way:** the student is weighing convenience against control. Name the trade-off explicitly.

---

# Appendix G · Speaker self-check

## An hour before

- Network reaches GitHub and app.all-hands.dev.
- OpenWorkers is installed and an API key is configured.
- The `ProductLaunch` folder with three files is ready on the desktop.
- OpenHands Cloud account is logged in and a model is configured.
- Sandbox has been started once to warm it up.
- Pre-recorded demo video is available as a fallback.

## Ten minutes before

- Terminal and browser tabs open for the demos.
- Projector resolution checked.
- Q&A fallbacks written down.

## Content check

- Can you state the four levels without notes?
- Can you explain the difference between scale up and scale out in one sentence?
- Can you justify why orchestration is a source of value?
- Can you demo the closed loop without reading from the script?

## Mindset

- Part 5 may fail. Have the fallback and move on calmly.
- Some students will want to debate the philosophy. Answer briefly and return to the throughline.
- Protect the break and part 6.

---

# Appendix H · Per-slide timing

| Slide | Topic | Minutes |
| --- | --- | --- |
| 01 | Cover | 3 |
| 02 | Four questions | 4 |
| 03 | Not a lab concept | 3 |
| 04 | Talking to doing | 4 |
| 05 | Four levels | 4 |
| 06 | One line each | 3 |
| 07 | Five components | 3 |
| 08 | Secretary vs agent | 3 |
| 09 | Why not train a stronger one | 4 |
| 10 | Moonshot and Kimi K3 | 3 |
| 11 | How the swarm operates | 3 |
| 12 | Scale up and scale out | 3 |
| 13 | Sakana Fugu | 3 |
| 14 | Fugu's four mechanisms | 3 |
| 15 | Performance and sovereignty | 3 |
| 16 | Kimi vs Sakana | 3 |
| 17 | Google ADK | 4 |
| 18 | LangGraph | 4 |
| 19 | Two philosophies | 4 |
| 20 | Tools not frameworks | 3 |
| 21 | Four layers | 3 |
| 22 | Break | 15 |
| 23 | Environment setup | 4 |
| 24 | Material and instruction | 5 |
| 25 | Decompose and deliver | 6 |
| 26 | It proposes, you decide | 5 |
| 27 | OpenHands architecture | 4 |
| 28 | Three steps | 3 |
| 29 | The one prompt | 5 |
| 30 | Six stages | 5 |
| 31 | A development task | 3 |
| 32 | Four levels | 3 |
| 33 | Three lines | 2 |
| 34 | Closing | 3 |

---

# Appendix I · Homework and assessment

## 1. Homework (to complete within a week)

**Task one · Run a real task (required).** Use OpenWorkers on something from your actual work. Submit the artefact and one sentence on what surprised you.

**Task two · Build a small tool (required).** Use OpenHands Cloud to build a small app from a single prompt. Submit the prompt and the result.

**Task three · Add verification (required).** Take your prompt from task two and add an explicit instruction to run and verify. Report what changed.

**Task four · Design a swarm (optional).** For a task in your work, write out how many agents you would use, their roles, and why a single agent would not do.

**Task five · Framework reading (optional).** Skim the Google ADK or LangGraph introduction and note which layer it sits at.

## 2. Assessment criteria

| Criterion | What good looks like |
| --- | --- |
| Conceptual grasp | Explains the four levels in their own words |
| Decomposition | Can break a task into agent-sized pieces |
| Instruction quality | Objective and format always specified; verification requested |
| Judgement | Knows when multi-agent is warranted and when it is not |
| Safety awareness | Understands approval gating and sandbox isolation as preconditions |

## 3. Self-check questions

1. What changes when you add the word agentic?
2. Name the four levels and why they cannot be skipped.
3. What are the five components of agentic AI?
4. Why is multi-agent not always better?
5. What does dynamic agent generation trade away?
6. What does scale out mean?
7. What is Minsky's claim about intelligence?
8. What does Fugu do that other models do not?
9. What does AI sovereignty mean here?
10. What is the difference between a framework and a tool?
11. Why is a closed loop the key difference from a code generator?
12. Why is approval gating a precondition rather than a feature?

**Questions 1, 4 and 11 matter most.**

## 4. Further reading

**Docs.** The Google ADK and LangGraph introductions — the concepts sections, not the full API.

**Product.** OpenHands Cloud free tier. The fastest way to understand a closed loop is to watch one.

**Regulation.** AI export controls and their effect on model availability. It explains why a replaceable model pool is a strategy.

---

# Appendix J · Classroom situations

## Situation one · The network drops

**What to do:** switch to the pre-recorded demo. If part 5 is affected, go straight to part 6, which only needs a browser. Say plainly that live demos depend on the network.

## Situation two · A student cannot install OpenWorkers

**What to do:** tell them not to install anything. Parts 5 and 6 are demonstrations; they can watch and do it at home. Not installing costs them nothing in this session.

## Situation three · A question you cannot answer

**What to do:** say you do not know and look it up together. In a session about agents, modelling verification behaviour matters more than having every answer.

## Situation four · Running badly over time

**What to do:** compress part 4 to the four-layer diagram only, keep both demos, and deliver parts 5 and 6 as demonstrations rather than walkthroughs.

## Situation five · Very mixed ability in the room

**What to do:** give the more experienced students an extension — have them design the swarm for a task from their own work while you help the others follow the demo.

## Situation six · Nobody asks anything in Q&A

**What to do:** ask your own prepared question out loud and answer it. Once the first question is asked, others usually follow. The three from appendix B work well.

---

*This script accompanies `agentic-ai-deck.html` — 34 slides, seven parts, roughly 120 minutes.*
