"""
Fichier : 'main.py'
Contenu : Boucle principale du jeu
Auteurs :
    - lamsen
    - unearobase
    - 3 autres collaborateurs
"""

game_name='Adventure Smash'
last_version='v2.0.0'

# --------------------------------------------------------------------------- #

import sys
try:
    import pygame
except:
    print("\nFR -- Erreur d'exécution : vous n'avez pas installé la bibliothèque Pygame. Veuillez l'installer pour pouvoir lancer le programme.")
    print("Si vous ne parvenez pas à résoudre ce problème, vous pouvez nous contacter à l'adresse email suivante : projet.pygame.groupek@gmail.com")
    print("\nEN -- Runtime Error: you did not install the Pygame library. Please install it to be able to launch the program.")
    print("If you are unable to resolve this issue, you can contact us at the following email address: projet.pygame.groupek@gmail.com")
    sys.exit()

pygame_version=pygame.__version__
if int(pygame_version[:pygame_version.index('.')])>=2:
    import variables as v, functions as f, main_menu
    #info=pygame.display.Info()
    #v.W,v.H=round(0.8*info.current_w),round(0.8*info.current_h)
    v.W,v.H=1280,720
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    pygame.display.set_icon(pygame.image.load("../img/General/Icons/play.png"))
    logo=f.load('../img/General/Logo/logo.png',(v.W,v.H))
    pygame.display.set_caption(f"{game_name} - {last_version}")
    keyp=False
    running=True
    while running:
        for event in pygame.event.get():        
            if event.type==pygame.QUIT: 
                pygame.quit()
                running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    running=False
                else:
                    main_menu.main()
        v.surface.fill(v.BLACK)
        f.imgbox(v.surface,logo,None,v.W/2,v.H/2)
        f.imgbox(v.surface,logo,None,v.W/2,v.H*2/5)
        f.textbox(v.surface,last_version,20,v.W/2,v.H*3/5,color=v.WHITE)
        f.textbox(v.surface,"Press any key to continue",60,v.W/2,v.H*3/4,color=v.WHITE,police='arial black')
        f.textbox(v.surface,"Credits : Evan LE BIGOT, Noé LACAILLE, Jean-Marc WU, Louis COURTOUX, Kevin NGE   //   Copyright © March 2021 - All rights reserved",20,v.W/2,v.H-40,color=v.WHITE)
        pygame.display.update()
    print("\nEND\nCredits : Evan LE BIGOT (Project Manager), Noé LACAILLE, Jean-Marc WU, Louis COURTOUX, Kevin NGE\nCopyright © March 2021 - All rights reserved")
else:
    print(f"\nFR -- Erreur d'exécution : votre version de Pygame ({pygame_version}) est trop ancienne. Veuillez la mettre à jour (version 2.0.0 requise).")
    print("Si vous ne parvenez pas à résoudre ce problème, vous pouvez nous contacter à l'adresse email suivante : projet.pygame.groupek@gmail.com")
    print(f"\nEN -- Runtime Error: your version of Pygame ({pygame_version}) is too old. Please update it (version 2.0.0 required).")
    print("If you are unable to resolve this issue, you can contact us at the following email address: projet.pygame.groupek@gmail.com")
