import random
import csv
import cv2
import os

# Function to load image using OpenCV
def load_image_opencv(image_path):
    image = cv2.imread(image_path)
    return image

# Define your image folder path
image_folder = "C:\\Users\\fidha\\OneDrive\\Desktop\\LOGISTICS\\logistica-1.0.0\\Evaluation and analysis of Logistics and Packaging\\material_images"


# Example image paths corresponding to packaging materials
packaging_material_images = {
    "Cardboard boxes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Cardboard boxes\Image_1.jpg", 
    "Bubble wrap":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Bubble wrap\Image_1.jpg",
    "Foam padding":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Foam padding\Image_1.jpg",
    "Air pillows":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Air pillows\Image_1.jpg",
    "Packing peanuts":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Packing peanuts\Image_1.jpg",
    "Corrugated mailers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corrugated mailers\Image_1.jpg", 
    "Shipping envelopes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Shipping envelopes\Image_1.jpg", 
    "Kraft paper":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Kraft paper\Image_1.jpg", 
    "Plastic wrap":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Plastic wrap\Image_1.jpeg", 
    "Packing tape":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Packing tape\Image_1.JPG",
    "Packaging tape dispenser":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Packaging tape dispenser\Image_1.jpg", 
    "Stretch wrap":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Stretch wrap\Image_1.jpg", 
    "Anti-static packaging materials":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Anti-static packaging materials\Image_1.jpg", 
    "Foam pouches":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Foam pouches\Image_1.jpg",
    "Cardboard dividers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Cardboard dividers\Image_1.jpg", 
    "Polyethylene bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Polyethylene bags\Image_1.jpg", 
    "Shrink wrap":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Shrink wrap\Image_1.jpg", 
    "Corrugated rolls":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corrugated rolls\Image_1.jpg",
    "Mailing tubes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Mailing tubes\Image_1.jpg", 
    "Strapping materials":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Strapping materials\Image_1.png", 
    "Dunnage bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Dunnage bags\Image_1.jpg", 
    "Tyvek envelopes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Tyvek envelopes\Image_1.jpg", 
    "Molded pulp trays":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Molded pulp trays\Image_1.png",
    "Corrugated corner protectors":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corrugated corner protectors\Image_1.jpg", 
    "Padded mailers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Padded mailers\Image_1.jpg",
    "Void fillers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Void fillers\Image_1.jpg", 
    "Paperboard cartons":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Paperboard cartons\Image_1.jpg", 
    "Biodegradable packaging materials":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Biodegradable packaging materials\Image_1.jpg", 
    "Eco-friendly packaging materials":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Eco-friendly packaging materials\Image_1.jpg", 
    "VCI bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\VCI bags\Image_1.jpg",
    "Jiffy bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Jiffy bags\Image_1.jpg", 
    "Composite containers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Composite containers\Image_1.jpeg", 
    "Reusable packaging materials":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Reusable packaging materials\Image_1.jpg", 
    "Thermal insulation packaging":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Thermal insulation packaging\Image_1.png",
    "Vacuum packaging materials":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Vacuum packaging materials\Image_1.jpg", 
    "Moisture barrier bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Moisture barrier bags\Image_1.jpg", 
    "Static shielding bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Static shielding bags\Image_1.jpg",
    "Corrugated plastic sheets":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corrugated plastic sheets\Image_1.jpg",
    "Wooden crates":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Wooden crates\Image_1.jpg", 
    "Metal shipping containers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Metal shipping containers\Image_1.jpg", 
    "Composite strapping":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Composite strapping\Image_1.jpg", 
    "Molded fiber packaging":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Molded fiber packaging\Image_1.jpg",
    "Polypropylene straps":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Polypropylene straps\Image_1.png", 
    "Kraft tubes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Kraft tubes\Image_1.jpg", 
    "Paper cushioning":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Paper cushioning\Image_1.jpg", 
    "PLA packaging":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\PLA packaging\Image_1.png", 
    "Bio-based foam":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Bio-based foam\Image_1.jpg",
    "Anti-tamper packaging":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Anti-tamper packaging\Image_1.jpg", 
    "Hazardous materials packaging":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Hazardous materials packaging\Image_1.jpeg",
    "Tyvek rolls":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Tyvek rolls\Image_1.jpg", 
    "Kraft mailers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Kraft mailers\Image_1.jpg", 
    "Biodegradable bubble wrap":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Biodegradable bubble wrap\Image_1.jpg", 
    "Air cushion machines":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Air cushion machines\Image_1.jpg", 
    "Ziplock bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Ziplock bags\Image_1.jpg",
    "Corrugated plastic mailers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corrugated plastic mailers\Image_1.jpg", 
    "Composite packaging tape":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Composite packaging tape\Image_1.jpg", 
    "Security seals":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Security seals\Image_1.jpg", 
    "Corrugated cardboard sheets":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corrugated cardboard sheets\Image_1.jpg", 
    "Dunnage air bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Dunnage air bags\Image_1.jpg", 
    "Foam corner protectors":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Foam corner protectors\Image_1.jpg", 
    "Gel packs":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Gel packs\Image_1.jpg", 
    "Tamper-evident packaging":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Tamper-evident packaging\Image_1.jpg", 
    "Pallet wrap dispenser":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Pallet wrap dispenser\Image_1.jpg",
    "Vacuum sealing bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Vacuum sealing bags\Image_1.jpeg", 
    "Silica gel packets":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Silica gel packets\Image_1.jpg", 
    "ESD bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\ESD bags\Image_1.jpg", 
    "Water-activated tape":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Water-activated tape\Image_1.jpg", 
    "Honeycomb cardboard":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Honeycomb cardboard\Image_1.jpg",
    "Thermal shipping labels":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Thermal shipping labels\Image_1.JPG", 
    "Insulated shipping containers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Insulated shipping containers\Image_1.jpg", 
    "Molded pulp clamshells":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Molded pulp clamshells\Image_1.jpg", 
    "Retail packaging boxes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Retail packaging boxes\Image_1.jpg",
    "Anti-static bubble wrap":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Anti-static bubble wrap\Image_1.jpg", 
    "Pallet covers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Pallet covers\Image_1.png", 
    "Foam sheets":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Foam sheets\Image_1.jpg", 
    "Corrugated plastic totes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corrugated plastic totes\Image_1.jpg", 
    "Steel banding":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Steel banding\Image_1.jpg",
    "Collapsible crates":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Collapsible crates\Image_1.jpg", 
    "Barrier films":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Barrier films\Image_1.png", 
    "Composite foam panels":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Composite foam panels\Image_1.jpg", 
    "Custom-printed packaging tape":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Custom-printed packaging tape\Image_1.png", 
    "Bulk bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Bulk bags\Image_1.jpg",
    "Dunnage trays":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Dunnage trays\Image_1.png", 
    "Plastic strapping kits":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Plastic strapping kits\Image_1.jpg", 
    "Hazard labels":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Hazard labels\Image_1.jpg", 
    "Fiber drums":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Fiber drums\Image_1.jpg", 
    "Absorbent pads":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Absorbent pads\Image_1.png",
    "Composite shipping tubes":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Composite shipping tubes\Image_1.jpg", 
    "Molded pulp inserts":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Molded pulp inserts\Image_1.png", 
    "Polyethylene foam rolls":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Polyethylene foam rolls\Image_1.jpg", 
    "Shrink bands":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Shrink bands\Image_1.jpg", 
    "Security bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Security bags\Image_1.jpg",
    "Pulp bottle trays":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Pulp bottle trays\Image_1.jpg", 
    "Polypropylene woven bags":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Polypropylene woven bags\Image_1.jpg", 
    "Tensioners and sealers":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Tensioners and sealers\Image_1.png", 
    "Desiccant packets":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Desiccant packets\Image_1.jpg", 
    "Cardboard display stands":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Cardboard display stands\Image_1.jpg",
    "Plastic pallets":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Plastic pallets\Image_1.png", 
    "Corner boards":r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Corner boards\Image_1.jpg"
    }


