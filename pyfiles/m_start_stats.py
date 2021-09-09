"""
Fichier : 'm_start_stats.py'
Contenu : Rappel des données avant le début du jeu
Auteur : unearobase
"""

import pygame

def main():
    
    import variables as v
    import functions as f
    import inGame, m_options
    
    # WINDOW
    
    trans=True
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    bg=f.load('../img/General/Backgrounds/red.jpg',(v.W,v.H))
    
    # VARIABLES
    
    ok_clic=smash_clic=settings_clic=False
    ok_bool=smash_bool=settings_bool=False
    
    # FONCTIONS
    
    image=lambda x:f.load(f'../img/General/Keys icons/{x}.png',(40,40))
    arrows=image('up-arrow'),image('left-arrow'),image('down-arrow'),image('right-arrow'),image('knock'),image('shield')
    
    def data(name,value,W,H,suffix=''):
        f.textbox(v.surface,f"{name} : {value} {suffix}",40,W,H)
    
    def details(numPerso,numMin,numMax,W,H):
        f.textbox(v.surface,v.trad['keysofpn'][v.lg].replace('N',str(numPerso)),40,W/5,H)
        Wpos=[1.5,2,2.5,3,3.5,4]
        for i in range(6):
            f.imgbox(v.surface,arrows[i],None,W*Wpos[i]/5+30,H)
            key=v.ltKeys[v.pyKeys.index(v.keysTaken[numMin:numMax][i])]
            f.textbox(v.surface,key,round(f.sizeFor(key,0.8)),W*Wpos[i]/5+80,H)
    
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
        
        if ok_clic:
            pygame.mixer.music.stop()
            inGame.main()
            ok_clic=False
        elif smash_clic:
            f.transitionSortie()
            return
        elif settings_clic:
            f.transitionSortie()
            m_options.main(3)
            f.transitionSortie()
            settings_clic=False
        
        # AFFICHAGE
        
        W,H=v.W,v.H
        events=(v.mouse_click,v.mouse_pos)
        v.surface.blit(bg,(0,0))
        
        data(v.trad['nboflives'][v.lg],v.nbLives,W/3,H*1/11,'♥')
        data(v.trad['timelimit'][v.lg],v.timeLimit,W*2/3,H*1/11,'min')
        if v.matchFormat==0:
            data(v.trad['matchform'][v.lg],v.trad['perc'][v.lg],W/3,H*2/11)
            data(v.trad['percbase'][v.lg],v.pourcentBase,W*2/3,H*2/11,'%')
        else:
            data(v.trad['matchform'][v.lg],v.trad['lifepts'][v.lg],W/3,H*2/11)
            data(v.trad['lifepts'][v.lg],v.nbLifePts,W*2/3,H*2/11,'pts')
        data(v.trad['gravite'][v.lg],v.gravite,W/3,H*3/11)
        data(v.trad['multejec'][v.lg],v.multiKb,W*2/3,H*3/11)
        
        if v.nbp==2:
            details(1,0,6,W,H*4.5/10)
            details(2,6,12,W,H*6/10)
        if v.nbp==3:
            details(1,0,6,W,H*4.5/10)
            details(2,6,12,W,H*5.5/10)
            details(3,12,18,W,H*6.5/10)
        if v.nbp==4:
            details(1,0,6,W,H*4/10)
            details(2,6,12,W,H*5/10)
            details(3,12,18,W,H*6/10)
            details(4,18,24,W,H*7/10)
        
        ok_clic,ok_bool=f.button2(v.surface,v.trad['confirm'][v.lg],(W/2,H*6/7,350,125),ok_clic,ok_bool,events,v.OKGREEN,v.OKGREENHOVER,textsize=60)
        smash_clic,smash_bool=f.button2(v.surface,v.trad['changesmash'][v.lg],(W/5,H*6/7,250,90),smash_clic,smash_bool,events,v.DARKORANGE,v.ORANGE,textsize=30)
        settings_clic,settings_bool=f.button2(v.surface,v.trad['changeoptions'][v.lg],(W*4/5,H*6/7,250,90),settings_clic,settings_bool,events,v.ORCHID,v.PLUM,textsize=30)
        
        trans=f.doTrans(trans)
        pygame.display.update()
