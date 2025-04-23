# 🎭 Anonymous Animated Generator

> Crée ton propre **GIF animé ou MP4 stylisé** avec apparition du **masque Anonymous** dans une brume cyberpunk.  
> Full CLI, full style, full GPT-4 + DALL·E 3. No bullshit.

---

## 🚀 Fonctionnalités

- Génère **6 ou 8 frames** cohérentes avec DALL·E 3 (apparition progressive)
- Ajoute du **texte interactif ligne par ligne** (tu choisis ce qui s’affiche)
- Exporte en **GIF animé** et **vidéo MP4**
- Style hacker, cyberpunk, glitch, dramatique…  
  *Bienvenue dans la matrice.*

---

## 🛠️ Installation

### 1. Clone le repo (ou copie ce projet)
```bash
git clone https://github.com/trh4ckn0n/trkn-gengif.git
cd gengif
```

### 2. Installe les dépendances
```bash
pip install -r requirements.txt
```

> **Note** : utilise Python 3.10 ou 3.11 (3.13 n’est pas 100% compatible avec MoviePy)

---

## 🔑 Configuration

Ajoute ta clé OpenAI dans le script :
```python
openai.api_key = "sk-..."
```

Tu dois avoir accès à **GPT-4** et **DALL·E 3**.

---

## 🎬 Utilisation

```bash
python3 app.py
```

Tu seras guidé pas à pas :

1. Choisis **6 ou 8 frames**
2. Pour chaque image, un prompt est généré automatiquement
3. Tu écris (ou non) une **phrase courte** à afficher
4. À la fin :  
   - `anonymous_animation.gif`  
   - `anonymous_animation.mp4`  

Prêt à publier sur **TikTok, Instagram, Reels, X...**

---

## ✨ Exemples de texte stylé

- `Nous sommes légion.`
- `Le code est notre voix.`
- `We are not human. Don’t prospect us.`
- `Derrière l'écran, un monde sans maître.`

---

## 📦 Fichiers générés

- `anonymous_animation.gif` → animé, pour Discord, X, Insta
- `anonymous_animation.mp4` → fluide, pour Reels, Shorts, TikTok

---

## 🧠 Powered by

- [GPT-4](https://platform.openai.com/)
- [DALL·E 3](https://platform.openai.com/docs/guides/images)
- `moviepy`, `PIL`, `imageio`, `numpy`

---

## 👾 Auteur

> Créé par **trhacknon** et un assistant qui dort jamais (GPT-4).

Feel free to fork, améliorer, glitcher le code.
