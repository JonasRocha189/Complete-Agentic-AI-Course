# Complete Agentic AI Course

Hands-on notes and projects from the [Complete Agentic AI Course](https://www.youtube.com/watch?v=rV3HJ4LEZ7k), covering LangChain, LangGraph, RAG (vector-based and vectorless), deep agents, LLM evaluation, and LLM gateways.

Each numbered folder is a self-contained module with its own `pyproject.toml`/`requirements.txt`, `.env`, and `notes.txt` with extra details from following along.

## Modules

### [1-LangChain](1-LangChain/)
Introduction to LangChain fundamentals via notebooks in `updatedlangchain/`:
- Core concepts, model integration (Google AI Studio, Groq, OpenAI)
- Tools (functions need docstrings so the model understands what they do)
- Messages and structured output
- Middleware (Summarization, Human in the Loop, Model Call Limit, etc.)
- `model.invoke` (single call, full response) vs `model.stream` (incremental chunks) vs `model.batch` (multiple prompts, concurrent)
- `guardrails.ipynb` — deterministic vs model-based guardrails, built-in `PIIMiddleware` and `HumanInTheLoopMiddleware`, custom `before_agent`/`after_agent` hooks, layering multiple guardrails, and a healthcare-chatbot case study

### [2-langGraph](2-langGraph/)
Building agents as graphs, based on [krishnaik06's Agentic LangGraph crash course](https://github.com/krishnaik06/Agentic-LanggraphCrash-course):
- `1-basic-chatbot/` — a basic chatbot using LangGraph's core components (Nodes, Edges, State)
- `2-human-in-the-loop/` — human-in-the-loop interrupts
- `3-mcp/` — Model Context Protocol servers/clients (`math_server.py`, `weather.py`, `client.py`) using `stdio` and `streamable-http` transports; the server (e.g. `weather.py`) must be running before `client.py` connects
- Uses Tavily as a web search/scraping tool (requires its own API key)
- Libraries: `langchain-mcp-adapters` (LangChain MCP support) and `mcp` (FastMCP)

### [3-RAG](3-RAG/)
Retrieval-Augmented Generation, progressing in complexity:
- `notebook/1-document.ipynb` — a basic RAG pipeline
- `notebook/2-pdf_loader.ipynb` — RAG variants that read and process PDF files
- `src/` — a full pipeline (`data_loader.py`, `embedding.py`, `vector_store.py`, `search.py`) runnable via `app.py`
- Vector storage examples with both Chroma (`data/vector_store/`) and FAISS (`faiss_store/`)

### [4-Vectorless-RAG](4-Vectorless-RAG/)
PageIndex — reasoning-based RAG with no vector database and no chunking:
- Key idea: build a hierarchical tree index of a document (like a smart table of contents) and have an LLM reason over the tree to find exact sections, instead of chunk → embed → cosine-similarity retrieval
- Upload/index a PDF via the PageIndex cloud API, inspect the resulting tree structure
- LLM tree search (`llm_tree_search`) and a full end-to-end pipeline: search → retrieve → generate grounded answers with page citations
- Expert-guided retrieval — inject domain routing rules (e.g. financial-document sections) directly into the prompt instead of fine-tuning embeddings
- PageIndex's Chat API for a zero-setup Q&A interface, plus the self-hosted open-source option for on-prem/private deployments
- Side-by-side comparison of traditional vector RAG vs. PageIndex, and cleanup of cloud-hosted document trees

### [5-Deep-Agents](5-Deep-Agents/)
Deep Agents — agents that plan, delegate to subagents, and use a virtual file system for complex, multi-step tasks (built on LangGraph, using the `deepagents` library, inspired by Claude Code/Deep Research/Manus-style agents):
- When to reach for a deep agent vs. a simple tool-calling agent
- Building a basic deep agent with a web-search tool (Tavily) and comparing it against a simple `create_agent` baseline
- What a deep agent does automatically: planning via a built-in `write_todos` tool, research via tool calls, and context management via file system tools (`write_file`, `read_file`)
- Customizing deep agents: swapping models (Groq, GPT-5), writing a custom system prompt, and defining specialized subagents

### [6-LLM-Evaluation](6-LLM-Evaluation/)
Chatbot and RAG evaluation using LangSmith:
- Creating a LangSmith dataset of test cases for an application
- Defining metrics with LLM-as-a-judge, plus simple heuristic metrics (e.g. concision)
- Running evaluations across experiments and comparing different models
- Evaluating a full RAG pipeline with four evaluator types: **Correctness** (response vs. reference answer), **Relevance** (response vs. input), **Groundedness** (response vs. retrieved docs), and **Retrieval Relevance** (retrieved docs vs. input)

### [7-LLM-Gateway](7-LLM-Gateway/)
Building an LLM Gateway with LiteLLM + LangChain:
- What an LLM Gateway is and the production problems it solves (provider lock-in, no unified API)
- LiteLLM's unified `completion()` API across providers (OpenAI, Anthropic, Groq, Gemini, etc.)
- Automatic fallbacks across providers/models, cost tracking via `completion_cost`, and response caching
- Smart routing with LiteLLM's `Router` — least-busy, latency-based, and cost-based routing strategies, plus load balancing across multiple API keys/deployments
- Observability via custom callbacks for per-call audit logging
- Integrating the gateway into LangChain (`ChatLiteLLM`) so a whole chain can swap providers with a one-line model-string change, including a multi-provider chain with fallbacks
- A task-aware chatbot demo, and lightweight production guardrails implemented as LiteLLM callbacks (PII redaction, prompt-injection blocking, forbidden-topic filtering)

## Setup

Each module uses [uv](https://docs.astral.sh/uv/) for dependency management. From inside a module folder:

```bash
uv sync
```

Each module also expects a `.env` file (not committed) with the relevant API keys — see that module's `notes.txt` for which keys are needed (Google AI Studio, Groq, OpenAI, Tavily, PageIndex, LangSmith, Anthropic, etc.).
