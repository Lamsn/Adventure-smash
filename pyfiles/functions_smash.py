"""
Fichier : "functions_smash.py"
Contenu : Fonctions du menu Smash
Auteur : Noé Lacaille
"""

import pygame
import variables as v
import functions as f

def validate(events,ok,rc):
    f.opacityRect(0,0,v.W,v.H,False,False)
    ok[0],ok[1]=f.button2(v.surface,v.trad['valider'][v.lg].upper(),(v.W/2,v.H/2,350,125),ok[0],ok[1],events,v.OKGREEN,v.OKGREENHOVER,textsize=70,bradius=20)
    rc[0],rc[1]=f.textbox(v.surface,v.trad['rechoose'][v.lg],30,v.W/2,v.H/2+100,rc[0],rc[1],events)
    return ok,rc

def m_nbpersos(events,buttons_clic,buttons_bool,Wpos,Hpos):
    
    if True in buttons_clic:
        if buttons_clic[0]:
            v.nbp=2
            buttons_clic[0]=False
        elif buttons_clic[1]:
            v.nbp=3
            buttons_clic[1]=False
        elif buttons_clic[2]:
            v.nbp=4
            buttons_clic[2]=False
    
    f.textbox(v.surface,v.trad['choosenbp'][v.lg],60,v.W/2,v.H/2,color=v.WHITE)
    for i in range(3):
        buttons_clic[i],buttons_bool[i]=f.button2(v.surface,v.trad['nbplayers'][v.lg].replace('N',str(i+2)),(v.W*Wpos[i],v.H*Hpos[i],400,150),buttons_clic[i],buttons_bool[i],events)
    
    return buttons_clic,buttons_bool

def chosenCharBox(left,top,width,height,bradius,toselect):
    left,top=f.center(left,top,width,height)
    try:
        pygame.draw.rect(v.surface,v.LIGHTGRAY,(left,top,width,height),border_radius=bradius)
    except:
        pygame.draw.rect(v.surface,v.LIGHTGRAY,(left,top,width,height))
    if toselect:
        f.textbox(v.surface,v.trad['choosechar'][v.lg],30,left+width/2,top+height/2)
        try:
            pygame.draw.rect(v.surface,v.RED,(left+30,top+height-20,width-60,10),border_radius=10)
        except:
            pygame.draw.rect(v.surface,v.RED,(left+30,top+height-20,width-60,10))

def m_persos(events,nbchoix,Limgs,LimgsNames,char,char_name,perso_click,perso_bool,Lselect,okShow,validate=False):
    
    Lselect=[False]*4
    if nbchoix<v.nbp:
        Lselect[nbchoix]=True
    
    multWidth=[]
    if v.nbp==1:
        chosenCharBox(v.W/2,v.H*6/7,300,150,35,Lselect[0])
        multWidth=[2]
    if v.nbp==2:
        chosenCharBox(v.W*1.5/4-50,v.H*6/7,300,150,35,Lselect[0])
        chosenCharBox(v.W*2.5/4+50,v.H*6/7,300,150,35,Lselect[1])
        multWidth=[43/32,85/32] # résultat pour x des équations W*x/4=W*y/4-50 avec y1=1.5 et y2=2.5
    if v.nbp==3:
        chosenCharBox(v.W*1/4,v.H*6/7,300,150,35,Lselect[0])
        chosenCharBox(v.W*2/4,v.H*6/7,300,150,35,Lselect[1])
        chosenCharBox(v.W*3/4,v.H*6/7,300,150,35,Lselect[2])
        multWidth=[1,2,3]
    if v.nbp==4:
        chosenCharBox(v.W*0.5/4,v.H*6/7,300,150,35,Lselect[0])
        chosenCharBox(v.W*1.5/4,v.H*6/7,300,150,35,Lselect[1])
        chosenCharBox(v.W*2.5/4,v.H*6/7,300,150,35,Lselect[2])
        chosenCharBox(v.W*3.5/4,v.H*6/7,300,150,35,Lselect[3])
        multWidth=[0.5,1.5,2.5,3.5]
    
    for i in range(v.nbp):
        if char[i]!=None:
            f.imgbox(v.surface,char[i],None,v.W*multWidth[i]/4,v.H*6/7)
    
    x,y=1,2
    for i in range(8):
        if perso_bool[i] and not okShow:
            f.opacityRect(v.W*x/5-62.5,v.H*y/7-62.5,125,125,False,False)
            f.textbox(v.surface,char_name[i],20,v.W*x/5,v.H*y/7+85,color=v.WHITE)
        perso_click[i],perso_bool[i]=f.imgbox(v.surface,Limgs[i],None,v.W*x/5,v.H*y/7,perso_click[i],perso_bool[i],events)
        x+=1
        if x>4:
            x,y=1,4
    
    if (True in perso_click) and (nbchoix<v.nbp):            
        char[nbchoix]=Limgs[perso_click.index(True)]                      
        if nbchoix!=v.nbp:                
            v.combattants[nbchoix]=LimgsNames[perso_click.index(True)%len(LimgsNames)]
        
        perso_click[perso_click.index(True)]=False
        nbchoix+=1
        if nbchoix==v.nbp:
            perso_click=[False]*8
            validate=True
    
    return nbchoix,char,perso_click,perso_bool,Lselect,validate

def m_maps(events,map_clic,map_bool,mapDatas,okShow,validate=False):
    
    if True in map_clic:
        v.mapChoisie=mapDatas[map_clic.index(True)][3]
        v.mapChoisieNom=mapDatas[map_clic.index(True)][3]
        map_clic=[False]*4
        validate=True
    
    f.textbox(v.surface,v.trad['choosemap'][v.lg],40,v.W/2,v.H/2,color=v.WHITE)
    
    for i in range(len(mapDatas)):
        width,height=mapDatas[i][1]
        map_a=mapDatas[i][0]
        map_surface=pygame.Rect(width-map_a.get_width()//2,height-map_a.get_height()//2,map_a.get_width(),map_a.get_height())
        map_bool[i]=f.eventBools(map_surface,events,hover=map_bool[i])[1]
        if map_bool[i] and (not okShow):
            height-=10
        f.textbox(v.surface,mapDatas[i][2],30,mapDatas[i][1][0],mapDatas[i][1][1]+130,color=v.WHITE)
        map_clic[i]=f.imgbox(v.surface,map_a,None,width,height,map_clic[i],True,events)[0]
    
    return map_clic,map_bool,validate
