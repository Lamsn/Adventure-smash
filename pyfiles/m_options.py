"""
Fichier : 'm_options.py'
Contenu : Menu des options
Auteur : unearobase
"""

import pygame

def main(current_menu=0):
    
    import variables as v
    import functions as f
    import functions_options as fo
    
    # WINDOW
    
    trans=True
    pygame.init()
    v.surface=pygame.display.set_mode((v.W,v.H))
    
    # VARIABLES GENERALES
    
    bg=f.load('../img/General/Backgrounds/green.jpg',(v.W,v.H))
    back_arrow=f.load('../img/General/Icons/back_arrow.png',(45,45))
    nav_clic=[False]*6
    nav_bool=[False]*6
    
    # VARIABLES SPECIFIQUES
    
    # SONS
    mute=f.load('../img/General/Icons/mute.png',(60,60))
    low=f.load('../img/General/Icons/low.png',(60,60))
    high=f.load('../img/General/Icons/high.png',(60,60))
    cut_clic=[False]*3
    cut_bool=[False]*3
    
    # LANG
    Llang=['Français','English','Español','Deutsche','Pусский','Português']
    Lflags=[f.load(f'../img/General/Flags/{i}.png',(100,66)) for i in ['France','USA-UK','Espagne','Allemagne','Russie','Bresil-Portugal']]
    lang_clic=[False]*len(Llang)
    lang_bool=[False]*len(Llang)
    Wpos1=[1/3,1/3,1/3,2/3,2/3,2/3]
    Hpos1=[1/4,2/4,3/4,1/4,2/4,3/4]
    
    # TOUCHES
    retour_keys_clic=False
    retour_keys_bool=False
    mainPage=True
    buttons_clic=[False]*4
    buttons_bool=[False]*4
    keys_clic=[[False for i in range(6)] for i in range(4)]
    keys_bool=[[False for i in range(6)] for i in range(4)]
    kt=[[False for i in range(6)] for i in range(4)]
    ku=[[False for i in range(6)] for i in range(4)]
    Wpos2=[1/3,2/3,1/3,2/3]
    Hpos2=[1/3,1/3,2/3,2/3]
    k_ex=lambda x,y:[v.ltKeys[v.pyKeys.index(i)] for i in v.keysTaken[x:y]]
    keysP=[k_ex(0,6),k_ex(6,12),k_ex(12,18),k_ex(18,24)]
    eventsKeys=[[-10,-10],[-10,-10]]
    
    # PARAMETRES JEU
    toleftCH=f.load('../img/General/Icons/left.png',(60,60))
    torightCH=f.load('../img/General/Icons/right.png',(60,60))
    random=f.load('../img/General/Icons/random.png',(50,50))
    arrows1=[False]*4
    arrows2=[False]*4
    img_clic=[False]*3
    img_bool=[False]*3
    otherpage_clic=False
    otherpage_bool=False
    page=1
    
    # FONCTIONS
    
    def nav_bar(current_menu,liste,clic,hover,back_arrow):
        f.opacityRect(0,50,v.W,4,False,False)
        nb=len(liste)
        for i in range(nb):
            if clic[i] or hover[i] or i==current_menu:
                rectopacity=128
                elemcolor=v.BLACK
            else:
                rectopacity=0
                elemcolor=v.WHITE
            clic[i],hover[i]=f.opacityRect(v.W*i/nb,0,v.W/nb,50,clic[i],hover[i],a=rectopacity,events=events)
            f.textbox(v.surface,liste[i],30,v.W*(i+0.5)/nb,25,color=elemcolor)
        clic[-1],hover[-1]=f.imgbox(v.surface,back_arrow,None,45,v.H-45,clic[-1],hover[-1],events)
        if hover[-1]:
            f.textbox(v.surface,v.trad['back'][v.lg],30,110,v.H-45)
        return clic,hover
    
    # BOUCLE
    
    running=True
    while running:
        v.mouse_click=(-10,-10)
        eventsAll=pygame.event.get()
        for event in eventsAll:
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
        
        if nav_clic[-1]:
            f.transitionSortie()
            running=False
        if True in nav_clic[:5]:
            current_menu=nav_clic.index(True)
            nav_clic=[False]*6
        
        # AFFICHAGE MENUS
        
        events=(v.mouse_click,v.mouse_pos)
        eventsKeys[1]=v.mouse_pos
        if v.mouse_click!=(-10,-10):
            eventsKeys[0]=v.mouse_click
        v.surface.blit(bg,(0,0))
        Lform=[v.trad['perc'][v.lg],v.trad['lifepts'][v.lg]]
        Lwinform=['1280x720',v.trad['fullscreen'][v.lg]]
        liste=[v.trad['sound'][v.lg],v.trad['lang'][v.lg],v.trad['keys'][v.lg],v.trad['gameset'][v.lg]]
        nav_bar(current_menu,liste,nav_clic,nav_bool,back_arrow)
        
        if current_menu==0:
            cut_clic,cut_bool=fo.m_sons(events,cut_clic,cut_bool,mute,low,high)
        elif current_menu==1:
            lang_clic,lang_bool=fo.m_lang(events,Llang,Lflags,lang_clic,lang_bool,Wpos1,Hpos1)
        elif current_menu==2:
            retour_keys_clic,retour_keys_bool,mainPage,buttons_clic,buttons_bool,keys_clic,keys_bool,keysP=fo.m_touches(eventsKeys,bg,retour_keys_clic,retour_keys_bool,mainPage,buttons_clic,buttons_bool,keys_clic,keys_bool,Wpos2,Hpos2,keysP,eventsAll,kt,ku)
        elif current_menu==3:
            arrows1,arrows2,img_clic,img_bool,otherpage_clic,otherpage_bool,page=fo.m_parametres_jeu(events,random,Lform,Lwinform,arrows1,arrows2,img_clic,img_bool,otherpage_clic,otherpage_bool,page,toleftCH,torightCH)
        
        trans=f.doTrans(trans)
        pygame.display.update()
