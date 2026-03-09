from PIL import Image
import os

background_path = "laboratory.png"
obstruction_path = "laboratory_obstructions.png"
robot_dir = "kenney_toon-characters-1/Robot/PNG/Poses/"

print("Rescaling background image...")
with Image.open(background_path) as img:
    width, height = img.size
    max_dim = max(width, height)
    scale_factor = 600 / max_dim
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    resized_img.save(background_path)
    print(f"Background rescaled to {new_width}x{new_height}")

print("Rescaling obstruction image...")
with Image.open(obstruction_path) as img:
    width, height = img.size
    max_dim = max(width, height)
    scale_factor = 600 / max_dim
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    resized_img.save(obstruction_path)
    print(f"Obstruction image rescaled to {new_width}x{new_height}")

print("Rescaling robot sprites...")
robot_files = [f for f in os.listdir(robot_dir) if f.endswith(".png")]
for file_name in robot_files:
    file_path = os.path.join(robot_dir, file_name)
    with Image.open(file_path) as img:
        width, height = img.size
        scale_factor = 60 / height
        new_width = int(width * scale_factor)
        new_height = 60
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save(file_path)
        print(f"Rescaled {file_name} to {new_width}x{new_height}")

print("Image rescaling completed!")