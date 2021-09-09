"""
Fichier : 'functions.py'
Contenu : Fonctions référence
Auteur : unearobase
"""

import pygame, variables as v, random

default=((-10,-10),(-10,-10))

def load(path,size=None):
    if size!=None:
        return pygame.transform.scale(pygame.image.load(path),(round(size[0]),round(size[1]))).convert_alpha()
    else:
        return pygame.image.load(path).convert_alpha()

def eventBools(elem,events,hover=False,clic=False):
    if elem.collidepoint(events[0]):
        if clic!=True:
            pygame.mixer.Sound.play(v.Menus[0])
        clic=True
    else:
        clic=False
    if elem.collidepoint(events[1]):
        if hover!=True:
            pygame.mixer.Sound.play(v.Menus[1])
        hover=True
    else:
        hover=False
    # if clic or hover:
    #     pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND) # curseur mode clic
    # else:
    #     pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW) # curseur mode normal
    return clic,hover

def textbox(surface,text,size,W,H,clic=False,hover=False,events=default,
            color=v.BLACK,hcolor=v.DARKSLATEGRAY,police='arial'):
    if hover:        
        color=hcolor
    font=pygame.font.SysFont(police,size)
    text=font.render(text,True,color)
    text_rect=text.get_rect()
    text_rect.center=(W,H)
    surface.blit(text,text_rect)
    return eventBools(text_rect,events,hover,clic)

def imgbox(surface,img,size,W,H,clic=False,hover=False,events=default):
    if type(img)==str:
        img=pygame.image.load(img)
    if size!=None:
        img=pygame.transform.scale(img,size)
    img_rect=img.get_rect()
    img_rect.center=(W,H)
    surface.blit(img,img_rect)
    return eventBools(img_rect,events,hover,clic)

def center(left,top,width,height):
    return left-width/2,top-height/2

def rectBorder(surface,color,dimensions,borderWidth=2):
    left,top,width,height=dimensions
    pygame.draw.lines(surface,color,True,[(left,top),(left,top+height),(left+width,top+height),(left+width,top)],width=borderWidth)

def convert(params):
    x,y,mini,maxi=params
    return [(mini+i,round(x+(y-x)/(maxi-mini)*i,2)) for i in range(maxi-mini+1)]

def getPosByValue(params,value):
    values=[i[0] for i in convert(params)]
    return convert(params)[values.index(value)][1]

def getValueByPos(params,posx):
    posxs=[i[1] for i in convert(params)]
    return params[2]+min(range(len(posxs)),key=lambda i: abs(posxs[i]-posx)) # renvoie la position la plus proche

def rounded(n):
    n=str(n)
    try:
        dec=n[n.index('.')+1:]
        if len(dec)==1:
            return n+'0'
        else:
            return n
    except:
        return n+'.00'

def slider(surface,dimensions,slidercolor,buttoncolor,buttonwidth,posx,mouse_click,mini,maxi,default,unit='',infinite=False,textcolor=v.BLACK,divide=1):
    """ @params : surface, (left,top,width,height), couleur slider, couleur boutton, largeur boutton,
    position x du clic, évènement du clic, valeur min, valeur max, unité """
    left,top,width,height=dimensions
    left,top=center(left,top,width,height)
    params=left,left+width-buttonwidth,mini,maxi
    if posx=='N/A': # si valeur non-initialisée
        posx=getPosByValue(params,default)
    objslider=pygame.draw.rect(surface,v.WHITE,(left,top,width,height)) # le slider
    pygame.draw.rect(surface,slidercolor,(left,top,posx-left,height)) # la partie "remplie" du slider avant déplacement
    pygame.draw.rect(surface,buttoncolor,(posx,top,buttonwidth,height)) # le boutton avant déplacement
    if pygame.mouse.get_pressed()[0]!=0 and objslider.collidepoint(mouse_click): # clic gauche de la souris dans la zone du slider
        posx=pygame.mouse.get_pos()[0] # position x de la souris
        posx-=buttonwidth/2 # pour que ce soit le centre du boutton qui soit à l'endroit du clic
        if posx<params[0]:
            posx=params[0] # pour pas que le boutton sorte à gauche du slider
        elif posx>params[1]:
            posx=params[1] # pour pas que le boutton sorte à droite du slider
        pygame.draw.rect(surface,buttoncolor,(posx,top,buttonwidth,height)) # le boutton après déplacement
        pygame.draw.rect(surface,slidercolor,(left,top,posx-left,height)) # la partie "remplie" du slider après déplacement
    val=getValueByPos(params,posx) # valeur en fonction de la position
    if divide>1:
        val=rounded(val/divide)
    if infinite and val==maxi/divide:
        val='∞'
    textbox(surface,str(val)+unit,60,left+width/2,top+height/2,color=textcolor) # affichage de la valeur
    return posx,val

def sliderLR(surface,size,W,H,space,Lelems,idxelem,arrows,events):
    arrows[0],arrows[1]=textbox(surface,'<',size+20,W-space,H,arrows[0],arrows[1],events)
    textbox(surface,Lelems[idxelem],size,W,H,color=v.BLACK)
    arrows[2],arrows[3]=textbox(surface,'>',size+20,W+space,H,arrows[2],arrows[3],events)
    if arrows[0]:
        idxelem-=1
    elif arrows[2]:
        idxelem+=1
    return arrows,idxelem%len(Lelems)
    # modulo pour recommencer la liste à l'endroit ou à l'envers si l'on est au premier ou au dernier élément

def sizeFor(key,coef=1):
    if len(key)==1: return 50*coef
    elif len(key)==2: return 40*coef
    elif len(key)==3: return 35*coef
    elif len(key)>=4: return 30*coef
    else: return 25*coef

