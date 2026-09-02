# Complete Agentic AI Course

Hands-on notes and projects from the [Complete Agentic AI Course](https://www.youtube.com/watch?v=rV3HJ4LEZ7k), covering LangChain, LangGraph, and Retrieval-Augmented Generation (RAG).

Each numbered folder is a self-contained module with its own `pyproject.toml`/`requirements.txt`, `.env`, and `notes.txt` with extra details from following along.

## Modules

### [1-LangChain](1-LangChain/)
Introduction to LangChain fundamentals via notebooks in `updatedlangchain/`:
- Core concepts, model integration (Google AI Studio, Groq, OpenAI)
- Tools (functions need docstrings so the model understands what they do)
- Messages and structured output
- Middleware (Summarization, Human in the Loop, Model Call Limit, etc.)
- `model.invoke` (single call, full response) vs `model.stream` (incremental chunks) vs `model.batch` (multiple prompts, concurrent)

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

## Setup

Each module uses [uv](https://docs.astral.sh/uv/) for dependency management. From inside a module folder:

```bash
uv sync
```

Each module also expects a `.env` file (not committed) with the relevant API keys — see that module's `notes.txt` for which keys are needed (Google AI Studio, Groq, OpenAI, Tavily, etc.).