# List of packaging materials
packaging_materials = [
    "Cardboard boxes", "Bubble wrap", "Foam padding", "Air pillows", "Packing peanuts",
    "Corrugated mailers", "Shipping envelopes", "Kraft paper", "Plastic wrap", "Packing tape",
    "Packaging tape dispenser", "Stretch wrap", "Anti-static packaging materials", "Foam pouches",
    "Cardboard dividers", "Polyethylene bags", "Shrink wrap", "Corrugated rolls", "Edge protectors",
    "Mailing tubes", "Strapping materials", "Dunnage bags", "Tyvek envelopes", "Molded pulp trays",
    "Corrugated corner protectors", "Padded mailers", "Void fillers", "Paperboard cartons", 
    "Biodegradable packaging materials", "Eco-friendly packaging materials", "VCI bags",
    "Jiffy bags", "Composite containers", "Reusable packaging materials", "Thermal insulation packaging",
    "Vacuum packaging materials", "Moisture barrier bags", "Static shielding bags", "Corrugated plastic sheets",
    "Wooden crates", "Metal shipping containers", "Composite strapping", "Molded fiber packaging",
    "Polypropylene straps", "Kraft tubes", "Paper cushioning", "PLA packaging", "Bio-based foam",
    "Anti-tamper packaging", "Hazardous materials packaging","Tyvek rolls", "Kraft mailers", "Biodegradable bubble wrap", "Air cushion machines", "Ziplock bags",
    "Corrugated plastic mailers", "Composite packaging tape", "Security seals", "Corrugated cardboard sheets", 
    "Dunnage air bags", "Foam corner protectors", "Gel packs", "Tamper-evident packaging", "Pallet wrap dispenser",
    "Vacuum sealing bags", "Silica gel packets", "ESD bags", "Water-activated tape", "Honeycomb cardboard",
    "Thermal shipping labels", "Insulated shipping containers", "Molded pulp clamshells", "Retail packaging boxes",
    "Anti-static bubble wrap", "Pallet covers", "Foam sheets", "Corrugated plastic totes", "Steel banding",
    "Collapsible crates", "Barrier films", "Composite foam panels", "Custom-printed packaging tape", "Bulk bags",
    "Dunnage trays", "Plastic strapping kits", "Hazard labels", "Fiber drums", "Absorbent pads",
    "Composite shipping tubes", "Molded pulp inserts", "Polyethylene foam rolls", "Shrink bands", "Security bags",
    "Pulp bottle trays", "Polypropylene woven bags", "Tensioners and sealers", "Desiccant packets", "Cardboard display stands",
    "Plastic pallets", "Corner boards"
]

# Define Fragility Levels
fragility_levels = {
    "Not Fragile": (0, 5),      # Weight range for not fragile products
    "Moderately Fragile": (5, 10),  # Weight range for moderately fragile products
    "Highly Fragile": (10, float('inf'))  # Weight range for highly fragile products
} 

# Define Weight Categories
def categorize_weight(weight):
    for fragility, (lower, upper) in fragility_levels.items():
        if lower <= weight < upper:
            return fragility

# Function to generate protective packaging tips
def generate_protective_packaging_tip(product):
    fragility = product["Fragility"]
    weight_category = product["Weight Category"]
    if fragility == "Not Fragile":
        if weight_category == "Not Fragile":
            return "Products in this category are not very fragile and can be packed in standard cardboard boxes."
        elif weight_category == "Moderately Fragile":
            return "Although not very fragile, products in this category might require additional padding such as bubble wrap."
        elif weight_category == "Highly Fragile":
            return "While these products are not extremely fragile, it's recommended to use extra padding and cushioning materials like foam padding or air pillows."
    elif fragility == "Moderately Fragile":
        if weight_category == "Not Fragile":
            return "While moderately fragile, products in this category can be packed in standard cardboard boxes with some added protection like foam padding or air pillows."
        elif weight_category == "Moderately Fragile":
            return "Products in this category are moderately fragile and require adequate protection with materials like bubble wrap or foam padding."
        elif weight_category == "Highly Fragile":
            return "These products are moderately fragile but leaning towards highly fragile. It's recommended to use substantial padding and cushioning materials to prevent damage during transit."
    elif fragility == "Highly Fragile":
        if weight_category == "Not Fragile":
            return "Highly fragile products should be handled with extreme care during packaging. Consider using sturdy boxes with ample cushioning materials like bubble wrap or foam padding."
        elif weight_category == "Moderately Fragile":
            return "Although not the most fragile, products in this category require special attention during packaging. Ensure to use strong boxes and plenty of cushioning materials."
        elif weight_category == "Highly Fragile":
            return "Products in this category are highly fragile and require the utmost care during packaging. Use multiple layers of padding and consider double boxing for added protection."


