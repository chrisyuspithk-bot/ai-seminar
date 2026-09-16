# Machine Learning, Step One: From Data to Model — English Script

> Companion deck: `ml-titanic-deck.html` (33 slides)
> Language: English (translated from the Cantonese script)
> How to use: one section per slide. The first block in each section is the script you read aloud. The "Ops note", "Aside" and "Likely question" blocks are speaker reminders and are not read out.
> Speaker note: keep sentences short, one idea per slide. The first time a technical term appears, give the English term and then explain it in plain words.

---

## How to use this script (read first)

1. This script maps page by page to the deck. Each page holds roughly two to three minutes of material. If you are short on time, read only the bolded sentences in each section.
2. "You" means the whole class. If you are teaching one to one, switch everything to the singular.
3. **No coding is required in this lesson.** Students need a browser, a camera and a microphone. That is all.
4. Part 5 needs forty-five minutes and is the core of the session. If you run short, cut detail from part 4 rather than from part 3 or part 5.
5. The lesson has one throughline: **machine learning finds patterns in data and uses them to answer questions it has never seen before.**

---

# Opening · Course map (2 min · 01–02)

## Slide 01 · Cover: machine learning, step one, from data to model

Hello everyone, and welcome to machine learning, step one.

Let me say one thing up front: **this lesson does not require you to write any code.** You may have heard the term machine learning and assumed it is a deep technical subject needing maths, Python and a pile of papers. Today I want to prove that the core ideas can be explained with everyday examples, and that to actually train a model you need nothing more than a browser.

We will move in three stages. **First, build the concepts:** what is machine learning, and is it a neighbour of ChatGPT or something completely separate? **Second, understand the principles:** what is generalisation, and why does a model that memorises answers collapse the moment it meets new data? **Third, do it:** train three models by hand with Teachable Machine — images, sound and pose — and then map the whole process onto the Titanic dataset.

On the right of the cover you may notice an old photograph: the Titanic, 1912. In the second half we use its passenger dataset as our example. Why use historical data to teach machine learning? Because it is the classic beginner problem: clean data, intuitive columns, and a clear right answer.

**Today's goal is this: by the end of the session you can explain to someone else what machine learning is, and you have a model you trained yourself.**

> **Ops note** Before you start, confirm the classroom network, camera and microphone all work. If you plan to use a screen recording as a fallback, test the playback in advance.

## Slide 02 · Today we take "AI can learn" apart

Slide two, and here is the map. Let me frame it this way: **today we take the idea that AI can learn, and we take it apart.**

When we talk about AI it often feels like a black box — you put something in, something comes out, and what happened in between is a mystery. Today I want to open the box.

Three stages. **First, build the concepts:** what is machine learning, and how does it relate to large language models? You will find that on the surface they look very different — one handles numeric tables, the other handles text — but underneath the logic is the same: finding patterns in data. **Second, understand the principles:** what is generalisation, and why does a model that memorises collapse on new data? This part also answers a question a lot of you are curious about: why does AI make things up? **Third, do it:** train three models with Teachable Machine and map the process onto Titanic.

**I want to stress that last point: no coding is required in this lesson. You only need to bring your curiosity and follow along.**

Before we start, one question. **Which AI features have you used today?**

(Pause, let students answer.)

Someone will say unlocking their phone, or Netflix recommendations, or ChatGPT, or Google search. Good — I will note those answers, because throughout today we will keep connecting them back to the three stages.

**You will find that you have been living inside machine learning all along. You just did not know its name.**

> **Teaching note** This opening question matters, because it turns machine learning from an abstract technical term into the students' own experience. You will reuse the answers on slide 04, so write them on the board.

---

# Part 1 · Traditional machine learning and LLMs (15 min · 03–07)

## Slide 03 · Part 1 divider

Part 1. In this section I want to deal with a very basic question that a lot of people cannot answer clearly.

**Both find patterns in data. So why does one need humans to supply the features, while the other can read the whole encyclopaedia itself?**

The answer is the difference between traditional machine learning and large language models. That difference is also why many people find AI magical — they do not realise these are two different technical routes.

In this part we will look at four everyday scenarios, a three-step process, and one comparison table. Fifteen minutes, nothing deep, but it is the foundation for everything after.

> **Aside** If your students already have some background, you can say up front: "if you have heard the terms feature engineering and deep learning, watch how I line them up together."

## Slide 04 · You have been living inside machine learning all along

Let's look at six everyday scenarios.

**One, spam filtering.** How does your email system know which messages are spam? It has seen millions of messages labelled as spam and learned that certain features — words like "free" or "click now" — are associated with spam.

**Two, video recommendations.** How does Netflix know which film you will watch? It looks at what you watched before and what similar people watched.

**Three, face unlock.** How does your phone recognise you? It learned your facial features. **Pay attention to this one, because it is very close to home.**

**Four, house price estimation.** How does a bank estimate what a flat is worth? It looks at historical sale prices.

**Five, credit scoring.** How does a bank decide whether to lend you money? It uses your repayment record to assess risk.

**Six, weather forecasting.** How does the observatory predict rain tomorrow? It uses decades of past weather data.

**Six scenarios. Do you notice what they have in common?**

(Pause.)

**The common factor is this: all of them use past data to predict something that has not happened yet.**

That sentence is simple, but it is the core of machine learning. Every AI feature you have used can be explained by it.

**I especially want to dwell on face unlock**, because it contains a good teaching point: your phone learned your face, but if you wear a mask or change your hairstyle it may not recognise you. That is the generalisation problem we come to later — **is the pattern it learned general enough?**

> **Teaching note** Write the students' answers from the opening on the board here, then circle the phrase "use the past to predict the future." That gesture makes students feel their answers are part of the lesson, and engagement rises.

## Slide 05 · Traditional machine learning: feature engineering is the key

First technical route: traditional machine learning.

What data does it handle? **Structured data** — data as tidy as a spreadsheet. Each row is an example, each column an attribute. A customer table, for instance: name, age, income, whether they defaulted on a loan.

Its process has three steps. **Step one, a human picks the features.** This is the key part. You decide which columns to use for prediction. If you think age and income are relevant, you include them. If you think star sign is not, you leave it out. **Step two, the model finds the rules.** You give it the data and it works out the relationship between age, income and default. **Step three, it predicts.** A new customer arrives and it estimates, from the learned rules, whether they will default.

**I especially want you to notice step one: a human picks the features.**

That is the crux of traditional machine learning and also its bottleneck. **Success depends heavily on whether you picked the right features.** Miss an important one and no amount of model sophistication can rescue you. This work has a name: feature engineering.

Think about how laborious it is. You face a table with two hundred columns and have to decide which ten matter. That takes domain knowledge, experience, and repeated attempts.

**So the ceiling on traditional machine learning is often not the model's ceiling. It is the ceiling on human ability to choose features.**

> **Aside** This explains why machine learning used to require hiring a domain expert: somebody had to know how to pick the features. And that is exactly what LLMs broke, as the next slide shows.

