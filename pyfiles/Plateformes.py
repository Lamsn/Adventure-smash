import pygame
import variables as v
W,H=v.W,v.H
class map1(pygame.sprite.Sprite):
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(1680,100)).convert_alpha()# elle occupe une place de 1280 par 32 pixels            
            self.rect = self.image.get_rect(center=(W//2,H*9//10))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=False
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(300,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(center=(W//3,H*6//10)) 
                self.solid=False
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(300,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels         
                self.rect = self.image.get_rect(center=(W*2//3,H*6//10))
                self.solid=False
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(300,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(center=(W//2,H*3//10))  
                self.solid=False
class map2(pygame.sprite.Sprite):
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeMarais.png"),(1000,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(109,567))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=False
class map3(pygame.sprite.Sprite):
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeTerre.png"),(1000,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(109,567))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=False
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeTerre.png"),(455,15)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(413,52)) 
                self.solid=False
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeTerre.png"),(455,15)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(413,152))
                self.solid=False
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeTerre.png"),(455,15)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(413,252))       
                self.solid=False    
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeTerre.png"),(455,15)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(413,352))
                self.solid=False   
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeTerre.png"),(455,15)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(413,452))
                self.solid=False   
class map4(pygame.sprite.Sprite):
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeDesert.png"),(580,330)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(801,471))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeDesert.png"),(492,330)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(-10,471)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeDesert.png"),(511,17)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(395,233))
                self.solid=False
class stage1(pygame.sprite.Sprite):
    spawnPoint=((0,0))
    class fin(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.Surface((50, 50))# elle occupe une place de 1280 par 32 pixels
            self.image.fill((0,0,255))# elle est remplie en blanc
            self.rect = self.image.get_rect(center=(W-25,25))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(1680,100)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(center=(W//2,H*9//10))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(330,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(center=(W//3,H*6//10)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(300,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(center=(W*2//3,H*6//10))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(330,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(center=(W//2,H*3//10))  
                self.solid=True
class stage2(pygame.sprite.Sprite):
    spawnPoint=((0,200))
    class fin(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.Surface((50, 50))# elle occupe une place de 1280 par 32 pixels
            self.image.fill((0,0,255))# elle est remplie en blanc
            self.rect = self.image.get_rect(center=(W-25,25))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(1680,100)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(midleft=(0,H*9//10))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(330,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(midleft=(W//5,H*6//10)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(330,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(midleft=(W*5//10,H*6//10))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(330,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(midleft=(W//3,H*3//10))  
                self.solid=True
    class spike1(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(100,500)).convert()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(midleft=(W//5,H*3//10))  
                self.solid=True
    class spike2(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(100,400)).convert()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(midleft=(W*5//10,H*11//20))  
            self.solid=True
class stage3(pygame.sprite.Sprite):
    spawnPoint=((0,0))
    class fin(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.Surface((50, 50))# elle occupe une place de 1280 par 32 pixels
            self.image.fill((0,0,255))# elle est remplie en blanc
            self.rect = self.image.get_rect(center=(W-25,25))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(265,100)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(286,490))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(290,70)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(190,190)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(285,55)).convert_alpha()# elle occupe une place de 1280 par 32 pixels             
                self.rect = self.image.get_rect(topleft=(630,115))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(270,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(890,390))  
                self.solid=True
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(80,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1180,220))  
                self.solid=True
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(80,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1080,110))  
                self.solid=True
class stage4(pygame.sprite.Sprite):
    spawnPoint=((50,450))
    class fin(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.Surface((50, 50))# elle occupe une place de 1280 par 32 pixels
            self.image.fill((0,0,255))# elle est remplie en blanc
            self.rect = self.image.get_rect(center=(W-25,25))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(1280,100)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(0,490))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(260,95)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(285,390)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(290,80)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(190,190))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(5,280)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(650,210))  
                self.solid=True
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(285,50)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(635,115))  
                self.solid=True
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(275,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(890,390))  
                self.solid=True
    class plateforme7(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(5,75)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1050,0))  
                self.solid=True
    class plateforme8(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(80,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1080,110))  
                self.solid=True
    class plateforme9(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(80,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1180,220))  
                self.solid=True
  
            
class stage5(pygame.sprite.Sprite):
    spawnPoint=((60,320))
    class fin(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.Surface((50, 50))# elle occupe une place de 1280 par 32 pixels
            self.image.fill((0,0,255))# elle est remplie en blanc
            self.rect = self.image.get_rect(center=(W-25,25))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(220,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(0,500))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(240,35)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(210,450)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(50,345)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(250,0))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(60,330)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(390,130))  
                self.solid=True
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(70,550)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(600,0))  
                self.solid=True
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(310,60)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(600,700))  
                self.solid=True
    class plateforme7(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(275,90)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(670,230))  
                self.solid=True
    class plateforme8(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(60,230)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(450,490))  
                self.solid=True
    class plateforme9(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(230,90)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(830,510))  
                self.solid=True
    class plateforme10(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(65,350)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1065,140))  
                self.solid=True

            
class stage6(pygame.sprite.Sprite):
    spawnPoint=((50,530))
    class fin(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.Surface((50, 50))# elle occupe une place de 1280 par 32 pixels
            self.image.fill((0,0,255))# elle est remplie en blanc
            self.rect = self.image.get_rect(center=(W-25,25))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
    
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(390,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(0,240))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(390,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(0,420)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(390,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(0,615))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(80,470)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(580,190))  
                self.solid=True
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(300,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(770,230))  
                self.solid=True
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(300,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(770,370))  
                self.solid=True
    class plateforme7(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(80,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(780,600))  
                self.solid=True
    class plateforme8(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(180,400)).convert_alpha()
                self.rect = self.image.get_rect(topleft=(1045,640))  
                self.solid=True
    class plateforme9(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(5,550)).convert_alpha()
                self.rect = self.image.get_rect(topleft=(1100,0))  
                self.solid=True
    class plateforme10(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(5,550)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1275,0))  
                self.solid=True
class stage7(pygame.sprite.Sprite):
    spawnPoint=((0,0))
    class fin(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.Surface((1280, 115))# elle occupe une place de 1280 par 32 pixels
            self.image.fill((0,0,255))# elle est remplie en blanc
            self.rect = self.image.get_rect(topleft=(1250 , 25))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(60,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(40,620))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(90,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(270,475)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(30,10)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(510,290))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(100,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(705,460))  
                self.solid=True
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(170,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(980,550))  
                self.solid=True
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(80,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1230,340))  
                self.solid=True
    class plateforme7(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(110,30)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1070,130))  
                self.solid=True
                
    class spike1(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(30,40)).convert()
                self.rect = self.image.get_rect(topleft=(70,580))  
                self.solid=True
    class spike2(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(60,75)).convert()
            self.rect = self.image.get_rect(topleft=(300,400))  
            self.solid=True
    class spike3(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(220,420)).convert()
            self.rect = self.image.get_rect(topleft=(420,300))  
            self.solid=True
    class spike4(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(50,50)).convert()
            self.rect = self.image.get_rect(topleft=(705,390))  
            self.solid=True
    class spike5(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(80,270)).convert()
            self.rect = self.image.get_rect(topleft=(980,280))  
            self.solid=True
    class spike6(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Pic.jpg"),(90,190)).convert()
            self.rect = self.image.get_rect(topleft=(1150,365))  
            self.solid=True   

class target1(pygame.sprite.Sprite):
    spawnPoint=((0,0))
    cibles=[[40,630],[1165,27],[100,50],[560,400],[170,600],[970,0]] 
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(1280,90)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topleft=(0,630))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(20,281)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(329,92)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(565,19)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(349,354))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(73,384)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1056,0))  
                self.solid=True   
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(37,153)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(574,480))  
                self.solid=True  
class target2(pygame.sprite.Sprite):
    spawnPoint=((0,0))
    class plateforme1(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(40,720)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(0,0)) 
                self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(565,19)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(349,354))
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(73,384)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1056,0))  
                self.solid=True   
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(37,153)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(574,480))  
                self.solid=True  
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(50,700)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(100,120))
                self.solid=True