# Function to determine Packaging Material based on fragility and other criteria
def determine_packaging_material(product):
    fragility = product["Fragility"]
    # Logic to determine packaging material based on fragility and other criteria
    # You would replace this logic with your specific criteria
    if fragility == "Highly Fragile":
        return "Bubble wrap", "Foam padding", "Air pillows", "Packing peanuts", "Foam pouches", "Edge protectors"
    elif fragility == "Moderately Fragile":
        return "Corrugated mailers", "Corrugated plastic sheets","Molded fiber packaging","Paper cushioning", "Biodegradable bubble wrap", "Foam sheets", "Composite foam panels","Polyethylene foam rolls"
    else:
        return "Cardboard boxes", "Shipping envelopes", "Plastic wrap", "Stretch wrap","Polyethylene bags", "Mailing tubes", "PLA packaging","Strapping materials", "Tyvek envelopes","Corrugated plastic mailers", "Ziplock bags"



def determine_fragility(product_category, material_composition):
    fragility_mapping = {
        "Electronics": {
            "Fragile Materials": ["Glass", "Thin plastic"],
            "Moderate Materials": ["Metal", "Thick plastic"],
            "Fragility Level": "Moderately Fragile"
        },
        "Clothing and Textiles": {
            "Fragile Materials": [],
            "Moderate Materials": ["Fabric", "Cotton", "Polyester"],
            "Fragility Level": "Not Fragile"
        },
        "Books and Stationery": {
            "Fragile Materials": [],
            "Moderate Materials": ["Paper"],
            "Fragility Level": "Not Fragile"
        },
        "Toys and Games": {
            "Fragile Materials": ["Plastic"],
            "Moderate Materials": ["Wood"],
            "Fragility Level": "Moderately Fragile"
        },
        "Home Appliances": {
            "Fragile Materials": ["Glass", "Thin plastic"],
            "Moderate Materials": ["Metal", "Thick plastic"],
            "Fragility Level": "Moderately Fragile"
        },
        "Sports Equipment": {
            "Fragile Materials": [],
            "Moderate Materials": ["Metal", "Rubber"],
            "Fragility Level": "Moderately Fragile"
        },
        "Cosmetics and Toiletries": {
            "Fragile Materials": ["Glass", "Thin plastic"],
            "Moderate Materials": ["Thick plastic"],
            "Fragility Level": "Moderately Fragile"
        },
        "Furniture": {
            "Fragile Materials": ["Glass"],
            "Moderate Materials": ["Wood", "Metal", "Fabric"],
            "Fragility Level": "Moderately Fragile"
        },
        "Food and Beverages": {
            "Fragile Materials": [],
            "Moderate Materials": ["Packaging"],
            "Fragility Level": "Not Fragile"
        },
        "Medical Equipment": {
            "Fragile Materials": ["Glass", "Thin plastic"],
            "Moderate Materials": ["Metal", "Thick plastic"],
            "Fragility Level": "Highly Fragile"
        }
    }
    
    category_mapping = fragility_mapping.get(product_category, {})
    if not category_mapping:
        return "Moderately Fragile"  # Default to Moderately Fragile if category not found
    
    if material_composition in category_mapping["Fragile Materials"]:
        return "Highly Fragile"
    elif material_composition in category_mapping["Moderate Materials"]:
        return "Moderately Fragile"
    else:
        return category_mapping["Fragility Level"]


def get_material_composition(product_name):
    # Placeholder function for material composition extraction using keyword extraction
    # You'll need to customize this based on your dataset and material composition indicators
    
    material_keywords = ["metal", "plastic", "cotton", "wood", "glass", "leather", "ceramic", "rubber"]
    
    # Check if any material keywords are present in the product name
    extracted_materials = [material for material in material_keywords if material in product_name.lower()]
    
    if extracted_materials:
        return ", ".join(extracted_materials)  # Return a comma-separated list of extracted materials
    else:
        return "Unknown"