## Slide 06 · LLMs: features learned automatically, probabilistic by nature

Second route: large language models.

They handle **unstructured data** — text, images, sound. This data has no notion of columns. You cannot say "which column is this character in."

So how do they learn? **They find the features themselves.** You give them text and they learn grammar, meaning and common sense on their own. You do not have to tell them that verbs matter. They work it out.

Their core task is **computing the most likely next word.** I covered this last lesson: it is a probability machine.

**And here is the core difference: traditional ML is humans give features, machine finds rules. An LLM is the machine finds even the features itself.**

Think about how large that change is. You used to hire a specialist and spend months choosing features. Now you hand over raw data and it sorts itself out. That is why LLMs apply across so many domains — you do not need a domain expert to pick features for each one.

**But there is one very important sentence I must say: fundamentally, the two are the same.**

It is not new technology replacing old. It is two methods with one essence. That essence is **learning statistical patterns from data and using them to predict.** Do not assume traditional ML is obsolete because LLMs are impressive, and do not assume LLMs are something else entirely because you know traditional ML.

**They are two members of the same family.**

> **Likely question** "So is an LLM machine learning?" Yes. An LLM is a branch of machine learning, just at a much larger scale and learning in a different way.

## Slide 07 · One table to see the difference between the two worlds

Here is a table summarising the two worlds. Four dimensions.

**First, data type.** Traditional ML: structured, meaning tables. LLM: unstructured, meaning text, images and sound.

**Second, source of features.** Traditional ML: humans choose. LLM: it learns them. **This is the most central difference.**

**Third, tasks they excel at.** Traditional ML: predicting numbers or classifying — will this customer default. LLM: generating and understanding language — write me a letter.

**Fourth, data requirement.** Traditional ML: a few thousand to a few tens of thousands of records to begin. LLM: the text of the entire internet.

**But notice the bottom row: the shared essence.**

**Both find patterns in data and use them to predict situations they have not seen.**

That sentence runs through the whole lesson. Everything today — generalisation, overfitting, Titanic, Teachable Machine — is an extension of it.

**So if you take away one sentence today, let it be this: machine learning is finding patterns in data and using them to predict situations it has not seen.**

> **Teaching note** The "humans pick features versus it learns features itself" contrast returns in part 5 with Teachable Machine. Say now: "remember this distinction — I will ask you about it again later", so students have something to expect.

---

# Part 2 · How does a machine actually learn? (20 min · 08–13)

## Slide 08 · Part 2 divider

Part 2. Here we take learning apart down to its smallest unit.

You will learn three words: **data, features, labels.** These are the basic vocabulary of machine learning. Anyone who talks about machine learning will use them. Learn them and you can follow ninety percent of the discussion.

We then look at two fundamental tasks: **regression and classification.** Between them they cover most practical applications.

Finally, two of the simplest models: **a line (linear regression) and a tree (decision tree).** No mathematics, just the intuition.

Twenty minutes, and I will use everyday examples throughout. You do not need formulas. You need the picture.

> **Aside** If your students are complete beginners, this is the section that most needs to be slow. After each term, pause and ask whether anyone is unsure. If these three words are not clear, parts 3 and 4 will be hard to follow.

## Slide 09 · A dataset has three elements

Three words, using the Titanic data because we will need it in the second half.

**First, a sample.** One row in the table. In the Titanic dataset, one passenger is one sample. There are eight hundred and ninety-one passengers, so eight hundred and ninety-one samples.

**Second, a feature.** The clue you use to judge. Sex, age, passenger class, fare. Those are features. You can think of them as the information you already have.

**Third, a label.** The answer you want to predict. For Titanic, the label is whether this passenger survived or died.

**And with those three words I can give you the definition of learning.**

Learning means **looking at a large number of feature-to-label pairings and finding the pattern in them.** Afterwards you can give it only the features and it predicts the label.

A concrete example. You give the model data on ten thousand passengers and it observes that women in first class survived at a high rate, and men in third class at a low rate. That is the pattern. Then you give it a new passenger — a woman in first class — and it predicts a high chance of survival.

**Notice: it has never seen this new passenger. It is judging from the pattern it learned.**

> **Teaching note** Draw a table live with three rows of passenger data, then circle in different colours the sample (one row), the features (most columns) and the label (the last column). The visual makes the three words click immediately.

## Slide 10 · Two fundamental tasks: regression and classification

With those three words, we can look at two tasks.

The only question that separates them: **is what you want to predict a number or a category?**

**If it is a number, it is regression.** Predicting what a flat sells for, tomorrow's temperature, next month's revenue. The answer is a specific number, possibly a decimal, possibly very large.

**If it is a category, it is classification.** Is this email spam? Will this customer default? Is this a cat or a dog? The answer is a label, one of a limited set of options.

**Today's Titanic task — survived or died — is classification**, because the answer is one of two categories, not a number.

**Why does the distinction matter? Because very often, choosing the wrong task type means your model will not work.**

An example. If your task is "predict how much the customer will pay" and you use a classification model, it will only answer high, medium or low. But you want the number: thirteen thousand dollars. The answer is not usable.

Conversely, if the task is "is this a cat or a dog" and you use a regression model, it answers zero point three seven. How do you read that? Do you set your own threshold at zero point five and call anything above it a dog? Then you have quietly used classification thinking anyway.

**So the first step is always to ask clearly: is the answer I want a number or a category?**

> **Likely question** "What if the answer is whether they will buy, but I want the probability?" Good question. A probability is a number, so technically regression. In practice we usually treat it as classification, because what we care about is crossing a threshold.

## Slide 11 · The simplest learning: finding the closest line

First model: linear regression. The simplest example: using floor area to predict house price.

The core is one formula: **price is approximately a times area, plus b.**

a is the slope, meaning how much more per extra unit of area. b is the intercept, the base price at zero area, which is not physically real but mathematically necessary.

**So what does learning do? It finds the best a and b.**

What counts as best? The line that sits closest to all the data points. You have a hundred sales records, each a pair of area and price. Plot a hundred points, then find the line where the total distance to all points is smallest.

**That is the most primitive picture of machine learning: find the line that sits closest to all the points.**

**And every model shares the same goal: make the gap between the prediction and the truth as small as possible.** That gap has a name: error. Learning is the process of repeatedly adjusting the parameters to shrink the error.

Your model might be a line, a tree, or a neural network, but the goal is identical: **reduce the error.**

> **Teaching note** Draw this live. Plot a few points, draw a line through them, then draw a second line further from the points, and ask which is better. The visual contrast makes error concrete immediately.

## Slide 12 · From a line to a tree: decision trees

Second model: the decision tree.

An analogy: **a decision tree is like a doctor taking a history.**

You see a doctor and they ask a series of yes-or-no questions. Are you female? Are you in a premium cabin? Are you over fifty? Each question sorts your situation into a more specific category. At the end they reach a conclusion: this passenger's survival chance is high, or low.

