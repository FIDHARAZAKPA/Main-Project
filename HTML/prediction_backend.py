from flask import Flask, render_template, request, jsonify
from prediction import predict_packaging_recommendation

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    product_name = request.form['product_name']
    product_category = request.form['product_category']
    product_weight = request.form['product_weight']

    # Call prediction function
    packaging_material_prediction, protective_tip_prediction, image_path = predict_packaging_recommendation(product_category, product_name)

    # Process prediction results as needed
    # For example, you can convert numpy arrays to lists for JSON serialization
    packaging_material_prediction = packaging_material_prediction.tolist()
    protective_tip_prediction = protective_tip_prediction.tolist()

    # Return the predicted packaging material, protective tip, and image path as JSON
    return jsonify({
        'packaging_material_prediction': packaging_material_prediction,
        'protective_tip_prediction': protective_tip_prediction,
        'image_path': image_path
    })

if __name__ == '__main__':
    app.run(debug=True)
