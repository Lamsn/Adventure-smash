# -*- coding: utf-8 -*-
"""



"""
import pygame,os.path
Personnage="Waluigi"
marche=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_height()))  for i in range(len(os.listdir('Personnages/'+Personnage+'/marche')))]
attaque=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height())) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueAir=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height())) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueUp=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_height())) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueUp')))]
saut=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_height())) for i in range(len(os.listdir('Personnages/'+Personnage+'/saut')))]
immobile=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_height())) for i in range(len(os.listdir('Personnages/'+Personnage+'/immobile')))]
attaqueDown=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_height())) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueDown')))]
hit=pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/hit.png'),(pygame.image.load('Personnages/'+Personnage+'/hit.png').get_width(),pygame.image.load('Personnages/'+Personnage+'/hit.png').get_height()))
rect=pygame.Rect(600,600,626,486)
taille=[48,112]
offset=[0,0]    
speedAnim=10
speed=6
jumpPower=14
poids=110
attaqueDroite=[60,122,40,-10,10,10,100,20,450,300,0]#w,h,x,y,orientation,degats,echelle,kbBase,startup,active,latence
attaqueDroiteAir=[60,122,40,-10,10,10,100,20,450,300,0]
attaqueGauche=[60,122,-52,-10,160,10,100,20,450,300,0]
attaqueGaucheAir=[60,122,-52,-10,160,10,100,20,450,300,0]
attaqueHaut=[112,88,0,-20,90,5,200,20,150,300,150]
attaqueBas=[88,20,-20,92,50,7,100,20,150,300,150]
      