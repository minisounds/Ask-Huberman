from flask import Flask, render_template, request
from utils import setup_langchain_environment, invoke_rag_chain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invoke', methods=['POST'])
def invoke_rag():
    # api_key = request.form.get('api_key')
    question = request.form.get('question')
    
    # Set the OpenAI API key to environment
    # setup_langchain_environment(api_key)
    
    result = invoke_rag_chain(question)
    
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)