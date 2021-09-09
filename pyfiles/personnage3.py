"""
Fichier : 'personnage3.py'
Contenu : Stats du personnnage 3
Auteur : Evan Le Bigot
"""

import pygame
import variables as v

from Personnages.Kirby import Stats as Kirby


class Player(pygame.sprite.Sprite):
    
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.combattant=Kirby
        self.name="player3"
        self.image = pygame.Surface((self.combattant.taille[0],self.combattant.taille[1]))
        self.image.fill((255,255,255))
        self.displayedImage=self.combattant.marche[0]
        self.rect = pygame.Rect(400,50,self.combattant.taille[0],self.combattant.taille[1])  
        self.mask = pygame.mask.from_surface(self.displayedImage)
        self.velocity = [0, 0]
        self.vies=0
        self.elimine=False
        self.attaque=''
        self.shield=0
        self.shielding=False
        self.shieldTemps=0
        self.attackTime=0
        self.doubleJump=1
        self.enTrainDattaquer=False
        self.isAttacked=False
        self.attaqueJoueur=[]
        self.Stun=False      
        self.kb=0
        self.statsAttaque=[0]*7#["orientation","dégât","echelle de kb","kb de base","startup","active frame","endlag"]
        self.pourcentage=0
        self.sursol=False     
        self.frameAnim=0
        self.animPrev=''
        self.frameMort=0
        self.Mort=False
        self.finStartup=0
        self.finActiveFrame=0
        self.finEndlag=0
        self.posMort=[]
        self.lieuMort=''
        self.spawnPoint=(400,50)
        self.moveKeys=v.keysTaken[12:18]
        self.orientation="Droite"
        #self.affichagePourcent=font.render(('Pourcentage du joueur 1 : '+str(self.pourcentage)+"%"), True, (255,255,255))
    
    def gravity(self):
        if self.velocity[1]<8:
            self.velocity[1] += float(v.gravite)
    
    def update(self):
        self.rect.move_ip(self.velocity)
    
    def anim(self,n,keysHolded,moveKeys,screen,animPrev):    
        displayedImage=0
        if self.isAttacked and self.combattant.hit!=0:
            n=0
            if self.orientation=='Gauche':              
                    screen.blit(pygame.transform.flip(self.combattant.hit,True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.hit.get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.hit.get_size()[1]))
                    displayedImage=pygame.transform.flip(self.combattant.hit,True,False)
            else:    
                screen.blit(self.combattant.hit,(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.hit.get_size()[1]))
                displayedImage=self.combattant.hit
        elif self.enTrainDattaquer:
            if animPrev!="attaque":
                n=0
            
            if self.attaque=='up' and self.combattant.attaqueUp!=[]:   
                if self.orientation=='Gauche':              
                    screen.blit(pygame.transform.flip(self.combattant.attaqueUp[n//self.combattant.speedAnim],True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.attaqueUp[n//self.combattant.speedAnim].get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.attaqueUp[n//self.combattant.speedAnim].get_size()[1]))
                    displayedImage=pygame.transform.flip(self.combattant.attaqueUp[n//self.combattant.speedAnim],True,False)
                else:    
                    screen.blit(self.combattant.attaqueUp[n//self.combattant.speedAnim],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.attaqueUp[n//self.combattant.speedAnim].get_size()[1]))
                    displayedImage=self.combattant.attaqueUp[n//self.combattant.speedAnim]
                n+=1
                if n>=len(self.combattant.attaqueUp)*self.combattant.speedAnim:
                    n=0
            elif self.attaque=='down' and self.combattant.attaqueDown!=[]:   
                if self.orientation=='Gauche':              
                    screen.blit(pygame.transform.flip(self.combattant.attaqueDown[n//self.combattant.speedAnim],True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.attaqueDown[n//self.combattant.speedAnim].get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.attaqueDown[n//self.combattant.speedAnim].get_size()[1]))
                    displayedImage=pygame.transform.flip(self.combattant.attaqueDown[n//self.combattant.speedAnim],True,False)
                else:    
                    screen.blit(self.combattant.attaqueDown[n//self.combattant.speedAnim],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.attaqueDown[n//self.combattant.speedAnim].get_size()[1]))
                    displayedImage=self.combattant.attaqueDown[n//self.combattant.speedAnim]
                n+=1
                if n>=len(self.combattant.attaqueDown)*self.combattant.speedAnim:
                    n=0
            elif self.attaque=='air' and self.combattant.attaqueAir!=[]:
                if self.orientation=='Gauche':              
                    screen.blit(pygame.transform.flip(self.combattant.attaqueAir[n//self.combattant.speedAnim],True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.attaqueAir[n//self.combattant.speedAnim].get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.attaqueAir[n//self.combattant.speedAnim].get_size()[1]))
                    displayedImage=pygame.transform.flip(self.combattant.attaqueAir[n//self.combattant.speedAnim],True,False)
                else:    
                    screen.blit(self.combattant.attaqueAir[n//self.combattant.speedAnim],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]))
                    displayedImage=self.combattant.attaqueAir[n//self.combattant.speedAnim]
                n+=1
                if n>=len(self.combattant.attaqueAir)*self.combattant.speedAnim:
                    n=0
            else:  
                if self.orientation=='Gauche':
              
                    screen.blit(pygame.transform.flip(self.combattant.attaque[n//self.combattant.speedAnim],True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.attaque[n//self.combattant.speedAnim].get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.attaque[n//self.combattant.speedAnim].get_size()[1]))
                    displayedImage=pygame.transform.flip(self.combattant.attaque[n//self.combattant.speedAnim],True,False)
                else:    
                    screen.blit(self.combattant.attaque[n//self.combattant.speedAnim],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]))
                    displayedImage=self.combattant.attaque[n//self.combattant.speedAnim]
                n+=1
                if n>=len(self.combattant.attaque)*self.combattant.speedAnim:
                    n=0
            animPrev="attaque"
        elif self.velocity[1]<0:
            if animPrev!=self.moveKeys[0]:
                n=0
            if self.orientation=='Gauche':
                screen.blit(pygame.transform.flip(self.combattant.saut[n//self.combattant.speedAnim],True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.saut[n//self.combattant.speedAnim].get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.saut[n//self.combattant.speedAnim].get_size()[1]))    
                displayedImage=pygame.transform.flip(self.combattant.saut[n//self.combattant.speedAnim],True,False)
            else:
                screen.blit(self.combattant.saut[n//self.combattant.speedAnim],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]))
                displayedImage=self.combattant.saut[n//self.combattant.speedAnim]
            n+=1
            if n>=len(self.combattant.saut)*self.combattant.speedAnim:
                n=len(self.combattant.saut)*self.combattant.speedAnim-1
            animPrev=self.moveKeys[0]
        
        elif self.velocity[0]!=0 and not self.Stun and self.sursol:
            if self.orientation=='Gauche' :
                if animPrev!=self.moveKeys[1]:
                    n=0
                screen.blit(pygame.transform.flip(self.combattant.marche[n//self.combattant.speedAnim],True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.marche[n//self.combattant.speedAnim].get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.marche[n//self.combattant.speedAnim].get_size()[1]))
                displayedImage=pygame.transform.flip(self.combattant.marche[n//self.combattant.speedAnim],True,False)
                n+=1
                if n>=len(self.combattant.marche)*self.combattant.speedAnim:
                    n=0
                animPrev=self.moveKeys[1]  
            elif self.orientation=='Droite' :
                if animPrev!=self.moveKeys[3]:
                    n=0
                screen.blit(self.combattant.marche[n//self.combattant.speedAnim],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.marche[n//self.combattant.speedAnim].get_size()[1]))
                displayedImage=self.combattant.marche[n//self.combattant.speedAnim]
                n+=1
                if n>=len(self.combattant.marche)*self.combattant.speedAnim:
                    n=0
                animPrev=self.moveKeys[3]
        else : 
            if animPrev!="marche":
                    n=0
            
            if self.orientation=='Gauche':
                if self.sursol:                        
                    screen.blit(pygame.transform.flip(self.combattant.immobile[n//self.combattant.speedAnim],True,False),(self.rect.x+self.combattant.offset[0]+self.combattant.immobile[0].get_size()[0]-self.combattant.immobile[n//self.combattant.speedAnim].get_size()[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.immobile[n//self.combattant.speedAnim].get_size()[1]))
                    displayedImage=pygame.transform.flip(self.combattant.immobile[n//self.combattant.speedAnim],True,False)
                else:
                    screen.blit(pygame.transform.flip(self.combattant.saut[-1],True,False),(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]))    
                    displayedImage=pygame.transform.flip(self.combattant.saut[-1],True,False)
            else: 
                if self.sursol:  
                    screen.blit(self.combattant.immobile[n//self.combattant.speedAnim],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]+self.combattant.immobile[0].get_size()[1]-self.combattant.immobile[n//self.combattant.speedAnim].get_size()[1]))                        
                    displayedImage=self.combattant.immobile[n//self.combattant.speedAnim]
                else:
                    screen.blit(self.combattant.saut[-1],(self.rect.x+self.combattant.offset[0],self.rect.y+self.combattant.offset[1]))                            
                    displayedImage=self.combattant.saut[-1]
            n+=1
            if n>=len(self.combattant.immobile)*self.combattant.speedAnim:
                n=0
            
            animPrev="marche"
            
        return n,animPrev,displayedImage
    
    def animMort(self,player,frameMortDuJoueur,lieuMort,posMort,explosion,screen):
      
        """se déclenche quand  un joueur est mort"""
        
        if frameMortDuJoueur==20*2:  # cette variable est l'avancée de l'animation en fonction du temps, ici, si elle atteint la fin de l'animation, elle est égale à 0 et l'anim s'arrete
            return 0
        if lieuMort=='bas':  #Si le personnnage est mort en bas, on va orienter l'animation vers le bas avec pygame.transform.rotate(). l'orientation de l'animation est la seule valeur qui distingue les trois conditions suivantes
            screen.blit(pygame.transform.rotate(explosion[frameMortDuJoueur//2],90),(posMort[0]-120,400)) #on affiche ici à l'aide de la liste précédement faite l'animation orientée à 90°
        elif lieuMort=='gauche':#voir les commetaires précédents
            screen.blit(explosion[frameMortDuJoueur//2],(-100,posMort[1]-120))
        elif lieuMort=='droite':#voir les commetaires précédents
            screen.blit(pygame.transform.flip(explosion[frameMortDuJoueur//2],True,False),(900,posMort[1]-120))  
        else:
            screen.blit(pygame.transform.rotate(explosion[frameMortDuJoueur//2],270),(posMort[0]-120,-100))
        return frameMortDuJoueur+1 # renvoie l'avancée de l'animation + 1
    
    class carrerouge:
        """C'est la boite de collision du coup du joueur 1"""
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)   
            self.image=pygame.Surface((20,20))
            self.image.fill((255,0,0))
            self.rect = pygame.Rect(10000,1000,20,20)
            self.mask=pygame.mask.from_surface(self.image)