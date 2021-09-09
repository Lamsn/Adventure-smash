"""
Fichier : 'main_menu.py'
Contenu : Menu principal du jeu
Auteur : unearobase
"""

import pygame

def main():
    
    import variables as v
    import functions as f
    import m_smash, m_options, m_bonus
    
    # WINDOW
    
    trans=True
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    
    # VARIABLES
    
    smash_clic=options_clic=bonus_clic=False
    smash_bool=options_bool=bonus_bool=False
    
    red=f.load('../img/General/Backgrounds/red.jpg',(v.W/2,v.H))
    green=f.load('../img/General/Backgrounds/green.jpg',(v.W/2,v.H/2))
    blue=f.load('../img/General/Backgrounds/blue.jpg',(v.W/2,v.H/2))
    pygame.mixer.music.load("../Sons/Background.mp3")
    pygame.mixer.music.play(loops=-1,fade_ms=5000)
    
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
        
        if smash_clic:
            f.transitionSortie()
            m_smash.main()
            f.transitionSortie()
            smash_clic=False
        elif options_clic:
            f.transitionSortie()
            m_options.main()
            f.transitionSortie()
            options_clic=False
        elif bonus_clic:
            f.transitionSortie()
            m_bonus.main()
            f.transitionSortie()
            bonus_clic=False
        
        # AFFICHAGE
        
        W,H=v.W,v.H
        events=(v.mouse_click,v.mouse_pos)
        
        v.surface.blit(red,(0,0))
        f.textbox(v.surface,v.trad['smash'][v.lg],100,W/4,H/2,False,smash_bool,events,v.WHITE,v.BLACK)
        smash_clic,smash_bool=f.eventBools(pygame.Rect(0,0,W/2,H),events,smash_bool,smash_clic)
        
        v.surface.blit(green,(v.W/2,0))
        f.textbox(v.surface,v.trad['options'][v.lg],100,W*3/4,H/4,False,options_bool,events,v.WHITE,v.BLACK)
        options_clic,options_bool=f.eventBools(pygame.Rect(W/2,0,W,H/2),events,options_bool,options_clic)
        
        v.surface.blit(blue,(v.W/2,v.H/2))
        f.textbox(v.surface,v.trad['solo'][v.lg],100,W*3/4,H*3/4,False,bonus_bool,events,v.WHITE,v.BLACK)
        bonus_clic,bonus_bool=f.eventBools(pygame.Rect(W/2,H/2,W,H),events,bonus_bool,bonus_clic)
		
        trans=f.doTrans(trans)
        pygame.display.update()
