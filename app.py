import time
import urllib
import numpy as np
from PIL import Image
import streamlit as st
from tensorflow import keras

image = None

html_temp = """
<div style="padding:20px">
<center><h1>Fruit Classifier</h1></center>
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)

html_temp = """
<div>
<center><h3>Please upload any Fruit Image</h3></center>
<center><h3>[Apple, Banana, Orange, Mango, Pineapple]</h3></center>
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)

opt = st.selectbox(
    "How do you want to upload the image for classification?",
    ("Please Select", "Upload image via link", "Upload image from device"),
)

# Upload from device
if opt == "Upload image from device":
    file = st.file_uploader("Select", type=["jpg", "png", "jpeg"])

    if file is not None:
        image = Image.open(file)

# Upload via URL
elif opt == "Upload image via link":

    img = st.text_input("Enter the Image Address")

    if img:
        try:
            image = Image.open(urllib.request.urlopen(img))
        except:
            st.error("Please enter a valid Image Address!")

# Prediction
if image is not None:

    st.image(image, width=300, caption="Uploaded Image")

    if st.button("Classify"):

        img_array = np.array(image.resize((128, 128)))
        img_array = img_array / 255.0

        model = keras.models.load_model("Model/model.h5")

        train_labels = {
            "Apple": 0,
            "Banana": 1,
            "Mango": 2,
            "Orange": 3,
            "Pineapple": 4,
        }

        labels = {v: k for k, v in train_labels.items()}

        predictions = model.predict(img_array[np.newaxis, ...])

        acc = np.max(predictions[0]) * 100
        result = labels[np.argmax(predictions[0])]

        st.success(
            f'The uploaded image has been classified as "{result}" with confidence {acc:.2f}%'
        )
