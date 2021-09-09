"""
Fichier : 'm_pause.py'
Contenu : Menu pause
Auteur : unearobase
"""

import pygame

def main(game='inGame'):
    
    import variables as v
    import functions as f
    import main_menu
    
    if game=='inGame':
        import inGame
    elif game=='parcours':
        import parcours
    elif game=='targetSmash':
        import targetSmash
    
    # WINDOW
    
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    
    # VARIABLES
    
    bg=f.load('../img/General/Backgrounds/yellow.jpg',(v.W,v.H))
    continue_clic=replay_clic=mainmenu_clic=False
    continue_bool=replay_bool=mainmenu_bool=False
    
    # SPECIAL COLORS
    
    main_RED=(229,77,38)
    main_GREEN=(141,185,62)
    main_ORANGE=(250,151,34)
    under_RED=(128,66,55)
    under_GREEN=(89,114,66)
    under_ORANGE=(138,99,53)
    
    # BOUCLE
    
    time=pygame.time.get_ticks()-v.timeOff
    running=True
    while running:
        v.timeOff=pygame.time.get_ticks()-time
        v.mouse_click=(-10,-10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()				
                running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    f.transitionSortie()
                    return
            elif event.type==pygame.MOUSEBUTTONUP:
                v.mouse_click=event.pos			
            elif event.type==pygame.MOUSEMOTION:
                v.mouse_pos=event.pos
        
        # EVENEMENTS
        
        if continue_clic:
            return
        elif replay_clic:
            f.transitionSortie()
            if game=='inGame':
                inGame.main()
            elif game=='parcours':
                parcours.main()
            elif game=='targetSmash':
                targetSmash.main()
            replay_clic=False
        elif mainmenu_clic:
            f.transitionSortie()
            main_menu.main()
            mainmenu_clic=False
        
        # AFFICHAGE
        
        W,H=v.W,v.H
        events=(v.mouse_click,v.mouse_pos)
        v.surface.blit(bg,(0,0))
        
        f.textbox(v.surface,v.trad['pause'][v.lg].upper(),200,W/2,H*1.25/4,color=v.WHITE)
        continue_clic,continue_bool=f.button1(v.surface,v.trad['continue'][v.lg],(W/4,H*3/4,300,150),continue_clic,continue_bool,events,main_RED,under_RED)
        replay_clic,replay_bool=f.button1(v.surface,v.trad['replay'][v.lg],(W/2,H*3/4,300,150),replay_clic,replay_bool,events,main_GREEN,under_GREEN)
        mainmenu_clic,mainmenu_bool=f.button1(v.surface,v.trad['mainmenu'][v.lg],(W*3/4,H*3/4,300,150),mainmenu_clic,mainmenu_bool,events,main_ORANGE,under_ORANGE)
        
        pygame.display.update()
