# -*- coding: utf-8 -*-
"""



"""
import pygame,os.path
Personnage="Kirby"
marche=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_height()//2))  for i in range(len(os.listdir('Personnages/'+Personnage+'/marche')))]
attaque=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueAir=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueUp=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueUp')))]
saut=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/saut')))]
immobile=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/immobile')))]
attaqueDown=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueDown')))]
hit=pygame.transform.scale(pygame.image.load('Personnages/Kirby/hit.png'),(pygame.image.load('Personnages/Kirby/hit.png').get_width()//2,pygame.image.load('Personnages/Kirby/hit.png').get_height()//2))
rect=pygame.Rect(600,600,626,486)
taille=[50,44]
offset=[0,6]
speedAnim=4
speed=4
jumpPower=12
poids=80
attaqueDroite=[12,20,44,15,10,3,100,10,0,320,0]#w,h,x,y,orientation,degats,echelle,kbBase,startup,active,latence
attaqueDroiteAir=[45,20,20,20,30,7,100,10,100,300,48]
attaqueGauche=[12,20,-10,15,170,3,100,10,0,320,0]
attaqueGaucheAir=[45,20,-10,20,150,7,100,10,100,300,48]
attaqueHaut=[25,70,12,-15,90,5,200,30,100,300,112]
attaqueBas=[56,58,-5,-5,50,10,100,10,100,600,4]
      