def buttonsRandom(surface,W,H,img,posx,val,img_clic,img_bool,mini,maxi,events):
    img_clic,img_bool=imgbox(surface,img,None,W*2/3+250,H,img_clic,img_bool,events)
    if img_bool:
        textbox(surface,v.trad['random'][v.lg],20,W*2/3+250,H+40,color=v.WHITE)
    if img_clic:
        val=random.choice(range(mini,maxi+1))
        params=(W*2/3-400/2,W*2/3-400/2+400-20,mini,maxi)
        posx=getPosByValue(params,val)
    return posx,val,img_clic,img_bool

def buttonsVolume(surface,W,H,mute,low,high,posx,val,img_clic,img_bool,events):
    if val<=0:
        img=mute
    elif val>=50:
        img=high
    else:
        img=low
    img_clic,img_bool=imgbox(surface,img,None,W*2/3+250,H,img_clic,img_bool,events)
    if img_bool:
        if val==0:
            textbox(surface,v.trad['unmute'][v.lg],20,W*2/3+250,H+40,color=v.WHITE)
        else:
            textbox(surface,v.trad['mute'][v.lg],20,W*2/3+250,H+40,color=v.WHITE)
    if img_clic:
        if val==0:
            val=50
        elif val>0:
            val=0
        params=(W*2/3-400/2,W*2/3-400/2+400-20,0,100)
        posx=getPosByValue(params,val)
    return posx,val,img_clic,img_bool

# button1 --> "boutton d'accès - suite indépendante" (ex: bouttons retour --> la suite sera toujours la même)
# button2 --> "boutton de choix - suite dépendante" (ex: bouttons nb de persos --> la suite dépendra du choix du boutton)

def button1(surface,text,dimensions,clic,hover,events,color=v.BLACK,undercolor=v.DARKSLATEGRAY,
            textcolor=v.WHITE,textsize=40):
    left,top,width,height=dimensions
    left,top=center(left,top,width,height)
    dist=0
    if hover:
        dist=height/18
    try:
        rect=pygame.draw.rect(surface,undercolor,(left,top,width,height+height/18),border_radius=8)
        pygame.draw.rect(surface,color,(left,top-dist,width,height),border_radius=8)
    except:
        rect=pygame.draw.rect(surface,undercolor,(left,top,width,height+height/18))
        pygame.draw.rect(surface,color,(left,top-dist,width,height))
    textbox(surface,text,textsize,left+width/2,top-dist+height/2,color=textcolor)
    return eventBools(rect,events,hover,clic)

def button2(surface,text,dimensions,clic,hover,events,color=v.BLACK,hcolor=v.DARKSLATEGRAY,
            textcolor=v.WHITE,textsize=40,bradius=12):
    left,top,width,height=dimensions
    left,top=center(left,top,width,height)
    if hover:
        color=hcolor
    try:
        rect=pygame.draw.rect(surface,color,(left,top,width,height),border_radius=bradius)
    except:
        rect=pygame.draw.rect(surface,color,(left,top,width,height))
    textbox(surface,text,textsize,left+width/2,top+height/2,color=textcolor)
    return eventBools(rect,events,hover,clic)

def transitionSortie(loading=False):
    if v.animations:
        W,H=v.W,v.H
        loop=0
        while loop<=8/5*W:
            if loop<=H:
                pygame.draw.polygon(v.surface,v.BLACK,[(0,0),(loop,0),(0,loop)])
            elif loop<=W:
                pygame.draw.polygon(v.surface,v.BLACK,[(0,0),(loop,0),(loop-H,H),(0,H)])
            else:
                pygame.draw.polygon(v.surface,v.BLACK,[(0,0),(W,0),(W,loop-W),(loop-H,H),(0,H)])
            loop+=30
            if loading:
                textbox(v.surface,'Loading...',75,W/2,H/2)
            pygame.display.update()
    return

def transitionEntree(img):
    W,H=v.W,v.H
    loop=8/5*W
    while loop>=0:
        imgbox(v.surface,img,None,W/2,H/2)
        if loop>=W:
            pygame.draw.polygon(v.surface,v.BLACK,[(W,H),(0,H),(0,H-loop+W),(W-loop+H,0),(W,0)])
        elif loop>=H:
            pygame.draw.polygon(v.surface,v.BLACK,[(W,H),(W-loop,H),(W-loop+H,0),(W,0)])
        else:
            pygame.draw.polygon(v.surface,v.BLACK,[(W,H),(W-loop,H),(W,H-loop)])
        loop-=70
        pygame.display.update()
    return

def doTrans(trans):
    if trans and v.animations:
        pygame.image.save(v.surface,'screen.jpg')
        transitionEntree(load('screen.jpg'))
        trans=False
    return trans

def gradientRect(surface,color1,color2,target): # pour faire un dégradé
    rect=pygame.Surface((2,2)) # surface 2*2 pour les lignes
    pygame.draw.line(rect,color1,(0,0),(1,0)) # ligne couleur 1
    pygame.draw.line(rect,color2,(0,1),(1,1)) # ligne couleur 2
    rect=pygame.transform.smoothscale(rect,(target.width,target.height)) # "mélange" des deux
    surface.blit(rect,target)

def opacityRect(left,top,width,height,clic,hover,r=255,g=255,b=255,a=128,events=default):
    obj=pygame.Surface((width,height),pygame.SRCALPHA) # pour "importer" alpha
    obj.fill((r,g,b,a)) # couleur en rgba (a pour alpha) : l'opacité (ici par défaut a=128=50%)
    v.surface.blit(obj,(left,top))
    return eventBools(pygame.Rect(left,top,width,height),events,hover,clic)