**So how does it differ from linear regression?**

Linear regression outputs a **continuous line** — you give it an area and it gives you a price, a continuous number.

A decision tree splits the data with **layers of conditions** — are you female, are you in first class — and finally sorts you into a category.

**Why learn decision trees? Because they are intuitive and easy to explain.**

Being easy to explain matters. If a decision tree says this passenger's survival chance is high, you can trace the reasoning: because she is female and in first class. You know why it decided.

But if a neural network says the survival chance is high, you cannot ask why. It has millions of parameters inside, and no single one represents "female."

**So in settings that require explanation — medicine, credit — easy-to-explain models like decision trees remain valuable.** It is also a good first model, because you can watch it learn.

> **Aside** Decision trees have a weakness: they overfit easily. In part 3 you will see overfitting explained, and one of the examples is a decision tree grown too deep. That is a thread we pick up shortly.

## Slide 13 · One line to remember

Last slide of part 2. One sentence.

**"Machine learning is letting a computer find patterns in a large number of examples, and then use those patterns to answer questions it has never seen."**

If I break that down, there are three key parts.

**"In a large number of examples"** — note both "large number" and "examples." Machine learning does not work from rules; it works from examples. You do not write "if female then survival rate is high." You give it ten thousand examples and it discovers that pattern.

**"Find patterns"** — that is the act of learning.

**"Answer questions it has never seen"** — this is the most important part. If it only answers the examples you gave it, it has not learned; it memorised. **Real learning means answering questions it has not seen.**

That point is the theme of part 3: **generalisation.**

**You may have noticed I keep repeating this sentence.** That is deliberate, because it is the melody of the whole lesson. After every model we train, I will come back and ask: did it find the pattern, or did it just memorise the answers?

> **Teaching note** Write this sentence on the board and do not erase it. Every time a model finishes training in part 5, point at it and ask the question again. That repetition is what makes the definition stick.

---

# Part 3 · Generalisation and overfitting (20 min · 14–19)

## Slide 14 · Part 3 divider

Part 3. I consider this the most important section of the lesson, and the conceptual high point.

Let me start with one line: **it is not hard for a model to score well. The hard part is scoring well on a paper it has never seen.**

What does that mean? You give a model a pile of data, it memorises it, and it scores a hundred on the training set. Then you give it new data and it collapses immediately. That is the difference between rote memorisation and genuine understanding.

**You may think this is only a technical matter. But today I will show you it connects directly to something very familiar: why AI makes things up.**

In this part we cover three terms: **generalisation, overfitting, underfitting.** You will meet them in any machine learning book. They are also where the answer lies to the question students ask most: why does AI get things wrong?

> **Teaching note** This is the densest conceptual section. Do not rush it. Use an everyday example for each term. If time is short, sacrifice detail from the Titanic section in part 4 rather than this part.

## Slide 15 · Generalisation: learn the principle, not the answers

Let's use an exam example, which will resonate immediately.

Two students prepare for a test. **Student A memorises:** they learn the answer to every question in the textbook, including the question numbers. In the exam, if the questions are identical, they score full marks. But change one number or reword the question and they freeze.

**Student B understands:** what they remember is not "question one is B" but "this is how you think about this kind of problem." Faced with a question they have never seen, they can reason to an answer.

**So which student is better?**

(Pause.)

Most people say B. But if you look only at the score on the same paper, A and B both score a hundred. **You simply cannot tell which one memorised.**

**So the real difference is not in the training score. It is in performance on new questions.**

And that is the definition of generalisation: **generalisation is a model's ability to perform well on new data it has not seen.**

I want to stress the words "not seen." If the data is data it has seen, performing well is guaranteed — it memorised it. That is not ability. **Real ability is performing well on what it has not seen.**

**That is why in part 4 we split the data** — we hold part of it back from the model and use it to test. Because only then do you know whether it is A or B.

> **Likely question** "So what if it memorised? It still gets the answer right." The problem is that the real world does not set identical questions. The data you meet tomorrow will differ from today's. So memorising does not help.

## Slide 16 · Overfitting: memorising the noise too

The last slide was about memorising. Now the technical name: **overfitting.**

A concrete scenario. Suppose you have data on only a hundred students and you learn with a very complex model. What happens?

**It treats each student's peculiar circumstances as a pattern.** It might learn that students surnamed Chan who sit in the third row and wear glasses do well. That is not a pattern; it is a coincidence. But because your model is too complex, it has enough capacity to memorise that coincidence.

The result: **near-perfect on the training data, and collapse on new data.**

Another analogy that makes it clearer. **You memorise every answer in a reference book, including the position of question three on page seven.** In the exam, if the questions are in a different order, you cannot answer at all — because what you learned was not why this kind of problem works, but what to write at that location.

**Those coincidences have a name: noise. Overfitting means memorising the noise along with the patterns.**

**Why does it happen? Because the model is too complex and has the capacity to memorise every detail.** A sufficiently complex model can memorise a hundred data points perfectly. But memorising perfectly and learning the pattern are two different things.

> **Aside** Here is the counter-intuitive part: **a model that is too capable can learn badly.** Many people find that strange on first hearing. An analogy: a student with an extraordinary memory who uses it to memorise answers rather than to understand will do worse than a student of ordinary memory who thinks.

## Slide 17 · Underfitting, just right, overfitting

Let's put this on a spectrum. As model complexity rises from simple to complex, there are three regions.

**Far left, too simple: underfitting.** The model is so simple it cannot even capture the pattern in the training data. Fitting a straight line to an obviously curved relationship. The result: **poor on training, poor on new data.** It has not learned anything.

**Middle, just right.** The complexity is enough to capture the pattern but not enough to memorise noise. The result: **good on both training and new data.** That is what we want.

**Far right, too complex: overfitting.** The model is complex enough to memorise every data point, noise included. The result: **perfect on training, collapse on new data.**

**Now notice something important: the middle of this spectrum is not "more complex is better" and not "simpler is better."**

Many people assume a stronger model is always better. But too complex is a problem, and too simple is a problem. **The goal is not the highest training score. It is the best generalisation.**

**So "just right" is not a compromise in the middle. It is the optimum.** Once you have that idea, every model you build afterwards prompts the question: have I overfitted yet?

> **Teaching note** Draw the classic curve: horizontal axis model complexity, vertical axis error. Plot two lines — training error falling continuously, test error falling then rising. This is the most famous graph in machine learning. Students remember it after seeing it once.

## Slide 18 · Four ways to avoid overfitting

How do you avoid overfitting? Four measures.

**First, give it more data.** The more data, the harder it is for a coincidence to be mistaken for a pattern. A real pattern recurs across more data; a coincidence gets diluted.

**Second, limit complexity.** Cap the depth of a decision tree, for instance. If it cannot grow deep, it cannot memorise individual noise.

**Third, keep a validation set.** Hold part of the data back so the model does not see it during training, and use it to check real ability.

