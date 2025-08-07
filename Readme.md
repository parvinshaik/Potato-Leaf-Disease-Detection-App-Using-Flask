# Potato Leaf Disease Detection using CNN
This project is a web-based application built with **Flask** and **CNN (Convolutional Neural Network)** that detects diseases in potato leaves. Users can upload an image of a potato leaf, and the system will predict whether the leaf is:

- `Potato___healthy`
- `Potato___Early_blight`
- `Potato___Late_blight`


## Features

- Upload a potato leaf image and get instant prediction
- View uploaded image and prediction with confidence score
- Lightweight Flask web interface
- Supports real-time plant disease diagnosis



## Technologies Used

| Category     | Tools/Libraries                          |
|--------------|-------------------------------------------|
| **Frontend** | HTML, CSS                                 |
| **Backend**  | Python, Flask                             |
| **ML Model** | TensorFlow, Keras, CNN                    |
| **Utilities**| NumPy, Werkzeug (for secure file upload)  |



## 🗂️ Project Structure
Potato-Leaf-Disease-Detection/
│
├── app.py # Main Flask application
├── model/
│ └── model.h5 # Trained CNN model
├── templates/
│ └── index.html # HTML frontend
├── static/
│ └── uploads/ # Folder for uploaded images
├── dataset/ # Contains training/val data
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





