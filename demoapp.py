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
    confidence = np.max(prediction)
    return predicted_class_name if confidence >= 0.5 else None, confidence

# Function to display ingredients and nutrition info
def display_info(predicted_class, dishes):
    info = dishes.get(predicted_class.lower(), None)
    if info:
        ingredients, nutrition_info = info['ingredients'], info['nutrition_info']
        return ingredients, nutrition_info
    else:
        return None, None

# Streamlit app layout
def main():
    st.title('Food Vision System')
    st.sidebar.title('Upload Image')

    uploaded_image = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    model = load_model()
    class_names = ['burger', 'butter_naan', 'chai', 'chapati', 'chole_bhature', 'dal_makhani', 'dhokla', 'fried_rice', 'idli', 'Jalebi', 'Kaathi_rolls', 'kadai_paneer', 'kulfi', 'masala_dosa', 'momos', 'paani_puri', 'pakoda', 'pav_bhaji', 'pizza', 'samosa']
    
    dishes = {
    "burger": {
        "ingredients": "Ground beef or meat alternative, Burger buns, Lettuce, Tomato slices, Onion slices, Pickles, Cheese slices, Ketchup, Mustard, Mayonnaise",
        "nutrition_info": "Calories: 300, Protein: 20g, Fat: 15g, Carbs: 25g"
    },
    "butter_naan": {
        "ingredients": "All-purpose flour, Yeast, Yogurt, Butter, Salt, Sugar, Baking powder",
        "nutrition_info": "Calories: 250, Protein: 10g, Fat: 8g, Carbs: 35g"
    },
    "chai": {
        "ingredients": "Tea leaves or tea bags, Water, Milk, Sugar, Spices (like cardamom, cinnamon, ginger)",
        "nutrition_info": "Calories: 100, Protein: 5g, Fat: 3g, Carbs: 15g"
    },
    "chapati": {
        "ingredients": "Whole wheat flour, Water, Salt",
        "nutrition_info": "Calories: 150, Protein: 5g, Fat: 2g, Carbs: 30g"
    },
    "chole_bhature": {
        "ingredients": "Chickpeas, Onions, Tomatoes, Ginger, Garlic, Spices (like cumin, coriander, turmeric), All-purpose flour, Yogurt, Baking powder, Salt, Oil for frying",
        "nutrition_info": "Calories: 400, Protein: 12g, Fat: 18g, Carbs: 45g"
    },
    "dal_makhani": {
        "ingredients": "Lentils (black gram and kidney beans), Onions, Tomatoes, Garlic, Ginger, Cream, Butter, Spices (like cumin, coriander, garam masala)",
        "nutrition_info": "Calories: 350, Protein: 15g, Fat: 10g, Carbs: 40g"
    },
    "dhokla": {
        "ingredients": "Chickpea flour (besan), Yogurt, Water, Ginger, Green chilies, Baking soda, Mustard seeds, Curry leaves",
        "nutrition_info": "Calories: 200, Protein: 8g, Fat: 5g, Carbs: 30g"
    },
    "fried_rice": {
        "ingredients": "Cooked rice, Vegetables (like carrots, peas, bell peppers), Eggs, Soy sauce, Garlic, Ginger, Green onions",
        "nutrition_info": "Calories: 350, Protein: 10g, Fat: 8g, Carbs: 50g"
    },
    "idli": {
        "ingredients": "Rice, Lentils (black gram), Salt",
        "nutrition_info": "Calories: 100, Protein: 5g, Fat: 1g, Carbs: 20g"
    },
    "Jalebi": {
        "ingredients": "All-purpose flour, Yogurt, Sugar, Saffron, Cardamom, Ghee or oil for frying",
        "nutrition_info": "Calories: 250, Protein: 5g, Fat: 10g, Carbs: 40g"
    },
    "Kaathi_rolls": {
        "ingredients": "Paratha or roti, Grilled or cooked meat (chicken, lamb, beef) or paneer (Indian cottage cheese), Onions, Bell peppers, Spices (like cumin, coriander, garam masala), Mint chutney, Yogurt sauce",
        "nutrition_info": "Calories: 400, Protein: 15g, Fat: 12g, Carbs: 30g"
    },
    "kadai_paneer": {
        "ingredients": "Paneer (Indian cottage cheese), Onions, Tomatoes, Bell peppers, Ginger, Garlic, Spices (like coriander, cumin, garam masala)",
        "nutrition_info": "Calories: 300, Protein: 18g, Fat: 15g, Carbs: 20g"
    },
    "kulfi": {
        "ingredients": "Milk, Sugar, Cardamom, Pistachios, Almonds, Saffron",
        "nutrition_info": "Calories: 200, Protein: 6g, Fat: 10g, Carbs: 25g"
    },
    "masala_dosa": {
        "ingredients": "Rice and lentil batter, Potatoes, Onions, Mustard seeds, Curry leaves, Turmeric, Green chilies",
        "nutrition_info": "Calories: 300, Protein: 8g, Fat: 5g, Carbs: 40g"
    },
    "momos": {
        "ingredients": "All-purpose flour (for wrappers), Ground meat or vegetables, Garlic, Ginger, Soy sauce, Sesame oil",
        "nutrition_info": "Calories: 150, Protein: 7g, Fat: 5g, Carbs: 20g"
    },
    "paani_puri": {
        "ingredients": "Semolina or wheat flour (for puris), Boiled potatoes, Chickpeas, Tamarind chutney, Mint-coriander chutney, Chaat masala, Spiced water (pani)",
        "nutrition_info": "Calories: 100, Protein: 3g, Fat: 1g, Carbs: 15g"
    },
    "pakoda": {
        "ingredients": "Chickpea flour (besan), Potatoes or onions or spinach, Spices (like cumin, coriander, chili powder), Baking soda, Oil for frying",
        "nutrition_info": "Calories: 200, Protein: 5g, Fat: 10g, Carbs: 25g"
    },
    "pav_bhaji": {
        "ingredients": "Potatoes, Tomatoes, Onions, Bell peppers, Peas, Carrots, Cauliflower, Pav (bread rolls), Butter, Spices (like cumin, coriander, garam masala)",
        "nutrition_info": "Calories: 350, Protein: 8g, Fat: 10g, Carbs: 45g"
    },
    "pizza": {
        "ingredients": "Pizza dough (flour, yeast, water, salt), Pizza sauce (tomato sauce, herbs), Cheese (mozzarella), Toppings (like pepperoni, mushrooms, onions, bell peppers)",
        "nutrition_info": "Calories: 300, Protein: 12g, Fat: 15g, Carbs: 35g"
    },
    "samosa": {
        "ingredients": "All-purpose flour (for pastry), Potatoes, Peas, Spices (like cumin, coriander, garam masala), Oil for frying",
        "nutrition_info": "Calories: 200, Protein: 5g, Fat: 10g, Carbs: 20g"
    }
}


    predicted_class = None

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        if st.button('Predict'):
            predicted_class, confidence = predict_image(image, model, class_names)
            if confidence < 0.5:
                st.write("This item can't be predicted.")
            else:
                st.write("Predicted Food Class:", predicted_class)

    if predicted_class:
        if predicted_class.lower() in class_names:
            ingredients, nutrition_info = display_info(predicted_class.lower(), dishes)
            if ingredients and nutrition_info:
                st.write("Ingredients:", ingredients)
                st.write("Nutrition Info:", nutrition_info)

if __name__ == '__main__':
    main()
