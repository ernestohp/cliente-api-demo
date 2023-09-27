from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # The folder where uploaded files will be stored
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = file.filename
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully  (' + filename + ')'}), 200

@app.route('/hola', methods=['GET'])
def hola():
    return jsonify({'message': 'Hola MundoX'}), 200

@app.route('/', methods=['GET'])
def hola2():
    return "Prueba okX", 200


if __name__ == '__main__':
    app.run(debug=True)
