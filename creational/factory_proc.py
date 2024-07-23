def create_toy(toy_type):
    if toy_type == "car":
        return {"type": "car", "wheels": 4, "color": "red"}
    elif toy_type == "doll":
        return {"type": "doll", "hair_color": "blonde", "height": "12 inches"}
    else:
        return None

# Usage
toy = create_toy("car")
print(toy)  # Output: {'type': 'car', 'wheels': 4, 'color': 'red'}
