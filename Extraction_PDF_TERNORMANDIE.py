import requests
from bs4 import BeautifulSoup
import urllib.request
import ssl
import os.path
from datetime import datetime

# Ignorer les erreurs de certificat SSL
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# URL de la page contenant les liens vers les fichiers PDF
url = "https://www.ter.sncf.com/normandie/se-deplacer/info-trafic/ponctualite"

# En-tête d'agent utilisateur
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Nom du dossier où enregistrer les fichiers PDF
dossier_pdf = "EXTRACTION SNCF"

# Vérifier si le dossier existe, sinon le créer
if not os.path.exists(dossier_pdf):
    os.makedirs(dossier_pdf)

# Liste pour stocker les URLs des fichiers PDF téléchargés
urls_deja_telecharges = []

# Parcourir les fichiers PDF déjà téléchargés et enregistrer leur URL
for filename in os.listdir(dossier_pdf):
    if filename.endswith(".pdf"):
        urls_deja_telecharges.append(filename.split('.')[0])

# Envoyer une requête GET à l'URL avec l'en-tête spécifié
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Analyser le contenu HTML de la page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver tous les liens (balise <a>) sur la page
    links = soup.find_all('a')

    # Parcourir tous les liens pour trouver ceux qui pointent vers des fichiers PDF
    for link in links:
        # Vérifier si l'attribut 'href' existe dans la balise <a>
        if 'href' in link.attrs and link['href'].endswith('.pdf'):
            pdf_url = link['href']
            print("URL du PDF trouvé :", pdf_url)

            # Vérifier si l'URL a déjà été téléchargée
            if pdf_url not in urls_deja_telecharges:
                # Télécharger le fichier PDF
                with urllib.request.urlopen(pdf_url, context=ssl_context) as response:
                    with open(os.path.join(dossier_pdf, pdf_url.split('/')[-1]), "wb") as pdf_file:
                        pdf_file.write(response.read())
                print("Le fichier PDF a été téléchargé avec succès.")

                # Ajouter l'URL du fichier PDF téléchargé à la liste
                urls_deja_telecharges.append(pdf_url)
            else:
                print("Ce fichier PDF a déjà été téléchargé.")

# Mettre à jour la liste des fichiers PDF téléchargés
with open(os.path.join(dossier_pdf, "urls.txt"), "w") as f:
    for url in urls_deja_telecharges:
        f.write(url + "\n")