**Fourth, stop early.** During training, if validation performance starts to worsen, stop. Do not train until training error is minimal, because by then you have probably overfitted.

**In today's hands-on section we will use measures one and three.**

Measure one: in Teachable Machine you will change the **number** of samples — record more and see whether it improves. You will also change their **diversity** — different angles, distances and lighting.

Measure three: you will see the difference between training and testing for yourself.

**You will see underfitting, just right and overfitting with your own eyes.** That is the core activity of part 5.

> **Aside** Of the four, more data is the most effective and the most expensive, because collecting and labelling data costs time and money. In practice we often use measures two, three and four precisely because they require no extra collection.

## Slide 19 · Understanding AI hallucination through overfitting

This closes part 3 and it is the slide I most want you to remember.

People ask me every time: **why does AI state something wrong with total confidence?** Today I can give you a concrete answer.

Recall overfitting. An LLM read the text of the entire internet — note, **the entire internet, including what is correct and what is wrong, what is new and what is outdated, what is sourced and what is nonsense.**

During training it learns all those associations. Most are correct. But some are not — a rare but wrong association gets learned too.

**When it meets a question that triggers that wrong association, it confidently produces an answer that sounds entirely reasonable and is not correct.**

**That is hallucination.**

And here is the key line: **hallucination is not the model trying to deceive you. It is noise mixed into the patterns it learned.**

Notice this is the same problem as overfitting. Overfitting is treating noise as a pattern; hallucination is treating noise as knowledge. **Same disease, different symptom.**

**And that leads to one conclusion: AI answers need verifying.**

Why verify? Because you do not know whether an answer came from a real pattern or from learned noise. Neither does it — it has no mechanism to tell the two apart.

**You may have thought of AI getting things wrong as a defect, a bug. Now you understand it is a necessary consequence.** As long as it learns from data containing noise, it will learn noise. That is not poor engineering. It is a property of the method.

> **Teaching note** This is the conceptual high point. Pause afterwards and let it settle. You can ask: "so how will you use AI from now on?" Most will say "verify." At that moment they have reached the conclusion themselves, and you do not need to add anything.

> **Likely question** "So there is no fix?" There are partial measures: cleaner training data, retrieval-augmented generation so it answers from documents you supply, instructing it to say it does not know when unsure, and verifying yourself. Eliminating it entirely is not possible.

---

# Part 4 · Titanic: the setup (10 min · 20–23)

## Slide 20 · Part 4 divider

Part 4. In the first fifteen minutes we covered concepts — traditional ML versus LLMs. In twenty minutes we covered principles: three words, two tasks, two models. In another twenty, generalisation and overfitting.

Now I hand you a real dataset and say: we are going to run one complete machine learning process on this.

This part is only ten minutes and I will not ask you to do anything. Three things: **one, what this dataset is. Two, why it is the classic beginner problem. Three, what preparation it needs.** Then in part 5 we run the process with Teachable Machine and come back to compare.

**This part is a bridge.** You do not need the details. You need one fact: **real data is never clean.** That is what separates it from textbook examples.

## Slide 21 · Why does every beginner start with Titanic?

Why does every machine learning beginner in the world start with Titanic? Four reasons.

**One, the data is clean.** There are no completely scrambled formats. There are missing values, but missing values are normal; garbled data is not.

**Two, the columns are intuitive.** Sex, age, class, fare — you understand them at a glance, with no domain knowledge. You do not need to be a shipping expert to read it.

**Three, there is a clear right answer.** You know which passengers survived. So you can score yourself and know how well you did.

**Four, and most importantly, it contains features, labels, noise and missing values all at once.**

That last point deserves expanding. **Every problem you meet in real data appears in this dataset.** Missing values, since some ages are blank. Noise, since some fields have inconsistent formats. Candidate features, from which you must choose. So practising on it teaches you not just how to do machine learning but how to handle imperfect data.

**Four key numbers: eight hundred and ninety-one passengers, twelve columns, two labels, a thirty-eight percent survival rate.**

Note the last one: **thirty-eight percent.** That number tells you the two classes are imbalanced. If you built a model that always answered "died", it would be sixty-two percent accurate. That is an important warning: **high accuracy does not mean a good model.** That thread returns in part 5.

A little historical background: in April 1912 the Titanic struck an iceberg and sank on its maiden voyage. That is a real tragedy, and today's dataset was compiled from its passenger list.

> **Teaching note** Real historical photographs help here. When students understand that each row is a real person, engagement rises sharply. It is also a chance to raise data ethics — the data you handle represents people.

## Slide 22 · What does this data look like?

Let's open the dataset.

Opening the CSV you see a table. Each row is a passenger, each column a piece of information.

**The label first: Survived.** It is one or zero. One is survived, zero is died. That is the answer we want to predict.

**Now the candidate features.** **Pclass** is passenger class. **Sex** is sex. **Age** is age. **SibSp** and **Parch** are counts of family travelling together. **Fare** is ticket price. Those six are the main candidates.

**Now the columns to treat carefully.** **Name**, **Ticket** and **Cabin**. Why careful? Because their formats are messy or badly missing. Names come in various formats with titles; ticket numbers are irregular strings; cabin numbers are mostly blank. **Beginners usually skip these three at first.**

**Finally, missing values.** **Age has gaps, and Cabin is missing extensively.** That is the normal state of real data.

**One sentence I want you to notice: these problems are not accidents. They are the norm.**

Many people meet real data for the first time and think it is a mess. But understand this: **real data is always like this.** Clean data lives in textbooks, not in the world. Handling that imperfection is part of your job.

> **Likely question** "So what do we do about missing ages?" Several options: fill with the mean, fill with the median, or drop those rows. There is no single right answer; it depends. Week 5, after part 5, covers this properly.

## Slide 23 · Before you start, split the data in two

This is the most important slide in part 4 and the step most beginners skip.

**Before you start, split the data into two parts.**

**First, the training set, eighty percent, about seven hundred and twelve passengers.** The model learns the patterns from feature-and-label pairings.

**Second, the test set, twenty percent, about a hundred and seventy-nine passengers.** The model has never seen this.

**Why do this? Because if I train on all the data, the model gets a chance to see the answers.**

Recall student A from part 3, who memorised every answer. If I test them on the same paper, of course they score a hundred. But that hundred means nothing, because they memorised it.

So I hold part of the data back, unseen, and test with it.

**And the key sentence: the test set score is the report card for generalisation.** The training score does not count, because the model has seen that data.

Back to the student analogy. The training set is the practice questions in the textbook; the test set is the exam. How well you did the practice questions does not matter. What matters is the exam.

**This principle shows up immediately in part 5.** You will record dozens of photos with the camera as the training set, then perform a new pose as the test. You will feel for yourself that doing well on training and doing well on test are two different things.

> **Teaching note** Ask the class: "why can't we just look at the training score?" Let them answer. Most will say "because it memorised it." At that point they have applied the idea from part 3 themselves.

