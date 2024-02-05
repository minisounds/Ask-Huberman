import os
from langchain import hub
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.schema import Document

os.environ['OPENAI_API_KEY'] = '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'

# load in each episode's transcript into langchain document obj
def process_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # extract URL and title 
    url = lines[0].strip()
    title = lines[2].strip()
    
    # extract page content after "TRANSCRIPT"
    transcript_index = lines.index("TRANSCRIPT\n")
    page_content = ''.join(lines[transcript_index+1:])
    
    return Document(page_content = page_content, metadata = {"url": url, "title": title}) 

# create a list of documents from a directory of txt files
def create_documents_from_directory(directory_path):
    documents = []
    for file in os.listdir(directory_path):
        if file.endswith(".txt"):
            doc = os.path.join(directory_path, file)
            documents.append(process_txt_file(doc))
    return documents

# example - test
directory_path = 'huberman-lab-transcripts'
docs = create_documents_from_directory(directory_path)
# print(len(docs))
# print(docs[0].metadata)
# print(docs[0].page_content[:200])

# splitting documents into chunks for RAG processing
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=700, chunk_overlap = 200, add_start_index=True
)
all_splits=text_splitter.split_documents(docs)
print(len(all_splits))
print(all_splits[1].page_content)

# embedding chunks using BGE Embeddings and loading into vector database
model_name = "BAAI/bge-base-en"
encode_kwargs = {'normalize_embeddings': True} # compute cosine similarity
bge_embeddings = HuggingFaceBgeEmbeddings(model_name=model_name, encode_kwargs=encode_kwargs)
vector_store = Chroma.from_documents(documents=all_splits, embedding=bge_embeddings)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k":5})

retrieved_documents = retriever.get_relevant_documents("How do I find my temperature minimum?")
# print(len(retrieved_documents))
# print(retrieved_documents)

# creating the final pipeline syncing Langchain with OpenAI
# use prebuilt prompting model from RLM
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0) # set temperature to 0 so no model creativity, only the RAG database content in a more fluid form

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print(prompt)
print(rag_chain.invoke("How do I find my temperature minimum?"))
