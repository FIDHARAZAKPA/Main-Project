import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout
import os

# Material composition keywords
material_keywords = {
    "Metal": ["metal", "aluminum", "steel", "iron"],
    "Plastic": ["plastic", "polyethylene", "polypropylene", "PVC"],
    "Glass": ["glass", "crystal", "transparent"],
    "Ceramics": ["ceramic", "porcelain", "earthenware"],
    "Wood": ["wood", "timber", "plywood", "hardwood"],
    # Add more material keywords as needed
}

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

    # Determine fragility level based on category and material composition
    if category in fragility_mapping:
        if any(material in fragility_mapping[category] for material in material_composition):
            return "Moderately Fragile" if category == "Fragile" else "Highly Fragile"
        else:
            return "Not Fragile"
    else:
        return "Moderately Fragile"  # Default to Moderately Fragile if category not found


# Function to append material composition keywords to the product name
def append_material_keywords(product_name, material_composition):
    appended_name = product_name
    for material in material_composition:
        keywords = material_keywords.get(material, [])
        if keywords:
            appended_name += " " + " ".join(keywords)
    return appended_name

# Function to get material composition from product name
def get_material_composition(product_name):
    extracted_materials = []
    for material, keywords in material_keywords.items():
        for keyword in keywords:
            if keyword.lower() in product_name.lower():
                extracted_materials.append(material)
                break
    return extracted_materials if extracted_materials else ["Unknown"]

# Load the dataset
dataset_filename = 'Dataset_Packaging.csv'
dataset = pd.read_csv(dataset_filename)

# Perform data exploration and analysis
print("Dataset Information:")
print(dataset.info())

print("\nDescriptive Statistics:")
print(dataset.describe())

print("\nValue Counts for Categorical Variables:")
for column in dataset.select_dtypes(include=['object']).columns:
    print("\n" + column + ":\n", dataset[column].value_counts())

# Encode categorical variables
label_encoders = {}
categorical_columns = ['Category', 'Fragility', 'Material Composition', 'Predicted Packaging Material',
                       'Protective Packaging Tip']
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    dataset[column] = label_encoders[column].fit_transform(dataset[column])

# Split dataset into features and target variables
X = dataset[['Category', 'Fragility']]
y_packaging_material = dataset['Predicted Packaging Material']
y_protective_tip = dataset['Protective Packaging Tip']


# Split data into training and validation sets for packaging material prediction
X_train_pm, X_val_pm, y_train_pm, y_val_pm = train_test_split(X, y_packaging_material, test_size=0.2, random_state=42)

# Split data into training and validation sets for protective tip prediction
X_train_pt, X_val_pt, y_train_pt, y_val_pt = train_test_split(X, y_protective_tip, test_size=0.2, random_state=42)

# Define neural network model for packaging material prediction
model_pm = Sequential()
model_pm.add(Dense(64, activation='relu'))
model_pm.add(Dropout(0.5))
model_pm.add(Dense(32, activation='relu'))
model_pm.add(Dropout(0.5))
model_pm.add(Dense(len(np.unique(y_packaging_material)), activation='softmax'))

# Compile the packaging material prediction model
model_pm.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the packaging material prediction model
model_pm.fit(X_train_pm, y_train_pm, epochs=100, batch_size=32, validation_data=(X_val_pm, y_val_pm))

# Evaluate packaging material prediction model
loss_pm, accuracy_pm = model_pm.evaluate(X_val_pm, y_val_pm)
print("\nPackaging Material Prediction Validation Accuracy:", accuracy_pm)

# Define neural network model for protective tip prediction
model_pt = Sequential()
model_pt.add(Dense(64, activation='relu'))
model_pt.add(Dropout(0.5))
model_pt.add(Dense(32, activation='relu'))
model_pt.add(Dropout(0.5))
model_pt.add(Dense(len(np.unique(y_protective_tip)), activation='softmax'))

# Compile the protective tip prediction model
model_pt.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the protective tip prediction model
model_pt.fit(X_train_pt, y_train_pt, epochs=100, batch_size=32, validation_data=(X_val_pt, y_val_pt))

# Evaluate protective tip prediction model
loss_pt, accuracy_pt = model_pt.evaluate(X_val_pt, y_val_pt)
print("\nProtective Tip Prediction Validation Accuracy:", accuracy_pt)

# Save the models in the native Keras format
model_pm_filename = 'packaging_material_model.keras'
model_pt_filename = 'protective_tip_model.keras'
model_pm.save(model_pm_filename)
model_pt.save(model_pt_filename)

# Check if models are saved successfully
if os.path.exists(model_pm_filename) and os.path.exists(model_pt_filename):
    print("\nModels saved successfully.")
else:
    print("\nError: Failed to save models.")
