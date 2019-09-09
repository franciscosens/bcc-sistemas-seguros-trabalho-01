from flask import Flask
import pyzipper
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/download-seguro" target="_blank">Download Seguro</a>\
        <a href="/download-inseguro" target="_blank">Download Inseguro</a>'

@app.route('/download-seguro')
def download_seguro():
    file = requests.get('http://localhost:5000')
    arquivo_nome = 'libs/arquivo-seguro.zip'
    with open(arquivo_nome, 'wb') as f:
        f.write(file.content)

    try:
        with pyzipper.AESZipFile(arquivo_nome) as zf:
            zf.pwd = b'123'
            zf.extractall()
            return 'Feito o download do arquivo de forma segura'
    except:
        return 'Cuidado não foi possível descompactar o arquivo de forma segura'

@app.route('/download-inseguro')
def download_inseguro():
    file = requests.get('http://localhost:5001')
    with open('libs/arquivo-inseguro.zip', 'wb') as f:
        f.write(file.content)
    return 'Feito o download do arquivo'
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5002)