"""
Fihcier : 'parcours.py'
Contenu : Code du Parcours 
Auteur : Evan Le Bigot
"""

import pygame

def main(): #Mise sous forme de fonction pour être utilisée dans le fichier main 
    import personnage1,Plateformes  #importe tous les modules nécessaires  
    import variables as v, functions as f, m_fin_plateforme as fin, m_pause
    v.morts=0
    niveau=1
    W,H=v.W,v.H
    # mouse_pos=(0,0)
    #charge toutes les images de l'animation de l'explosion (car on ne peut pas utiliser de gif sur pygame :\)    
    screen = pygame.display.set_mode((W,H))#Met la fenêtre en format 1280x720 pixels
    # explosion=[pygame.image.load('../img/Animation K.O/'+str(i)+'.png').convert_alpha() for i in range(1,21)]    
    clock = pygame.time.Clock() 
    montrerHitboxes=False         
    if isinstance(v.timeLimit, int):
        if v.timeLimit>0:
            timeDeb=pygame.time.get_ticks()
            timeLim=v.timeLimit*60
    pygame.init()
    FPS = 60
    joueurs=[personnage1.Player()]#J'ai fait une liste de tous les joueurs présents dans la partie 
    # nomsJoueurs=[joueurs[i].name for i in range(len(joueurs))]
    for player in joueurs :
        player.carrerouge.rect=pygame.Rect(10000,1000,20,20)#J'ai affecté cette valeur directement avec un script car y a des problèmes sans faire ça   
        player.carrerouge.image=pygame.Surface((20,20))        
        player.carrerouge.image.fill((255,0,0))
        player.pourcentage=0
        player.vies=v.nbLives
    plateformesLevels={"stage1":[Plateformes.stage1.plateforme1(),Plateformes.stage1.plateforme2(),Plateformes.stage1.plateforme3(),Plateformes.stage1.plateforme4()],"stage2":[Plateformes.stage2.plateforme1(),Plateformes.stage2.plateforme2(),Plateformes.stage2.plateforme3(),Plateformes.stage2.plateforme4()],"stage3":[Plateformes.stage3.plateforme1(),Plateformes.stage3.plateforme2(),Plateformes.stage3.plateforme3(),Plateformes.stage3.plateforme4(),Plateformes.stage3.plateforme5(),Plateformes.stage3.plateforme6()],"stage4":[Plateformes.stage4.plateforme1(),Plateformes.stage4.plateforme2(),Plateformes.stage4.plateforme3(),Plateformes.stage4.plateforme4(),Plateformes.stage4.plateforme5(),Plateformes.stage4.plateforme6(),Plateformes.stage4.plateforme7(),Plateformes.stage4.plateforme8(),Plateformes.stage4.plateforme9()],"stage5":[Plateformes.stage5.plateforme1(),Plateformes.stage5.plateforme2(),Plateformes.stage5.plateforme3(),Plateformes.stage5.plateforme4(),Plateformes.stage5.plateforme5(),Plateformes.stage5.plateforme6(),Plateformes.stage5.plateforme7(),Plateformes.stage5.plateforme8(),Plateformes.stage5.plateforme9(),Plateformes.stage5.plateforme10()],"stage6":[Plateformes.stage6.plateforme1(),Plateformes.stage6.plateforme2(),Plateformes.stage6.plateforme3(),Plateformes.stage6.plateforme4(),Plateformes.stage6.plateforme5(),Plateformes.stage6.plateforme6(),Plateformes.stage6.plateforme7(),Plateformes.stage6.plateforme8(),Plateformes.stage6.plateforme9(),Plateformes.stage6.plateforme10()],'stage7':[Plateformes.stage7.plateforme1(),Plateformes.stage7.plateforme2(),Plateformes.stage7.plateforme3(),Plateformes.stage7.plateforme4(),Plateformes.stage7.plateforme5(),Plateformes.stage7.plateforme6(),Plateformes.stage7.plateforme7()]}
    picsLevels={"stage1":[],"stage2":[Plateformes.stage2.spike1(),Plateformes.stage2.spike2()],"stage3":[],"stage4":[],"stage5":[],"stage6":[],"stage7":[Plateformes.stage7.spike1(),Plateformes.stage7.spike2(),Plateformes.stage7.spike3(),Plateformes.stage7.spike4(),Plateformes.stage7.spike5(),Plateformes.stage7.spike6()]}
    levels2=[Plateformes.stage1(),Plateformes.stage2(),Plateformes.stage3(),Plateformes.stage4(),Plateformes.stage5(),Plateformes.stage6(),Plateformes.stage7()]
    plateformes=[Plateformes.stage1.plateforme1(),Plateformes.stage1.plateforme2(),Plateformes.stage1.plateforme3(),Plateformes.stage1.plateforme4()]
    pics=[]
    running = True#Etat du jeu. Si running=False, le jeu s'arrête
    keysHolded=[]#Liste qui répertorie les touches que le joueur appuie (pas toutes, seulement celles qui sont utilisées par le jeu)
    
    pause=f.load('../img/General/Icons/pause.png',(60,60))
    pause_hover=f.load('../img/General/Icons/pause_hover.png',(60,60))
    pause_clic=False
    pause_bool=False
    
    font=pygame.font.SysFont(None, 100)# Police d'écriture du texte 
    time=pygame.time.get_ticks()
    while running: #Boucle pricipale
        screen.blit(pygame.transform.scale(pygame.image.load("../img/Fonds/map1.jpg").convert(),(1280,720)),(0,0))
        time=pygame.time.get_ticks()
        #variable qui permet d'obtenir le temps actuel(et qui permet de faire des mesures de durées)
        dt = clock.tick(FPS) / 1000  #Limite la vitesse du jeu à 60 FPS       
        for player in joueurs : #Au lieu de faire un script pour le joueur 1 et 2, j'ai fait une boucle pour chaque joueurs (ce qui permet aussi de mettre possiblement 100 joueurs dans une seule partie, à voir si un ordi arrive à tenir ça...)                       
            player.mask=pygame.mask.from_surface(player.displayedImage) 
            player.carrerouge.mask=pygame.mask.from_surface(player.carrerouge.image)
        """code sur la mort des joueurs"""        
        for player in joueurs :#Jai mis plusieurs fois cette boucle car certaines actions on besoin d'être dans un certain ordre       
            if player.rect.left < -200 or player.rect.bottom > 720 or player.rect.right > 1480 or player.rect.top < -300:# Si le joueur est en dehors des limites du terrain, déclenche sa mort
               if player.rect.left < -40 : #Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
                   player.lieuMort='gauche'#Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
               elif player.rect.bottom > 720 : #Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
                   player.lieuMort='bas'#Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
               elif player.rect.right > 1480:
                   player.lieuMort='droite'#Cherche précisément où est mort le joueur pour ensuite mettre l'animation de mort
               else:
                   player.lieuMort='haut'    
               player.posMort=[player.rect.x,player.rect.y]   # crée une liste sur la position du joueur à sa mort
               v.morts+=1
               player.rect=pygame.Rect(levels2[niveau-1].spawnPoint[0],levels2[niveau-1].spawnPoint[1],player.rect.width,player.rect.height)               
               player.Stun=False  #le joueur peut à nouveau bouger s'il ne pouvait pas encore le faire              
               player.pourcentage=0 #Le joueur revient à 0%
               player.Mort=True   #Variable qui servira à activer la fonction sur l'animation de mort plus tard      
        """Collisions avec la plateforme"""       
        for player in joueurs :
            TouchePlateforme=False 
            if player.rect.colliderect(levels2[niveau-1].fin().rect):
                niveau+=1
                try:
                    plateformes=plateformesLevels["stage"+str(niveau)]
                except:
                    f.transitionSortie()
                    fin.main()
                pics=picsLevels["stage"+str(niveau)]
                player.rect=pygame.Rect(levels2[niveau-1].spawnPoint[0],levels2[niveau-1].spawnPoint[1],player.rect.width,player.rect.height)
            for pic in pics:
                if player.rect.colliderect(pic.rect):
                    v.morts+=1
                    player.rect=pygame.Rect(levels2[niveau-1].spawnPoint[0],levels2[niveau-1].spawnPoint[1],player.rect.width,player.rect.height)               
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
        """Tous les rendus du jeu"""        
        for player in joueurs :#pour chaque joueur
            player.update()#Déplace le joueur 1 en fonction de sa vélocité       

        for player in joueurs :#pour chaque joueur      
            player.frameAnim,player.animPrev,player.displayedImage=player.anim(player.frameAnim,keysHolded,player.moveKeys,screen,player.animPrev)
        for i in plateformes:
            screen.blit(i.image,i.rect) #Affiche la plateforme à l'écran  
        for i in pics:
            screen.blit(i.image,i.rect)
        screen.blit(levels2[niveau-1].fin().image,levels2[niveau-1].fin().rect)
        if v.nbLives==0:
            screen.blit(pygame.transform.scale(pygame.image.load("../img/General/P1.png"),(50,50)),(joueurs[0].rect.centerx-25,joueurs[0].rect.y-50))            
        if montrerHitboxes :
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
            m_pause.main('parcours')
            pause_clic=False
        
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
                """Controles du joueur 1"""
                if event.key==pygame.K_ESCAPE:
                    running=False
                    return
                if event.key==pygame.K_n:                    
                    if montrerHitboxes==True:
                        montrerHitboxes=False
                    else:
                        montrerHitboxes=True
                for player in joueurs :#pour chaque joueur
                    if event.key == player.moveKeys[0] and (player.sursol or player.doubleJump==1) and not player.enTrainDattaquer and not player.Stun: #Si la touche est celle qui permet au joueur de sauter(moveKeys=[touche de saut,touche gauche,touche bas,touche droite,touche coup]), que le joueur est sur le sol(ou qu'il a toujours son double saut disponible), qu'il n'est pas en train d'attaquer et qu'il n'est pas paralysé par une attaque :
                        if player.moveKeys[0] not in keysHolded:   #Permet d'éviter les doublons dans la liste des touches enfoncées
                            keysHolded.append(player.moveKeys[0])  #Ajoute cette touche à la liste des touches enfoncées                                
                        player.doubleJump=0              #Enlève le double saut(si le joueur est en l'air car elle s'annule avec le code qui donne un double saut au joueur au sol)         
                        player.velocity[1] = -player.combattant.jumpPower    #Donne au joueur de la vitesse vers le haut
                    elif event.key == player.moveKeys[2] and not player.enTrainDattaquer and not player.Stun: #Même chose
                        if player.moveKeys[2] not in keysHolded:
                            keysHolded.append(player.moveKeys[2])
                        
                                                               
                    elif event.key == player.moveKeys[1] and not  player.enTrainDattaquer and not player.Stun:
                        if player.moveKeys[1] not in keysHolded:
                            keysHolded.append(player.moveKeys[1]) 
                        player.orientation="Gauche"     
                    elif event.key == player.moveKeys[3] and not player.enTrainDattaquer and not player.Stun:
                        if player.moveKeys[3] not in keysHolded:
                            keysHolded.append(player.moveKeys[3])  
                        player.orientation="Droite"                                                
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
                    if event.key == player.moveKeys[1] or event.key == player.moveKeys[3] :#Si la touche est une touche qui déplace vers la droite ou la gauche le joueur :
                        player.velocity[0] = 0 #Réinitialise la vitesse horizontale
        """mouvements"""
        for i in keysHolded: #Pour toutes les touches maintenues
            for player in joueurs :#pour chaque joueur
                if i==player.moveKeys[1]:#Si la touche est celle qui permet de se déplacer vers la gauche :
                    player.velocity[0] = -player.combattant.speed#Déplace le joueur vers la gauche, même logique pour le reste
                elif i==player.moveKeys[2]:
                    if player.velocity[1]>0:
                        player.velocity[1]=15
                elif i==player.moveKeys[3]:
                    player.velocity[0] = player.combattant.speed        
        if v.timeLimit>0:
            timeActuel=timeLim-(time-timeDeb)//1000
            renduTime=f"{timeActuel//60}min {timeActuel%60}s"
            f.textbox(screen,renduTime,100,W/2,80,color=v.WHITE)
            screen.blit(renduTime,(W/2,80))
            if timeActuel==0:
                return
        if v.nbLives==0:
            renduPourcentP1=f"{joueurs[0].pourcentage}%" #Crée un rendu du texte avec les infos utiles
            f.textbox(screen,renduPourcentP1,100,W/2,30,color=v.WHITE) #Affiche le texte des infos utiles
            
        pygame.display.update()  #Met à jour l'écran
