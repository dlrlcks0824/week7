from flask import Flask, render_template, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_and_analyze():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"

        if file:
            image = Image.open(io.BytesIO(file.read()))
            # 이미지 분석 로직을 추가

            # 예시: 이미지 크기 분석
            width, height = image.size

            # 분석 결과를 JSON 형식으로 반환
            result = {
                "width": width,
                "height": height
            }
            return jsonify(result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
