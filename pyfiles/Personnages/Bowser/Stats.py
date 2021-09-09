# -*- coding: utf-8 -*-
"""



"""
import pygame,os.path
Personnage="Bowser"
marche=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_height()//2))  for i in range(len(os.listdir('Personnages/'+Personnage+'/marche')))]
attaque=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueAir=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueUp=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueUp')))]
saut=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/saut')))]
immobile=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/immobile')))]
attaqueDown=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueDown')))]
hit=pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/hit.png'),(pygame.image.load('Personnages/'+Personnage+'/hit.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/hit.png').get_height()//2))
rect=pygame.Rect(600,600,626,486)
taille=[118,114]
offset=[0,0]    
speedAnim=6
speed=4
jumpPower=10
poids=120
attaqueDroite=[60,60,88,40,20,20,100,50,800,640,0]#w,h,x,y,orientation,degats,echelle,kbBase,startup,active,latence
attaqueDroiteAir=[60,88,40,20,40,20,100,50,800,640,0]
attaqueGauche=[60,60,-30,40,160,20,100,50,800,640,0]
attaqueGaucheAir=[60,60,-30,40,140,20,100,50,800,640,0]
attaqueHaut=[118,100,0,-50,90,5,200,30,100,300,112]
attaqueBas=[90,86,0,0,50,10,100,10,0,600,4]
      