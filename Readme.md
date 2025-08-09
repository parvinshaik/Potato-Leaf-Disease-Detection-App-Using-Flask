🍃 Potato Leaf Disease Detection using CNN: 
This is a web-based application developed using Flask and a Convolutional Neural Network (CNN) to detect diseases in potato leaves. The model can classify an uploaded potato leaf image into one of the following categories:

✅ Potato___Healthy

⚠️ Potato___Early_blight

❌ Potato___Late_blight

Project Description: 
This project uses deep learning to identify and classify potato leaf diseases. A CNN model was trained using Keras and TensorFlow to accurately detect leaf conditions based on images. The model is integrated into a Flask web application that allows users to upload leaf images through a simple interface and receive instant predictions.

## Features
- Upload a potato leaf image and get instant prediction
- View uploaded image and prediction with confidence score
- Lightweight Flask web interface
- Supports real-time plant disease diagnosis



## Technologies Used

| Category     | Tools/Libraries                                  | Usage                                                                 |
|--------------|--------------------------------------------------|-----------------------------------------------------------
| **Frontend** | HTML, CSS                                        | To design the user interface for uploading images and viewing results |
| **Backend**  | Python, Flask                                    | Flask handles server-side logic and routes the uploaded image to the model |
| **ML Model** | TensorFlow, Keras, CNN (Deep Learning)           | Used to build and train the Convolutional Neural Network (CNN) for image classification |
| **Utilities**| NumPy, Pillow, Werkzeug                          | NumPy for numerical operations, Pillow for image processing, Werkzeug for secure file uploads |


 ## Project Structure 
Potato-Leaf-Disease-Detection/
│
├── app.py # Main Flask application
├── model/
│ └── model.h5 # Trained CNN model
├── templates/
│ └── index.html # HTML frontend
├── static/
│ └── uploads/ # Folder for uploaded images
├── dataset/ # Contains training/validation data
├── README.md # Project documentation
└── requirements.txt # Python dependencies



## How to Run the Project Locally

1. Clone the Repository

git clone https://github.com/yourusername/potato-leaf-disease-detection.git

cd potato-leaf-disease-detection

2. Install Dependencies

pip install -r requirements.txt
 
     Or install manually:

pip install flask tensorflow keras numpy pillow 

3. Run the App

python app.py





