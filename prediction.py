import cv2
import numpy as np
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder

# Load the trained models
model_pm = load_model('packaging_material_model.keras')
model_pt = load_model('protective_tip_model.keras')

# Load the dataset to retrieve image paths
dataset = pd.read_csv('Dataset_Packaging.csv')

# Load label encoders
label_encoders = {}
for column in ['Category', 'Fragility', 'Predicted Packaging Material']:
    label_encoders[column] = LabelEncoder()
    dataset[column] = label_encoders[column].fit_transform(dataset[column])

# Material composition keywords
material_keywords = {
    "Metal": ["metal", "aluminum", "steel", "iron"],
    "Plastic": ["plastic", "polyethylene", "polypropylene", "PVC"],
    "Glass": ["glass", "crystal", "transparent"],
    "Ceramics": ["ceramic", "porcelain", "earthenware"],
    "Wood": ["wood", "timber", "plywood", "hardwood"],
    # Add more material keywords as needed
}


# Function to extract material composition keywords from product name
def get_material_composition(product_name):
    extracted_materials = []
    for material, keywords in material_keywords.items():
        for keyword in keywords:
            if keyword.lower() in product_name.lower():
                extracted_materials.append(material)
                break
    return extracted_materials if extracted_materials else ["Unknown"]

# Function to determine fragility level based on category and material composition
def determine_fragility(category, material_composition):
    # Define fragility mapping based on category and material composition
    fragility_mapping = {
        "Electronics": ["Aluminum", "Plastic", "Glass", "Metal"],
        "Clothing and Textiles": ["Cotton", "Polyester", "Rayon", "Denim (cotton)", "Silk",
                                  "Chiffon", "Leather", "Wool", "Acrylic", "Cashmere", "Linen", "Nylon", "Spandex",
                                  "Fleece", "Down", "Modal"],
        "Books and Stationery": ["Paper", "Cardboard", "Leather", "Plastic", "Metal", "Ink", "Adhesive", "Rubber",
                                 "Wood"],
        "Toys and Games": ["Plastic", "Rubber", "Fabric", "Cardboard", "Paper", "Metal", "Wood"],
        "Home Appliances": ["Metal", "Plastic", "Ceramic", "Glass"],
        "Sports Equipment": ["Plastic", "Metal", "Rubber", "Synthetic leather", "Fabric", "Foam", "Wood", "Paper",
                             "Digital", "Glass"],
        "Cosmetics and Toiletries": ["Water", "Surfactants", "Conditioning agents", "Fragrance", "Wax", "Oils",
                                     "Pigments", "Emollients",
                                     "Alcohol", "Fragrance oils", "Humectants", "Preservatives",
                                     "Electrical components", "Clays", "Active ingredients", "UV filters",
                                     "Occlusives", "Exfoliants", "Salts", "Baking soda", "Citric acid",
                                     "Colorants", "Binders", "Butters", "Polymers", "Solvents",
                                     "Abrasive material", "Handle", "Sponge", "Silicone", "Adhesive material",
                                     "Transfer film", "Design", "Synthetic bristles"],
        "Furniture": ["Wood", "Metal", "Plastic", "Fabric", "Foam", "Glass", "Stone"],
        
        "Medical Equipment": ["Metal", "Plastic", "Glass", "Stainless steel", "Rubber", "Mercury",
                              "Digital components",
                              "Nylon", "Leather", "Phosphor bronze", "Bacteria culture", "Wood"]
    }

    if category in fragility_mapping:
        if any(material in fragility_mapping[category] for material in material_composition):
            return "Moderately Fragile" if category == "Fragile" else "Highly Fragile"
        else:
            return "Not Fragile"
    else:
        return "Moderately Fragile"  # Default to Moderately Fragile if category not found



# Function to preprocess images
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    # Perform preprocessing steps here if needed
    return image

# Function to retrieve image path based on predicted packaging material
def get_image_path(packaging_material_prediction):
    predicted_class_index = np.argmax(packaging_material_prediction)
    predicted_material = label_encoders['Predicted Packaging Material'].inverse_transform([predicted_class_index])[0]
    
    # Debugging: Print predicted material
    print("Predicted Material:", predicted_material)
    
    # Find image path in dataset
    try:
        image_path = dataset.loc[dataset['Predicted Packaging Material'] == predicted_material, 'Image Paths'].values[0]
        return image_path
    except IndexError:
        print("No image path found for predicted material:", predicted_material)
        return None


# Function to display predicted image
def display_predicted_image(image_path):
    if image_path:
        image = cv2.imread(image_path)
        cv2.imshow('Predicted Packaging Material', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image path is None.")


# Function to predict packaging recommendation
def predict_packaging_recommendation(category, product_name):
    material_composition = get_material_composition(product_name)
    fragility = determine_fragility(category, material_composition)
    
    category_encoded = label_encoders['Category'].transform([category])[0]
    fragility_encoded = label_encoders['Fragility'].transform([fragility])[0]
    
    input_data = np.array([[category_encoded, fragility_encoded]])
    
    packaging_material_prediction = model_pm.predict(input_data)
    protective_tip_prediction = model_pt.predict(input_data)
    
    # Get the image path for the predicted packaging material
    image_path = get_image_path(packaging_material_prediction)
    
    # Display the predicted image
    display_predicted_image(image_path)
    
    # Return the predictions and image path
    return packaging_material_prediction, protective_tip_prediction, image_path



# Handle user input for product category and name
category = input("Enter the product category: ")
product_name = input("Enter the product name: ")

# Call the function with user inputs
packaging_material_prediction, protective_tip_prediction, image_path = predict_packaging_recommendation(category, product_name)
print("Predicted Packaging Material:", packaging_material_prediction)
print("Predicted Protective Packaging Tip:", protective_tip_prediction)