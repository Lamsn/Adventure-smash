"""
Fichier : 'm_ecran_fin.py'
Contenu : Menu fin du jeu
Auteur : Noé Lacaille
"""

import pygame

def main():
    
    import variables as v
    import functions as f
    import targetSmash, main_menu
    
    # WINDOW
    
    trans=True
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    
    # VARIABLES
    
    bg=f.load('../img/General/Backgrounds/yellow.jpg',(v.W,v.H))
    time=f"{v.temps//60}min {v.temps%60}s {v.temps%1000}ms"
    replay_clic=menu_clic=quit_clic=False
    replay_bool=menu_bool=quit_bool=False
    
    # SPECIAL COLORS
    
    main_RED=(229,77,38)
    main_GREEN=(141,185,62)
    main_ORANGE=(250,151,34)
    under_RED=(128,66,55)
    under_GREEN=(89,114,66)
    under_ORANGE=(138,99,53)
    
    # BOUCLE
    
    running=True
    while running:
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
        
        if replay_clic:
            f.transitionSortie()
            targetSmash.main()
            f.transitionSortie()
            replay_clic=False
        elif menu_clic:
            f.transitionSortie()
            main_menu.main()
            f.transitionSortie()
            menu_clic=False
        elif quit_clic:
            f.transitionSortie()
            pygame.quit()
            running=False
        
        # AFFICHAGE
        
        W,H=v.W,v.H
        events=(v.mouse_click,v.mouse_pos)
        v.surface.blit(bg,(0,0))
        
        f.textbox(v.surface,time,100,W/2,H/2+20,color=v.WHITE,police=None)
        f.textbox(v.surface,v.trad['end'][v.lg].upper(),300,W/2,H*1/4,color=v.WHITE)
        replay_clic,replay_bool=f.button1(v.surface,v.trad['replay'][v.lg],(W/4,H*3/4,300,150),replay_clic,replay_bool,events,main_RED,under_RED)
        menu_clic,menu_bool=f.button1(v.surface,v.trad['mainmenu'][v.lg],(W/2,H*3/4,300,150),menu_clic,menu_bool,events,main_GREEN,under_GREEN)
        quit_clic,quit_bool=f.button1(v.surface,v.trad['quit'][v.lg],(W*3/4,H*3/4,300,150),quit_clic,quit_bool,events,main_ORANGE,under_ORANGE)
        
        trans=f.doTrans(trans)
        pygame.display.update()
