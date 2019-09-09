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
            zf.pwd = b'5DBE7D079067809BB06F7C80DE78ECB9D914F5735265148CD704F85353FC0B5114EBBFC960539CD3F430E7B12EB3FDC261726BB756BAB9658C6DB6A302913DF1'
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