# Define categories and corresponding products
category_to_products = {
    "Electronics":  [
        "Laptop", "Smartphone", "Tablet", "Headphones", "Camera", "Smartwatch", "Printer", "Keyboard", "Mouse", 
        "Monitor", "Speaker system", "External hard drive", "Graphics tablet", "Wireless charger", "Action camera", 
        "Drone", "Gaming console", "Virtual reality headset", "Fitness tracker", "Digital camera", "E-reader", 
        "Portable power bank", "USB flash drive", "Bluetooth earbuds", "Microphone", "Projector", "Webcam", 
        "Solar charger", "GPS device", "LED flashlight", "CCTV camera", "Barcode scanner", "Satellite phone", 
        "Wireless presenter", "Voice recorder", "Calculator", "Electric toothbrush", "Hair straightener", 
        "Air purifier", "Humidifier", "Robot vacuum cleaner", "Bluetooth speaker", "Digital voice assistant", 
        "Car dash cam", "Electric shaver", "Portable DVD player", "Digital photo frame", "Handheld game console", 
        "Portable CD player", "Graphing calculator", "Electronic dictionary", "Wireless mouse", "Fitness smartwatch", 
        "Wi-Fi range extender", "Mini projector", "Bluetooth keyboard", "External DVD drive", "Flashlight", 
        "USB hub", "Action camera accessories", "Screen protector", "Gaming headset", "Wireless charging pad", 
        "Bluetooth FM transmitter", "Dash cam accessories", "Laptop cooling pad", "Wireless remote control", 
        "USB microphone", "Smartphone tripod", "USB fan", "External SSD", "Graphics card", "Wireless earphones", 
        "Wireless router", "Portable scanner", "Digital voice recorder", "USB-C hub", "Bluetooth receiver", 
        "VR headset accessories", "Wireless barcode scanner", "Solar power bank", "MicroSD card", "Smart glasses", 
        "Wireless presenter remote", "USB LED light", "Bluetooth gamepad", "Mini keyboard", "Portable keyboard",
        "USB fingerprint reader", "Bluetooth speakerphone", "Wireless charging stand", "Smartphone gimbal", 
        "External monitor stand", "Wireless presenter pen", "Portable power station", "Wireless presenter clicker", 
        "USB desk fan", "Bluetooth stylus pen", "Wireless charging mat"
    ],
    "Clothing and Textiles": [
        "T-shirt", "Jeans", "Dress", "Jacket", "Sweater", "Skirt", "Blouse", "Coat", "Pants", "Shirt", 
        "Shorts", "Suit", "Scarf", "Socks", "Leggings", "Hoodie", "Vest", "Cardigan", "Tie", "Pajamas", 
        "Underwear", "Bra", "Swimsuit", "Trench coat", "Pullover", "Tank top", "Blazer", "Sweatshirt", 
        "Windbreaker", "Parka", "Poncho", "Gloves", "Hat", "Beanie", "Cap", "Beret", "Headband", "Bow tie", 
        "Belt", "Tights", "Shawl", "Waistcoat", "Thermal underwear", "Jumpsuit", "Sweatpants", "Overalls", 
        "Camisole", "Kimono", "Polo shirt", "Duster coat", "Puffer jacket", "Fleece jacket", "Raincoat", 
        "Fur coat", "Motorcycle jacket", "Bomber jacket", "Peacoat", "Duffle coat", "Turtleneck", "Cape", 
        "Anorak", "Denim jacket", "Jersey", "Chinos", "Corduroy pants", "Cargo pants", "Khakis", "Slacks", 
        "Tailored trousers", "Culottes", "Gaucho pants", "Palazzo pants", "Cargo shorts", "Chino shorts", 
        "Bermuda shorts", "Board shorts", "Basketball shorts", "Cycling shorts", "Running shorts", 
        "Swim trunks", "Boxer briefs", "Bikini briefs", "Thong", "Boxer shorts", "Briefs", "Boyshorts", 
        "Long johns", "Boxer pants", "Trunks"
    ],
    "Books and Stationery": [
    "Notebook", "Pen", "Marker", "Stapler", "Scissors", "Pencil", "Eraser", "Ruler", "Glue stick", 
    "Highlighter", "Correction tape", "Tape dispenser", "Paper clips", "Binder clips", "Push pins", 
    "Thumbtacks", "Rubber bands", "Index cards", "Post-it notes", "Sticky notes", "Desk organizer", 
    "Letter tray", "File organizer", "File folder", "Binder", "Pocket folder", "Report cover", 
    "Presentation binder", "Binder dividers", "Sheet protectors", "Portfolio", "Clipboard", 
    "Document holder", "Business card holder", "Pencil case", "Pencil pouch", "Pen holder", 
    "Desk pad", "Mouse pad", "Desk calendar", "Wall calendar", "Planner", "Weekly planner", 
    "Monthly planner", "Yearly planner", "Daily planner", "Student planner", "Teacher planner", 
    "Appointment book", "Agenda", "Journal", "Diary", "Sketchbook", "Drawing pad", "Coloring book", 
    "Activity book", "Spiral notebook", "Composition notebook", "Legal pad", "Graph paper", 
    "Lined paper", "Grid paper", "Dot grid paper", "Isometric paper", "Calligraphy paper", 
    "Construction paper", "Tracing paper", "Watercolor paper", "Pastel paper", "Charcoal paper", 
    "Sketch paper", "Marker paper", "Tracing pad", "Drawing paper", "Acid-free paper", "Cardstock", 
    "Craft paper", "Origami paper", "Tissue paper", "Crepe paper", "Wrapping paper", "Gift wrap", 
    "Decorative paper", "Stationery paper", "Letter paper", "Invitation paper", "Greeting card", 
    "Thank you card", "Sympathy card", "Get well card", "Birthday card", "Anniversary card", 
    "Wedding card", "Graduation card", "Holiday card", "Christmas card", "New Year card", 
    "Valentine's Day card", "Easter card", "Mother's Day card",
        "Novel", "Textbook", "Biography", "Poetry", "Cookbook", "Self-help book", "Fantasy novel", 
        "Science fiction novel", "Mystery novel", "Romance novel", "Historical fiction", "Thriller", 
        "Young adult novel", "Drama", "Non-fiction book", "Memoir", "Autobiography", "Travel guide", 
        "Art book", "Photography book", "Children's book", "Graphic novel", "Comic book", "Reference book", 
        "Encyclopedia", "Dictionary", "Almanac", "Atlas", "Magazine", "Journal", "Newspaper", "Fairy tale", 
        "Fable", "Mythology", "Folklore", "Short stories", "Essays", "Poetry anthology", "Philosophy book", 
        "Religious text", "Spirituality book", "Self-improvement book", "Health book", "Fitness book", 
        "Diet book", "Cooking magazine", "History book", "Biographical novel", "Adventure novel", 
        "Horror novel", "Detective novel", "Crime novel", "Legal thriller", "Psychological thriller", 
        "Political thriller", "Medical thriller", "Romantic thriller", "Historical romance", "Paranormal romance", 
        "Erotic novel", "Chick lit", "True crime book", "Survival guide", "Gardening book", "DIY book", 
        "Craft book", "Knitting book", "Crochet book", "Sewing book", "Quilting book", "Woodworking book", 
        "Home improvement book", "Financial advice book", "Business book", "Marketing book", "Sales book", 
        "Leadership book", "Management book", "Economics book", "Investing book", "Accounting book", 
        "Personal finance book", "Real estate book", "Stock market book", "Computer programming book", 
        "Web development book", "Software engineering book", "Data science book", "Machine learning book", 
        "Artificial intelligence book", "Mathematics book", "Physics book", "Chemistry book", "Biology book", 
        "Geology book", "Astronomy book", "Astrophysics book", "Environmental science book", "Psychology book", 
        "Sociology book", "Anthropology book", "Political science book", "Philosophy anthology", "Ethics book"
    ],
    "Toys and Games": [
        "Action figure", "Doll", "Puzzle", "Board game", "Stuffed animal", "LEGO set", "Model car", 
        "Remote control car", "Train set", "Barbie doll", "Transformers toy", "Play-Doh set", "Hot Wheels car", 
        "Nerf gun", "Rubik's cube", "Fidget spinner", "Jigsaw puzzle", "Chess set", "Uno card game", 
        "Monopoly board game", "Play kitchen set", "Building blocks", "Toy dinosaur", "Dollhouse", 
        "Toy train", "Toy soldier", "Scooter", "Tricycle", "Balance bike", "Rocking horse", 
        "Bicycle", "Kick scooter", "Sled", "Play tent", "Toy drum set", "Toy guitar", "Toy microphone", 
        "Toy piano", "Dress-up costume", "Doctor playset", "Tool set", "Construction set", 
        "Toy kitchen appliances", "Toy cash register", "Toy vacuum cleaner", "Toy lawnmower", 
        "Toy tool bench", "Play food set", "Toy shopping cart", "Toy doctor kit", "Toy phone", 
        "Toy camera", "Toy laptop", "Art supplies set", "Craft kit", "Model airplane", "Model rocket", 
        "Remote control helicopter", "RC boat", "RC airplane", "RC truck", "RC tank", "RC robot", 
        "RC dinosaur", "RC spider", "RC snake", "RC scorpion", "RC tarantula", "RC frog", "RC lizard", 
        "RC bird", "RC fish", "RC octopus", "RC crab", "RC shrimp", "RC turtle", "RC jellyfish", 
        "RC squid", "RC whale", "RC dolphin", "RC shark", "RC seal", "RC sea lion", "RC penguin", 
        "RC polar bear", "RC walrus", "RC narwhal", "RC beluga", "RC manatee", "RC dugong", 
        "RC sea otter", "RC sea turtle", "RC manta ray", "RC stingray", "RC angelfish", "RC clownfish", 
        "RC butterflyfish", "RC parrotfish", "RC surgeonfish", "RC pufferfish", "RC triggerfish", 
        "RC lionfish", "RC grouper", "RC barracuda", "RC moray eel", "RC seahorse", "RC shrimp", 
        "RC lobster", "RC crab", "RC jellyfish", "RC octopus", "RC squid", "RC cuttlefish", "RC nautilus"
    ],
    "Home Appliances": [
        "Refrigerator", "Microwave", "Coffee maker", "Blender", "Toaster", "Food processor", "Dishwasher", 
        "Juicer", "Slow cooker", "Stand mixer", "Electric kettle", "Rice cooker", "Air fryer", "Pressure cooker", 
        "Hand mixer", "Electric grill", "Waffle maker", "Electric can opener", "Popcorn maker", "Bread maker", 
        "Ice cream maker", "Electric skillet", "Electric fondue pot", "Sous vide machine", "Espresso machine", 
        "Milk frother", "Soda maker", "Food dehydrator", "Vacuum sealer", "Water filter", "Water dispenser", 
        "Humidifier", "Dehumidifier", "Air purifier", "Space heater", "Fan", "Air conditioner", "HVAC system", 
        "Smart thermostat", "Garbage disposal", "Trash compactor", "Instant hot water dispenser", "Garage door opener", 
        "Home security system", "Smart doorbell", "Smart lock", "Smart light bulbs", "Smart plugs", "Smart switches", 
        "Smart blinds", "Smart thermostat", "Smart sprinkler system", "Smart smoke detector", "Smart carbon monoxide detector", 
        "Smart leak detector", "Smart alarm clock", "Smart vacuum cleaner", "Smart air purifier", "Smart air conditioner", 
        "Smart ceiling fan", "Smart bathroom scale", "Smart toothbrush", "Smart mirror", "Smart scale", "Smart pet feeder", 
        "Smart litter box", "Smart cat door", "Smart dog door", "Smart bird feeder", "Smart thermostat", "Smart pool controller", 
        "Smart irrigation controller", "Smart plant sensor", "Smart garden system", "Smart greenhouse", "Smart weather station", 
        "Smart camera", "Smart doorbell camera", "Smart floodlight camera", "Smart security camera", "Smart baby monitor", 
        "Smart pet camera", "Smart wildlife camera", "Smart door sensor", "Smart window sensor", "Smart motion sensor", 
        "Smart contact sensor", "Smart temperature sensor", "Smart humidity sensor", "Smart light sensor", 
        "Smart water sensor", "Smart gas sensor", "Smart carbon dioxide sensor", "Smart smoke sensor", "Smart air quality sensor"
    ],
    "Sports Equipment": [
        "Tennis racket", "Basketball", "Soccer ball", "Yoga mat", "Dumbbells", "Jump rope", "Resistance bands", 
        "Exercise ball", "Foam roller", "Balance board", "Pilates ring", "Swiss ball", "Kettlebell", 
        "Medicine ball", "Pull-up bar", "Push-up bars", "Ab roller", "Gymnastics mat", "Agility ladder", 
        "Boxing gloves", "Punching bag", "Boxing speed bag", "Boxing reflex bag", "Boxing heavy bag", 
        "Boxing stand", "Boxing focus pads", "Boxing double-end bag", "Boxing headgear", "Boxing mouthguard", 
        "Boxing groin guard", "Boxing shoes", "Boxing shorts", "Boxing robe", "Boxing hand wraps", 
        "Boxing tape", "Boxing skipping rope", "Boxing ring", "Boxing timer", "Boxing scoring machine", 
        "Boxing judge chair", "Boxing ring ropes", "Boxing ring canvas", "Boxing corner stool", 
        "Boxing corner spit bucket", "Boxing ring card girls", "Boxing ring announcer", "Boxing referee", 
        "Boxing coach", "Boxing promoter", "Boxing judge", "Boxing trainer", "Boxing cutman", "Boxing timekeeper", 
        "Boxing inspector", "Boxing matchmaker", "Boxing ring doctor", "Boxing photographer", "Boxing videographer", 
        "Boxing journalist", "Boxing commentator", "Boxing analyst", "Boxing broadcaster", "Boxing historian", 
        "Boxing statistician", "Boxing artist", "Boxing collector", "Boxing fan", "Boxing memorabilia", 
        "Boxing autograph", "Boxing ticket", "Boxing program", "Boxing poster", "Boxing magazine", 
        "Boxing book", "Boxing movie", "Boxing documentary", "Boxing video game", "Boxing trading card", 
        "Boxing action figure", "Boxing glove keychain", "Boxing glove air freshener", "Boxing glove stress ball", 
        "Boxing glove pencil topper", "Boxing glove mug", "Boxing glove coasters", "Boxing glove plush toy", 
        "Boxing glove backpack", "Boxing glove luggage tag", "Boxing glove sticker", "Boxing glove decal", 
        "Boxing glove poster", "Boxing glove banner", "Boxing glove flag", "Boxing glove pennant", 
        "Boxing glove bobblehead", "Boxing glove ornament", "Boxing glove cookie cutter", "Boxing glove cookie jar", 
        "Boxing glove cake pan", "Boxing glove cake topper", "Boxing glove cake decorations", "Boxing glove cake stand", 
        "Boxing glove cake pops", "Boxing glove cupcakes", "Boxing glove cookies", "Boxing glove candy", "Boxing glove lollipop", 
        "Boxing glove gumballs", "Boxing glove chocolate", "Boxing glove pretzels", "Boxing glove popcorn", 
        "Boxing glove chips", "Boxing glove salsa", "Boxing glove dip", "Boxing glove punch", "Boxing glove cocktail", 
        "Boxing glove mocktail", "Boxing glove smoothie", "Boxing glove juice", "Boxing glove energy drink", 
        "Boxing glove protein shake", "Boxing glove recovery drink", "Boxing glove electrolyte drink", "Boxing glove water"
    ],
    "Cosmetics and Toiletries": [
        "Shampoo", "Lipstick", "Perfume", "Moisturizer", "Hairdryer", "Conditioner", "Cologne", 
        "Body lotion", "Face wash", "Cleanser", "Toner", "Serum", "Face mask", "Sunscreen", 
        "Eye cream", "Body wash", "Hand cream", "Body scrub", "Foot cream", "Foot scrub", 
        "Bubble bath", "Bath salts", "Bath bomb", "Shower gel", "Bar soap", "Hand soap", 
        "Body oil", "Body butter", "Body mist", "Face mist", "Facial oil", "Facial scrub", 
        "Facial peel", "Facial toner", "Facial serum", "Facial mask", "Facial cleanser", 
        "Facial moisturizer", "Foundation", "Concealer", "Powder", "Blush", "Bronzer", 
        "Highlighter", "Eyeshadow", "Eyeliner", "Mascara", "Eyebrow pencil", "Eyebrow gel", 
        "Lip gloss", "Lip liner", "Lip balm", "Nail polish", "Nail polish remover", 
        "Nail file", "Nail buffer", "Nail clipper", "Nail scissors", "Nail art kit", 
        "Nail sticker", "Nail decal", "Nail wrap", "Nail stamp", "Nail stencil", 
        "Nail stamping plate", "Nail stamping polish", "Nail stamping scraper", "Nail stamping mat", 
        "Nail stamping pad", "Nail stamping glove", "Nail stamping brush", "Nail stamping stick", 
        "Nail stamping machine", "Nail stamping lamp", "Nail stamping station", "Nail stamping storage", 
        "Nail stamping organizer", "Nail stamping case", "Nail stamping box", "Nail stamping tray", 
        "Nail stamping rack", "Nail stamping display", "Nail stamping shelf", "Nail stamping cabinet", 
        "Nail stamping drawer", "Nail stamping divider", "Nail stamping partition", "Nail stamping separator", 
        "Nail stamping holder", "Nail stamping stand", "Nail stamping tower", "Nail stamping tree", 
        "Nail stamping hanger", "Nail stamping hook", "Nail stamping loop", "Nail stamping ring", 
        "Nail stamping clip", "Nail stamping peg", "Nail stamping pin", "Nail stamping rod", 
        "Nail stamping stick", "Nail stamping dowel", "Nail stamping pole", "Nail stamping staff", 
        "Nail stamping baton", "Nail stamping wand", "Nail stamping scepter", "Nail stamping crown", 
        "Nail stamping throne", "Nail stamping pedestal", "Nail stamping platform", "Nail stamping stage", 
        "Nail stamping podium", "Nail stamping dais", "Nail stamping rostrum", "Nail stamping tribune", 
        "Nail stamping lectern", "Nail stamping pulpit", "Nail stamping altar", "Nail stamping sanctuary"
    ],
    "Furniture": [
        "Chair", "Table", "Sofa", "Bed", "Bookshelf", "Desk", "Dining table", "Coffee table", "Nightstand", 
        "Wardrobe", "Cabinet", "Drawer", "Dresser", "TV stand", "Shelf", "Sideboard", "Buffet", "Console table", 
        "Vanity table", "Bar stool", "Counter stool", "Bench", "Ottoman", "Chaise lounge", "Futon", "Recliner", 
        "Rocking chair", "Armchair", "Accent chair", "Wingback chair", "Club chair", "Tub chair", "Swivel chair", 
        "Lounge chair", "Bar chair", "Counter chair", "Papasan chair", "Egg chair", "Bubble chair", "Ball chair", 
        "Hanging chair", "Glider chair", "Massage chair", "Theater seating", "Bean bag chair", "Floor chair", 
        "Pouf", "Footstool", "Stool", "Step stool", "Ladder stool", "Storage bench", "Storage ottoman", 
        "Storage chest", "Storage trunk", "Storage cabinet", "Storage shelf", "Storage rack", "Storage drawer", 
        "Storage basket", "Storage bin", "Storage box", "Storage crate", "Storage tower", "Storage locker", 
        "Storage caddy", "Storage cart", "Storage trolley", "Storage organizer", "Storage unit", 
        "Storage system", "Storage solution", "Storage furniture", "Storage bed", "Storage sofa", 
        "Storage table", "Storage desk", "Storage chair", "Storage bench seat", "Storage ottoman bench", 
        "Storage chest trunk", "Storage cabinet shelf", "Storage drawer organizer", "Storage bin container", 
        "Storage box with lid", "Storage crate with handles", "Storage tower with baskets", "Storage locker with key", 
        "Storage caddy with compartments", "Storage cart with wheels", "Storage organizer with drawers", 
        "Storage unit with doors", "Storage system with shelves", "Storage solution with bins", "Storage furniture with baskets", 
        "Storage bed with drawers", "Storage sofa with chaise", "Storage table with baskets", "Storage desk with hutch", 
        "Storage chair with ottoman", "Storage bench seat with drawers", "Storage ottoman bench with tray", 
        "Storage chest trunk with lock", "Storage cabinet shelf with doors", "Storage drawer organizer with dividers", 
        "Storage bin container with lid", "Storage box with handles", "Storage crate with wheels", 
        "Storage tower with drawers", "Storage locker with shelves", "Storage caddy with handle", 
        "Storage cart with drawers", "Storage organizer with bins", "Storage unit with baskets", 
        "Storage system with doors", "Storage solution with shelves", "Storage furniture with doors", 
        "Storage bed with headboard", "Storage sofa with storage", "Storage table with drawers", 
        "Storage desk with shelves", "Storage chair with storage", "Storage bench seat with back", 
        "Storage ottoman bench with storage", "Storage chest trunk with drawers", "Storage cabinet shelf with glass doors", 
        "Storage drawer organizer with compartments", "Storage bin container with dividers", 
        "Storage box with lock", "Storage crate with lid", "Storage tower with doors", "Storage locker with lock", 
        "Storage caddy with lid", "Storage cart with shelves", "Storage organizer with doors", "Storage unit with drawers", 
        "Storage system with bins", "Storage solution with hooks", "Storage furniture with wheels", "Storage bed with storage drawers", 
        "Storage sofa with storage chaise", "Storage table with shelves", "Storage desk with drawers and shelves", 
        "Storage chair with arms", "Storage bench seat with storage baskets", "Storage ottoman bench with tray and storage", 
        "Storage chest trunk with drawers and lock", "Storage cabinet shelf with doors and shelves", 
        "Storage drawer organizer with dividers and compartments", "Storage bin container with lid and dividers", 
        "Storage box with handles and lock", "Storage crate with wheels and handles", "Storage tower with drawers and doors", 
        "Storage locker with shelves and lock", "Storage caddy with handle and lid", "Storage cart with drawers and wheels", 
        "Storage organizer with bins and drawers", "Storage unit with baskets and doors", "Storage system with shelves and doors", 
        "Storage solution with baskets and shelves", "Storage furniture with doors and shelves", "Storage bed with headboard and drawers", 
        "Storage sofa with storage and chaise", "Storage table with drawers and shelves", "Storage desk with shelves and drawers", 
        "Storage chair with storage and arms", "Storage bench seat with back and storage", "Storage ottoman bench with storage and tray", 
        "Storage chest trunk with drawers and lock", "Storage cabinet shelf with glass doors and shelves", 
        "Storage drawer organizer with compartments and dividers", "Storage bin container with dividers and lid", 
        "Storage box with lock and handles", "Storage crate with lid and wheels", "Storage tower with doors and drawers", 
        "Storage locker with lock and shelves", "Storage caddy with lid and handle", "Storage cart with shelves and drawers", 
        "Storage organizer with doors and bins", "Storage unit with drawers and baskets", "Storage system with bins and shelves", 
        "Storage solution with hooks and shelves", "Storage furniture with wheels and doors", "Storage bed with storage drawers and headboard", 
        "Storage sofa with storage chaise and pillows", "Storage table with shelves and drawers", "Storage desk with drawers and shelves", 
        "Storage chair with arms and storage", "Storage bench seat with storage baskets and back", "Storage ottoman bench with tray and storage", 
        "Storage chest trunk with drawers, lock, and wheels", "Storage cabinet shelf with doors, shelves, and drawers", 
        "Storage drawer organizer with dividers, compartments, and lid", "Storage bin container with dividers, lid, and wheels", 
        "Storage box with lock, handles, and wheels", "Storage crate with lid, wheels, and handles", 
        "Storage tower with doors, drawers, and shelves", "Storage locker with lock, shelves, and hooks", 
        "Storage caddy with lid, handle, and wheels", "Storage cart with drawers, shelves, and wheels", 
        "Storage organizer with doors, bins, and drawers", "Storage unit with baskets, drawers, and shelves", 
        "Storage system with shelves, bins, and doors", "Storage solution with hooks, shelves, and baskets", 
        "Storage furniture with doors, shelves, and drawers"
    ],
    "Food and Beverages": [
        "Cereal", "Pasta", "Canned soup", "Chocolate", "Frozen pizza", "Cookies", "Chips", 
        "Crackers", "Granola bars", "Trail mix", "Nuts", "Dried fruit", "Popcorn", "Pretzels", 
        "Rice cakes", "Oatmeal", "Pancake mix", "Maple syrup", "Honey", "Jam", "Peanut butter", 
        "Nutella", "Marshmallows", "Graham crackers", "Cake mix", "Brownie mix", "Cookie mix", 
        "Muffin mix", "Bread mix", "Pizza dough", "Pie crust", "Tortillas", "Breadsticks", 
        "Bagels", "English muffins", "Croissants", "Danishes", "Scones", "Biscuits", "Rolls", 
        "Buns", "Pita bread", "Flatbread", "Naan bread", "Tortilla chips", "Salsa", "Guacamole", 
        "Sour cream", "Dip", "Hummus", "Tzatziki", "Baba ganoush", "Tabbouleh", "Falafel", 
        "Stuffed grape leaves", "Baklava", "Pita chips", "Greek yogurt", "Feta cheese", 
        "Halloumi cheese", "Goat cheese", "Mozzarella cheese", "Cheddar cheese", "Brie cheese", 
        "Camembert cheese", "Blue cheese", "Gorgonzola cheese", "Parmesan cheese", "Ricotta cheese", 
        "Provolone cheese", "Swiss cheese", "Gouda cheese", "Havarti cheese", "Monterey Jack cheese", 
        "Pepper jack cheese", "Colby cheese", "Muenster cheese", "Asiago cheese", "Fontina cheese", 
        "Gruyere cheese", "Emmental cheese", "Edam cheese", "Manchego cheese", "Stilton cheese", 
        "Roquefort cheese", "Bleu cheese", "Gjetost cheese", "Cheese curds", "Cheese slices", 
        "Cheese sticks", "Cheese cubes", "Cheese wheels", "Cheese wedges", "Cheese balls", 
        "Cheese spread", "Cheese dip", "Cheese sauce", "Cheese fondue", "Cheese souffle", 
        "Cheese toast", "Cheese sandwich", "Cheeseburger", "Cheese pizza", "Cheese fries", 
        "Cheese omelette", "Cheese quiche", "Cheese pasta", "Cheese salad", "Cheese soup", 
        "Cheese bread", "Cheese croissant", "Cheese Danish", "Cheese biscuit", "Cheese straws", 
        "Cheese crackers", "Cheese popcorn", "Cheese puffs", "Cheese curls", "Cheese twists", 
        "Cheese crisps", "Cheese wafers", "Cheese crisps", "Cheese squares", "Cheese circles", 
        "Cheese stars", "Cheese hearts", "Cheese flowers", "Cheese animals", "Cheese people","Drinks"
    ],
    "Medical Equipment" : [
    "Stethoscope", "Blood pressure monitor", "Thermometer", "Otoscope", "Ophthalmoscope",
    "Sphygmomanometer", "Pulse oximeter", "ECG machine", "Electrocardiograph", "Glucometer",
    "Nebulizer", "Spirometer", "Ultrasound machine", "X-ray machine", "MRI machine",
    "CT scanner", "Defibrillator", "Fetal monitor", "Doppler ultrasound", "Blood glucose meter",
    "Hemoglobin meter", "Hemoglobin A1c analyzer", "Centrifuge", "Autoclave", "Incubator",
    "Microscope", "Endoscope", "Surgical instruments", "Surgical lights", "Surgical table",
    "Anesthesia machine", "Ventilator", "Respirator", "Oxygen concentrator", "CPAP machine",
    "BiPAP machine", "Infusion pump", "Syringe pump", "Patient monitor", "Cardiac monitor",
    "ECG Holter monitor", "EEG machine", "EMG machine", "TENS unit", "Wheelchair", "Hospital bed",
    "Examination table", "IV pole", "Suction machine", "Blood collection chair", "Traction equipment",
    "Nebulizer compressor", "Kidney dialysis machine", "Cryotherapy machine", "Hyperbaric chamber",
    "ECG electrodes", "ECG leads", "EEG electrodes", "EEG leads", "Electrosurgical unit",
    "Laser therapy machine", "Diathermy machine", "EKG machine", "Blood gas analyzer", "Dental chair",
    "Dental drill", "Dental scaler", "Dental X-ray machine", "Dental curing light",
    "Dental suction unit", "Dental autoclave", "Dental handpieces", "Dental amalgamator",
    "Dental compressor", "Dental radiography equipment", "Dental impression materials",
    "Dental articulators", "Dental casting machines", "Dental laboratory microscopes",
    "Dental ultrasonic cleaners", "Dental model trimmers", "Dental lathes",
    "Dental vacuum forming machines", "Dental burnout furnaces", "Dental air abrasion systems",
    "Dental microscopes", "Dental lasers", "Dental intraoral cameras", "Dental film processors",
    "Dental apex locators", "Dental ultrasonic scalers", "Dental air compressors",
    "Dental curing lights", "Dental suction units", "Dental sterilizers", "Dental implant motors"
]

}


