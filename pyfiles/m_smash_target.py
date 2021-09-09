"""
Fichier : 'm_smash_target.py'
Contenu : Menus choix persos et maps du bonus Targets
Auteur : unearobase
"""

import pygame

def main(current_menu=0):
    
    import variables as v
    import functions as f
    import functions_smash as fs
    import Personnages.Kirby.Stats as Kirby, Personnages.Bowser.Stats as Bowser, Personnages.Koopa.Stats as Koopa, Personnages.Link.Stats as Link, Personnages.Mario.Stats as Mario, Personnages.Luigi.Stats as Luigi, Personnages.Donkey_Kong.Stats as Donkey_Kong, Personnages.Waluigi.Stats as Waluigi
    import targetSmash
    
    # WINDOW
    
    trans=True
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    
    # VARIABLES GENERALES
    
    bg=f.load('../img/General/Backgrounds/blue.jpg',(v.W,v.H))
    back_arrow=f.load('../img/General/Icons/back_arrow.png',(45,45))
    nav_clic=[False]*3
    nav_bool=[False]*3
    
    # VARIABLES SPECIFIQUES
    
    # PERSOS
    nbchoix=0
    p=lambda i:f.load(f'Personnages/{i}/immobile/1.png',(pygame.image.load('Personnages/'+i+'/immobile/1.png').get_width()//2,pygame.image.load('Personnages/'+i+'/immobile/1.png').get_height()//2))
    char_name=['Kirby','Bowser','Koopa','Link','Mario','Luigi','Donkey_Kong','Waluigi']
    Limgs=[p(i) for i in char_name]
    LimgsNames=[Kirby,Bowser,Koopa,Link,Mario,Luigi,Donkey_Kong,Waluigi]
    char=[None]*4
    perso_click=[False]*8
    perso_bool=[False]*8
    Lselect=[False]*4
    
    # MAPS
    map_clic=[False]*4
    map_bool=[False]*4
    Wpos2=[1,3,1,3]
    Hpos2=[1,1,3,3]
    mapDatas=[(f.load(f'../img/Fonds/map{i+1}.jpg',(400,200)),(v.W*Wpos2[i]/4,v.H*Hpos2[i]/4),f'Map {i+1}',f'map{i+1}') for i in range(4)]
    
    # VALIDATE
    ok=[False,False] # for validate
    rc=[False,False] # for rechoose
    V1=False # first validation
    V2=False # second validation
    okShow=False # for showing or not the OK button
    
    # FONCTIONS
    
    def nav_bar(current_menu,liste,clic,hover,back_arrow):
        f.opacityRect(0,50,v.W,4,False,False)
        for i in range(2):
            if clic[i] or hover[i] or i==current_menu:
                rectopacity=128
                elemcolor=v.BLACK
            else:
                rectopacity=0
                elemcolor=v.WHITE
            clic[i],hover[i]=f.opacityRect(v.W*i/2,0,v.W/2,50,clic[i],hover[i],a=rectopacity,events=events)
            f.textbox(v.surface,liste[i],30,v.W*(i+0.5)/2,25,color=elemcolor)
        clic[-1],hover[-1]=f.imgbox(v.surface,back_arrow,None,45,v.H-45,clic[-1],False,events)
        if hover[-1]:
            f.textbox(v.surface,v.trad['back'][v.lg],30,110,v.H-45)
        return clic,hover
    
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
            elif event.type==pygame.MOUSEBUTTONDOWN:
                v.slider_click=event.pos
            elif event.type==pygame.MOUSEBUTTONUP:
                v.mouse_click=event.pos			
            elif event.type==pygame.MOUSEMOTION:
                v.mouse_pos=event.pos
        
        # EVENEMENTS
        
        if ok[0]:
            f.transitionSortie()
            targetSmash.main()
            f.transitionSortie()
        if rc[0]:
            v.nbp=0
            main()
        if nav_clic[-1]:
            f.transitionSortie()
            running=False
        if True in nav_clic[:2]:
            current_menu=nav_clic.index(True)
            nav_clic=[False]*3
        
        # AFFICHAGE MENUS
        
        events=(v.mouse_click,v.mouse_pos)
        v.surface.blit(bg,(0,0))
        liste=[v.trad['char'][v.lg],v.trad['maps'][v.lg]]
        nav_bar(current_menu,liste,nav_clic,nav_bool,back_arrow)
        
        if current_menu==0:
            v.nbp=1
            nbchoix,char,perso_click,perso_bool,Lselect,V1=fs.m_persos(events,nbchoix,Limgs,LimgsNames,char,char_name,perso_click,perso_bool,Lselect,okShow)
        elif current_menu==1:
            map_clic,map_bool,V2=fs.m_maps(events,map_clic,map_bool,mapDatas,okShow)
        
        if okShow:
            ok,rc=fs.validate(events,ok,rc)
        
        if V1 and V2:
            okShow=True
        elif V1:
            current_menu=1
        elif V2:
            current_menu=0
        
        trans=f.doTrans(trans)
        pygame.display.update()
