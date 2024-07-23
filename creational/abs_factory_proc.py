def create_modern_chair():
    return {"type": "chair", "style": "modern", "material": "plastic"}

def create_modern_table():
    return {"type": "table", "style": "modern", "material": "glass"}

def create_victorian_chair():
    return {"type": "chair", "style": "victorian", "material": "wood"}

def create_victorian_table():
    return {"type": "table", "style": "victorian", "material": "wood"}

def create_furniture_set(style):
    if style == "modern":
        return {"chair": create_modern_chair(), "table": create_modern_table()}
    elif style == "victorian":
        return {"chair": create_victorian_chair(), "table": create_victorian_table()}
    else:
        return None

# Usage
furniture_set = create_furniture_set("modern")
print(furniture_set)
# Output: {'chair': {'type': 'chair', 'style': 'modern', 'material': 'plastic'}, 'table': {'type': 'table', 'style': 'modern', 'material': 'glass'}}
