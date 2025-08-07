from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
import numpy as np
import os

app = Flask(__name__)
model = load_model('model/model.h5')

class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    img_path = None

    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400
        file = request.files['file']
        if file.filename == '':
            return "No file selected", 400
        if file:
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # ✅ Ensure folder exists

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            img_path = filepath

            # Preprocess image
            img = image.load_img(filepath, target_size=(128, 128))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            # Predict
            preds = model.predict(img_array)
            predicted_class = class_names[np.argmax(preds[0])]
            confidence = np.max(preds[0]) * 100
            prediction = f"{predicted_class} ({confidence:.2f}%)"

    return render_template('index.html', prediction=prediction, image=img_path)

if __name__ == '__main__':
    app.run(debug=True)
