"""
Fichier : 'variables.py'
Contenu : Variables globales du jeu
Auteurs : Noé Lacaille / Evan Le Bigot
"""

import pygame
pygame.init()

# GENERAL

W,H=1280,720 # default
surface=None
mouse_pos=(-10,-10)
mouse_click=(-10,-10)
slider_click=(-10,-10)
animations=True

# CONSTANTES

lg=1
nbLives=3
nbLifePts=100
timeLimit=0
mapChoisie=""
mapChoisieNom=""
temps=0
nbp=0
volumeCoups=25
volumeMusic=25
volumeMenu=25
matchFormat=0
winform=0
posCoups='N/A'
posMusic='N/A'
posMenu='N/A'
posNbv='N/A'
posTlim='N/A'
posLifePts='N/A'
posPercBase='N/A'
posGravite='N/A'
posMultiKb='N/A'
combattants=[0,0,0,0]
gravite=0.35
multiKb=1
pourcentBase=0
morts=0
joueurRestant=""
timeOff=0

#SONS

KO=pygame.mixer.Sound("../Sons/bruitages/K.O..mp3")
coupFaible=pygame.mixer.Sound("../Sons/bruitages/coupFaible.wav")
coupMoyen=pygame.mixer.Sound("../Sons/bruitages/coupMoyen.wav")
coupFort=pygame.mixer.Sound("../Sons/bruitages/coupFort.wav")
coupVent=pygame.mixer.Sound("../Sons/bruitages/coupVent.wav")
cible=pygame.mixer.Sound("../Sons/bruitages/cible.wav")
saut=pygame.mixer.Sound("../Sons/bruitages/saut.wav")
Sons=[KO,coupFaible,coupMoyen,coupFort,coupVent,cible,saut]
Sonclic=pygame.mixer.Sound("../Sons/bruitages/CurseurClic.wav")
SonHover=pygame.mixer.Sound("../Sons/bruitages/Curseur.wav")
Menus=[Sonclic,SonHover]
pygame.mixer.music.set_volume(0.25)
for i in Sons:
    pygame.mixer.Sound.set_volume(i,0.25)
for i in Menus:
    pygame.mixer.Sound.set_volume(i,0.25)

# COULEURS
# https://htmlcolorcodes.com/fr/noms-de-couleur/

BLACK=(0,0,0)
BLUE=(0,0,255)
BLUEVIOLET=(138,43,226)
CYAN=(0,255,255)
DARKSLATEGRAY=(49,79,79)
DARKGRAY=(169,169,169)
DARKORANGE=(255,140,0)
DIMGRAY=(105,105,105)
GOLD=(255,215,0)
GRAY=(112,128,144)
GREEN=(0,255,0)
LIGHTGRAY=(220,220,220)
LIGHTYELLOW=(240,230,140)
LIME=(0,255,0)
LIMEGREEN=(50,205,50)
MEDIUMSEAGREEN=(60,179,113)
MEDIUMPURPLE=(147,112,219)
OKGREEN=(11,121,8)
OKGREENHOVER=(67,168,43)
ORANGE=(255,165,0)
ORCHID=(218,112,214)
PLUM=(221,160,221)
RED=(255,0,0)
SALMON=(250,128,114)
SEAGREEN=(46,139,87)
SILVER=(192,192,192)
SKYBLUE=(100,149,237)
WHITE=(255,255,255)

# TRADUCTIONS
# trié par ordre alphabétique

