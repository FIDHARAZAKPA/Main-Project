import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout
import pandas as pd

# Load and preprocess your dataset
dataset = pd.read_csv('Dataset_PackagingProduct.csv')

# Encode categorical variables
label_encoders = {}
for column in ['Category', 'Fragility', 'Weight Category', 'Predicted Packaging Material', 'Protective Packaging Tip']:
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
model_pm.fit(X_train_pm, y_train_pm, epochs=50, batch_size=32, validation_data=(X_val_pm, y_val_pm))

# Evaluate packaging material prediction model
loss_pm, accuracy_pm = model_pm.evaluate(X_val_pm, y_val_pm)
print("Packaging Material Prediction Validation Accuracy:", accuracy_pm)

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
model_pt.fit(X_train_pt, y_train_pt, epochs=50, batch_size=32, validation_data=(X_val_pt, y_val_pt))

# Evaluate protective tip prediction model
loss_pt, accuracy_pt = model_pt.evaluate(X_val_pt, y_val_pt)
print("Protective Tip Prediction Validation Accuracy:", accuracy_pt)

# After training and evaluation

# Save the models in the native Keras format
model_pm.save('packaging_material_model.keras')
model_pt.save('protective_tip_model.keras')

print("Models saved successfully.")

