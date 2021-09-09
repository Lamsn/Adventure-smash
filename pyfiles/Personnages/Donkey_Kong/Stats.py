# -*- coding: utf-8 -*-
"""



"""
import pygame,os.path
Personnage="Donkey_Kong"
marche=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/marche/'+str(i)+'.png').get_height()//2))  for i in range(len(os.listdir('Personnages/'+Personnage+'/marche')))]
attaque=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueAir=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaque/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaque')))]
attaqueUp=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueUp/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueUp')))]
saut=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/saut/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/saut')))]
immobile=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/immobile/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/immobile')))]
attaqueDown=[pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png'),(pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/attaqueDown/'+str(i)+'.png').get_height()//2)) for i in range(len(os.listdir('Personnages/'+Personnage+'/attaqueDown')))]
hit=pygame.transform.scale(pygame.image.load('Personnages/'+Personnage+'/hit.png'),(pygame.image.load('Personnages/'+Personnage+'/hit.png').get_width()//2,pygame.image.load('Personnages/'+Personnage+'/hit.png').get_height()//2))
rect=pygame.Rect(600,600,626,486)
taille=[68,76]
offset=[0,0]    
speedAnim=6
speed=6
jumpPower=14
poids=110
attaqueDroite=[60,40,48,20,10,10,100,20,360,270,90]#w,h,x,y,orientation,degats,echelle,kbBase,startup,active,latence
attaqueDroiteAir=[60,40,48,20,20,10,100,20,250,300,200]
attaqueGauche=[60,40,-40,20,160,20,100,20,250,300,200]
attaqueGaucheAir=[60,40,-40,20,160,20,100,20,250,300,200]
attaqueHaut=[115,44,-20,-30,90,5,200,20,180,360,90]
attaqueBas=[132,94,0,0,50,7,100,20,180,270,0]
      