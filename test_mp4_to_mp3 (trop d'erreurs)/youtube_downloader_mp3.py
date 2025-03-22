import os
from moviepy import VideoFileClip

Télechargements = []
def fichier_dans_le_repertoire(repertoire, extension) -> list:
    liste_lambda = []
    for fichier in os.listdir(repertoire):
        if fichier.endswith(extension):
            liste_lambda.append(os.path.join(fichier))
    return liste_lambda
Télechargements = fichier_dans_le_repertoire('vidéos_a_convertir/','.mp4')
print(Télechargements)

def renommer_fichiers_mp4(liste_original):
    sans_extension = [fichier.replace(".mp4","") for fichier in liste_original]
    return sans_extension
Noms_Téléchargement_uniquement = renommer_fichiers_mp4(Télechargements)

def tout_telecharger(noms : list,fichiers : list) -> None:
    for element in range(len(fichiers)):
        nom = noms[element]
        clip = str(fichiers[element])
        myclip = VideoFileClip(clip)
        audio = myclip.audio
        audio.write_audiofile("musiques/" + nom + ".mp3")

fin = tout_telecharger(Noms_Téléchargement_uniquement, Télechargements)