from flask import Flask, render_template, request, jsonify
from langchain_community.llms.ollama import Ollama
import os

app = Flask(__name__)

# Configure o diretório para armazenar arquivos carregados
UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure o endereço do Ollama a partir da variável de ambiente
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:11434')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():

    user_message = request.json.get('message')
    # Aqui você pode integrar com o seu modelo LLM

    model = Ollama(model="llama3.1")
    response_text = model.invoke(user_message)
    
    return jsonify({'response': response_text})


@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'Nenhum arquivo enviado'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'Nenhum arquivo selecionado'})
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    return jsonify({'success': True, 'message': 'Arquivo carregado com sucesso'})


if __name__ == '__main__':
    app.run(debug=True)

