"""
Fihcier : 'inGame.py'
Contenu : Code du combat 
Auteur : Evan Le Bigot
"""

import pygame

def main(): #Mise sous forme de fonction pour être utilisée dans le fichier main 
    
    import personnage1,personnage2,personnage3,personnage4,math,Plateformes,m_ecran_fin,random  #importe tous les modules nécessaires  
    import variables as v, functions as f, m_pause
    
    def prendreUnCoups(joueur,rectJoueur,pourcentage,degat,poids,echelleDeKb,KbBase):
        Knockback=((((pourcentage/10+pourcentage*degat/20)*200/(poids+100)*1.4)+18)*echelleDeKb/100)+KbBase
        return Knockback
    W,H=v.W,v.H
    v.surface=pygame.display.set_mode((W,H))#Met la fenêtre en format 1280x720 pixels
    screen=v.surface
    explosion=[pygame.image.load('../img/Animation K.O/'+str(i)+'.png').convert_alpha() for i in range(1,21)]    
    #charge toutes les images de l'animation de l'explosion (car on ne peut pas utiliser de gif sur pygame :\)    
    clock = pygame.time.Clock() 
    montrerHitboxes=False
    if isinstance(v.timeLimit, int):
        if v.timeLimit>0 and v.timeLimit!='∞':
            timeDeb=0
            timeLim=v.timeLimit*60
    pygame.init()
    FPS = 60
    pygame.mixer.music.load("../Sons/backgroundFight/"+str(random.randint(1,7))+".mp3")
    pygame.mixer.music.play(loops=-1, fade_ms = 5000)
    v.joueurRestant=""
    joueurs={"2":[personnage1.Player(),personnage2.Player()],"3":[personnage1.Player(),personnage2.Player(),personnage3.Player()],"4":[personnage1.Player(),personnage2.Player(),personnage3.Player(),personnage4.Player()]}#J'ai fait une liste de tous les joueurs présents dans la partie 
    joueurs=joueurs[str(v.nbp)]
    for i in range(len(joueurs)):
        joueurs[i].combattant=v.combattants[i]
        joueurs[i].image = pygame.Surface((joueurs[i].combattant.taille[0],joueurs[i].combattant.taille[1]))
        joueurs[i].rect = pygame.Rect(joueurs[i].spawnPoint[0],joueurs[i].spawnPoint[1],joueurs[i].combattant.taille[0],joueurs[i].combattant.taille[1])  
    nomsJoueurs=[joueurs[i].name for i in range(len(joueurs))]
    for player in joueurs :
        player.carrerouge.rect=pygame.Rect(10000,1000,20,20)#J'ai affecté cette valeur directement avec un script car y a des problèmes sans faire ça   
        player.carrerouge.image=pygame.Surface((20,20))        
        player.carrerouge.image.fill((255,0,0))
        player.pourcentage=v.pourcentBase
        player.vies=v.nbLives
    if v.matchFormat==1:
        for i in joueurs:
            i.pourcentage=v.nbLifePts
    maps={'map1':[Plateformes.map1.plateforme1(),Plateformes.map1.plateforme2(),Plateformes.map1.plateforme3(),Plateformes.map1.plateforme4()],'map2':[Plateformes.map2.plateforme1()],'map3':[Plateformes.map3.plateforme1(),Plateformes.map3.plateforme2(),Plateformes.map3.plateforme3(),Plateformes.map3.plateforme4(),Plateformes.map3.plateforme5(),Plateformes.map3.plateforme6()],'map4':[Plateformes.map4.plateforme1(),Plateformes.map4.plateforme2(),Plateformes.map4.plateforme3()]}
    plateformes=maps[v.mapChoisie]
    running = True#Etat du jeu. Si running=False, le jeu s'arrête
    keysHolded=[]#Liste qui répertorie les touches que le joueur appuie (pas toutes, seulement celles qui sont utilisées par le jeu)
    
    font=pygame.font.SysFont(None,72) # Police d'écriture du texte 
    time=pygame.time.get_ticks()
    timeAtStart=time
    timeFromStart=0
    stunDeb=True
    sizes={'3':(130,148),'2':(124,148),'1':(96,148),'go':(352,144)}
    anims=[f.load(f'../img/General/Start/{i}.png',sizes[i]) for i in sizes]
    # animTime=[(5000,15000),(20000,30000),(35000,45000),(50000,65000)] # animation + rapide (10000/animation)
    animTime=[(500,1250),(1500,2250),(2500,3250),(3500,4500)] # animation + lente (15000/animation)
    anim_count=0
    pause=f.load('../img/General/Icons/pause.png',(60,60))
    pause_hover=f.load('../img/General/Icons/pause_hover.png',(60,60))
    pause_clic=False
    pause_bool=False
    
    while running:      #Boucle pricipale        
        #screen.blit(pygame.transform.scale(pygame.image.load("../img/Fonds/fond_ciel.jpg").convert(),(1280,720)),(0,0))
        
        time=pygame.time.get_ticks()
        timeFromStart=(time-timeAtStart)
        #variable qui permet d'obtenir le temps actuel(et qui permet de faire des mesures de durées)
        dt = clock.tick(FPS) / 1000  #Limite la vitesse du jeu à 60 FPS       
        try :
            screen.blit(pygame.transform.scale(pygame.image.load('../img/Fonds/'+v.mapChoisie+'.jpg'),(W,H)),(0,0))
        except:
            screen.fill(v.BLACK)#Remplit l'écran de noir
        for player in joueurs : #Au lieu de faire un script pour le joueur 1 et 2, j'ai fait une boucle pour chaque joueurs (ce qui permet aussi de mettre possiblement 100 joueurs dans une seule partie, à voir si un ordi arrive à tenir ça...)                       
            player.mask=pygame.mask.from_surface(player.displayedImage) 
            player.carrerouge.mask=pygame.mask.from_surface(player.carrerouge.image)
        """code sur la mort des joueurs"""        
        for player in joueurs :#Jai mis plusieurs fois cette boucle car certaines actions on besoin d'être dans un certain ordre       
            if player.rect.left < -200 or player.rect.bottom > 1000 or player.rect.right > 1480 or player.rect.top < -300:# Si le joueur est en dehors des limites du terrain, déclenche sa mort
               pygame.mixer.Sound.play(v.Sons[0])
               if player.rect.left < -40 : #Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
                   player.lieuMort='gauche'#Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
               elif player.rect.bottom > 720 : #Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
                   player.lieuMort='bas'#Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
               elif player.rect.right > 1480:
                   player.lieuMort='droite'#Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
               else:
                   player.lieuMort='haut'    
               player.posMort=[player.rect.x,player.rect.y]   # crée une liste sur la position du joueur à sa mort
               player.rect=pygame.Rect(player.spawnPoint[0],player.spawnPoint[1],player.rect.width,player.rect.height)   #On le téléporte ensuite en (200,50)
               player.Stun=False  #le joueur peut à nouveau bouger s'il ne pouvait pas encore le faire
               player.vies-=1
               if player.vies==0:
                   joueurs.pop(int(nomsJoueurs.index(player.name)))
                   nomsJoueurs.pop(int(nomsJoueurs.index(player.name)))
                   if len(joueurs)==1:
                       pygame.mixer.music.load("../Sons/Background.mp3")
                       pygame.mixer.music.play(loops=-1,fade_ms = 5000)
                       v.joueurRestant=nomsJoueurs[0]
                       f.transitionSortie()
                       m_ecran_fin.main()
               player.pourcentage=v.pourcentBase #Le joueur revient à 0%
               player.Mort=True   #Variable qui servira à activer la fonction sur l'animation de mort plus tard      
        """Collisions avec la plateforme"""       
        for player in joueurs :
            TouchePlateforme=False 
            for plateforme in plateformes:         
                if player.rect.colliderect(plateforme.rect)==1: #On utilise la méthode colliderect() pour détecter si le joueur touche la plateforme
                    TouchePlateforme=True
                    player.doubleJump=1     
                #On met la variable sursol à True puisque le joueur est sur la plateforme 
                    if plateforme.solid:
                        if player.velocity[1]<0 and plateforme.rect.collidepoint(player.rect.midtop)==1:                  
                            player.rect.top=plateforme.rect.bottom+1
                            player.velocity[1]=0
                        if player.velocity[0]<0 and plateforme.rect.colliderect(player.rect) and player.rect.midleft[0]-player.velocity[0]+1>=plateforme.rect.midright[0]:
                            player.rect.left=plateforme.rect.right-1
                       # on lui redonne également la possibilité de faire un double saut
                        if player.velocity[0]>0 and plateforme.rect.colliderect(player.rect) and player.rect.midright[0]-player.velocity[0]-1<=plateforme.rect.midleft[0]:
                            player.rect.right=plateforme.rect.left+1
                    if player.velocity[1]>0 and not player.sursol and player.rect.midbottom[1]-player.velocity[1]-1<plateforme.rect.y: #Si le joueur était en train de se déplacer vers le bas
                        player.rect.bottom=plateforme.rect.top+1 #Met le joueur au niveau de la plateforme
                        player.velocity[1] =0 #Met la vélocité verticale du joueur à 0              
                        player.sursol=True            
            if not TouchePlateforme:
                player.sursol=False  
        """Applique la gravité"""        
        for player in joueurs :
            if not player.sursol :   #Si le joueur n'est pas sur le sol    
                player.gravity()    #applique la gravité
        """ Dégâts des joueurs """
        for player in joueurs :#Pour chaque joueur
            for i in joueurs :#Pour chaque joueur également
                if player!=i :#Si le joueur de la deuxième boucle et de la première sont identique, ne pas activer la suite
                    if pygame.sprite.collide_mask(player,i.carrerouge) and player.Stun==False :  #Si le joueur touche l'attaque du joueur 2 et qu'il n'est pas paralysé par une attaque        
                        if player.shielding:
                            if time-player.shieldTemps>300:
                                player.shield-=int(i.statsAttaque[1])*3
                                player.shieldTemps=time 
                            if not player.shield<=0:
                                continue
                        player.carrerouge.rect = pygame.Rect(20,20,-2000,-2000)
                        if v.matchFormat==0:
                            player.kb=prendreUnCoups(player,player.rect,player.pourcentage+int(i.statsAttaque[1]),int(i.statsAttaque[1]),player.combattant.poids,int(i.statsAttaque[2]),int(i.statsAttaque[3]))#optimisable #On appelle une fonction qui calcule les dégâts de recul subis par le joueur
                            player.pourcentage+=i.statsAttaque[1]#Le joueur prend les pourcentages de l'attaque subie
                        elif v.matchFormat==1:
                            player.kb=prendreUnCoups(player,player.rect,0,int(i.statsAttaque[1]),player.combattant.poids,int(i.statsAttaque[2]),int(i.statsAttaque[3]))#optimisable #On appelle une fonction qui calcule les dégâts de recul subis par le joueur
                            player.pourcentage-=i.statsAttaque[1]#Le joueur prend les pourcentages de l'attaque subie                           
                            if player.pourcentage<=0:
                                pygame.mixer.Sound.play(v.Sons[0])
                                player.rect=pygame.Rect(player.spawnPoint[0],player.spawnPoint[1],player.rect.width,player.rect.height)   #On le téléporte ensuite en (200,50)
                                player.Stun=False  #le joueur peut à nouveau bouger s'il ne pouvait pas encore le faire
                                player.vies-=1
                                if player.vies==0:
                                    joueurs.pop(int(nomsJoueurs.index(player.name)))
                                    nomsJoueurs.pop(int(nomsJoueurs.index(player.name)))
                                    if len(joueurs)==1:
                                        pygame.mixer.music.load("../Sons/Background.mp3")
                                        pygame.mixer.music.play(loops=-1,fade_ms = 5000)
                                        v.joueurRestant=nomsJoueurs[0]
                                        f.transitionSortie()
                                        m_ecran_fin.main()
                                player.pourcentage=v.nbLifePts #Le joueur revient à 0%
                        player.kb*=float(v.multiKb)
                        if player.kb<70 :
                            pygame.mixer.Sound.play(v.Sons[1])
                        elif player.kb>70 and player.kb<140:
                            pygame.mixer.Sound.play(v.Sons[2])
                        else:
                            pygame.mixer.Sound.play(v.Sons[3])
                        player.Stun=True     #Met le joueur dans un état de paralysie
                        player.isAttacked=True   #variable qui déclenche l'éjection du joueur
                        player.enTrainDattaquer=False #Le joueur a son attaque coupée dans sa course
                        player.attackTime=30     #Le nombre de fois que le joueur se fera éjecter dans le temps 
                        i.attaqueJoueur.append(player.name)
                        player.velocity[1]=0         #Réinitialise la gravité   
                    if player.isAttacked and player.name in i.attaqueJoueur:  #Si le joueur est en train de se faire attaquer
                        player.attackTime-=1            #Réduit le nombre de répétions de 1
                        player.rect.x+=math.cos(math.radians(int(i.statsAttaque[0])))*player.kb/30*player.attackTime/4     #Formule qui calcule les coordonnées x et y du joueur en se prenant le coup.   
                        player.rect.y-=math.sin(math.radians(abs(int(i.statsAttaque[0]))))*player.kb/30*player.attackTime/4      #Formule qui calcule les coordonnées x et y du joueur en se prenant le coup.        
                        if player.attackTime==0: #Si le coup s'est terminé
                            player.Stun=False#Le joueur peut à nouveau se déplacer
                            player.isAttacked=False   #Ne déclenche plus l'éjection                              
                            i.attaqueJoueur.remove(str(player.name))
        """Tous les rendus du jeu"""        
        for player in joueurs :#pour chaque joueur
            player.update()#Déplace le joueur 1 en fonction de sa vélocité       
        for player in joueurs :#pour chaque joueur
            if player.Mort:    #Si le joueur 1 est mort
                player.frameMort=player.animMort(player, player.frameMort, player.lieuMort,player.posMort,explosion,screen)#Fait la fonction de l'animation de mort et met à jour l'avancée de l'animation de mort du joueur 1
                if player.frameMort==0:#Si l'animation se termine
                    player.Mort=False#Met un terme à l'etat de mort du joueur/ arrête l'animation
        for player in joueurs :#pour chaque joueur
            if not player.shielding and player.shield<100:
                player.shield+=1
            player.frameAnim,player.animPrev,player.displayedImage=player.anim(player.frameAnim,keysHolded,player.moveKeys,screen,player.animPrev)
        for i in plateformes:
            screen.blit(i.image,i.rect) #Affiche la plateforme à l'écran 
        for i in range(len(joueurs)):            
            screen.blit(pygame.transform.scale(pygame.image.load("../img/General/Persos/P"+str(joueurs[i].name[-1])+".png").convert_alpha(),(50,50)),(joueurs[i].rect.centerx-25,joueurs[i].rect.y-50))
        
        if montrerHitboxes:
            for i in joueurs:
                try:screen.blit(i.mask.to_surface(), i.rect)#Affiche le joueur 
                except:screen.blit(i.image, i.rect)
        
        if pause_bool:
            pause_button=pause_hover
            f.textbox(screen,v.trad['pause'][v.lg],25,40,80,color=v.BLACK)
        else:
            pause_button=pause
        pause_clic,pause_bool=f.imgbox(v.surface,pause_button,None,40,40,pause_clic,pause_bool,(v.mouse_click,v.mouse_pos))
        if pause_clic:
            m_pause.main()
            pause_clic=False
        if stunDeb:
            for i in joueurs:
                i.Stun=True
        if timeFromStart>animTime[0][0] and timeFromStart<animTime[-1][-1]:
            if timeFromStart>animTime[anim_count][0] and timeFromStart<animTime[anim_count][1]:
                f.imgbox(screen,anims[anim_count],None,W/2,H/2)
            elif timeFromStart>animTime[anim_count][1]:
                anim_count+=1
        elif timeFromStart>animTime[-1][-1] and stunDeb:   
            timeDeb=pygame.time.get_ticks()
            for i in joueurs:
                i.Stun=False
            stunDeb=False
           
        
        """ Contrôles """
        for event in pygame.event.get():  #Pour chaque événement reçu par le jeu      
            if event.type == pygame.QUIT: #Si l'événement quitte le jeu
                pygame.quit()       #Quitte la fenêtre pygame
                running = False     #Casse la boucle
            elif event.type==pygame.MOUSEBUTTONUP:
                v.mouse_click=event.pos			
            elif event.type==pygame.MOUSEMOTION:
                v.mouse_pos=event.pos
            elif event.type == pygame.KEYDOWN : #Si l'événement est une touche appuyée 
                """Controles du joueur """
                if event.key==pygame.K_ESCAPE:
                    running=False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("../Sons/Background.mp3")
                    pygame.mixer.music.play(loops=-1, fade_ms = 5000)
                    return
                if event.key==pygame.K_n:                    
                    if montrerHitboxes==True:
                        montrerHitboxes=False
                    else:
                        montrerHitboxes=True
                for player in joueurs :#pour chaque joueur                   
                    if event.key == player.moveKeys[0] and (player.sursol or player.doubleJump==1) and not player.enTrainDattaquer and not player.Stun and not player.shielding: #Si la touche est celle qui permet au joueur de sauter(moveKeys=[touche de saut,touche gauche,touche bas,touche droite,touche coup]), que le joueur est sur le sol(ou qu'il a toujours son double saut disponible), qu'il n'est pas en train d'attaquer et qu'il n'est pas paralysé par une attaque :
                        if player.moveKeys[0] not in keysHolded:   #Permet d'éviter les doublons dans la liste des touches enfoncées
                            keysHolded.append(player.moveKeys[0])  #Ajoute cette touche à la liste des touches enfoncées                                
                        player.doubleJump=0              #Enlève le double saut(si le joueur est en l'air car elle s'annule avec le code qui donne un double saut au joueur au sol)         
                        player.velocity[1] = -player.combattant.jumpPower    #Donne au joueur de la vitesse vers le haut
                        pygame.mixer.Sound.play(v.Sons[6])
                    elif event.key == player.moveKeys[2] and not player.enTrainDattaquer and not player.Stun and not player.shielding: #Même chose
                        if player.moveKeys[2] not in keysHolded:
                            keysHolded.append(player.moveKeys[2])
                        
                                                               
                    elif event.key == player.moveKeys[1] and not  player.enTrainDattaquer and not player.Stun and not player.shielding:
                        if player.moveKeys[1] not in keysHolded:
                            keysHolded.append(player.moveKeys[1]) 
                        player.orientation="Gauche"     
                    elif event.key == player.moveKeys[3] and not player.enTrainDattaquer and not player.Stun and not player.shielding:
                        if player.moveKeys[3] not in keysHolded:
                            keysHolded.append(player.moveKeys[3])  
                        player.orientation="Droite"                              
                    elif event.key == player.moveKeys[4] and not player.Stun and not player.enTrainDattaquer:                             
                        Stats=player.combattant
                        if player.moveKeys[4] not in keysHolded:
                            keysHolded.append(player.moveKeys[4])
                        if player.moveKeys[3] in keysHolded:#Si la touche pour se déplacer vers la droite est maintenue
                            if player.sursol:#Si le joueur est au sol
                                player.attaque='basic'#L'attaque est vers la droite                            
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueDroite[4],Stats.attaqueDroite[5],Stats.attaqueDroite[6],Stats.attaqueDroite[7],Stats.attaqueDroite[8],Stats.attaqueDroite[9],Stats.attaqueDroite[10]
                            else:#Sinon
                                player.attaque='air'#L'atttaque est en l'air vers la droite
                                #Affecte les caractéristiques de l'attaque dans une liste (les valeurs sont les suivantes : ["orientation en °","dégât en %","echelle de kb en pourcent","kb de base","temps avant que le coup commence, ici 0","temps où l'attaque est activée (en ms)","temps d'attente après le coup"])
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueDroiteAir[4],Stats.attaqueDroiteAir[5],Stats.attaqueDroiteAir[6],Stats.attaqueDroiteAir[7],Stats.attaqueDroiteAir[8],Stats.attaqueDroiteAir[9],Stats.attaqueDroiteAir[10]
                        elif player.moveKeys[1]in keysHolded:#La même chose que précédemment
                            if player.sursol:
                                player.attaque='basic'
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueGauche[4],Stats.attaqueGauche[5],Stats.attaqueGauche[6],Stats.attaqueGauche[7],Stats.attaqueGauche[8],Stats.attaqueGauche[9],Stats.attaqueGauche[10]
                            else:
                                player.attaque='air'
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueGaucheAir[4],Stats.attaqueGaucheAir[5],Stats.attaqueGaucheAir[6],Stats.attaqueGaucheAir[7],Stats.attaqueGaucheAir[8],Stats.attaqueGaucheAir[9],Stats.attaqueGaucheAir[10]
                        elif player.moveKeys[0]in keysHolded:
                            if player.sursol:
                                player.attaque='up' 
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueHaut[4],Stats.attaqueHaut[5],Stats.attaqueHaut[6],Stats.attaqueHaut[7],Stats.attaqueHaut[8],Stats.attaqueHaut[9],Stats.attaqueHaut[10]
                            else:
                                player.attaque='up'                       
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueHaut[4],Stats.attaqueHaut[5],Stats.attaqueHaut[6],Stats.attaqueHaut[7],Stats.attaqueHaut[8],Stats.attaqueHaut[9],Stats.attaqueHaut[10]                        
                        elif player.moveKeys[2]in keysHolded:
                            if player.sursol:
                                player.attaque='down'  
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueHaut[4],Stats.attaqueHaut[5],Stats.attaqueHaut[6],Stats.attaqueHaut[7],Stats.attaqueHaut[8],Stats.attaqueHaut[9],Stats.attaqueHaut[10]
                            else:
                                player.attaque='down'                                           
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueHaut[4],Stats.attaqueHaut[5],Stats.attaqueHaut[6],Stats.attaqueHaut[7],Stats.attaqueHaut[8],Stats.attaqueHaut[9],Stats.attaqueHaut[10]                                                  
                        elif player.orientation=='Gauche':
                            if player.sursol:
                                player.attaque='basic'
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueGauche[4],Stats.attaqueGauche[5],Stats.attaqueGauche[6],Stats.attaqueGauche[7],Stats.attaqueGauche[8],Stats.attaqueGauche[9],Stats.attaqueGauche[10]
                            else:
                                player.attaque='air'
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueGaucheAir[4],Stats.attaqueGaucheAir[5],Stats.attaqueGaucheAir[6],Stats.attaqueGaucheAir[7],Stats.attaqueGaucheAir[8],Stats.attaqueGaucheAir[9],Stats.attaqueGaucheAir[10]
                        elif player.orientation=='Droite':
                            if player.sursol:#Si le joueur est au sol
                                player.attaque='basic'#L'attaque est vers la droite
                                #Affecte les caractéristiques de l'attaque dans une liste (les valeurs sont les suivantes : ["orientation en °","dégât en %","echelle de kb en pourcent","kb de base","temps d'attaque en ms"])
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueDroite[4],Stats.attaqueDroite[5],Stats.attaqueDroite[6],Stats.attaqueDroite[7],Stats.attaqueDroite[8],Stats.attaqueDroite[9],Stats.attaqueDroite[10]
                            else:#Sinon
                                player.attaque='basic'#L'atttaque est en l'air vers la droite
                                #Affecte les caractéristiques de l'attaque dans une liste (les valeurs sont les suivantes : ["orientation en °","dégât en %","echelle de kb en pourcent","kb de base","temps avant que le coup commence, ici 0","temps où l'attaque est activée (en ms)","temps d'attente après le coup"])
                                player.statsAttaque[0],player.statsAttaque[1],player.statsAttaque[2],player.statsAttaque[3],player.statsAttaque[4],player.statsAttaque[5],player.statsAttaque[6]=Stats.attaqueDroiteAir[4],Stats.attaqueDroiteAir[5],Stats.attaqueDroiteAir[6],Stats.attaqueDroiteAir[7],Stats.attaqueDroiteAir[8],Stats.attaqueDroiteAir[9],Stats.attaqueDroiteAir[10]
                        
                        player.enTrainDattaquer=True#Le joueur est en train d'attaquer
                        player.finStartup=time+int(player.statsAttaque[4])#Temps où le joueur a fini le startup de l'attaque
                        player.finActiveframe=time+int(player.statsAttaque[4])+int(player.statsAttaque[5])#Le temps pour lequel la hitbox de l'attaque prend fin
                        player.finEndlag=time+int(player.statsAttaque[4])+int(player.statsAttaque[5])+int(player.statsAttaque[6])#temps où le joueur peut agir à nouveau
                    elif event.key == player.moveKeys[5] and not player.Stun and not player.enTrainDattaquer and player.sursol:
                        if player.moveKeys[5] not in keysHolded:   #Permet d'éviter les doublons dans la liste des touches enfoncées
                            keysHolded=[player.moveKeys[5]]  #Ajoute cette touche à la liste des touches enfoncées           
            elif event.type == pygame.KEYUP:#Si l'événement est une touche qui n'est plus pressée
                for player in joueurs :
                    if event.key == player.moveKeys[1] and player.moveKeys[1] in keysHolded :#Si cette touche est celle qui permet de se déplacer vers la gauche
                        keysHolded.remove(player.moveKeys[1])#Supprimer cette touche de la liste des touches maintenues
                    elif event.key == player.moveKeys[0] and player.moveKeys[0] in keysHolded:#Et ainsi de suite, c'est la même chose 
                        keysHolded.remove(player.moveKeys[0])
                    elif event.key == player.moveKeys[2] and player.moveKeys[2] in keysHolded:
                        keysHolded.remove(player.moveKeys[2])
                    elif event.key == player.moveKeys[3] and player.moveKeys[3] in keysHolded:
                        keysHolded.remove(player.moveKeys[3])
                    elif event.key == player.moveKeys[4] and player.moveKeys[4] in keysHolded:
                        keysHolded.remove(player.moveKeys[4])
                    elif event.key == player.moveKeys[5] and player.moveKeys[5] in keysHolded:
                        keysHolded.remove(player.moveKeys[5])
                        player.shielding=False
                    if event.key == player.moveKeys[1] or event.key == player.moveKeys[3] :#Si la touche est une touche qui déplace vers la droite ou la gauche le joueur :
                        player.velocity[0] = 0 #Réinitialise la vitesse horizontale
        """actions hors coups"""
        for i in keysHolded: #Pour toutes les touches maintenues
            for player in joueurs :#pour chaque joueur
                if i==player.moveKeys[1]:#Si la touche est celle qui permet de se déplacer vers la gauche :
                    player.velocity[0] = -player.combattant.speed#Déplace le joueur vers la gauche, même logique pour le reste
                elif i==player.moveKeys[2]:
                    if player.velocity[1]>0:
                        player.velocity[1]=15
                elif i==player.moveKeys[3]:
                    player.velocity[0] = player.combattant.speed 
                elif i==player.moveKeys[5]:
                    player.shielding=True
                    player.shield-=0.5
                    player.velocity[0]=0
                    tailleShield=int(round(80*player.shield/100))
                    if tailleShield<0:
                        tailleShield=0
                    screen.blit(pygame.transform.scale(pygame.image.load("../img/General/Icons/shield.png"),(tailleShield,tailleShield)).convert_alpha(),(player.rect.centerx-tailleShield//2,player.rect.centery-tailleShield//2))                       
                    if player.shield==0:
                        player.shielding=False
        """Hitbox de l'attaque"""
       
        for player in joueurs :
            
            if player.enTrainDattaquer :#Si le joueur est en train d'attaquer :
                if player.sursol:  #Si le joueur est sur le sol : 
                    player.velocity[0]=0   #Le joueur ne peut pas bouger pendant l'attaque                    
                if time < player.finStartup :#Si le joueur est dans son startup : 
                    player.stun=True#le joueur ne peut pas bouger
                elif time > player.finStartup and time < player.finActiveframe :#Sinon si le joueur est dans ses "active frames"
                    
                    if time-(pygame.time.get_ticks()-time)-3 <= player.finStartup:
                        pygame.mixer.Sound.play(v.Sons[4])
                    if player.attaque=='basic':#Si l'attaque est vers la droite :                     
                        if player.orientation=='Droite':
                            player.carrerouge.rect=pygame.Rect(player.rect.x+player.combattant.attaqueDroite[2],player.rect.y+player.combattant.attaqueDroite[3],player.combattant.attaqueDroite[0],player.combattant.attaqueDroite[1])#La hitbox de l'attaque est à droite du joueur
                            player.carrerouge.image=pygame.Surface((player.combattant.attaqueDroite[0],player.combattant.attaqueDroite[1]))
                            if montrerHitboxes:
                                screen.blit(pygame.transform.scale(player.carrerouge().image,(player.combattant.attaqueDroite[0],player.combattant.attaqueDroite[1])),(player.rect.x+player.combattant.attaqueDroite[2],player.rect.y+player.combattant.attaqueDroite[3]))#Affiche la hitbox du coup. peut être supprimable par la suite, c'est juste à titre indicatif pour l'instant. C'est surtout la ligne du haut qui importe
                        elif player.orientation=='Gauche':                            
                            player.carrerouge.rect=pygame.Rect(player.rect.x+player.combattant.attaqueGauche[2],player.rect.y+player.combattant.attaqueGauche[3],player.combattant.attaqueGauche[0],player.combattant.attaqueGauche[1]) 
                            player.carrerouge.image=pygame.Surface((player.combattant.attaqueGauche[0],player.combattant.attaqueGauche[1]))                        
                            if montrerHitboxes:
                                screen.blit(pygame.transform.scale(player.carrerouge().image,(player.combattant.attaqueGauche[0],player.combattant.attaqueGauche[1])),(player.rect.x+player.combattant.attaqueGauche[2],player.rect.y+player.combattant.attaqueGauche[3]))
                    elif player.attaque=='air':
                        if player.orientation=='Droite':
                            player.carrerouge.rect=pygame.Rect(player.rect.x+player.combattant.attaqueDroiteAir[2],player.rect.y+player.combattant.attaqueDroiteAir[3],player.combattant.attaqueDroiteAir[0],player.combattant.attaqueDroiteAir[1])#La hitbox de l'attaque est à droite du joueur
                            player.carrerouge.image=pygame.Surface((player.combattant.attaqueDroiteAir[0],player.combattant.attaqueDroiteAir[1]))
                            if montrerHitboxes:
                                screen.blit(pygame.transform.scale(player.carrerouge().image,(player.combattant.attaqueDroiteAir[0],player.combattant.attaqueDroiteAir[1])),(player.rect.x+player.combattant.attaqueDroiteAir[2],player.rect.y+player.combattant.attaqueDroiteAir[3]))#Affiche la hitbox du coup. peut être supprimable par la suite, c'est juste à titre indicatif pour l'instant. C'est surtout la ligne du haut qui importe
                        elif player.orientation=='Gauche':   
                            player.carrerouge.rect=pygame.Rect(player.rect.x+player.combattant.attaqueGaucheAir[2],player.rect.y+player.combattant.attaqueGaucheAir[3],player.combattant.attaqueGaucheAir[0],player.combattant.attaqueGaucheAir[1]) 
                            player.carrerouge.image=pygame.Surface((player.combattant.attaqueGaucheAir[0],player.combattant.attaqueGaucheAir[1]))                        
                            if montrerHitboxes:
                                screen.blit(pygame.transform.scale(player.carrerouge().image,(player.combattant.attaqueGaucheAir[0],player.combattant.attaqueGaucheAir[1])),(player.rect.x+player.combattant.attaqueGaucheAir[2],player.rect.y+player.combattant.attaqueGaucheAir[3]))      
                        
                    elif player.attaque=='down'or player.attaque=='downAir' and player.combattant.attaqueBas!=[0,0,0,0]:
                        player.carrerouge.rect=pygame.Rect(player.rect.x+player.combattant.attaqueBas[2],player.rect.y+player.combattant.attaqueBas[3],player.combattant.attaqueBas[0],player.combattant.attaqueBas[1])
                        player.carrerouge.image=pygame.Surface((player.combattant.attaqueBas[0],player.combattant.attaqueBas[1]))     
                        if montrerHitboxes:
                            screen.blit(pygame.transform.scale(player.carrerouge().image,(player.combattant.attaqueBas[0],player.combattant.attaqueBas[1])),(player.rect.x+player.combattant.attaqueBas[2],player.rect.y+player.combattant.attaqueBas[3]))
                    elif player.attaque=='up'or player.attaque=='upAir' and player.combattant.attaqueHaut!=[0,0,0,0]:
                        player.carrerouge.rect=pygame.Rect(player.rect.x+player.combattant.attaqueHaut[2],player.rect.y+player.combattant.attaqueHaut[3],player.combattant.attaqueHaut[0],player.combattant.attaqueHaut[1]) 
                        player.carrerouge.image=pygame.Surface((player.combattant.attaqueHaut[0],player.combattant.attaqueHaut[1]))
                        if montrerHitboxes:
                            screen.blit(pygame.transform.scale(player.carrerouge().image,(player.combattant.attaqueHaut[0],player.combattant.attaqueHaut[1])),(player.rect.x+player.combattant.attaqueHaut[2],player.rect.y+player.combattant.attaqueHaut[3]))                  
                elif time>player.finActiveframe:#Si le joueur est dans un état d'endlag                                        
                    player.carrerouge.rect = pygame.Rect(20,20,-2000,-2000)#La hitbox du coup est téléportée très loin pour éviter tout souci                                                   
                    if time<player.finEndlag:
                        player.stun=True
                if time>player.finEndlag : #Si le joueur a fini son etat d'endlag
                    player.stun=False# le joueur peut à nouveau agir
                    player.enTrainDattaquer=False# le joueur n'est plus en train d'attaquer
        if isinstance(v.timeLimit, int):
            if v.timeLimit>0 and v.timeLimit!='∞' and timeDeb!=0:
                timeActuel=timeLim-(time-timeDeb)//1000
                renduTime=f"{timeActuel//60}min {timeActuel%60}s"
                f.textbox(screen,renduTime,72,W/2,50,color=v.WHITE)
                if timeActuel==0:
                    pygame.mixer.music.load("../Sons/Background.mp3")
                    pygame.mixer.music.play(loops=-1,fade_ms = 5000)
                    f.transitionSortie()
                    m_ecran_fin.main()
        if v.matchFormat==0:
            if "player1" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP1 = font.render((str(joueurs[0].pourcentage)+"%(∞)"), True, (255,0,0)) #Crée un rendu du texte avec les infos utiles
                else:
                    renduPourcentP1 = font.render((str(joueurs[0].pourcentage)+"%("+str(joueurs[0].vies)+")"), True, (255,0,0)) #Crée un rendu du texte avec les infos utiles
                screen.blit(renduPourcentP1, (0, H-65))
            if "player2" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP2 = font.render((str(joueurs[1].pourcentage)+"%(∞)"), True, (0,0,255)) #Crée un rendu du texte avec les infos utiles
                else:
                    renduPourcentP2 = font.render((str(joueurs[1].pourcentage)+"%("+str(joueurs[1].vies)+")"), True, (0,0,255)) #Crée un rendu du texte avec les infos utiles
                screen.blit(renduPourcentP2, (1100, H-65))#Affiche le texte des infos utiles
            if "player3" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP3 = font.render((str(joueurs[2].pourcentage)+"%(∞)"), True, (0,255,0))
                else:
                    renduPourcentP3 = font.render((str(joueurs[2].pourcentage)+"%("+str(joueurs[2].vies)+")"), True, (0,255,0)) #Crée un rendu du texte avec les infos utiles
                screen.blit(renduPourcentP3, (400, H-65))
            if "player4" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP4 = font.render((str(joueurs[3].pourcentage)+"%(∞)"), True, (255,255,0))
                else:
                    renduPourcentP4 = font.render((str(joueurs[3].pourcentage)+"%("+str(joueurs[2].vies)+")"), True, (255,255,0)) #Crée un rendu du texte avec les infos utiles       
                screen.blit(renduPourcentP4, (800, H-65))
        elif v.matchFormat==1:
            if "player1" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP1 = font.render((str(joueurs[0].pourcentage)+"pv(∞)"), True, (255,0,0)) #Crée un rendu du texte avec les infos utiles
                else:
                    renduPourcentP1 = font.render((str(joueurs[0].pourcentage)+"pv("+str(joueurs[0].vies)+")"), True, (255,0,0)) #Crée un rendu du texte avec les infos utiles
                screen.blit(renduPourcentP1, (0, H-65))
            if "player2" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP2 = font.render((str(joueurs[1].pourcentage)+"pv(∞)"), True, (0,0,255)) #Crée un rendu du texte avec les infos utiles
                else:
                    renduPourcentP2 = font.render((str(joueurs[1].pourcentage)+"pv("+str(joueurs[1].vies)+")"), True, (0,0,255)) #Crée un rendu du texte avec les infos utiles
                screen.blit(renduPourcentP2, (1100, H-65))#Affiche le texte des infos utiles
            if "player3" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP3 = font.render((str(joueurs[2].pourcentage)+"pv(∞)"), True, (0,255,0))
                else:
                    renduPourcentP3 = font.render((str(joueurs[2].pourcentage)+"pv("+str(joueurs[2].vies)+")"), True, (0,255,0)) #Crée un rendu du texte avec les infos utiles
                screen.blit(renduPourcentP3, (400, H-65))
            if "player4" in nomsJoueurs:
                if v.nbLives==0:
                    renduPourcentP4 = font.render((str(joueurs[3].pourcentage)+"pv(∞)"), True, (255,255,0))
                else:
                    renduPourcentP4 = font.render((str(joueurs[3].pourcentage)+"pv("+str(joueurs[2].vies)+")"), True, (255,255,0)) #Crée un rendu du texte avec les infos utiles       
                screen.blit(renduPourcentP4, (800, H-65))
        pygame.display.update()  #Met à jour l'écran