# Iterate through subfolders and their images
for root, dirs, files in os.walk(image_folder):
        for file in files:
            # Check if the file is an image file
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                # Extract packaging material name from subfolder name
                packaging_material = os.path.basename(root)
                if packaging_material in packaging_materials:
                    # Load image using OpenCV
                    image_path = os.path.join(root, file)
                    image = load_image_opencv(image_path)
                    
                    if image is not None:
                        # Save the image to the dataset folder or convert to base64 and store as string in CSV
                        # For example, you can save the image to a folder and store its file path in the CSV
                        image_filename = packaging_material + "_" + file  # Include packaging material name in the image filename
                        image_save_path = os.path.join("dataset_images", image_filename)
                        cv2.imwrite(image_save_path, image)


# Generate product details for the packaging material
def generate_product_details(category):
    products = []
    product_names = category_to_products.get(category, [])
    for product_name in product_names:
        product = {}
        product["Category"] = category
        product["Product Name"] = product_name
        product["Weight (kg)"] = random.uniform(0.1, 50)  # Random weight between 0.1 and 50 kg
        material_composition = get_material_composition(product_name)  # You need to implement this function
        product["Fragility"] = determine_fragility(category, material_composition)  
        product["Weight Category"] = categorize_weight(product["Weight (kg)"])
        product["Predicted Packaging Material"] = random.choice(determine_packaging_material(product))
        product["Protective Packaging Tip"] = generate_protective_packaging_tip(product)
        # Assign image paths based on predicted packaging material
        predicted_material = product["Predicted Packaging Material"]
        image_paths = packaging_material_images.get(predicted_material, [])
        if image_paths:
            product["Image Paths"] = image_paths
        else:
            # If no image paths are found, assign a default image path or handle accordingly
            product["Image Paths"] = [r"C:\Users\fidha\OneDrive\Desktop\LOGISTICS\logistica-1.0.0\material_images\Cardboard boxes\Image_1.jpg"]

        products.append(product)
    return products





# Generate product details for each category
all_products = []
for category in category_to_products.keys():
    products = generate_product_details(category)
    all_products.extend(products)

# Write product details to CSV
output_file = "Dataset_PackagingProduct.csv"
header = ["Category", "Product Name", "Weight (kg)", "Fragility", "Weight Category", "Predicted Packaging Material", "Protective Packaging Tip","Image Paths"]

with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for product in all_products:
        writer.writerow(product)

print("Product details generated successfully!")
