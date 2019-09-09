from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/download-seguro" target="_blank">Download Seguro</a>\
        <a href="/download-inseguro" target="_blank">Download Inseguro</a>'

@app.route('/download-seguro')
def download_seguro():
    file = requests.get('http://localhost:5000')
    with open('libs/arquivo-seguro.zip', 'wb') as f:
        f.write(file.content)


    return 'Feito o download do arquivo de forma segura'

@app.route('/download-inseguro')
def download_inseguro():
    file = requests.get('http://localhost:5001')
    with open('libs/arquivo-inseguro.zip', 'wb') as f:
        f.write(file.content)
    return 'Feito o download do arquivo'
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5002)