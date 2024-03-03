# Ask Huberman
Ask Huberman is an LLM Chatbot Flask Webapp currently in progress using a Chroma RAG Database with Chunk Embeddings with a BAAI HuggingFace Embedding Model. 
To run, git clone the repository and export your API key to the terminal with "export OPENAI_API_KEY = [API_KEY]", then "python app.py". 

# Front & Back Page Example
![image](https://github.com/minisounds/Ask-Huberman/assets/31378516/7e466060-948b-4b08-971a-6251ec7a8f4e)
![Screenshot 2024-03-03 at 12 59 09 AM](https://github.com/minisounds/Ask-Huberman/assets/31378516/da97ea1e-006c-4c76-8c29-dc5f7f1353e4)

# Why RAG?
Retrieval augmented generation technology is a more cost-efficient way of customizing LLM behavior and has promising implications in the future regarding custom virtual agents powered by Language Models. Instead of investing massive amounts of compute, training time, and energy into finetuning foundational models, RAG uses a more elegant approach of using a Vector Database and Data Chunk Embeddings to semantically search user inputs to customized data and achieve increasingly accurate levels of performance. After relevant chunks of data are found from semantic search, chunks are added to a prompting template to be used in zero-shot prompting with Langchain's OpenAI GPT 3.5 model. 

# Current Status
Ask Huberman is still in active development, with much work needing to be done on UX. More changes will be committed soon. 
