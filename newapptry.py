import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the CNN model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('C:/Users/272720/OneDrive/Desktop/Food 20/model_v1_inceptionV3.h5')
    return model

# Function to preprocess the image
def preprocess_image(image):
    img = image.resize((299, 299))  # Resize image to match model's expected sizing
    img_array = np.array(img)  # Convert PIL image to numpy array
    img_array = img_array / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to make predictions
def predict_image(image, model, class_names):
    processed_img = preprocess_image(image)
    prediction = model.predict(processed_img)
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_class_index]
    return predicted_class_name

# Function to display ingredients
def display_ingredients(predicted_class, dishes):
    ingredients = dishes.get(predicted_class, "Ingredients not available")
    return ingredients

# Streamlit app layout
def main():
    st.title('Food Vision with Streamlit')
    st.sidebar.title('Upload Image')

    uploaded_image = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    model = load_model()
    class_names = ['burger', 'butter_naan', 'chai', 'chapati', 'chole_bhature', 'dal_makhani', 'dhokla', 'fried_rice', 'idli', 'Jalebi', 'Kaathi_rolls', 'kadai_paneer', 'kulfi', 'masala_dosa', 'momos', 'paani_puri', 'pakoda', 'pav_bhaji', 'pizza', 'samosa']
    dishes = {
    "burger": "Ground beef or meat alternative, Burger buns, Lettuce, Tomato slices, Onion slices, Pickles, Cheese slices, Ketchup, Mustard, Mayonnaise",
    "butter_naan": "All-purpose flour, Yeast, Yogurt, Butter, Salt, Sugar, Baking powder",
    "chai": "Tea leaves or tea bags, Water, Milk, Sugar, Spices (like cardamom, cinnamon, ginger)",
    "chapati": "Whole wheat flour, Water, Salt",
    "chole_bhature": "Chickpeas, Onions, Tomatoes, Ginger, Garlic, Spices (like cumin, coriander, turmeric), All-purpose flour, Yogurt, Baking powder, Salt, Oil for frying",
    "dal_makhani": "Lentils (black gram and kidney beans), Onions, Tomatoes, Garlic, Ginger, Cream, Butter, Spices (like cumin, coriander, garam masala)",
    "dhokla": "Chickpea flour (besan), Yogurt, Water, Ginger, Green chilies, Baking soda, Mustard seeds, Curry leaves",
    "fried_rice": "Cooked rice, Vegetables (like carrots, peas, bell peppers), Eggs, Soy sauce, Garlic, Ginger, Green onions",
    "idli": "Rice, Lentils (black gram), Salt",
    "Jalebi": "All-purpose flour, Yogurt, Sugar, Saffron, Cardamom, Ghee or oil for frying",
    "Kaathi_rolls": "Paratha or roti, Grilled or cooked meat (chicken, lamb, beef) or paneer (Indian cottage cheese), Onions, Bell peppers, Spices (like cumin, coriander, garam masala), Mint chutney, Yogurt sauce",
    "kadai_paneer": "Paneer (Indian cottage cheese), Onions, Tomatoes, Bell peppers, Ginger, Garlic, Spices (like coriander, cumin, garam masala)",
    "kulfi": "Milk, Sugar, Cardamom, Pistachios, Almonds, Saffron",
    "masala_dosa": "Rice and lentil batter, Potatoes, Onions, Mustard seeds, Curry leaves, Turmeric, Green chilies",
    "momos": "All-purpose flour (for wrappers), Ground meat or vegetables, Garlic, Ginger, Soy sauce, Sesame oil",
    "paani_puri": "Semolina or wheat flour (for puris), Boiled potatoes, Chickpeas, Tamarind chutney, Mint-coriander chutney, Chaat masala, Spiced water (pani)",
    "pakoda": "Chickpea flour (besan), Potatoes or onions or spinach, Spices (like cumin, coriander, chili powder), Baking soda, Oil for frying",
    "pav_bhaji": "Potatoes, Tomatoes, Onions, Bell peppers, Peas, Carrots, Cauliflower, Pav (bread rolls), Butter, Spices (like cumin, coriander, garam masala)",
    "pizza": "Pizza dough (flour, yeast, water, salt), Pizza sauce (tomato sauce, herbs), Cheese (mozzarella), Toppings (like pepperoni, mushrooms, onions, bell peppers)",
    "samosa": "All-purpose flour (for pastry), Potatoes, Peas, Spices (like cumin, coriander, garam masala), Oil for frying"
    }


    predicted_class = None

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        if st.button('Predict'):
            predicted_class = predict_image(image, model, class_names)
            st.write("Predicted Food Class:", predicted_class)

    if predicted_class:
        ingredients = display_ingredients(predicted_class.lower(), dishes)
        st.write("Ingredients:", ingredients)

if __name__ == '__main__':
    main()