trad={
'back':('Retour','Back','Atrás','Zurück','Назад','Voltar'),
'bonus':('Bonus','Bonus','Prima','Bonus','Бонус','Bônus'),
'char':('Personnages','Characters','Personajes','Figuren','Символы','Personagens'),
'changeoptions':('Changer les options','Change options','Cambiar opciones','Optionen ändern','Изменить параметры','Opções de mudança'),
'changesmash':('Changer smash','Change smash','Cambiar Smash','Smash ändern','Изменить Smash','Smash de mudança'),
'choosechar':('Choisissez un personnage','Choose a character','Elige un personaje','Wähle einen Charakter','Выберите персонажа','Escolha um personagem'),
'choosemap':('Veuillez choisir une map','Please choose a map','Elija un mapa','Bitte wählen Sie eine Karte','Пожалуйста, выберите карту','Por favor escolha um mapa'),
'choosenbp':('Choisissez le nombre de joueurs','Choose the number of players','Elige el número de jugadores','Wählen Sie die Anzahl der Spieler','Выберите количество игроков','Escolha o número de jogadores'),
'confirm':('Confirmer','Confirm','Confirmar','Bestätigen','Подтверждать','Confirme'),
'continue':('Continuer','Continue','Continuar','Fortsetzung','Продолжатель','Continuer'),
'deaths':('morts','deaths','muertos','tod','мертвых','mortes'),
'down':('Bas','Down','Abajo','Nieder','вниз','Baixa'),
'end':('Fin','End','Fin','Ende','Конецu','Fim'),
'end2':('La partie est terminée','The game is over','El juego ha terminado','Das Spiel ist vorbei','Игра окончена','O jogo acabou'),
'errorkeytaken':('Erreur: cette touche est déjà prise','Error: this key is already taken','Error: esta clave ya está en uso','Fehler: Dieser Schlüssel ist bereits vergeben','Ошибка: этот ключ уже занят','Erro: esta chave já está em uso'),
'errorkeyunav':('Erreur: cette touche n\'est pas disponible','Error: this key isn\'t available','Error: esta clave no está disponible','Fehler: Dieser Schlüssel ist nicht verfügbar','Ошибка: этот ключ недоступен','Erro: esta chave não está disponível'),
'fullscreen':('Plein écran','Full screen','Pantalla completa','Vollbild','Полноэкранный','Tela cheia'),
'gameoptions':('Options du jeu','Game options','Opciones de juego','Spieleinstellungen','Варианты игры','Opções de jogo'),
'gameset':('Paramètres du jeu','Game settings','Configuraciones de juego','Spieleinstellungen','Игровые настройки','Configurações do jogo'),
'gravite':('Gravité','Gravity','Gravedad','Schwere','Сила тяжести','Gravidade'),
'keys':('Touches','Keys','Teclas','Tasten','Ключи','Chaves'),
'keysofN':('Touches du joueur N','Player N keys','Teclas del jugador N','Spieler N Tasten','Ключи игрока N','Chaves do jogador N'),
'keysofpn':('Touches du PN','Keys of PN','Llaves PN','PN-Tasten','Ключи PN','Chaves PN'),
'keyset':('Paramètres des touches','Key settings','Configuraciones clave','Tasteneinstellungen','Основные настройки','Parâmetros Chave'),
'knock':('Coup','Knock','Golpe','Klopfen','Стучать','Bater'),
'lang':('Langue','Language','Lengua','Sprache','Язык','Língua'),
'left':('Gauche','Left','Izquierda','Links','Осталось','Esquerda'),
'lifepts':('Points de vies','Life points','Puntos de vida','Lebens Punkte','Очки жизни','Pontos de vida'),
'mainmenu':('Menu principal','Main Menu','Menú principal','Hauptmenü','Главное меню','Menu principal'),
'maps':('Cartes','Maps','Mapas','Karten','Карты','Mapas'),
'matchform':('Format du match','Match format','Formato de partido','Übereinstimmungsformat','Формат матча','Formato de correspondência'),
'multejec':('Multiplicateur d\'éjection','Ejection multiplier','Multiplicador de eyección','Auswurfmultiplikator','Множитель выброса','Multiplicador de ejeção'),
'musicgame':('Musique du jeu','Game music','Música de juego','Spielemusik','Игровая музыка','Musica do jogo'),
'musicmenu':('Musique du menu','Menu music','Música de menú','Menümusik','Музыка меню','Música do menu'),
'mute':('Muet','Mute','Mudo','Stumm','Немой','Mudo'),
'nboflives':('Nombres de vies','Number of lives','Número de vidas','Anzahl der Leben','Количество жизней','Numero de vidas'),
'nbplayers':('N Joueurs','N Players','N Jugadores','N Spieler','N игрока','N jogadores'),
'obstaclecourse':('Course d\'obstacles','Obstacle course','Pista de obstáculos','Hindernisstrecke','полоса препятствий','Pista de obstáculos'),
'options':('Options','Options','Opciones','Optionen','Опции','Opções'),
'pause':('Pause','Pause','Pausa','Pause','Пауза','Pausa'),
'perc':('Pourcentages','Percentages','Porcentajes','Prozentsätze','Проценты','Percentagens'),
'percbase':('Pourcentages de base','Basic percentages','Porcentajes básicos','Grundlegende Prozentsätze','Базовые проценты','Percentagens básicas'),
'play':('JOUER','PLAY','JUGAR','SPIELEN','ИГРАТЬ В','JOGAR'),
'player':('JOUEUR','PLAYER','JUGADOR','SPIELER','ИГРОК','JOGADOR'),
'player2':('Le joueur','Player','Jugador','Spieler','Игрок','Jogador'),
'presskey':('Appuyez sur une touche','Press a key','Presione una tecla','Drücke eine Taste','нажмите кнопку','Pressione uma tecla'),
'quit':('Quitter','Quit','Abandonar','Verlassen','Уволиться','Deixar'),
'random':('Aléatoire','Random','Aleatorio','Zufällig','Случайный','Aleatória'),
'rechoose':('Modifier les choix','Modify choices','Modificar las opciones','Auswahl ändern','Изменить варианты','Modificar escolhas'),
'replay':('Rejouer','Replay','Repetición','Wiederholung','Воспроизвести','Repetir'),
'return':('Retour','Return','Regreso','Rückkehr','Вернуть','Retornar'),
'returnmaj':('RETOUR','RETURN','REGRESO','RÜCKKEHR','ВЕРНУТЬ','RETORNA'),
'right':('Droite','Right','Derecha','Rechts','Правильно','Direita'),
'selectlpf':('Sélectionnez le format des points de vie pour le définir','Select the life points format to set it','Seleccione el formato de puntos de vida para configurarlo','Wählen Sie das Lebenspunktformat aus, um es festzulegen','Выберите формат очков жизни, чтобы установить его','Selecione o formato do ponto de vida para defini-lo'),
'shield':('Bouclier','Shield','Proteger','Schild','Щит','Escudo'),
'smash':('Smash','Smash','Smash','Smash','Играть','Smash'),
'solo':('Solo','Solo','Solo','Solo','Соло','Só'),
'sound':('Son et Musique','Sound and Music','Sonido y musica','Ton und Musik','Звук и музыка','Som e Música'),
'soundchar':('Son des personnages','Character sound','Sonido de personajes','Charaktersound','Звук персонажа','Som do personagem'),
'targetsmash':('Smash dans le mille !!','Target Smash !!','Dianas Smash !!','Ziel Smash !!','Удар в цель !!','Esmague o alvo !!'),
'timelimit':('Limite de temps','Time limit','Límite de tiempo','Zeitlimit','Лимит времени','Limite de tempo'),
'unmute':('Activer le son','Activate sound','Activar sonido','Stummschaltung aufheben','Активировать звук','Ativar som'),
'up':('Haut','Up','Arriba','Oben','Вверх','Acima'),
'valider':('Valider','Validate','Validar','Bestätigen','Подтвердить','Validar'),
'winform':('Fenêtre','Window','Ventana','Fenster','окно','Janela'),
'wins':('gagne','wins','gana','gewinnt','побеждает','vence'),
'.parcours':('Atteignez la zone $ bleue pour progresser $ dans les niveaux','Reach the blue $ zone to progress $ through the levels','Llega a la zona $ azul para avanzar $ por los niveles.','Erreichen Sie die $ blaue Zone, um die $ Level zu durchlaufen','Достигайте синей $ зоны, чтобы $ проходить уровни.','Alcance a zona $ azul para progredir $ nos níveis'),
'.targetSmash':('Détruisez toutes $ les cibles le plus $ rapidement possible','Destroy all $ targets as quickly $ as possible','Destruye todos $ los objetivos lo $ más rápido posible','Zerstöre alle $ Ziele so schnell $ wie möglich','Уничтожьте $ все цели как $ можно быстрее','Destrua todos $ os alvos o mais $ rápido possível'),
}

