### Gemini Agent on LlamaIndex with MCP

### Requirements

```
uv sync
```

### prepare .env

Create a `.env` file in the root directory of the project with the following content:

##### LLM Provider Configuration

Google Gemini API

```
GOOGLE_API_KEY=
#or
GEMINI_API_KEY=

GOOGLE_GENAI_MODEL="gemini-2.0-flash"
```

(Optional)Vertex AI Support

```
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="us-central1"
```

(Optional) Langfuse Configuration for tracing

```
# Langfuse
LANGFUSE_PUBLIC_KEY="pk-..."
LANGFUSE_SECRET_KEY="sk-..."
LANGFUSE_HOST="..."
```

##### MCP Configuration

(Optional) Firecrawl Configuration

```
export FIRECRAWL_API_KEY=
```

### Run

MCP servers

```bash
uv run fastmcp run --help --server-spec mcp.json
```

Chainlit server

```bash
uv run chainlit run main.py
```

### Development

Linting and type checking can be run with:

```bash
make lint type
```