---

# Part 5 · Hands-on: Teachable Machine and the Titanic comparison (45 min · 24–32)

## Slide 24 · Part 5 divider

Part 5. Forty-five minutes, and the heart of the lesson.

**I need you to open a browser.** No coding. A browser and a camera, that is all.

We will train three models today: **images, sound and pose.** The inputs are completely different, but the process is identical. I want you to feel this: **change the data, and the process does not move.**

Then we come back to Titanic. You will find that the five steps you just did are the same five steps used on Titanic.

**One thing up front: you are likely to get it wrong, and I want you to get it wrong.**

Why? Because we need to see underfitting, just right and overfitting with our own eyes. If you do it perfectly you will never see what overfitting looks like. So on slide 28 I will deliberately teach you how to build a bad model.

> **Ops note** Demonstrate image classification once, completely, then let students work in groups on sound and pose. If you cover all three at once they will not keep up. And if the network is unreliable, have a screen recording ready.

## Slide 25 · Teachable Machine: training a model in three buttons

What is Teachable Machine?

**It is a free online tool from Google. Three steps and you have trained a model.**

**Step one, create classes.** Tell it which things you want to distinguish.

**Step two, collect samples.** Open the camera and record dozens per class.

**Step three, train and test.** Press one button and it trains. Then you can test immediately.

**And here is the principle behind it, which I especially want to explain: transfer learning.**

What is transfer learning? **It borrows the visual foundation Google has already trained on tens of millions of images, and you only teach the top layer.**

That is an important concept. If you trained an image recognition model from scratch you would need millions of images and days of computing. Teachable Machine finishes in seconds. Why? Because it does not start from zero — it already has a foundation that knows how to see, and you only teach it that these shapes are called rock and those are scissors.

**It is like teaching someone who can already draw to learn a new style.** They do not relearn how to hold a pencil. They learn the new style. Much faster.

**Finally, let me connect this back to part 1.**

Remember: traditional ML needs humans to pick features; LLMs extract features from raw data themselves.

**Which one is Teachable Machine?**

(Pause.)

**It is the latter — it extracts features from the raw data, the pixels, itself.** You did not tell it which edges to look at. It looked. That is the answer to the question I said we would come back to.

> **Aside** A useful contrast: to recognise rock-paper-scissors with traditional machine learning, you would hand-write rules — how many straight lines, what edge angles. Teachable Machine needs none of that. You give it photos and it learns.

## Slide 26 · Create the classes, then feed it samples

Let's begin. We will use rock, paper, scissors — the classic game you all know.

**Step one, create classes.** We add three: rock, scissors, paper. **Those three classes correspond to the labels from part 2.**

**Step two, open the camera and collect samples.** Thirty to fifty per class. **These samples correspond to samples.**

**Step three, notice the camera image.** Every pixel the camera captures is a feature. **And those features are read by the model, not chosen by you.**

**Notice that you have just built the three terms from part 2 with your own hands.** Label, sample, feature — all happening in front of you.

**Now a key warning, which I need you to remember: for each class, record from different angles, distances and lighting.**

Why? **Because the quality of the data sets the ceiling on the model.**

Think about it. If you record rock from only one angle, the model does not learn the shape of rock. It learns that particular angle of your hand. Change the angle and it fails. That is the overfitting from part 3.

**So this step is not recording a few photos at random. It is deliberately recording variety.** Diversity is measure one from part 3 in practice — more data, where more means not just quantity but variety.

> **Ops note** Demonstrate the difference between bad and good recording. Record ten photos at the same angle, train, test, and it will fail. Then record with variety and test again. The contrast makes data quality concrete instantly.

## Slide 27 · Press train, then test it

Once you have recorded, press train. A few seconds and it is done.

**Now the most important step: we test it.**

Notice that what it saw during training was the few dozen photos you just recorded. What I want you to do now is **perform a pose it has not seen** — a different angle, further away, the other hand.

**That is the test set idea.** You should not test it with samples it has seen, because it has already done that paper. Use new ones.

**The model outputs a set of confidence scores.** For example rock zero point nine five, scissors zero point zero three, paper zero point zero two. You can read that as how certain it is.

**And the point is not how often it is right. The point is when it is wrong.**

If it fails when you change the angle, then what it learned was the angle, not the gesture. If it fails in dim light, what it learned was the lighting.

**Switch to test mode and do each class once. A low score or a wrong answer is the clue we want.**

Why do I say clue rather than mistake? Because you are not trying to do better. You are trying to find out why it is doing badly. **Knowing the reason tells you what data to add.**

That is the daily work of a machine learning engineer: not train once and finish, but train, test, find the problem, add data, train again.

> **Teaching note** Have students work in groups and test each other's models. Testing your own model, you tend to be gentle. Another group will happily break it. The interaction produces more failure cases.

## Slide 28 · Deliberately break it: seeing overfitting, underfitting and bias

This is the most important slide in part 5. **I am now going to teach you to deliberately build a bad model.**

**First way to break it: underfitting.** Record only two or three photos per class, moving around in front of the background. You will see the model fail to learn the essentials, because the data you gave it was too little and too messy.

**Second, just right.** Record a good number per class at different angles and distances. It performs well on training and test. That is what we want.

**Third way to break it: overfitting.** Record only one angle, wearing the same clothes. Training looks perfect, but move position and it fails. **Because what it memorised was this background, not this hand.**

**Do you see it? Those three conditions are the spectrum from part 3, and you can reproduce it by hand.**

**Now a new concept: bias.**

What is bias? **If you record only one condition for a class — for example you only record scissors in bright light — the model will be unsure about scissors in the dark.**

**That is data bias becoming model bias.**

This matters because it is not only a technical problem. Consider an AI used to screen CVs whose training data contains only successful male candidates. It will learn that male means suitable. That is not a broken model. It is biased data.

**So the concept of bias is the bridge between technique and ethics.** Today you are learning not only how to train a model but how to train one responsibly.

> **Teaching note** Give the bias section a little more time. Use the recruiter AI example to prompt discussion: if the model's training data is biased, whose responsibility is it? The engineer, or the person who collected the data? The discussion lifts the whole session.

## Slide 29 · Switching the data: training on sound

Let's switch the data. This time, sound.

In Teachable Machine, choose an audio project. Three classes: **clapping, talking, silence.**

The process is identical: create classes, collect samples, train and test. **Notice that the input changes from camera to microphone, but the process does not change at all.**

**The features change from pixels to waveforms and frequencies, but the model still extracts them itself.**

**This example contains a very instructive mistake, which I want to highlight.**

**If you record your silence class while the air conditioning is loud, what happens? The model treats the air conditioning as silence.**

Think about why. When you recorded silence, what you actually captured was not an absence of sound. It was the hum of the air conditioner. So the model learned that this kind of hum equals silence.

The result: in a room without air conditioning, you say silence and it cannot answer.