class target3(pygame.sprite.Sprite):
    spawnPoint=((0,0))  
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(130,70)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topright=(260,655))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(60,700)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(100,70)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(830,55)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(940,70))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(130,70)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(500,650))  
                self.solid=True   
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(37,37)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(850,220))  
                self.solid=True  
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(55,200)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(650,520))
                self.solid=True
    class plateforme7(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(345,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(984,684))
                self.solid=True
    class plateforme8(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(45,190)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(985,530))
                self.solid=True
    class plateforme9(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(160,45)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(1100,485))
                self.solid=True
    class plateforme10(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(30,60)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(1100,515))
                self.solid=True
class target4(pygame.sprite.Sprite):
    spawnPoint=((0,0))
    class plateforme1(pygame.sprite.Sprite):
        """Plateforme du stage"""
        def __init__(self): 
            self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(170,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
            self.rect = self.image.get_rect(topright=(210,80))#on positionne la plateforme dans un emplacement où son centre vaut x : 640 pixels et y : 700 pixels
            self.solid=True
    class plateforme2(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(170,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topleft=(1070,80)) 
                self.solid=True
    class plateforme3(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(170,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(540,160))
                self.solid=True
    class plateforme4(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(170,40)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(910,160))  
                self.solid=True   
    class plateforme5(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(50,250)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(150,315))  
                self.solid=True  
    class plateforme6(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/Mur.png"),(50,250)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(1180,315))
                self.solid=True
    class plateforme7(pygame.sprite.Sprite):
            """Plateforme du stage"""
            def __init__(self): 
                self.image = pygame.transform.scale(pygame.image.load("../img/Plateformes/PlateformeCiel.png"),(24,24)).convert_alpha()# elle occupe une place de 1280 par 32 pixels
                self.rect = self.image.get_rect(topright=(652,600))
                self.solid=True
