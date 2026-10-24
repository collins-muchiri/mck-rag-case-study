# mck-rag-case-study

Engineering case study: a production retrieval-augmented generation system over UN-Habitat SDG 11 documentation. Portfolio artifact 2 of 3.

The implementation code lives in [sdg-rag-system](https://github.com/collins-muchiri/sdg-rag-system). This repository holds the case study: what was built, why each choice was made, what it cost, and what broke first.

## What it does

Semantic search and question answering over UN-Habitat SDG 11 documentation, for programme staff in low-connectivity field conditions. Vector embeddings for retrieval, LangChain orchestration, RESTful query API, serverless inference on AWS Lambda with role-based access control.

## Architecture

    UN-Habitat SDG 11 documents
      -> chunking and embedding (Llama 3.1 embeddings)
      -> pgvector store in PostgreSQL
      -> LangChain retrieval and generation orchestration
      -> REST API on AWS Lambda, RBAC and encryption at rest
      -> programme staff client, sub-second responses, offline-tolerant

## Decisions and trade-offs

- pgvector inside the existing PostgreSQL estate rather than a managed vector store: one less service, one more dependency on my own operations discipline. Chosen because the client estate was already PostgreSQL and the retrieval volume did not justify a second system.
- Serverless Lambda inference rather than a resident container: cost follows usage, cold starts are the price. Acceptable because field queries are intermittent.
- Chunk size chosen for paragraph-level citation so answers can point at a page, not a document. Smaller chunks hurt recall; this was the compromise.

## Numbers, and their status

- Retrieval time for programme staff reduced by around 40 per cent against a timed manual search protocol.
- Response latency under 500 ms in low-connectivity conditions. Reported from the original build; the measurement harness is being rebuilt here and the figure will be re-published with its method, percentile and payload size, or corrected if it does not reproduce.
- Cost per query: to be measured and published here.

## What failed first

Pending. This section will record the first production failure and the fix, written from incident notes. It is deliberately left empty rather than filled with a plausible story.

## Data statement

UN-Habitat SDG 11 documentation is public. No client, beneficiary or personal data is present in this system or this repository.

## Licence

MIT. See LICENSE.