**What this mistake teaches us is that it learned the noise of the recording environment.**

**Notice that this is overfitting.** It is the same problem as memorising the background on the last slide. The model did not learn the abstract concept of silence. It learned the sound environment of this room.

**This example is especially valuable because it demonstrates an easy mistake — and one you would make yourself.** You thought you were giving it silence. You were giving it a room with air conditioning.

> **Aside** This links back to noise from part 3. The air conditioning is noise, and the model memorised it as a pattern. You can ask: "if you were building a voice assistant, what would this mistake cost?" The answer: it would be unusable in some environments.

## Slide 30 · Switching again: training on pose

Third time. Pose.

Choose a pose project. Three classes: **arms up, peace sign, arms crossed.** Record roughly thirty seconds each.

**And here the features advance to the key points of the human skeleton.**

Notice this is an interesting progression. **The image features were pixels. The sound features were waveforms. The pose features are joint positions in a skeleton.**

Three kinds of data, three completely different feature types. But the process is the same: **create classes, collect samples, train, test.**

**One sentence to close the hands-on section: images, sound and pose have completely different inputs, and an identical process.**

That sentence is what I set out to prove today. Many people think machine learning is a scattered subject — handling images is one thing, sound is another, tables yet another. But you have just seen with your own eyes that **the skeleton is the same.**

**And that skeleton is what you take away.** Specific tools change — today Teachable Machine, tomorrow something else — but the process does not.

> **Ops note** These three examples are the spine of this section. Demonstrate image classification completely, then have students work in groups on sound and pose. If the venue is unsuitable — noisy, or no camera — use a pre-recorded screen capture, but keep the part where students run their own tests.

## Slide 31 · One table connecting the two worlds

Back to Titanic. Here is a table mapping the Teachable Machine concepts onto it.

| Concept | Teachable Machine | Titanic |
| --- | --- | --- |
| Features | Pixels, audio waveforms, body key points | Class, sex, age, fare |
| Labels | Rock / scissors / paper | Survived / died |
| Samples | Every photo and clip the camera recorded | Every passenger |
| Train / test | Test with a new, unrecorded pose | Test with the unseen 20% of passengers |
| Overfitting | Memorising the recording environment or background | A decision tree grown too deep, memorising individual noise |

**Read down the rows and you see the pattern: the words on the left and the right are the same. Only the content differs.**

Features are features, whether pixels or passenger class. Labels are labels, whether scissors or died. Samples are samples. Train and test are train and test. Overfitting is overfitting.

**And the key line is: change the data, and the process does not move.**

That is the core of today. **Teachable Machine merely hands the laborious job of choosing features to the model. Every other concept is identical to Titanic.**

What you did in the last dozen minutes is the daily work of a machine learning engineer. You were not playing a small game. You were doing the real thing, at a smaller scale.

> **Teaching note** Project the two side by side on two sheets. Teachable Machine on the left, Titanic on the right, with arrows connecting the matching rows. The visual makes the "oh, they are the same" moment much stronger.

## Slide 32 · The whole process is really five steps

Last slide of part 5.

**Whether you are training on images, sound or tables, the skeleton is these five steps:**

**Step one, load the data.** You put the data in.

**Step two, clean the samples.** Handle missing values, remove garbled rows.

**Step three, convert categories.** Turn categories into a form the model can handle, such as male to zero and female to one.

**Step four, choose features and split the data.** Decide which columns to use and split into training and test sets.

**Step five, train and evaluate.** Train, then evaluate on the test set.

**Now one question: how many of those five steps did you just do in Teachable Machine?**

(Pause.)

**All five.** You did them. Teachable Machine simply hid the technical detail — you did not have to write how to clean samples, you pressed a button. But your process was the same.

**And for Titanic, you only swap photos for a table and do the same five things.**

**So today you have not learned to use a tool. You have learned a process.** That is a big difference. Tools change; processes do not. You will use these five steps with any machine learning tool, whether Python, Excel or a cloud platform.

> **Wrap-up note** This is the convergence point of the lesson. Afterwards you can say: "you have now completed a full machine learning process. Next lesson, Week 5, we return to Titanic and learn how to make it more accurate."

---

# Part 6 · Summary and bridge to Week 5 (5 min · 33)

## Slide 33 · Three things you take away today

Let's close. Three things to take away.

**First, the idea that machine learning finds patterns.**

You look at a large number of feature-to-label pairings, learn the rules in them, and use those to predict new data.

It sounds simple, but if you hold on to it, any time someone talks about AI learning you will know what it is doing. It is not thinking. It is finding patterns.

**Second, the idea that generalisation is the real skill.**

A high training score does not count. **Performing well on data it has not seen is what makes a good model.** And overfitting and hallucination both come from this problem.

This is the most important idea today, because it answers the question you really wanted answered: why does AI get things wrong? Because the patterns it learned have noise mixed into them.

**Third, the idea that you have built your first model.**

From creating classes and collecting samples to training and testing, you have walked through the complete machine learning process by hand.

I want to stress this: **you did not watch someone do it. You did it.** What you did today is the same process a professional machine learning engineer follows. The only differences are scale, since they use millions of images and you used dozens, and tools, since they use Python and you used a browser. But the skeleton is the same.

**So what are we doing next week?**

**In Week 5 we return to Titanic, aiming to make the model more accurate.**

Three things. **First, finer feature engineering.** Not just sex and age, but extracting titles from names — Mr, Mrs, Miss — and family size from ticket numbers. **Second, trying more models.** Random forests and logistic regression, and comparing which performs better. **Third, cross-validation.** Confirming generalisation more rigorously, which is the upgraded version of today's data splitting.

**You will find that everything in Week 5 extends today.** Today you learned how to do it once. In Week 5 you learn how to do it well.

> **Teaching note** Give this slide enough time; do not rush it because you are running late. These three takeaways are what students actually carry out of the room. Write the three points on the board and ask of each: "can anyone say it back in their own words?" If a student can, the lesson has worked.

---

# Appendix A · One line to take away from each part

| Part | One line |
| --- | --- |
| Opening | You have been living inside machine learning all along. |
| 1 | Humans give features versus it learns features itself. |
| 2 | Learning means finding patterns in examples. |
| 3 | Generalisation is the real skill; overfitting and hallucination are the same disease. |
| 4 | Real data is never clean. |
| 5 | Change the data, and the process does not move. |
| 6 | You built your first model — that is the same process professionals use. |

---

# Appendix B · Speaker notes

## 1. Timing

| Section | Slides | Planned | Trim to |
| --- | --- | --- | --- |
| Opening | 01–02 | 2 min | 2 min |
| Part 1 | 03–07 | 15 min | 10 min |
| Part 2 | 08–13 | 20 min | 15 min |
| Part 3 | 14–19 | 20 min | 20 min |
| Part 4 | 20–23 | 10 min | 6 min |
| Part 5 | 24–32 | 45 min | 40 min |
| Part 6 | 33 | 5 min | 5 min |

