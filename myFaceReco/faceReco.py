#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
from PyQt4.QtGui import *
import faceRecoGUI
import numpy
from scipy import linalg
from scipy.misc import imread, imsave
import glob
from os.path import basename


class MainDialog(QDialog,faceRecoGUI.Ui_Dialog):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)
        self.setupUi(self) 
        self.fname = None
        self.imgNames = None
        self.directory = None
        self.pngs = None
        self.image = None
        self.heigh = None
        self.length = None 
        self.imgs = None
        self.N = None
        self.img2find = None
        #self.moyenne = None
        
        self.lblMatch.hide()
        self.pbReconnaissance.hide()
        self.seuil = 2.0

    def changeSeuil(self):
        self.seuil = float(self.slideSeuil.value())/10
        self.lblSeuil.setText(str(self.seuil))
        
    def openFileDiagRef(self):
        print "Bouton Ref"
        self.directory = str(QFileDialog.getExistingDirectory(self, "Choisir un dossier ..."))
        self.lePath2Ref.setText(self.directory)
        
        self.pngs = glob.glob(self.directory+"/*.png")
        
        # Lecture de la première image
        # acquisition de ses dimensions (hxl) 
        self.image = imread(self.pngs[0], True)
        self.heigh = len(self.image[:,0])
        self.length= len(self.image[0])
        print "Dimensions des images : "+str(self.heigh) + " x "+ str(self.length)
        
        # Lecture de toutes les images en nuances de gris et transformation en vecteurs
        # imgs : tableau des vecteurs d'images de n=hxl dimensions
        self.imgs = numpy.array([imread(i, True).flatten() for i in self.pngs])
        
        # imgs contient N vecteurs d'images
        self.N = len(self.imgs)
        print self.directory+" : "+str(self.N)+" images chargées."       
        
        if (self.fname is not None ):
            self.pbReconnaissance.show()
        
        
    def openFileDiagIdent(self):
        print "Bouton Ident"
        self.fname = QFileDialog.getOpenFileName(self, 'Ouvrir une photo...','.',"Image file PNG (*.png)")
        self.lePhoto.setText(self.fname)
        self.lblPhotoToIdent.setPixmap(QPixmap(self.fname))
        # lire l'image à tester 
        self.img2find = numpy.array(imread(str(self.fname), True).flatten())
        if (self.directory is not None ):
            self.pbReconnaissance.show()
        
    def reconnaissance(self):
        print "Reconnaissance en cours"
        # Calcul, affichage et enregistrement de la moyenne des images 
        # moyenne : vecteur de l'image moyenne   
        moyenne = numpy.mean(self.imgs, 0)
        print "moyenne="+str(moyenne)
        # transformation du vecteur moyenne en matrice hxl et enregistrement
        imsave("moyenne/average.png",moyenne.reshape(self.heigh,self.length))
        
        # Calcul de phi = image - moyenne
        # Le but de soustraire l'image moyenne de chaque vecteur d'image 
        # est de garder uniquement les caractéristiques distinctives de chaque face 
        # et "enlever" l'information qui leur est commune.
        # phi : tableau de vecteurs d'images (N lignes x (hxl) colonnes)
        phi = self.imgs - moyenne
        
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
            imsave("eigenfaces/eigenfaces"+str(i)+".png", eigenfaces[:,i].reshape(self.heigh,self.length))
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
        
        # Identification d'une personne : trouver l'image qui lui ressemble le plus
        # La méthode est identique :
        # retirer de l'image à trouver les caractéristiques moyennes puis calculer les pondérateurs avec l'ensemble
        # des eigenfaces connus. On calcul ensuite la distance (sqrt(min(ecart²)) entre les pondérateurs des images 
        # de références et ceux de l'image à tester. 
        phi2 = self.img2find - moyenne
        w2 = numpy.dot(phi2,eigenfaces)
        #print "w2 = " + str(w2)
        #print "weights = " + str(weights)
        dist = numpy.min((weights-w2)**2,axis=1)
        #print "dist = " + str(dist)
        indiceImg = numpy.argmin(dist)
        mindist=numpy.sqrt(dist[indiceImg])
        
        print "Distance min : "+str(mindist)
        threshold = self.seuil
        if mindist <=threshold:
            print "MATCH !"
            self.lblMatch.setText("MATCH !")
            print "Nom image : "+self.pngs[indiceImg]
            self.lblPhotoIdentifier.setPixmap(QPixmap(self.pngs[indiceImg]))
            print "Image n° : "+str(indiceImg)
            
            self.lblResultat.setText(basename(self.pngs[indiceImg]))
        else:
            print "NO MATCH !"
            self.lblMatch.setText("NO MATCH !")
            self.lblPhotoIdentifier.setPixmap(QPixmap("inconnu.png"))
            self.lblResultat.setText("...")
        self.lblMatch.show()
        
        
        

app=QApplication(sys.argv) 
form=MainDialog()
form.show()
app.exec_()
