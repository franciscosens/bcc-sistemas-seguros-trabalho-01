from flask import Flask, send_file
import pyzipper
import os
app = Flask(__name__)

@app.route('/')
def download():

    dirname =  os.getcwd()
    with pyzipper.AESZipFile('arquivo.zip', 'w', compression=pyzipper.ZIP_LZMA) as zf:
        zf.pwd = b'5DBE7D079067809BB06F7C80DE78ECB9D914F5735265148CD704F85353FC0B5114EBBFC960539CD3F430E7B12EB3FDC261726BB756BAB9658C6DB6A302913DF1'
        zf.setencryption(pyzipper.WZ_AES, nbits=128)
        for folderName, subfolders, filenames in os.walk(os.path.join(dirname, "lib")):
            for filename in filenames:
                zf.write(os.path.join("lib", filename))
                
    return send_file(dirname + "/arquivo.zip", as_attachment=True)

@app.route('/status')
def status():
    return 'Running'

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)