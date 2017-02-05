# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:20:01 2017

@author: Marc Silanus
Note : Le dossier doit travail doit contenir 
- eigenfaces.py
- gallery : contient les photos de références
- eingenfaces : Contiendra les eigenfaces
- reconstruct : Contiendra les essais de reconstruction
"""

from scipy import linalg
from scipy.misc import imread, imsave
import glob
import numpy
import matplotlib.pyplot as plt

# Acquisition des images
# pngs : tableau d'images 
pngs = glob.glob('gallery/*.png')

# Lecture de la première image
# acquisition de ses dimensions (hxl) 
image = imread(pngs[0], True)
heigh = len(image[:,0])
length= len(image[0])
print "Dimensions des images : "+str(heigh) + " x "+ str(length)

# Lecture de toutes les images en nuances de gris et transformation en vecteurs
# imgs : tableau des vecteurs d'images de n=hxl dimensions
imgs = numpy.array([imread(i, True).flatten() for i in pngs])
# Affichages des N vecteurs d'images
N = len(imgs)
for i in range(N):
    print "imgs["+str(i)+"]="+str(imgs[i])

print " --------------------------------"
# Calcul, affichage et enregistrement de la moyenne des images 
# moyenne : vecteur de l'image moyenne   
moyenne = numpy.mean(imgs, 0)
print "moyenne="+str(moyenne)
# transformation du vecteur moyenne en matrice hxl et enregistrement
imsave("average.png",moyenne.reshape(heigh,length))

# Calcul de phi = image - moyenne
# Le but de soustraire l'image moyenne de chaque vecteur d'image 
# est de garder uniquement les caractéristiques distinctives de chaque face 
# et "enlever" l'information qui leur est commune.
# phi : tableau de vecteurs d'images (N lignes x (hxl) colonnes)
phi = imgs - moyenne

# Recherche des singularités des images : équivalent à la Covariance
# phi.transpose() : matrice phi transposée
# svd : Singular Value Decomposition
# eigenfaces : matrice unitaire dont les vecteurs singuliers sont en colonnes
# Les colonnes de eigenfaces sont des vecteurs propres. lorsqu'ils sont convertis 
# en matrice hxl, ils correspondent à des images ayant un visage comme apparence.
# Puisqu'il s'agit de vecteurs propres et ont un aspect semblable à un visage, 
# ils sont appelés Eigenfaces. Parfois, ils sont également appelés Ghost Images
# en raison de leur apparence bizarre.
eigenfaces, sigma, v = linalg.svd(phi.transpose(), full_matrices=False)

# Enregistrement des vecteurs eigenfaces (organisés en colonnes) transformés
# en N matrices hxl dans le dossier eigenfaces sous les noms 
# eigenfaces0.png ...eigenfacesN.png (N est le nombre d'images d'origine)
for i in range(eigenfaces.shape[1]): # eigenfaces.shape[1] = nombre de colonnes = N
    imsave("eigenfaces/eigenfaces"+str(i)+".png", eigenfaces[:,i].reshape(heigh,length))
    #print "eigenfaces"+str(i)+".png"+str( eigenfaces[:,i].reshape(heigh,length))

# Chaque image d'origine - l'image moyenne (phi) peut être représenté par une 
# combinaison linéaire des vecteurs eigenfaces pondérés :
# phi = weights x eigenfaces ou weight est le vecteur des pondérateurs
# phi est un vecteur organisé en ligne
# eigenfaces est un vecteur organisé en colonne
# il faudrait donc transposé eigenfaces pour réaliser cette opération
# phi = weights x eigenfaces.T
# Donc : weights = phi x eigenfaces.T.T => weights = phi x eigenfaces
weights = numpy.dot(phi, eigenfaces)

# La reconstruction des images d'origine consiste à ajouter à l'image moyenne
# les singularités de chaque eigenfaces pondérées. 
# recon : vecteur de l'image reconstituée
# recon = moyenne + weights x eigenfaces 
# On obtient un jeu de N² images reconstituées
 
for p in range(N):
    for i in range(N):
        recon = moyenne + numpy.dot(weights[p, :i], eigenfaces[:, :i].T)
        img_id = str(p)+"_"+str(i)
        imsave("reconst/img_"+ img_id + ".png", recon.reshape(heigh,length))
        
# Les meilleurs résultats sont obtenus pour i=N
# on peut cependant limiter le nombre d'eigenfaces à tester pour
# accélerer le processus de reconstruction
for p in range(N):
    recon = moyenne + numpy.dot(weights[p,:15], eigenfaces[:, :15].T)
    img_id = str(p)
    imsave("reconst2/img_"+ str(img_id) + ".png", recon.reshape(heigh,length))
    
# Identification d'une personne : trouver l'image qui lui ressemble le plus
# La méthode est identique :
# retirer de l'image à trouver les caractéristiques moyennes puis calculer les pondérateurs avec l'ensemble
# des eigenfaces connus. On calcul ensuite la distance (sqrt(min(ecart²)) entre les pondérateurs des images 
# de références et ceux de l'image à tester. 
#
# lire l'image à tester : amber2.png / zach1.png / erin2.png
img2find = numpy.array(imread("a_tester/zach1.png", True).flatten())
tofind=plt.figure(1)
plt.imshow(img2find.reshape(heigh,length))
plt.title("A trouver")
plt.gray()
tofind.show()
#print "img2find="+str(img2find)
phi2 = img2find - moyenne
w2 = numpy.dot(phi2,eigenfaces)
print "w2 = " + str(w2)
#print "weights = " + str(weights)
dist = numpy.min((weights-w2)**2,axis=1)
print "dist = " + str(dist)
indiceImg = numpy.argmin(dist)
mindist=numpy.sqrt(dist[indiceImg])

print "Distance min : "+str(mindist)
print "Image n° : "+str(indiceImg)
found=plt.figure(2)
plt.imshow(imgs[indiceImg].reshape(heigh,length))
plt.title("Trouver")
plt.gray()
found.show()
raw_input()

# Notion de seuil de reconnaissance :
# c'est la distance au dela de laquelle on ne peut pas être sur de la reconnaissance.
# Dans le cas de amber2.png qui n'a pas d'image de référence dans le dossier gallery,
# on obtient une identification fassue et une distance de 2.36145
# Dans le cas de zach1.png, lidentification est correcte sur une de ses images de
# référence pour une distance de 1.05518
# Dans le cas de erin2.png, la correspondance est parfaite avec une distance de 0
# On considérera une identification correcte pour une distance inférieure à 2
threshold = 2.0
if mindist <=threshold:
    print "MATCH !"
else:
    print "NO MATCH !"