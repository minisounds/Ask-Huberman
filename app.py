from flask import Flask, render_template, request
from utils import invoke_rag_chain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/invoke', methods=['POST'])
def invoke_rag():
    question = request.form.get('question')
    result = invoke_rag_chain(question)
    
    return render_template('result.html', result=result, question=question)

if __name__ == "__main__":
    app.run(debug=True)