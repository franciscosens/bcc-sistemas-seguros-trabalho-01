from flask import Flask, send_file
import pyzipper
import os
app = Flask(__name__)

@app.route('/')
def download():

    dirname =  os.getcwd()
    with pyzipper.AESZipFile('arquivo.zip', 'w', compression=pyzipper.ZIP_LZMA) as zf:
        zf.pwd = b'123'
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