"""
Fichier : "functions_options.py"
Contenu : Fonctions du menu Options
Auteur : Noé Lacaille
"""

import pygame
import variables as v
import functions as f

def m_sons(events,cut_clic,cut_bool,mute,low,high):
    
    f.textbox(v.surface,v.trad['soundchar'][v.lg],60,v.W/3,v.H/4)
    v.posCoups,v.volumeCoups,cut_clic[0],cut_bool[0]=f.buttonsVolume(v.surface,v.W,v.H/4,mute,low,high,v.posCoups,v.volumeCoups,cut_clic[0],cut_bool[0],events)
    v.posCoups,v.volumeCoups=f.slider(v.surface,(v.W*2/3,v.H/4,400,60),v.LIGHTYELLOW,v.GOLD,20,v.posCoups,v.slider_click,0,100,25,unit=' %')
    
    for i in v.Sons:
        pygame.mixer.Sound.set_volume(i,v.volumeCoups/100)
    
    f.textbox(v.surface,v.trad['musicgame'][v.lg],60,v.W/3,v.H*2/4)
    v.posMusic,v.volumeMusic,cut_clic[1],cut_bool[1]=f.buttonsVolume(v.surface,v.W,v.H/2,mute,low,high,v.posMusic,v.volumeMusic,cut_clic[1],cut_bool[1],events)
    v.posMusic,v.volumeMusic=f.slider(v.surface,(v.W*2/3,v.H*2/4,400,60),v.LIGHTYELLOW,v.GOLD,20,v.posMusic,v.slider_click,0,100,25,unit=' %')
    pygame.mixer.music.set_volume(v.volumeMusic/100)
    
    f.textbox(v.surface,v.trad['musicmenu'][v.lg],60,v.W/3,v.H*3/4)
    v.posMenu,v.volumeMenu,cut_clic[2],cut_bool[2]=f.buttonsVolume(v.surface,v.W,v.H*3/4,mute,low,high,v.posMenu,v.volumeMenu,cut_clic[2],cut_bool[2],events)
    v.posMenu,v.volumeMenu=f.slider(v.surface,(v.W*2/3,v.H*3/4,400,60),v.LIGHTYELLOW,v.GOLD,20,v.posMenu,v.slider_click,0,100,25,unit=' %')
    
    for i in v.Menus:
        pygame.mixer.Sound.set_volume(i,v.volumeMenu/100)
    
    return cut_clic,cut_bool

def m_lang(events,Llang,Lflags,lang_clic,lang_bool,Wpos,Hpos):
    
    if True in lang_clic:
        v.lg=lang_clic.index(True)
        lang_clic=[False]*len(Llang)
    
    for i in range(len(Llang)):
        if v.lg==i:
            langcolor=v.RED
            #lang_bool[i]=False
        else:
            langcolor=v.BLACK
        lang_clic[i],lang_bool[i]=f.textbox(v.surface,Llang[i],50,v.W*Wpos[i]+50,v.H*Hpos[i],lang_clic[i],lang_bool[i],events,color=langcolor)
        f.imgbox(v.surface,Lflags[i],None,v.W*Wpos[i]-120,v.H*Hpos[i])
    
    return lang_clic,lang_bool

def keyBox(events,function,key,left,top,clic,hover,eventsAll,keyTaken,keyUnavailable,width=300,height=100,color=v.WHITE,hcolor=v.LIGHTGRAY,borderColor=v.BLACK):
    if clic:
        borderColor=v.RED
    if hover:
        color=hcolor
    left,top=f.center(left,top,width,height)
    rect=pygame.draw.rect(v.surface,v.DARKSLATEGRAY,(left,top,width,height))
    f.rectBorder(v.surface,borderColor,(left,top,width,height))
    f.textbox(v.surface,function,40,left+width/3,top+height/2,color=v.WHITE)
    try:
        pygame.draw.rect(v.surface,color,(left+width*3/4-40,top+height/2-height*3/8,80,height*3/4),border_radius=100)
    except:
        pygame.draw.rect(v.surface,color,(left+width*3/4-40,top+height/2-height*3/8,80,height*3/4))
    f.textbox(v.surface,key,f.sizeFor(key),left+width*3/4,top+height/2)
    if clic:
        f.textbox(v.surface,v.trad['presskey'][v.lg],25,left+width/2,top+height+18)
        for event in eventsAll:
            if event.type==pygame.KEYDOWN:
                if event.key in v.pyKeys:
                    keyUnavailable=False
                    if event.key not in v.keysTaken:
                        locKey=v.pyKeys[v.ltKeys.index(key)]
                        v.keysTaken[v.keysTaken.index(locKey)]=event.key
                        key=v.ltKeys[v.pyKeys.index(event.key)]
                        keyTaken=False                        
                    else:
                        keyTaken=True 
                else:
                    keyUnavailable=True  
        if keyTaken:
            f.textbox(v.surface,v.trad['errorkeytaken'][v.lg],25,left+width/2,top+height+35,color=v.RED)
        elif keyUnavailable:
            f.textbox(v.surface,v.trad['errorkeyunav'][v.lg],25,left+width/2,top+height+35,color=v.RED)
    return key,f.eventBools(rect,events,hover,clic)[0],f.eventBools(rect,events,hover,clic)[1],keyTaken,keyUnavailable

