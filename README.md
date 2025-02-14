# langchain-raccoonai

This package contains the LangChain integration with RaccoonAI

## Installation

```bash
pip install -U langchain-raccoonai
```

And you should configure credentials by setting the following environment variables:

* TODO: fill this out

## Chat Models

`ChatRaccoonAI` class exposes chat models from RaccoonAI.

```python
from langchain_raccoonai import ChatRaccoonAI

llm = ChatRaccoonAI()
llm.invoke("Sing a ballad of LangChain.")
```

## Embeddings

`RaccoonAIEmbeddings` class exposes embeddings from RaccoonAI.

```python
from langchain_raccoonai import RaccoonAIEmbeddings

embeddings = RaccoonAIEmbeddings()
embeddings.embed_query("What is the meaning of life?")
```

## LLMs
`RaccoonAILLM` class exposes LLMs from RaccoonAI.

```python
from langchain_raccoonai import RaccoonAILLM

llm = RaccoonAILLM()
llm.invoke("The meaning of life is")
```
