"""
Fichier : 'm_bonus.py'
Contenu : Bonus
Auteur : Noé Lacaille
"""

import pygame

def main():
    
    import variables as v
    import functions as f
    import parcours, m_smash_target
    
    # WINDOW
    
    trans=True
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    bg=f.load('../img/General/Backgrounds/blue.jpg',(v.W,v.H))
    
    # VARIABLES
    
    back_arrow=f.load('../img/General/Icons/back_arrow.png',(45,45))
    info=f.load('../img/General/Icons/info.png',(45,45))
    parcours_clic=target_clic=retour_clic=False
    parcours_bool=target_bool=retour_bool=False
    info_bool1=info_bool2=False
    
    # FONCTIONS
    
    def info_bulle(texte,num):
        pygame.draw.polygon(v.surface,v.BLACK,[(W/2+260,H*num/3),(W/2+280,H*num/3+20),(W/2+280,H*num/3+50),(W/2+530,H*num/3+50),(W/2+530,H*num/3-50),(W/2+280,H*num/3-50),(W/2+280,H*num/3-20)])
        ec=-30
        for i in texte:
            f.textbox(v.surface,i,25,W/2+405,H*num/3+ec,color=v.WHITE)
            ec+=30
    
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
        
        if retour_clic:
            f.transitionSortie()
            return
        elif parcours_clic:
            f.transitionSortie()
            parcours.main()
            f.transitionSortie()
            parcours_clic=False
            v.mouse_click=(-10,-10)
        elif target_clic:
            f.transitionSortie()
            m_smash_target.main()
            f.transitionSortie()
            target_clic=False
            v.mouse_click=(-10,-10)
        
        # AFFICHAGE
        
        W,H=v.W,v.H
        events=(v.mouse_click,v.mouse_pos)
        v.surface.blit(bg,(0,0))
        
        parcours_clic,parcours_bool=f.button1(v.surface,v.trad['obstaclecourse'][v.lg],(W/2,H/3,400,150),parcours_clic,parcours_bool,events)
        target_clic,target_bool=f.button1(v.surface,v.trad['targetsmash'][v.lg],(W/2,H*2/3,400,150),target_clic,target_bool,events)
        info_bool1=f.imgbox(v.surface,info,None,W/2+230,H/3,False,info_bool1,events)[1]
        info_bool2=f.imgbox(v.surface,info,None,W/2+230,H*2/3,False,info_bool2,events)[1]
        
        if info_bool1:
            info_bulle(v.trad['.parcours'][v.lg].split('$'),1) # split() pour décomposer par mot le texte
        if info_bool2:
            info_bulle(v.trad['.targetSmash'][v.lg].split('$'),2) # split() pour décomposer par mot le texte
        
        retour_clic,retour_bool=f.imgbox(v.surface,back_arrow,None,45,v.H-45,retour_clic,retour_bool,events)
        if retour_bool:
            f.textbox(v.surface,v.trad['back'][v.lg],30,110,v.H-45)
        
        trans=f.doTrans(trans)
        pygame.display.update()
