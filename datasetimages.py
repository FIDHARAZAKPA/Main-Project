from bing_image_downloader import downloader

# List of 100 product names
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


# Output directory where images will be saved
output_dir = 'material_images'

# Download images for each product name
for product in packaging_materials:
    downloader.download(product, output_dir=output_dir, limit=1, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
