# Importation des modules nécessaires
import os
from tkinter import *
from tkinter import filedialog
import shutil

# Fonction pour créer le fichier Markdown et copier l'image
def create_file():
    # Création du dossier d'images s'il n'existe pas
    if not os.path.exists('static/img'):
        os.makedirs('static/img')

    # Obtention du nom de fichier personnalisé ou utilisation du nom par défaut "post.md"
    custom_filename = filedialog.asksaveasfilename(initialdir='C:/Users/prost/OneDrive/Documents/Site/o2switch/myproject/pages', defaultextension=".md", filetypes=[("Markdown Files", "*.md")])
    
    # Vérification si l'utilisateur a annulé la sélection du fichier
    if not custom_filename:
        return

    # Ajout de l'extension .md si elle n'est pas déjà présente
    if not custom_filename.endswith(".md"):
        custom_filename += ".md"

    # Écriture directe dans le fichier Markdown
    with open(custom_filename, 'w', encoding='utf-8') as md_file:
        md_file.write("""title: {title}
published: {date}
cat: {category}
desc: {description}
cover: {cover}

{content}""".format(
            title=title_entry.get(),
            date=date_entry.get(),
            category=category_entry.get(),
            description=description_entry.get("1.0", END),
            cover=cover_entry.get(),
            content=description_entry.get("1.0", END)
        ))

    # Copie de l'image dans le dossier d'images
    shutil.copy(cover_entry.get(), 'static/img/' + os.path.basename(cover_entry.get()))

# Création de la fenêtre principale
root = Tk()

# Widgets pour saisir les informations
Label(root, text="Title").grid(row=0)
title_entry = Entry(root)
title_entry.grid(row=0, column=1)

Label(root, text="Date").grid(row=1)
date_entry = Entry(root)
date_entry.grid(row=1, column=1)

Label(root, text="Category").grid(row=2)
category_entry = Entry(root)
category_entry.grid(row=2, column=1)

Label(root, text="Description").grid(row=3)
description_entry = Text(root)
description_entry.grid(row=3, column=1)

Label(root, text="Cover Image").grid(row=4)
Button(root, text="Choose File", command=lambda: cover_entry.insert(0, filedialog.askopenfilename())).grid(row=4, column=1)
cover_entry = Entry(root)
cover_entry.grid(row=4, column=2)

# Bouton pour créer le fichier
Button(root, text="Create File", command=create_file).grid(row=5, column=1)

# Lancement de la boucle principale de l'interface graphique
root.mainloop()
