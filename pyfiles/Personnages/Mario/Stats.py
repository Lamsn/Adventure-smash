# -*- coding: utf-8 -*-
"""



"""
import pygame,os.path
Personnage="Mario"
marche=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_height()//2))  for i in range(len(os.listdir('Personnages/'+Personnage+'/marche')))]
attaque=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueAir=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueUp=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueUp')))]
saut=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/saut')))]
immobile=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/immobile')))]
attaqueDown=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueDown')))]
hit=pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/hit.png'),(pygame.image.load('Personnages/'+Personnage+'/hit.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/hit.png').get_height()//2))
rect=pygame.Rect(600,600,626,486)
taille=[40,66]
offset=[0,0]    
speedAnim=6
speed=6
jumpPower=14
poids=60
attaqueDroite=[80,67,20,-0,20,10,100,20,250,300,200]#w,h,x,y,orientation,degats,echelle,kbBase,startup,active,latence
attaqueDroiteAir=[80,67,20,-0,20,10,100,20,250,300,200]
attaqueGauche=[80,67,-60,-0,160,20,100,20,250,300,200]
attaqueGaucheAir=[80,67,-60,-0,160,20,100,20,250,300,200]
attaqueHaut=[115,64,-20,-50,90,5,200,20,0,360,200]
attaqueBas=[48,80,0,0,50,7,100,20,0,270,150]
      