**Protect parts 3 and 5.** Part 3 holds the concepts; part 5 is where students experience them. If you must cut, cut detail from part 4, which is only setup.

## 2. Fallbacks for the hands-on section

**No camera or a broken camera:** pair students up, or use a pre-recorded screen capture and keep the testing step.

**Too noisy for audio:** skip the audio example and go straight to pose, or use a pre-recorded clip.

**Network too slow:** Teachable Machine loads slowly on weak connections. Load it once before the session and keep the tab open.

**Time short:** do image classification fully, then demonstrate sound and pose rather than having students do all three.

## 3. The five questions students ask most

1. Do I need maths for this? — No, not for the concepts. Maths matters for building models from scratch.
2. Can overfitting be avoided completely? — No. It is managed, not eliminated.
3. Why does AI make things up? — Noise in the training data, learned as if it were knowledge.
4. How far is Teachable Machine from real ML? — Same process, smaller scale, hidden details.
5. Should I learn Python? — Useful, but learn the process first. Tools change.

## 4. Links to other lessons

Part 1 connects to the LLM lesson: traditional ML picks features, LLMs learn them. Part 3 connects to the hallucination discussion there. Week 5 continues directly from part 4 and 5 of today.

---

# Appendix C · Common misconceptions

## Misconception 1: "Machine learning needs a lot of maths."

The concepts do not. You need maths to build a model from scratch, not to understand how one works or to use one well.

## Misconception 2: "AI looks answers up in a database."

There is no database. It learned statistical patterns and predicts from them.

## Misconception 3: "More data is always better."

More noisy or biased data makes things worse. Diversity matters more than raw quantity.

## Misconception 4: "A more complex model is better."

Too complex overfits. The optimum is in the middle of the spectrum, not at the right end.

## Misconception 5: "A good training score means a good model."

The training score is the practice paper. The test score is the exam.

## Misconception 6: "Overfitting is a bug."

It is a consequence of model capacity exceeding what the data supports. It is inherent, not a defect.

## Misconception 7: "Hallucination is sloppy engineering."

It follows necessarily from learning from noisy data. Better engineering reduces it; it cannot eliminate it.

## Misconception 8: "AI replaces people, so there is nothing to learn."

It replaces execution, not judgement. Knowing whether an output is right is the durable skill.

## Misconception 9: "Teachable Machine is just a toy."

It is the real process with the technical details hidden. The five steps are the same ones professionals use.

## Misconception 10: "Decision trees are obsolete."

They are interpretable, which matters in medicine and credit. Interpretability is a real requirement, not a nostalgia.

## Misconception 11: "Classification and regression are much the same."

Choosing the wrong one makes the output unusable. A category where you wanted a number cannot be used.

## Misconception 12: "Missing values mean poor data quality."

Missing values are normal in real data. Real data is never clean.

## Misconception 13: "High accuracy means a good model."

With Titanic, always answering died gives sixty-two percent. Accuracy alone hides everything that matters.

## Misconception 14: "After this lesson I can do machine learning."

You can run the process. Building models that work in production is a longer road.

---

# Appendix D · Classroom activities

## Activity one · Opening question (slide 02, five minutes)

Ask which AI features students used today. Write the answers on the board and return to them on slide 04.

## Activity two · Intuition vote (slide 10, five minutes)

Give five tasks — predict house price, decide spam, predict temperature, classify a photo, predict revenue — and have students vote regression or classification. Discuss the debatable ones.

## Activity three · Drawing lines (slide 11, eight minutes)

Plot points on the board and have students draw the best line by eye. Then draw a deliberately poor line and ask why it is worse. This makes error concrete.

## Activity four · Three students (slide 15, ten minutes)

Assign three students roles: the memoriser, the reasoner, and one who overfits to coincidences. Have the class question them and guess which is which.

## Activity five · Deliberate breakage (slide 28, twenty minutes)

The core activity. Have students build an underfit, a good, and an overfit model in turn, and record what each looks like when tested.

## Activity six · Bias discussion (after slide 28, ten minutes)

Use the CV screening example. Whose responsibility is biased training data — the engineer, the data collector, or the organisation?

---

# Appendix E · Glossary

| Term | Plain reading |
| --- | --- |
| Structured data | Data in tables, with rows and columns |
| Unstructured data | Text, images, audio; no columns |
| Feature | The information you use to judge; what is already known |
| Label | The answer you want to predict |
| Sample | One row; one example |
| Training set | Data the model learns from |
| Test set | Held-back data used to check generalisation |
| Regression | Predicting a number |
| Classification | Predicting a category |
| Linear regression | Fitting the closest straight line |
| Decision tree | Splitting data with layers of yes/no conditions |
| Feature engineering | Choosing and constructing the useful features |
| Generalisation | Performing well on unseen data |
| Overfitting | Memorising noise as if it were a pattern |
| Underfitting | Too simple to capture even the training pattern |
| Validation set | Held-back data used during training |
| Noise | Coincidence in the data that is not a real pattern |
| Bias | Systematic skew in the data, learned by the model |
| Transfer learning | Reusing a pretrained foundation and teaching only the top layer |
| Hallucination | Confident output that is not true, from learned noise |

**Speaker tip:** feature, label and sample are the three words that must be solid before part 3. Check those explicitly before moving on.

---

# Appendix F · Rehearsal: likely questions and answers

## Scene one · "I am no good at maths. Can I learn this?"

**You could answer:**

"For understanding how machine learning works, you do not need maths at all. Everything today was pictures and examples.

Maths matters when you build a model from scratch — deriving the update rules, proving convergence. That is a different job from understanding what a model does and judging whether it is any good.

**And in practice, most people who use machine learning are in the second group.** They need to know what overfitting is and how to spot it. That is judgement, not algebra."

**Why answer this way:** the fear is a gatekeeping fear. Separate understanding from derivation clearly.

## Scene two · "Can overfitting be avoided completely?"

**You could answer:**

"No, and that is important to accept.

Overfitting happens when a model has more capacity than the data can support. You can reduce it — more data, less complexity, validation, early stopping — but there will always be a trade-off, and some noise will always be learned.

**The practical goal is not elimination. It is knowing when you have overfitted and being able to tell.** That is why we split the data."

**Why answer this way:** a student hoping to eliminate it will be disappointed. Framing it as management is both true and useful.

## Scene three · "Why does AI make things up?"

**You could answer:**

"Because of exactly what we covered today.

The model read the entire internet, including what is wrong, outdated, and nonsense. It learned those associations along with the correct ones. When a question triggers a wrong association, it produces a confident, plausible, incorrect answer.

**It is not lying. It is repeating noise it learned as though it were knowledge.** And that is why you verify."

**Why answer this way:** this is the payoff of part 3. Answering with the concept just taught reinforces it.

## Scene four · "How far is Teachable Machine from real machine learning?"

**You could answer:**

"Closer than you think, and further than you think.