def playerKeys(events,numPlayer,k,c,h,eventsAll,kt,ku):
    f.textbox(v.surface,f"{v.trad['player'][v.lg]} {numPlayer}",50,v.W/2,v.H*1/5)
    k[5],c[5],h[5],kt[5],ku[5]=keyBox(events,v.trad['shield'][v.lg],k[5],v.W/4,v.H*3/6-25,c[5],h[5],eventsAll,kt[5],ku[5])
    k[0],c[0],h[0],kt[0],ku[0]=keyBox(events,v.trad['up'][v.lg],k[0],v.W/2,v.H*3/6-25,c[0],h[0],eventsAll,kt[0],ku[0])
    k[4],c[4],h[4],kt[4],ku[4]=keyBox(events,v.trad['knock'][v.lg],k[4],v.W*3/4,v.H*3/6-25,c[4],h[4],eventsAll,kt[4],ku[4])
    k[1],c[1],h[1],kt[1],ku[1]=keyBox(events,v.trad['left'][v.lg],k[1],v.W/4,v.H*4/6+25,c[1],h[1],eventsAll,kt[1],ku[1])
    k[2],c[2],h[2],kt[2],ku[2]=keyBox(events,v.trad['down'][v.lg],k[2],v.W/2,v.H*4/6+25,c[2],h[2],eventsAll,kt[2],ku[2])
    k[3],c[3],h[3],kt[3],ku[3]=keyBox(events,v.trad['right'][v.lg],k[3],v.W*3/4,v.H*4/6+25,c[3],h[3],eventsAll,kt[3],ku[3])
    return k,c,h

def m_touches(events,bg,retour_keys_clic,retour_keys_bool,mainPage,buttons_clic,buttons_bool,keys_clic,keys_bool,Wpos,Hpos,keysP,eventsAll,kt,ku):
    
    if mainPage:
        for i in range(4):
            buttons_clic[i],buttons_bool[i]=f.button1(v.surface,v.trad['keysofN'][v.lg].replace('N',str(i+1)),(v.W*Wpos[i],v.H*Hpos[i],300,100),buttons_clic[i],buttons_bool[i],events)
    
    for i in range(4):
        if buttons_clic[i]:
            mainPage=False
            v.surface.blit(bg,(0,0))
            retour_keys_clic,retour_keys_bool=f.textbox(v.surface,f"<  {v.trad['returnmaj'][v.lg]}",45,120,50,retour_keys_clic,retour_keys_bool,events)
            keysP[i],keys_clic[i],keys_bool[i]=playerKeys(events,i+1,keysP[i],keys_clic[i],keys_bool[i],eventsAll,kt[i],ku[i])
            if retour_keys_clic:
                buttons_clic[i]=False
                retour_keys_clic=False
                mainPage=True
                v.mouse_click=(-10,-10)
    
    return retour_keys_clic,retour_keys_bool,mainPage,buttons_clic,buttons_bool,keys_clic,keys_bool,keysP

def nextpage_buttons(otherpage_clic,otherpage_bool,page,arrow,posW,events):
    circleColor=v.WHITE
    if otherpage_bool:
        circleColor=v.LIGHTGRAY
    circle=pygame.draw.circle(v.surface,circleColor,(posW,v.H/2),40)
    otherpage_clic,otherpage_bool=f.eventBools(circle,events,otherpage_bool,otherpage_clic)
    f.imgbox(v.surface,arrow,None,posW,v.H/2)
    if otherpage_clic:
        if page==1:
            page=2
        else:
            page=1
    return otherpage_clic,otherpage_bool,page

