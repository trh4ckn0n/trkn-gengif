import os
import openai
import requests
import numpy as np
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageSequenceClip
from dotenv import load_dotenv

# Chargement du fichier .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Génère un prompt pour une frame d'apparition du masque Anonymous
def generate_frame_prompt(stage_desc):
    system = "Tu es expert en animation visuelle. Crée un prompt DALL·E 3 très visuel et cohérent avec un thème sombre et cyberpunk."
    user = f"Scène {stage_desc}. Apparition du masque Anonymous dans la brume numérique. Style hacker, lumière verte, ambiance cyberpunk."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}]
    )
    return response.choices[0].message.content.strip()

# Génère une image DALL·E
def generate_image(prompt):
    dalle = openai.Image.create(prompt=prompt, model="dall-e-3", size="1024x1024", response_format="url")
    url = dalle["data"][0]["url"]
    return Image.open(BytesIO(requests.get(url).content)).convert("RGBA")

# Stylise et place le texte sur l'image
def add_text_to_image(image, text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, 42)
    x, y = 40, image.height - 100
    shadow = (0, 0, 0)
    draw.text((x+2, y+2), text, font=font, fill=shadow)
    draw.text((x, y), text, font=font, fill=(0, 255, 0))
    return image

# Génère les images animées
def generate_animation(frames_count):
    stages = [
        "brume épaisse, aucun masque visible",
        "le masque commence à se deviner",
        "forme du masque plus claire",
        "lueur verte autour du masque",
        "masque presque net",
        "masque en plein centre, brillant"
    ]
    if frames_count == 8:
        stages += ["masque rayonnant de lumière", "fond de code et reflets cyberpunk"]

    images = []
    print("\n--- Texte interactif pour chaque frame ---")
    for i, stage in enumerate(stages):
        print(f"\n[Frame {i+1}/{frames_count}] Génération du prompt...")
        prompt = generate_frame_prompt(stage)
        image = generate_image(prompt)
        text = input("Texte à afficher sur cette frame (laisser vide pour aucun) :\n> ")
        if text.strip():
            image = add_text_to_image(image, text.strip())
        images.append(image)
    return images

# Sauve en GIF et MP4
def save_outputs(images, output_basename="anonymous_animation"):
    gif_path = f"{output_basename}.gif"
    mp4_path = f"{output_basename}.mp4"

    # GIF
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=700, loop=0)

    # MP4
    clip = ImageSequenceClip([np.array(img.convert("RGB")) for img in images], fps=1.5)
    clip.write_videofile(mp4_path, codec="libx264")

    print(f"\n✅ GIF enregistré : {gif_path}")
    print(f"✅ MP4 enregistré : {mp4_path}")

# === MAIN ===
def main():
    print("=== Générateur d'animation Anonymous ===")
    frames = input("Combien de frames ? (6 ou 8) > ").strip()
    frames = 6 if frames != "8" else 8
    images = generate_animation(frames)
    save_outputs(images)

if __name__ == "__main__":
    main()