**Closer:** the five steps are identical. Load, clean, convert, split, train and evaluate. You did all five.

**Further:** it hides feature engineering, and it applies transfer learning, so you never train from scratch. Real work involves choosing features, handling imbalance, and tuning.

**The skeleton is the same. The detail is where the profession lives.**"

**Why answer this way:** it respects the activity without overclaiming.

## Scene five · "Should I learn Python?"

**You could answer:**

"Eventually, yes — but not first.

If you learn Python before you understand generalisation and overfitting, you will write code that runs and produce models that are quietly wrong, without knowing why.

**Learn the process first, then the tool.** You already have the process from today. Python is how you scale it."

**Why answer this way:** students often want to skip to the tool. Giving an order is more useful than a yes.

## Scene six · "If my data is biased, whose fault is it?"

**You could answer:**

"That is the most important question in this appendix, and there is no single answer.

The engineer who used biased data without checking shares it. So does whoever assembled the dataset. So does the organisation that deployed a system without asking what it was trained on.

**What is clearly true is that the model cannot be blamed.** A model learns what it is shown. If the data is skewed, the model faithfully reproduces the skew.

So the responsibility sits with the people who chose the data — which includes whoever deploys the system."

**Why answer this way:** it refuses a tidy answer, which is honest, and names where responsibility actually lands.

---

# Appendix G · Speaker self-check

## The day before

- Test the camera, microphone and projector in the actual room.
- Load Teachable Machine and confirm it opens.
- Prepare three sample datasets in case the room is unsuitable.
- Prepare a screen recording of each of the three model types.
- Print or display the Titanic column list.

## An hour before

- Network checked.
- Teachable Machine tab loaded.
- Whiteboard cleared for the five-step process and the three-terms diagram.

## Content check

- Can you define feature, label and sample without notes?
- Can you explain the difference between regression and classification?
- Can you draw the underfitting-to-overfitting curve from memory?
- Can you link hallucination to overfitting in one sentence?

## Mindset

- Part 5 may fail technically. Have the recording and move on calmly.
- Some students will find the hands-on section childish. Frame it as the professional process at small scale, and they usually come round.
- Protect parts 3 and 5.

## Appendix G, continued · The three sentences that matter most

If you remember only three lines from today:

1. **Machine learning is finding patterns in data and using them to predict what it has not seen.**
2. **Generalisation is the real skill; a high training score means nothing.**
3. **Hallucination is noise learned as knowledge.**

---

# Appendix H · Per-slide timing

| Slide | Topic | Minutes |
| --- | --- | --- |
| 01 | Cover | 1 |
| 02 | Opening question | 3 |
| 03 | Part 1 divider | 1 |
| 04 | Six scenarios | 5 |
| 05 | Traditional ML | 4 |
| 06 | LLMs | 3 |
| 07 | Comparison table | 3 |
| 08 | Part 2 divider | 1 |
| 09 | Three elements | 5 |
| 10 | Regression and classification | 5 |
| 11 | Linear regression | 5 |
| 12 | Decision trees | 5 |
| 13 | One line | 3 |
| 14 | Part 3 divider | 1 |
| 15 | Generalisation | 5 |
| 16 | Overfitting | 5 |
| 17 | The spectrum | 5 |
| 18 | Four measures | 4 |
| 19 | Hallucination | 6 |
| 20 | Part 4 divider | 1 |
| 21 | Why Titanic | 4 |
| 22 | The data | 3 |
| 23 | Splitting the data | 4 |
| 24 | Part 5 divider | 2 |
| 25 | Teachable Machine | 5 |
| 26 | Classes and samples | 6 |
| 27 | Train and test | 6 |
| 28 | Deliberate breakage | 12 |
| 29 | Sound | 5 |
| 30 | Pose | 4 |
| 31 | Comparison table | 4 |
| 32 | Five steps | 4 |
| 33 | Three takeaways | 5 |

---

# Appendix I · Homework and assessment

## 1. Homework

**Task one · Train a model (required).** Train one Teachable Machine model on something from your own life. Record how many samples you used and what you did to make them diverse.

**Task two · Break it deliberately (required).** Deliberately build an overfitted version, describe how you did it, and explain what the test results showed.

**Task three · Titanic reasoning (required).** Without writing code, list which columns you would use as features for Titanic and which you would skip, with reasons.

**Task four · Bias analysis (optional).** Find an AI system in the news that was accused of bias. Describe what the training data probably looked like.

## 2. Assessment criteria

| Criterion | What good looks like |
| --- | --- |
| Conceptual grasp | Defines feature, label and sample correctly |
| Task type | Distinguishes regression from classification reliably |
| Generalisation | Explains why the test score is what counts |
| Diagnosis | Can identify overfitting from test behaviour |
| Ethics awareness | Recognises that data bias becomes model bias |

## 3. Self-check questions

1. What are the three elements of a dataset?
2. Define machine learning in one sentence.
3. What distinguishes regression from classification?
4. What is feature engineering, and why was it a bottleneck?
5. How do LLMs differ from traditional ML in handling features?
6. What is generalisation?
7. What is overfitting, and why does it happen?
8. Describe the three regions of the complexity spectrum.
9. Name four ways to reduce overfitting.
10. How does overfitting explain hallucination?
11. Why split data into training and test sets?
12. What are the five steps of the process?
13. What does transfer learning do?

**Questions 2, 7 and 10 matter most.**

## 4. Going further

**Tool.** Train one more model in Teachable Machine on a dataset you care about.

**Dataset.** Look at the Titanic CSV and note which columns have missing values.

**Reading.** Any introduction to the bias-variance trade-off, once you are comfortable with the spectrum.

---

# Appendix J · Classroom situations

## Situation one · No camera or a broken camera

**What to do:** pair students up so they can share a device, or use the pre-recorded demonstration. Crucially, keep the testing step, because that is where the learning happens.

## Situation two · The venue is too noisy for the audio example

**What to do:** skip audio and go to pose, or use a pre-recorded clip. Mention that the noise level in the room is itself an example of why the audio model is fragile.

## Situation three · A student's model is always right

**What to do:** they are testing with samples too similar to the training data. Ask them to test from a different angle, a different distance, or in different light. That is the lesson.

## Situation four · A student finds the activity childish

**What to do:** point out that the five steps are identical to what professionals do, and that the only differences are scale and tooling. Most come round. If not, invite them to deliberately break the model on slide 28, which is genuinely challenging.

## Situation five · Not enough time, only one example fits

**What to do:** do image classification in full, including the deliberate breakage. That single example contains the entire lesson's concepts.

## Situation six · "Why can't the computer choose the features for me?"

**What to do:** excellent question — and the answer is that it can, which is exactly what deep learning does. That is the bridge to the LLM lesson and to Week 5. Say so explicitly; it rewards the question.

---

*This script accompanies `ml-titanic-deck.html` — 33 slides, six parts, roughly 120 minutes.*
