from flask import Flask, send_file
import zipfile
import os
app = Flask(__name__)

@app.route('/')
def download():
    zip = zipfile.ZipFile("arquivo.zip", "w")
    dirname =  os.getcwd()
    for folderName, subfolders, filenames in os.walk(os.path.join(dirname, "lib")):
        for filename in filenames:
            zip.write(os.path.join("lib", filename))
    zip.close()

    return send_file(dirname + "/arquivo.zip", as_attachment=True)

@app.route('/status')
def status():
    return 'Running'

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)