# Ask Huberman
Ask Huberman is an LLM Chatbot Flask Webapp currently in progress using a Chroma RAG Database with Chunk Embeddings with a BAAI HuggingFace Embedding Model. 
To run, git clone the repository and export your API key to the terminal with "export OPENAI_API_KEY = [API_KEY]", then "python app.py". 

# Why RAG?
Retrieval augmented generation technology is a more cost-efficient way of customizing LLM behavior and has promising implications in the future regarding custom virtual agents powered by Language Models. Instead of investing massive amounts of compute, training time, and energy into finetuning foundational models, RAG uses a more elegant approach of using a Vector Database and Data Chunk Embeddings to semantically search user inputs to customized data and achieve increasingly accurate levels of performance. After relevant chunks of data are found from semantic search, chunks are added to a prompting template to be used in zero-shot prompting with Langchain's OpenAI GPT 3.5 model. 

# Current Status
Ask Huberman is still in active development, with much work needing to be done on UX. More changes will be committed soon. 
