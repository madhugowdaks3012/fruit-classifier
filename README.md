# 🍎 Fruit Classifier using Deep Learning

An interactive web application built using **Streamlit** and **TensorFlow/Keras** that classifies fruit images into different categories with high accuracy.

---

## 🚀 Features

- Upload image from **device**
- Upload image via **URL**
- Supports classification of:
  - Apple 🍎
  - Banana 🍌
  - Mango 🥭
  - Orange 🍊
  - Pineapple 🍍
- Displays prediction with **confidence score**
- Clean and simple UI

---

## 🧠 Model Details

- Built using **TensorFlow/Keras**
- Input image resized to **128x128**
- Normalized pixel values (0–1)
- Predicts probabilities for 5 classes

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🌐
- TensorFlow / Keras 🤖
- NumPy
- PIL (Python Imaging Library)

---

## 📂 Project Structure

Fruit-Classifier/
│── app.py
│── Model/
│ └── model.h5
│── requirements.txt
│── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the repository:
git clone https://github.com/madhugowdaks3012/Fruit-Classifier.git
cd Fruit-Classifier

###2. Install dependencies:
pip install -r requirements.txt

###3. Run the app:
streamlit run app.py

📸 Usage
Select upload method:
Upload from device ORPaste image URL
Upload image
Click "Classify"
View prediction result with confidence

📊 Example Output
The uploaded image has been classified as "Apple"
with confidence 99.99%

⚠️ Notes
Ensure the model file is located at:
Model/model.h5
Supported formats: JPG, PNG, JPEG

📌 Future Improvements
Add more fruit categories
Improve model accuracy
Deploy on cloud (Streamlit Cloud / AWS)
Add drag-and-drop UI enhancements

👨‍💻 Author
Madhu Gowda K S
madhugowdaks3012@gmail.com