# TOUCHES
# https://www.pygame.org/docs/ref/key.html

keys=[(pygame.K_BACKSPACE,'back'),(pygame.K_TAB,'tab'),(pygame.K_RETURN,'enter'),(pygame.K_PAUSE,'pause'),
      (pygame.K_ESCAPE,'esc'),(pygame.K_SPACE,'space'),(pygame.K_EXCLAIM,'!'),(pygame.K_QUOTEDBL,'"'),
      (pygame.K_HASH,'#'),(pygame.K_DOLLAR,'$'),(pygame.K_AMPERSAND,'&'),(pygame.K_LEFTPAREN,'('),
      (pygame.K_RIGHTPAREN,')'),(pygame.K_ASTERISK,'*'),(pygame.K_PLUS,'+'),(pygame.K_COMMA,','),
      (pygame.K_MINUS,'-'),(pygame.K_PERIOD,'.'),(pygame.K_SLASH,'/'),(pygame.K_0,'0'),(pygame.K_1,'1'),
      (pygame.K_2,'2'),(pygame.K_3,'3'),(pygame.K_4,'4'),(pygame.K_5,'5'),(pygame.K_6,'6'),(pygame.K_7,'7'),(pygame.K_8,'8'),
      (pygame.K_9,'9'),(pygame.K_COLON,':'),(pygame.K_SEMICOLON,';'),(pygame.K_LESS,'<'),(pygame.K_EQUALS,'='),
      (pygame.K_GREATER,'>'),(pygame.K_QUESTION,'?'),(pygame.K_AT,'@'),(pygame.K_LEFTBRACKET,'['),
      (pygame.K_BACKSLASH,'\\'),(pygame.K_RIGHTBRACKET,']'),(pygame.K_CARET,'^'),
      (pygame.K_UNDERSCORE,'_'),(pygame.K_BACKQUOTE,'`'),(pygame.K_a,'A'),(pygame.K_b,'B'),(pygame.K_c,'C'),
      (pygame.K_d,'D'),(pygame.K_e,'E'),(pygame.K_f,'F'),(pygame.K_g,'G'),(pygame.K_h,'H'),(pygame.K_i,'I'),(pygame.K_j,'J'),
      (pygame.K_k,'K'),(pygame.K_l,'L'),(pygame.K_m,'M'),(pygame.K_n,'N'),(pygame.K_o,'O'),(pygame.K_p,'P'),(pygame.K_q,'Q'),
      (pygame.K_r,'R'),(pygame.K_s,'S'),(pygame.K_t,'T'),(pygame.K_u,'U'),(pygame.K_v,'V'),(pygame.K_w,'W'),(pygame.K_x,'X'),
      (pygame.K_y,'Y'),(pygame.K_z,'Z'),(pygame.K_DELETE,'del'),(pygame.K_KP0,'0 (KP)'),(pygame.K_KP1,'1 (KP)'),
      (pygame.K_KP2,'2 (KP)'),(pygame.K_KP3,'3 (KP)'),(pygame.K_KP4,'4 (KP)'),(pygame.K_KP5,'5 (KP)'),
      (pygame.K_KP6,'6 (KP)'),(pygame.K_KP7,'7 (KP)'),(pygame.K_KP8,'8 (KP)'),(pygame.K_KP9,'9 (KP)'),
      (pygame.K_KP_PERIOD,'. (KP)'),(pygame.K_KP_DIVIDE,'/ (KP)'),(pygame.K_KP_MULTIPLY,'* (KP)'),
      (pygame.K_KP_MINUS,'- (KP)'),(pygame.K_KP_PLUS,'+ (KP)'),(pygame.K_KP_ENTER,'ent (KP)'),
      (pygame.K_KP_EQUALS,'= (KP)'),(pygame.K_UP,'↑'),(pygame.K_DOWN,'↓'),(pygame.K_RIGHT,'→'),
      (pygame.K_LEFT,'←'),(pygame.K_F1,'F1'),(pygame.K_F2,'F2'),(pygame.K_F3,'F3'),(pygame.K_F4,'F4'),
      (pygame.K_F5,'F5'),(pygame.K_F6,'F6'),(pygame.K_F7,'F7'),(pygame.K_F8,'F8'),(pygame.K_F9,'F9'),
      (pygame.K_F10,'F10'),(pygame.K_F11,'F11'),(pygame.K_F12,'F12'),(pygame.K_NUMLOCK,'num'),
      (pygame.K_CAPSLOCK,'maj'),(pygame.K_RSHIFT,'R-shift'),(pygame.K_LSHIFT,'L-shift'),
      (pygame.K_RCTRL,'R-ctrl'),(pygame.K_LCTRL,'L-ctrl'),(pygame.K_RALT,'R-alt'),
      (pygame.K_LALT,'L-alt'),(pygame.K_RMETA,'R-meta'),(pygame.K_LMETA,'L-meta')]

pyKeys=[i[0] for i in keys]
ltKeys=[i[1] for i in keys]

keysTaken=[pygame.K_z,pygame.K_q,pygame.K_s,pygame.K_d,pygame.K_e,pygame.K_a,
           pygame.K_t,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_y,pygame.K_r,
           pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_o,pygame.K_u,
           pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_KP0,pygame.K_KP1,
           pygame.K_ESCAPE,pygame.K_n]