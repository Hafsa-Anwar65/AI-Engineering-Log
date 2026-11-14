# 🧠 AI Engineering Log

My structured journey from Python fundamentals to Machine Learning, AI engineering, automation, and production-ready AI systems.

---

## 🔥 Progress Streak

<!-- STREAK:START -->
<div align="center">

![🔥 Current streak](https://img.shields.io/badge/%F0%9F%94%A5%20Current%20streak-14%20days-FF6B35?style=for-the-badge) ![🏆 Best streak](https://img.shields.io/badge/%F0%9F%8F%86%20Best%20streak-14%20days-F7B32B?style=for-the-badge) ![📅 Days done](https://img.shields.io/badge/%F0%9F%93%85%20Days%20done-14%20%2F%20162-3B82F6?style=for-the-badge)

**14 / 162 days** · 8% complete

`███░░░░░░░░░░░░░░░░░░░░░░░░░░░`

| Week of | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Oct 26 |   |   |   |   |   |   | 🟩 |
| Nov 2 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 |
| Nov 9 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | 🟩 | ⬜ |

<sub>🟩 day's topic completed · ⬜ upcoming · 🟥 behind schedule · updates automatically</sub>

</div>
<!-- STREAK:END -->

---

## 👋 About this log

I'm **Hafsa Anwar**, an AI & Automation Engineer and Robotics & Intelligent Systems student in Karachi. This repo is my public learning log: every day I learn one topic, write it in my own words and push code. Every skill on my CV gets rebuilt **from first principles**: Python, ML, computer vision, ROS 2, FastAPI, LangChain, LangGraph, RAG, n8n, Playwright, Docker, cloud and MLOps.

## 🔥 Latest

**Days completed:** 14 / 162

| Day | Date | Topic | What I built | Code |
|---|---|---|---|---|
| Day 014 | Nov 14 | 🛠️ Week 2 project | Linear regression from scratch in NumPy: R² 0.95, matches np.polyfit, 7 tests | [`linear_regression.py`](./Week-02-NumPy%20Pandas%20Math/Day%2014%20-%20Linear%20Regression%20Project/linear_regression.py) |
| Day 013 | Nov 13 | Loss functions (MSE) & gradient descent | MSE vs MAE, gradient descent, learning-rate experiments | [`Day 13 - Loss Functions and Gradient Descent.py`](./Week-02-NumPy%20Pandas%20Math/Day%2013%20-%20Loss%20Functions%20and%20Gradient%20Descent.py) |
| Day 012 | Nov 12 | Derivatives, chain rule, gradients + probability | Numerical derivatives, gradients, conditional probability | [`Day 12 - Derivatives Gradients and Probability.py`](./Week-02-NumPy%20Pandas%20Math/Day%2012%20-%20Derivatives%20Gradients%20and%20Probability.py) |
| Day 011 | Nov 11 | Linear algebra: vectors, dot product, matrix multiplication | Vectors, magnitude, matmul, transpose practice | [`Day 11 - Linear Algebra.py`](./Week-02-NumPy%20Pandas%20Math/Day%2011%20-%20Linear%20Algebra.py) |
| Day 010 | Nov 10 | pandas: CSVs, filtering, groupby, merges, missing values | Student data cleaning, groupby averages, merge | [`Day 10 - Pandas.py`](./Week-02-NumPy%20Pandas%20Math/Day%2010%20-%20Pandas.py) |
| Day 009 | Nov 9 | Broadcasting & vectorisation vs loops | Speed test: NumPy ~24x faster than a loop on 1M numbers | [`Day 09 - Broadcasting and Vectorization.py`](./Week-02-NumPy%20Pandas%20Math/Day%2009%20-%20Broadcasting%20and%20Vectorization.py) |
| Day 008 | Nov 8 | NumPy arrays: dtype, shape, reshape, indexing | Array and matrix practice | [`Day 08 - NumPy Arrays.py`](./Week-02-NumPy%20Pandas%20Math/Day%2008%20-%20NumPy%20Arrays.py) |

📒 Full day-by-day history: [LOG.md](./LOG.md)

## 🦾 Flagship: EscortBot Brain

The AI brain for **EscortBot**, a ROS 2 banking-assistant robot. Each phase adds one layer:

| Layer | What it does |
|---|---|
| 👁️ Perception | My fine-tuned YOLO detector finds people & queues, running as a ROS 2 node |
| 🧭 Navigation | Guides visitors to the counter, ATM or exit through Nav2 |
| 📚 Knowledge | RAG over public banking FAQs in English & Roman Urdu, with a 50-question eval |
| 🕸️ Reasoning | A LangGraph agent that decides: answer, guide, or call staff (human-in-the-loop) |
| 🎙️ Voice | Speech-to-text and text-to-speech as ROS 2 nodes |
| ☁️ Production | FastAPI + Docker + cloud + CI/CD + latency, safety & cost monitoring |

> The implementation lives in a separate repo for now (going public in Week 20). Weekly progress, clips and numbers are posted [below](#-escortbot-brain-updates).

## 🗺️ Roadmap at a glance

| Phase | Weeks | Focus | Gate ✅ |
|---|---|---|---|
| 📦 1 | 1–6 · Nov 1–Dec 13 | Python, ML, computer vision & ROS 2 | My detector runs as a ROS 2 node in Gazebo; robot reaches waypoints from Python |
| 🧠 2 | 7–13 · Dec 14–Jan 31 | APIs + LLM engineering: LangChain, RAG, LangGraph | RAG eval of 50 with accuracy measured + agent success rate on 30 scenarios |
| ☁️ 3 | 14–19 · Feb 1–Mar 14 | Automation, Linux/Docker, cloud, MLOps | Brain live on cloud with CI/CD + full robot demo in Gazebo; exam sat |
| 🎯 4 | 20–23 · Mar 15–Apr 11 | Polish, interviews, applications | 40+ applications and 4+ mock interviews |

---

# 📊 Progress

| # | Week | Theme | Status |
|:-:|---|---|:-:|
| 1 | Nov 1-Nov 7 | 🐍 [Python from the basics](./Week-01-Python%20Basics/) | ✅ Done |
| 2 | Nov 8-Nov 14 | 📐 [NumPy, pandas & the math you actually use](./Week-02-NumPy%20Pandas%20Math/) | ✅ Done |
| 3 | Nov 15-Nov 21 | 📊 [Classic machine learning with scikit-learn](./Week-03-Scikit-Learn%20ML/) | 🟡 Next |
| 4 | Nov 22-Nov 28 | 🔥 [Neural networks & PyTorch basics](./Week-04-PyTorch%20Basics/) | ⬜ |
| 5 | Nov 29-Dec 6 | 👁️ [Computer vision & object detection](./Week-05-Computer%20Vision/) | ⬜ |
| 6 | Dec 7-Dec 13 | 🤖 [ROS 2 for the AI brain](./Week-06-ROS2%20Basics/) | ⬜ |
| 7 | Dec 14-Dec 20 | ⚡ [FastAPI & Flask from the basics](./Week-07-FastAPI%20Flask/) | ⬜ |
| 8 | Dec 21-Dec 27 | 🧬 [Transformers, embeddings & vector search (plain Python first)](./Week-08-Embeddings%20Vector%20Search/) | ⬜ |
| 9 | Dec 28-Jan 3 | 🔗 [LangChain from the basics](./Week-09-LangChain%20Basics/) | ⬜ |
| 10 | Jan 4-Jan 10 | 📚 [RAG done properly](./Week-10-RAG/) | ⬜ |
| 11 | Jan 11-Jan 17 | 🕸️ [LangGraph from the basics](./Week-11-LangGraph%20Basics/) | ⬜ |
| 12 | Jan 18-Jan 24 | 🎙️ [Evals, voice & agent reliability](./Week-12-Evals%20and%20Voice/) | ⬜ |
| 13 | Jan 25-Jan 31 | 🎛️ [Fine-tuning small open models (on-robot model)](./Week-13-Fine-Tuning/) | ⬜ |
| 14 | Feb 1-Feb 7 | ⚙️ [n8n, Make & Playwright from the basics (+ SiteScout v1)](./Week-14-n8n%20Make%20Playwright/) | ⬜ |
| 15 | Feb 8-Feb 14 | 🐧 [Linux, Docker & Kubernetes from the basics](./Week-15-Linux%20Docker%20Kubernetes/) | ⬜ |
| 16 | Feb 15-Feb 21 | ☁️ [Cloud fundamentals](./Week-16-Cloud%20Fundamentals/) | ⬜ |
| 17 | Feb 22-Feb 28 | 🔁 [CI/CD & testing (ROS + AI)](./Week-17-CI-CD%20Testing/) | ⬜ |
| 18 | Mar 1-Mar 7 | 📈 [Observability, latency, safety & security](./Week-18-Observability/) | ⬜ |
| 19 | Mar 8-Mar 14 | 🏅 [Cloud AI certification](./Week-19-Cloud%20Certification/) | ⬜ |
| 20 | Mar 15-Mar 21 | 💼 [CV, portfolio & demo video](./Week-20-Portfolio/) | ⬜ |
| 21 | Mar 22-Mar 28 | 🏗️ [ML & LLM system design](./Week-21-System%20Design/) | ⬜ |
| 22 | Mar 29-Apr 4 | 🗣️ [Behavioral interviews & mocks](./Week-22-Behavioral%20Interviews/) | ⬜ |
| 23 | Apr 5-Apr 11 | 🚀 [Applications at volume](./Week-23-Applications/) | ⬜ |

<sub>⬜ not started · 🟡 in progress · ✅ done · 🏁 gate passed</sub>

---

## 📐 Week 2 · NumPy, pandas & the math you actually use

**📅 Nov 8–Nov 14, 2026**

This week focuses on the Python libraries and mathematical concepts that form the foundation of Machine Learning.

### Progress

**🎯 Done when:** I can write a small CLI program with classes, error handling, type hints and tests without looking things up  
**📖 Resources:** Python official tutorial (docs.python.org/3/tutorial), Corey Schafer Python playlist (YouTube), 'Automate the Boring Stuff' (free online)  
**🧩 Coding practice:** LeetCode easy: arrays, strings, hash maps  
**📁 Folder:** [`Week-01-Python Basics/`](./Week-01-Python%20Basics/)

- [x] **Day 1** · Sun Nov 1 · 🚀 Kickoff: set up my lab + Python basics (variables, types, input/output, strings)
- [x] **Day 2** · Mon Nov 2 · Control flow & data structures: if/loops, lists, tuples, dicts, sets, comprehensions
- [x] **Day 3** · Tue Nov 3 · Functions: args/kwargs, scope, lambdas; modules & imports; venv, pip/uv, requirements
- [x] **Day 4** · Wed Nov 4 · Files & errors: read/write files, JSON & CSV, try/except, custom exceptions, logging
- [x] **Day 5** · Thu Nov 5 · OOP: classes, __init__, methods, inheritance, composition, dataclasses, dunder methods
- [x] **Day 6** · Fri Nov 6 · Modern Python: type hints, iterators & generators, decorators, context managers, async/await basics
- [x] **Day 7** · Sat Nov 7 · 🛠️ **Build:** CLI bank-branch token & queue manager in pure Python

</details>

<details>
<summary><b>📐 Week 2 · Nov 8-Nov 14 · NumPy, pandas & the math you actually use</b></summary>

**🎯 Done when:** I can explain gradient descent on a whiteboard without notes  
**📖 Resources:** 3Blue1Brown (Essence of Linear Algebra, Calculus), Andrew Ng ML Specialization C1 (audit free)  
**🧩 Coding practice:** LeetCode easy: arrays, strings, hash maps  
**📁 Folder:** [`Week-02-NumPy Pandas Math/`](./Week-02-NumPy%20Pandas%20Math/)

- [x] **Day 8** · Sun Nov 8 · 🔁 Review Week 1 + NumPy arrays, dtype, shape, reshape, indexing
- [x] **Day 9** · Mon Nov 9 · NumPy broadcasting & vectorisation vs loops
- [x] **Day 10** · Tue Nov 10 · pandas: CSVs, filtering, groupby, merges, missing values
- [x] **Day 11** · Wed Nov 11 · Linear algebra: vectors, dot product, matrix multiplication
- [x] **Day 12** · Thu Nov 12 · Derivatives, chain rule, gradients + probability basics
- [x] **Day 13** · Fri Nov 13 · Loss functions (MSE) & gradient descent
- [x] **Day 14** · Sat Nov 14 · 🛠️ **Build:** linear regression from scratch in NumPy: predict queue wait time from queue length

</details>

<details>
<summary><b>📊 Week 3 · Nov 15-Nov 21 · Classic machine learning with scikit-learn</b></summary>

**🎯 Done when:** I can say why accuracy is misleading on imbalanced data  
**📖 Resources:** Andrew Ng ML Specialization C2, scikit-learn user guide, Kaggle Learn (Intro/Intermediate ML)  
**🧩 Coding practice:** LeetCode easy: arrays, strings, hash maps  
**📁 Folder:** [`Week-03-Scikit-Learn ML/`](./Week-03-Scikit-Learn%20ML/)

- [ ] **Day 15** · Sun Nov 15 · 🔁 Review Week 2 + start the EscortBot data collection
- [ ] **Day 16** · Mon Nov 16 · Supervised vs unsupervised; train/val/test splits & data leakage
- [ ] **Day 17** · Tue Nov 17 · Logistic regression & decision trees; text features with TF-IDF
- [ ] **Day 18** · Wed Nov 18 · Random forests & gradient boosting (XGBoost idea)
- [ ] **Day 19** · Thu Nov 19 · Overfitting, bias-variance, L1/L2; cross-validation & GridSearch
- [ ] **Day 20** · Fri Nov 20 · Metrics (precision, recall, F1, ROC-AUC, confusion matrix) + class imbalance
- [ ] **Day 21** · Sat Nov 21 · 🛠️ **Build:** visitor-intent classifier (FAQ / guide-me / complaint / staff), 3 models compared

</details>

<details>
<summary><b>🔥 Week 4 · Nov 22-Nov 28 · Neural networks & PyTorch basics</b></summary>

**🎯 Done when:** I can write a PyTorch training loop from memory  
**📖 Resources:** Karpathy 'Neural Networks: Zero to Hero' (micrograd), official PyTorch tutorials  
**🧩 Coding practice:** LeetCode easy: arrays, strings, hash maps  
**📁 Folder:** [`Week-04-PyTorch Basics/`](./Week-04-PyTorch%20Basics/)

- [ ] **Day 22** · Sun Nov 22 · 🔁 Review Week 3 + Karpathy micrograd part 1 + label my camera frames
- [ ] **Day 23** · Mon Nov 23 · Perceptron, neurons, layers, activations (ReLU, sigmoid, softmax)
- [ ] **Day 24** · Tue Nov 24 · Forward pass & backpropagation (finish micrograd, push my version)
- [ ] **Day 25** · Wed Nov 25 · PyTorch tensors, CPU/GPU, autograd, Dataset & DataLoader
- [ ] **Day 26** · Thu Nov 26 · The training loop + optimizers (SGD, momentum, Adam, LR schedules)
- [ ] **Day 27** · Fri Nov 27 · Batch size, epochs, early stopping, dropout, batchnorm, save/load, seeds
- [ ] **Day 28** · Sat Nov 28 · 🛠️ **Build:** MLP in PyTorch on Colab GPU

</details>

<details>
<summary><b>👁️ Week 5 · Nov 29-Dec 6 · Computer vision & object detection</b></summary>

**🎯 Done when:** My own detector is fine-tuned and evaluated (mAP, per-class errors)  
**📖 Resources:** fast.ai Practical Deep Learning lessons 1-2, torchvision transfer-learning tutorial, Ultralytics YOLO docs  
**🧩 Coding practice:** LeetCode easy: arrays, strings, hash maps  
**📁 Folder:** [`Week-05-Computer Vision/`](./Week-05-Computer%20Vision/)

- [ ] **Day 29** · Sun Nov 29 · 🔁 Review Week 4 + finish labels, make train/val split
- [ ] **Day 30** · Mon Nov 30 · Convolutions, filters, pooling, feature maps, why CNNs work
- [ ] **Day 31** · Tue Dec 1 · Pretrained ResNet/EfficientNet; fine-tuning vs feature extraction; freezing layers
- [ ] **Day 32** · Wed Dec 2 · Object detection: boxes, IoU, NMS, mAP; YOLO family; fine-tuning YOLO on custom data
- [ ] **Day 33** · Thu Dec 3 · Data augmentation, small datasets, sim-to-real gap (Gazebo frames vs real camera)
- [ ] **Day 34** · Fri Dec 4 · Error analysis + speed: FPS on CPU, model size, exporting to ONNX
- [ ] **Day 35** · Sat Dec 5 · 🛠️ **Build:** fine-tune a small YOLO on my frames to detect people (and queues)
- [ ] **Day 36** · Sun Dec 6 · 🔁 Review Week 5 + LinkedIn post #1: what I trained and its accuracy

</details>

<details>
<summary><b>🤖 Week 6 · Dec 7-Dec 13 · ROS 2 for the AI brain</b></summary>

**🎯 Done when:** GATE 1: my detector runs as a ROS 2 node in Gazebo and the robot reaches waypoints from Python  
**📖 Resources:** ROS 2 official tutorials (Humble or Jazzy, whatever my lab uses), Nav2 docs, Articulated Robotics (YouTube)  
**🧩 Coding practice:** LeetCode easy: arrays, strings, hash maps  
**📁 Folder:** [`Week-06-ROS2 Basics/`](./Week-06-ROS2%20Basics/)

- [ ] **Day 37** · Mon Dec 7 · ROS 2 from the basics: nodes, topics, publishers/subscribers in rclpy; workspaces, packages, colcon
- [ ] **Day 38** · Tue Dec 8 · Services, actions, parameters, launch files; ros2 CLI, rqt, rosbag
- [ ] **Day 39** · Wed Dec 9 · Gazebo simulation: URDF robot model, a bank-branch world, camera & lidar sensors
- [ ] **Day 40** · Thu Dec 10 · Nav2: mapping (slam_toolbox), localisation, sending goals from Python (nav2_simple_commander)
- [ ] **Day 41** · Fri Dec 11 · cv_bridge: run my YOLO model as a ROS 2 node that publishes /people detections
- [ ] **Day 42** · Sat Dec 12 · 🛠️ **Build:** Gazebo bank world, detector node publishes /people; a script drives to counter, ATM and exit
- [ ] **Day 43** · Sun Dec 13 · 🏁 **GATE 1 check + plan Phase 2**

</details>

### 🧠 Phase 2: APIs + LLM engineering: LangChain, RAG, LangGraph
<sub>Dec 14-Jan 31 (Weeks 7-13) · Gate: RAG eval of 50 with accuracy measured + agent success rate on 30 scenarios</sub>

<details>
<summary><b>⚡ Week 7 · Dec 14-Dec 20 · FastAPI & Flask from the basics</b></summary>

**🎯 Done when:** I can build a CRUD API with validation, a database and tests from scratch  
**📖 Resources:** FastAPI official tutorial, Flask Quickstart + Miguel Grinberg's Flask Mega-Tutorial (first chapters), MDN 'HTTP overview'  
**🧩 Coding practice:** LeetCode easy->medium: two pointers, sliding window, trees  
**📁 Folder:** [`Week-07-FastAPI Flask/`](./Week-07-FastAPI%20Flask/)

- [ ] **Day 44** · Mon Dec 14 · How the web works: HTTP methods, status codes, headers, JSON, REST design; curl & Postman
- [ ] **Day 45** · Tue Dec 15 · Flask basics: routes, request/response, templates, blueprints, a tiny API
- [ ] **Day 46** · Wed Dec 16 · FastAPI basics: path/query params, Pydantic models, auto docs, dependency injection
- [ ] **Day 47** · Thu Dec 17 · Databases: SQL basics, SQLite/Postgres, SQLAlchemy/SQLModel, CRUD endpoints
- [ ] **Day 48** · Fri Dec 18 · Auth (API keys, JWT basics), background tasks, async endpoints, WebSockets, tests with TestClient
- [ ] **Day 49** · Sat Dec 19 · 🛠️ **Build:** EscortBot Brain API v0 in FastAPI + an rclpy bridge node
- [ ] **Day 50** · Sun Dec 20 · 🔁 Review Week 7 + write-up: Flask vs FastAPI, when to use each

</details>

<details>
<summary><b>🧬 Week 8 · Dec 21-Dec 27 · Transformers, embeddings & vector search (plain Python first)</b></summary>

**🎯 Done when:** I can explain attention and embeddings in plain words  
**📖 Resources:** Hugging Face LLM Course, Karpathy 'Let's build GPT', FAISS & Chroma docs  
**🧩 Coding practice:** LeetCode easy->medium: two pointers, sliding window, trees  
**📁 Folder:** [`Week-08-Embeddings Vector Search/`](./Week-08-Embeddings%20Vector%20Search/)

- [ ] **Day 51** · Mon Dec 21 · Tokens & BPE, context windows & cost; temperature, top-p, why models hallucinate
- [ ] **Day 52** · Tue Dec 22 · Attention & the transformer (Q, K, V) at concept level
- [ ] **Day 53** · Wed Dec 23 · Embeddings & cosine similarity, compute them yourself with the SDK + NumPy
- [ ] **Day 54** · Thu Dec 24 · Vector databases: FAISS, Chroma, pgvector; HNSW at concept level
- [ ] **Day 55** · Fri Dec 25 · Chunking strategies (fixed, overlap, by heading) + hybrid search (BM25 + semantic)
- [ ] **Day 56** · Sat Dec 26 · 🛠️ **Build:** semantic search over public bank FAQs & SBP consumer guides in plain Python
- [ ] **Day 57** · Sun Dec 27 · 🔁 Review Week 8 + collect more bank documents, start the 50-question test set (English + Roman Urdu)

</details>

<details>
<summary><b>🔗 Week 9 · Dec 28-Jan 3 · LangChain from the basics</b></summary>

**🎯 Done when:** I can rebuild any of my LLM scripts as LangChain chains and explain every piece  
**📖 Resources:** LangChain official docs (Tutorials + How-to guides), DeepLearning.AI 'LangChain for LLM Application Development'  
**🧩 Coding practice:** LeetCode easy->medium: two pointers, sliding window, trees  
**📁 Folder:** [`Week-09-LangChain Basics/`](./Week-09-LangChain%20Basics/)

- [ ] **Day 58** · Mon Dec 28 · Why LangChain; chat models & messages, prompt templates, switching providers (OpenAI, Anthropic, Groq, Ollama)
- [ ] **Day 59** · Tue Dec 29 · LCEL: Runnables, the | pipe, RunnableParallel, RunnablePassthrough, streaming & batch
- [ ] **Day 60** · Wed Dec 30 · Output parsers & with_structured_output (Pydantic); chat history
- [ ] **Day 61** · Thu Dec 31 · Document loaders (PDF, web, CSV), text splitters, embeddings, vector stores, retrievers
- [ ] **Day 62** · Fri Jan 1 · Tools (@tool), bind_tools & tool calling, a first simple agent; set up LangSmith tracing
- [ ] **Day 63** · Sat Jan 2 · 🛠️ **Build:** chat-with-bank-docs bot in LangChain
- [ ] **Day 64** · Sun Jan 3 · 🔁 Review Week 9 + write-up: plain SDK vs LangChain

</details>

<details>
<summary><b>📚 Week 10 · Jan 4-Jan 10 · RAG done properly</b></summary>

**🎯 Done when:** You have numbers for retrieval quality, not just demos  
**📖 Resources:** DeepLearning.AI short courses (RAG), Chip Huyen 'AI Engineering'  
**🧩 Coding practice:** LeetCode easy->medium: two pointers, sliding window, trees  
**📁 Folder:** [`Week-10-RAG/`](./Week-10-RAG/)

- [ ] **Day 65** · Mon Jan 4 · Full RAG pipeline in LangChain (ingest, chunk, embed, retrieve, generate); compare with Week 8
- [ ] **Day 66** · Tue Jan 5 · Retrieval metrics (recall@k, MRR, hit rate), finish my 50-question test set
- [ ] **Day 67** · Wed Jan 6 · Reranking with cross-encoders; query rewriting (MultiQueryRetriever)
- [ ] **Day 68** · Thu Jan 7 · Grounded answers with citations; refusing when context is missing; short spoken-style answers
- [ ] **Day 69** · Fri Jan 8 · Prompt design (system prompts, few-shot) + conversational RAG with history
- [ ] **Day 70** · Sat Jan 9 · 🛠️ **Build:** EscortBot FAQ brain, RAG with the 50-question test set
- [ ] **Day 71** · Sun Jan 10 · 🔁 Review Week 10 + plug the RAG into the Brain API

</details>

<details>
<summary><b>🕸️ Week 11 · Jan 11-Jan 17 · LangGraph from the basics</b></summary>

**🎯 Done when:** I can draw an agent graph on paper and build it in LangGraph with state, routing, memory and a human-approval step  
**📖 Resources:** LangChain Academy 'Introduction to LangGraph' (free), LangGraph docs (concepts + tutorials)  
**🧩 Coding practice:** LeetCode easy->medium: two pointers, sliding window, trees  
**📁 Folder:** [`Week-11-LangGraph Basics/`](./Week-11-LangGraph%20Basics/)

- [ ] **Day 72** · Mon Jan 11 · Why graphs for agents; StateGraph, state (TypedDict, reducers), nodes, edges, START/END
- [ ] **Day 73** · Tue Jan 12 · Conditional edges & routing, classify-then-branch (compare with my Week 3 classifier)
- [ ] **Day 74** · Wed Jan 13 · Tools in LangGraph: ToolNode, tools_condition; ReAct agent by hand vs create_react_agent
- [ ] **Day 75** · Thu Jan 14 · Memory: checkpointers (MemorySaver, SQLite), threads per visitor, streaming modes
- [ ] **Day 76** · Fri Jan 15 · Human-in-the-loop (interrupt), subgraphs, multi-agent supervisor; LangGraph Studio
- [ ] **Day 77** · Sat Jan 16 · 🛠️ **Build:** EscortBot agent, FAQ → RAG, 'take me to...' → guide_to() Nav2 tool, complaint → call_staff() with human handover
- [ ] **Day 78** · Sun Jan 17 · 🔁 Review Week 11 + LinkedIn post: my robot's LangGraph brain

</details>

<details>
<summary><b>🎙️ Week 12 · Jan 18-Jan 24 · Evals, voice & agent reliability</b></summary>

**🎯 Done when:** My agent has a measured success rate on 30 scenarios  
**📖 Resources:** LangSmith docs (datasets & experiments), faster-whisper & Piper TTS docs, MCP docs (modelcontextprotocol.io)  
**🧩 Coding practice:** LeetCode easy->medium: two pointers, sliding window, trees  
**📁 Folder:** [`Week-12-Evals and Voice/`](./Week-12-Evals%20and%20Voice/)

- [ ] **Day 79** · Mon Jan 18 · Evals: golden scenario sets, regression tests, LLM-as-judge (rubrics, biases)
- [ ] **Day 80** · Tue Jan 19 · Structured outputs & agent reliability: validation, retries, max steps, timeouts, tool errors
- [ ] **Day 81** · Wed Jan 20 · Tracing & debugging agents; LangSmith datasets & experiments
- [ ] **Day 82** · Thu Jan 21 · Voice I/O: speech-to-text (faster-whisper) and text-to-speech (Piper) as ROS 2 nodes; latency
- [ ] **Day 83** · Fri Jan 22 · Frameworks: LangGraph vs LlamaIndex vs plain SDK; MCP basics
- [ ] **Day 84** · Sat Jan 23 · 🛠️ **Build:** 30-scenario eval harness (text + Gazebo) that runs on every change
- [ ] **Day 85** · Sun Jan 24 · 🔁 Review Week 12 + full voice loop demo in Gazebo

</details>

<details>
<summary><b>🎛️ Week 13 · Jan 25-Jan 31 · Fine-tuning small open models (on-robot model)</b></summary>

**🎯 Done when:** GATE 2: RAG eval of 50 with accuracy measured + agent success rate on 30 scenarios  
**📖 Resources:** Hugging Face course (transformers, datasets, PEFT), Unsloth Colab notebooks, Ollama docs  
**🧩 Coding practice:** LeetCode easy->medium: two pointers, sliding window, trees  
**📁 Folder:** [`Week-13-Fine-Tuning/`](./Week-13-Fine-Tuning/)

- [ ] **Day 86** · Mon Jan 25 · When to fine-tune vs prompt vs RAG; Hugging Face transformers, datasets, hub
- [ ] **Day 87** · Tue Jan 26 · SFT data format & data quality, build data for intent routing + short answers
- [ ] **Day 88** · Wed Jan 27 · LoRA & QLoRA, quantisation, the PEFT library
- [ ] **Day 89** · Thu Jan 28 · Train on Colab/Kaggle GPU; evaluate against my baseline
- [ ] **Day 90** · Fri Jan 29 · Serving with Ollama on the robot laptop; latency vs cloud API; offline fallback
- [ ] **Day 91** · Sat Jan 30 · 🛠️ **Build:** LoRA fine-tune of a small model + comparison table (cloud API vs local fine-tuned: accuracy, latency)
- [ ] **Day 92** · Sun Jan 31 · 🏁 **GATE 2 check + LinkedIn post #2 with numbers + plan Phase 3**

</details>

### ☁️ Phase 3: Automation, Linux/Docker, cloud, MLOps
<sub>Feb 1-Mar 14 (Weeks 14-19) · Gate: Brain live on cloud with CI/CD + full robot demo in Gazebo; exam sat</sub>

<details>
<summary><b>⚙️ Week 14 · Feb 1-Feb 7 · n8n, Make & Playwright from the basics (+ SiteScout v1)</b></summary>

**🎯 Done when:** I can build an n8n workflow with webhook, branching, error handling and an AI node, and a Playwright suite with reliable locators  
**📖 Resources:** n8n docs + n8n courses (Level 1 & 2), Make Academy, Playwright for Python docs  
**🧩 Coding practice:** LeetCode medium: graphs, BFS/DFS, heaps  
**📁 Folder:** [`Week-14-n8n Make Playwright/`](./Week-14-n8n%20Make%20Playwright/)

- [ ] **Day 93** · Mon Feb 1 · n8n basics: nodes, triggers (manual, schedule, webhook), credentials, expressions, items; self-host with Docker
- [ ] **Day 94** · Tue Feb 2 · n8n deeper: IF/Switch, Merge, Loop Over Items, Code node, error workflows, sub-workflows, AI Agent node
- [ ] **Day 95** · Wed Feb 3 · Make basics: scenarios, modules, routers, iterators/aggregators, filters; n8n vs Make vs code
- [ ] **Day 96** · Thu Feb 4 · Playwright basics: page, locators (get_by_role etc.), actions, auto-waiting, screenshots, codegen
- [ ] **Day 97** · Fri Feb 5 · Playwright deeper: pytest-playwright assertions, fixtures, network interception, saved auth state, headless
- [ ] **Day 98** · Sat Feb 6 · 🛠️ **Build:** SiteScout v1 (second project), Playwright collects local business websites + screenshots, n8n sends them to a sheet, LLM drafts outreach
- [ ] **Day 99** · Sun Feb 7 · 🔁 EscortBot: n8n staff-alert workflow (call_staff → WhatsApp/Telegram) + daily visitor report

</details>

<details>
<summary><b>🐧 Week 15 · Feb 8-Feb 14 · Linux, Docker & Kubernetes from the basics</b></summary>

**🎯 Done when:** I can SSH into a fresh machine, containerise ROS 2 + the brain and run everything with compose  
**📖 Resources:** Linux Journey (free), OverTheWire Bandit levels 0-15, Docker 'Get started', TechWorld with Nana (Docker, Kubernetes)  
**🧩 Coding practice:** LeetCode medium: graphs, BFS/DFS, heaps  
**📁 Folder:** [`Week-15-Linux Docker Kubernetes/`](./Week-15-Linux%20Docker%20Kubernetes/)

- [ ] **Day 100** · Mon Feb 8 · Linux CLI: filesystem, permissions, users, pipes & redirection, grep/find
- [ ] **Day 101** · Tue Feb 9 · Linux for robots & servers: processes, systemd, journalctl, networking, SSH keys, bash scripts, cron
- [ ] **Day 102** · Wed Feb 10 · Docker basics: images vs containers, Dockerfile, layers, build/run, ports, volumes, env vars
- [ ] **Day 103** · Thu Feb 11 · Docker deeper: multi-stage builds, compose, host networking for ROS 2 (DDS), GUI/Gazebo in containers
- [ ] **Day 104** · Fri Feb 12 · Kubernetes basics: pods, deployments, services, configmaps/secrets on kind (concept level)
- [ ] **Day 105** · Sat Feb 13 · 🛠️ **Build:** ROS 2 nodes + Brain API + Postgres + n8n in docker compose; Brain API on a local kind cluster
- [ ] **Day 106** · Sun Feb 14 · 🔁 Review Week 15 + Bandit levels + write-up

</details>

<details>
<summary><b>☁️ Week 16 · Feb 15-Feb 21 · Cloud fundamentals</b></summary>

**🎯 Done when:** I can deploy a container to the cloud from scratch in under an hour  
**📖 Resources:** Microsoft Learn (Azure for Students) or AWS Skill Builder  
**🧩 Coding practice:** LeetCode medium: graphs, BFS/DFS, heaps  
**📁 Folder:** [`Week-16-Cloud Fundamentals/`](./Week-16-Cloud%20Fundamentals/)

- [ ] **Day 107** · Mon Feb 15 · Cloud account, regions, billing alerts FIRST, IAM & least privilege
- [ ] **Day 108** · Tue Feb 16 · Compute: VMs, container services (Azure Container Apps / App Runner), serverless
- [ ] **Day 109** · Wed Feb 17 · Storage & data: Blob/S3, managed Postgres, secrets manager
- [ ] **Day 110** · Thu Feb 18 · Networking: HTTPS, DNS, custom domain, nginx reverse proxy
- [ ] **Day 111** · Fri Feb 19 · Managed AI services: Azure OpenAI / Bedrock
- [ ] **Day 112** · Sat Feb 20 · 🛠️ **Build:** Brain API + staff dashboard on the cloud; robot (Gazebo) calls it over HTTPS, local model as offline fallback
- [ ] **Day 113** · Sun Feb 21 · 🔁 Review Week 16, redo the deploy from scratch, timed (<1 h)

</details>

<details>
<summary><b>🔁 Week 17 · Feb 22-Feb 28 · CI/CD & testing (ROS + AI)</b></summary>

**🎯 Done when:** A broken prompt or a failing ROS test cannot reach production  
**📖 Resources:** GitHub Actions docs, ros-tooling/setup-ros action, pytest docs  
**🧩 Coding practice:** LeetCode medium: graphs, BFS/DFS, heaps  
**📁 Folder:** [`Week-17-CI-CD Testing/`](./Week-17-CI-CD%20Testing/)

- [ ] **Day 114** · Mon Feb 22 · Git workflow (branches, PRs, review) + GitHub Actions: workflows, jobs, secrets, caching
- [ ] **Day 115** · Tue Feb 23 · pytest: unit vs integration tests; mocking LLM calls; launch_testing for ROS 2 nodes
- [ ] **Day 116** · Wed Feb 24 · Run my scenario evals in CI and fail on regressions; dev/staging/prod via env vars
- [ ] **Day 117** · Thu Feb 25 · colcon build + tests in CI; Playwright tests for the staff dashboard
- [ ] **Day 118** · Fri Feb 26 · Build & push Docker images in CI, then automatic cloud deploy
- [ ] **Day 119** · Sat Feb 27 · 🛠️ **Build:** every push runs ROS tests + evals + Playwright, then auto-deploys
- [ ] **Day 120** · Sun Feb 28 · 🔁 Review Week 17 + flagship polish

</details>

<details>
<summary><b>📈 Week 18 · Mar 1-Mar 7 · Observability, latency, safety & security</b></summary>

**🎯 Done when:** I can state p95 response time, detector FPS and cost per conversation  
**📖 Resources:** Langfuse / LangSmith docs, OWASP Top 10 for LLM apps  
**🧩 Coding practice:** LeetCode medium: graphs, BFS/DFS, heaps  
**📁 Folder:** [`Week-18-Observability/`](./Week-18-Observability/)

- [ ] **Day 121** · Mon Mar 1 · Latency budget for a robot: detector FPS, STT/LLM/TTS timings, p50/p95; structured logs & tracing
- [ ] **Day 122** · Tue Mar 2 · Caching, streaming answers to TTS, retries with backoff, timeouts, model fallbacks
- [ ] **Day 123** · Wed Mar 3 · Monitoring quality after launch; drift between sim and real camera
- [ ] **Day 124** · Thu Mar 4 · Safety & security: prompt injection via speech, no unsafe motion commands, privacy (no stored faces/voices)
- [ ] **Day 125** · Fri Mar 5 · n8n in production: alerts on errors, latency and cost spikes
- [ ] **Day 126** · Sat Mar 6 · 🛠️ **Build:** wire my LLM cost monitor into the Brain + public latency/cost/success dashboard
- [ ] **Day 127** · Sun Mar 7 · 🔁 Review Week 18 + LangGraph in production: Postgres checkpointer, streaming over FastAPI

</details>

<details>
<summary><b>🏅 Week 19 · Mar 8-Mar 14 · Cloud AI certification</b></summary>

**🎯 Done when:** GATE 3: Brain live on cloud with CI/CD, full robot demo in Gazebo; exam sat  
**📖 Resources:** Microsoft Learn AI-102 path or AWS AI Practitioner on Skill Builder, ask MLSA/GDG for vouchers  
**🧩 Coding practice:** LeetCode medium: graphs, BFS/DFS, heaps  
**📁 Folder:** [`Week-19-Cloud Certification/`](./Week-19-Cloud%20Certification/)

- [ ] **Day 128** · Mon Mar 8 · Exam blueprint (AWS AI Practitioner or Azure AI-102); book the exam slot
- [ ] **Day 129** · Tue Mar 9 · Responsible AI + service-selection questions
- [ ] **Day 130** · Wed Mar 10 · Practice test 1, review every wrong answer
- [ ] **Day 131** · Thu Mar 11 · Weak areas from practice test 1
- [ ] **Day 132** · Fri Mar 12 · Practice test 2, review
- [ ] **Day 133** · Sat Mar 13 · 🛠️ Practice test 3 / SIT THE EXAM
- [ ] **Day 134** · Sun Mar 14 · 🏁 **GATE 3 check + LinkedIn post #3: EscortBot Brain architecture + plan Phase 4**

</details>

### 🎯 Phase 4: Polish, interviews, applications
<sub>Mar 15-Apr 11 (Weeks 20-23) · Gate: 40+ applications and 4+ mock interviews</sub>

<details>
<summary><b>💼 Week 20 · Mar 15-Mar 21 · CV, portfolio & demo video</b></summary>

**🎯 Done when:** A recruiter sees proof in 10 seconds  
**📖 Resources:** My own repos, personal portfolio project, NeetCode 150  
**🧩 Coding practice:** LeetCode medium, mixed topics, timed  
**📁 Folder:** [`Week-20-Portfolio/`](./Week-20-Portfolio/)

- [ ] **Day 135** · Mon Mar 15 · CV v2 around EscortBot Brain + SiteScout, a number on every line; say clearly which parts are yours
- [ ] **Day 136** · Tue Mar 16 · Impact bullets (problem → built → result); send CV to 2 engineers for review
- [ ] **Day 137** · Wed Mar 17 · LinkedIn: headline, About, Featured section with demo videos
- [ ] **Day 138** · Thu Mar 18 · Portfolio site: projects, architecture diagrams, demo links
- [ ] **Day 139** · Fri Mar 19 · GitHub cleanup (pins, READMEs) + record the EscortBot demo video (Gazebo + real robot if possible)
- [ ] **Day 140** · Sat Mar 20 · 🛠️ **Build:** portfolio live + SiteScout polished (screenshot classifier + measured accuracy)
- [ ] **Day 141** · Sun Mar 21 · 🔁 Review Week 20 + apply CV feedback + first 5 applications

</details>

<details>
<summary><b>🏗️ Week 21 · Mar 22-Mar 28 · ML & LLM system design</b></summary>

**🎯 Done when:** I can whiteboard a full system in 30 minutes  
**📖 Resources:** Chip Huyen 'Designing Machine Learning Systems'  
**🧩 Coding practice:** LeetCode medium, mixed topics, timed  
**📁 Folder:** [`Week-21-System Design/`](./Week-21-System%20Design/)

- [ ] **Day 142** · Mon Mar 22 · Design framework: requirements, data, model, serving, evaluation, monitoring
- [ ] **Day 143** · Tue Mar 23 · Design: RAG assistant for company documents
- [ ] **Day 144** · Wed Mar 24 · Design: an embodied AI assistant / robot brain (my EscortBot, at scale across 50 branches)
- [ ] **Day 145** · Thu Mar 25 · Design: support-ticket triage or recommendation system (concept)
- [ ] **Day 146** · Fri Mar 26 · Trade-offs & scaling: edge vs cloud, queues, caching, vector DB at scale, multi-agent designs
- [ ] **Day 147** · Sat Mar 27 · 🛠️ **Build:** 3 written design answers + 30-min timed whiteboard practice + 5 applications
- [ ] **Day 148** · Sun Mar 28 · 🔁 Review Week 21 + mock design round with a peer + 5 applications

</details>

<details>
<summary><b>🗣️ Week 22 · Mar 29-Apr 4 · Behavioral interviews & mocks</b></summary>

**🎯 Done when:** I can tell each story in 2 minutes  
**📖 Resources:** Pramp or peer mocks (MLSA, GDG, AI Baithak network)  
**🧩 Coding practice:** LeetCode medium, mixed topics, timed  
**📁 Folder:** [`Week-22-Behavioral Interviews/`](./Week-22-Behavioral%20Interviews/)

- [ ] **Day 149** · Mon Mar 29 · STAR method + write the EscortBot Brain story (team project, my part, the hardest bug)
- [ ] **Day 150** · Tue Mar 30 · Stories: Lead Engine & Facebook Lead Intelligence System
- [ ] **Day 151** · Wed Mar 31 · Failure story + ownership, conflict, deadline stories (6 total)
- [ ] **Day 152** · Thu Apr 1 · Explain each project at 3 depths: 30 s, 2 min, deep dive
- [ ] **Day 153** · Fri Apr 2 · Questions to ask interviewers; salary research & negotiation basics
- [ ] **Day 154** · Sat Apr 3 · 🛠️ Mock interviews #1 and #2 (record them) + 5 applications
- [ ] **Day 155** · Sun Apr 4 · 🔁 Review mock recordings, refine stories + 5 applications

</details>

<details>
<summary><b>🚀 Week 23 · Apr 5-Apr 11 · Applications at volume</b></summary>

**🎯 Done when:** GATE 4: 40+ applications and 4+ mock interviews  
**📖 Resources:** Application tracker (company, role, date, contact, status, follow-up)  
**🧩 Coding practice:** LeetCode medium, mixed topics, timed  
**📁 Folder:** [`Week-23-Applications/`](./Week-23-Applications/)

- [ ] **Day 156** · Mon Apr 5 · Target list: remote AI startups, robotics/embodied-AI companies, top Pakistani product companies; tracker
- [ ] **Day 157** · Tue Apr 6 · Referrals: message 5 engineers + 2 tailored applications
- [ ] **Day 158** · Wed Apr 7 · Tailor top 3 CV bullets per role (robotics vs pure AI roles) + 3 applications
- [ ] **Day 159** · Thu Apr 8 · 3 applications + follow up on anything older than 7 days
- [ ] **Day 160** · Fri Apr 9 · 2 applications + prep for mocks #3 and #4
- [ ] **Day 161** · Sat Apr 10 · 🛠️ Mock interviews #3 and #4 + 2 applications
- [ ] **Day 162** · Sun Apr 11 · 🏁 **GATE 4 check + retrospective + plan what comes next**

</details>

---

## 🦾 EscortBot Brain updates

_Every Sunday: one screenshot or clip + one real number._

| Week | Update | Number |
|---|---|---|
| Day 8 | NumPy arrays, dtype, shape, reshape & indexing | ✅ Done |
| Day 9 | NumPy broadcasting & vectorization vs loops | ✅ Done |
| Day 10 | Pandas: filtering, GroupBy & missing values | ✅ Done |
| Day 11 | Linear algebra: vectors, dot product & matrix multiplication | ⬜ Upcoming |
| Day 12 | Derivatives, chain rule, gradients & probability basics | ⬜ Upcoming |
| Day 13 | Loss functions (MSE) & gradient descent | ⬜ Upcoming |
| Day 14 | 🛠️ Build: Linear regression from scratch in NumPy | ⬜ Upcoming |

### 📚 What I'm learning

- NumPy arrays and vectorized operations
- Broadcasting and efficient numerical computation
- Pandas for data analysis and manipulation
- Filtering, grouping and handling missing data
- Linear algebra for Machine Learning
- Derivatives and gradients
- Loss functions and optimisation
- Gradient Descent
- Building Linear Regression from scratch

### 📁 Week 2 Structure

```text
Week-02-NumPy & Pandas/
│
├── Day 08 - NumPy Arrays, dtype, shape, reshape, indexing
├── Day 09 - Broadcasting & Vectorization vs Loops
├── Day 10 - Pandas: Filtering, GroupBy, Missing Values
└── Notes.md
```

---

## 🎯 Current Goal

I'm currently building my foundation in:

```text
Python
   ↓
NumPy & Pandas
   ↓
Mathematics for Machine Learning
   ↓
Machine Learning
   ↓
Computer Vision
   ↓
ROS 2 & Robotics
```

**Current status: Week 2 — Day 10 complete. 🚀**
