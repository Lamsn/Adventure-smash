# -*- coding: utf-8 -*-
"""



"""
import pygame,os.path
Personnage="Koopa"
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
attaqueDroite=[170,100,20,-34,20,10,100,20,600,300,200]#w,h,x,y,orientation,degats,echelle,kbBase,startup,active,latence
attaqueDroiteAir=[170,100,20,-34,40,20,100,20,600,300,200]
attaqueGauche=[170,100,-150,-34,160,20,100,20,600,300,200]
attaqueGaucheAir=[170,100,-30,-34,140,20,100,20,600,300,200]
attaqueHaut=[74,64,0,0,90,5,200,20,0,360,200]
attaqueBas=[48,80,0,0,50,7,100,20,0,270,150]
      