def m_parametres_jeu(events,random,Lform,Lwinform,arrows1,arrows2,img_clic,img_bool,otherpage_clic,otherpage_bool,page,toleftCH,torightCH):
    
    if page==1:
        
        f.textbox(v.surface,v.trad['nboflives'][v.lg],60,v.W/3,v.H/5)
        v.posNbv,v.nbLives,img_clic[0],img_bool[0]=f.buttonsRandom(v.surface,v.W,v.H/5,random,v.posNbv,v.nbLives,img_clic[0],img_bool[0],1,11,events)
        v.posNbv,v.nbLives=f.slider(v.surface,(v.W*2/3,v.H/5,400,60),v.SALMON,v.RED,20,v.posNbv,v.slider_click,1,11,3,unit=' ♥',infinite=True)
        
        f.textbox(v.surface,v.trad['timelimit'][v.lg],60,v.W/3,v.H*2/5)
        v.posTlim,v.timeLimit,img_clic[1],img_bool[1]=f.buttonsRandom(v.surface,v.W,v.H*2/5,random,v.posTlim,v.timeLimit,img_clic[1],img_bool[1],1,21,events)
        v.posTlim,v.timeLimit=f.slider(v.surface,(v.W*2/3,v.H*2/5,400,60),v.SKYBLUE,v.BLUE,20,v.posTlim,v.slider_click,1,21,21,unit=' min',infinite=True)
        
        f.textbox(v.surface,v.trad['matchform'][v.lg],60,v.W/3,v.H*3/5)
        arrows1,v.matchFormat=f.sliderLR(v.surface,60,v.W*2/3,v.H*3/5,185,Lform,v.matchFormat,arrows1,events)
    
        if v.matchFormat==1:
            f.textbox(v.surface,v.trad['lifepts'][v.lg],60,v.W/3,v.H*4/5)
            v.posLifePts,v.nbLifePts,img_clic[2],img_bool[2]=f.buttonsRandom(v.surface,v.W,v.H*4/5,random,v.posLifePts,v.nbLifePts,img_clic[2],img_bool[2],1,999,events)
            v.posLifePts,v.nbLifePts=f.slider(v.surface,(v.W*2/3,v.H*4/5,400,60),v.PLUM,v.ORCHID,20,v.posLifePts,v.slider_click,1,999,100,unit=' pts')
        else:
            f.textbox(v.surface,v.trad['percbase'][v.lg],60,v.W/3,v.H*4/5)
            v.posPercBase,v.pourcentBase,img_clic[2],img_bool[2]=f.buttonsRandom(v.surface,v.W,v.H*4/5,random,v.posPercBase,v.pourcentBase,img_clic[2],img_bool[2],0,999,events)
            v.posPercBase,v.pourcentBase=f.slider(v.surface,(v.W*2/3,v.H*4/5,400,60),v.MEDIUMSEAGREEN,v.SEAGREEN,20,v.posPercBase,v.slider_click,0,999,0,unit=' %')
        
        otherpage_clic,otherpage_bool,page=nextpage_buttons(otherpage_clic,otherpage_bool,page,torightCH,v.W-50,events)
    
    elif page==2:
        
        f.textbox(v.surface,v.trad['gravite'][v.lg],60,v.W/3,v.H/5)
        v.posGravite,v.gravite,img_clic[0],img_bool[0]=f.buttonsRandom(v.surface,v.W,v.H/5,random,v.posGravite,v.gravite,img_clic[0],img_bool[0],10,100,events)
        v.posGravite,v.gravite=f.slider(v.surface,(v.W*2/3,v.H/5,400,60),v.ORANGE,v.DARKORANGE,20,v.posGravite,v.slider_click,10,100,35,divide=100)
        
        f.textbox(v.surface,v.trad['multejec'][v.lg],60,v.W/3,v.H*2/5)
        v.posMultiKb,v.multiKb,img_clic[1],img_bool[1]=f.buttonsRandom(v.surface,v.W,v.H*2/5,random,v.posMultiKb,v.multiKb,img_clic[1],img_bool[1],25,400,events)
        v.posMultiKb,v.multiKb=f.slider(v.surface,(v.W*2/3,v.H*2/5,400,60),v.MEDIUMPURPLE,v.BLUEVIOLET,20,v.posMultiKb,v.slider_click,25,400,100,divide=100)
        
        f.textbox(v.surface,v.trad['winform'][v.lg],60,v.W/3,v.H*3/5)
        arrows2,v.winform=f.sliderLR(v.surface,60,v.W*2/3,v.H*3/5,165,Lwinform,v.winform,arrows2,events)
        if v.winform!=0:
            warning='FR -- Plein écran indisponible pour l\'instant.','Veuillez rester en format 1280x720.','','EN -- Full screen unavailable at this time.','Please stay in 1280x720 format.'
            for i in range(len(warning)):
                f.textbox(v.surface,warning[i],25,v.W/2,v.H*4/5-50+30*i,color=v.WHITE)
        
        otherpage_clic,otherpage_bool,page=nextpage_buttons(otherpage_clic,otherpage_bool,page,toleftCH,50,events)
    
    return arrows1,arrows2,img_clic,img_bool,otherpage_clic,otherpage_bool,page
