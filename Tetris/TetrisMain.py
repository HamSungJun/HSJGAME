import pygame, random , sys
pygame.init()

side = 15
dime = (300 , 600)
game_screen = pygame.display.set_mode(dime)
clock = pygame.time.Clock()

class Block():
    def __init__(self , rel_pos):
        self.rel_pos = rel_pos
        self.color = None
    
    def setColor(self , color):
        self.color = color
    
    def draw(self , pos):
        x = (self.rel_pos[0] + pos[0])*side
        y = (self.rel_pos[1] + pos[1])*side
        game_screen.fill(self.color , pygame.Rect(x+1 , y+1 , side-2 , side-2))

class Group():
    def __init__(self , blocks , color , height) :
        self.blocks = blocks
        self.color = color
        self.h = height
        for block in blocks :
            block.setColor(self.color)
        
    def draw(self , pos) :
        for block in self.blocks:
            block.draw(pos)
            
class SavedGroup():
    def __init__(self):
        self.stuffs = []
        
    def save(self, cGroup):
        for block in cGroup.group.blocks:
            self.stuffs.append((block.rel_pos[0] + cGroup.x,block.rel_pos[1] + cGroup.y , cGroup.group.color))
    
    def draw(self):
        for stuff in self.stuffs:
            game_screen.fill(stuff[2], pygame.Rect(stuff[0]*side+1 , stuff[1]*side+1 , side-2 , side-2))
        
groups = (Group((Block((0,0)), Block((0,1)) , Block((1,0)) , Block((1,1))) , (200, 100, 50) , 2),
         Group((Block((0,0)), Block((0,1)) , Block((0,2)) , Block((0,3))) , (50, 200 , 100) , 4),
         Group((Block((1,0)), Block((2,0)) , Block((1,1)) , Block((0,1))) , (47, 112 , 200) , 2),
         Group((Block((0,0)), Block((1,0)) , Block((1,1)) , Block((2,1))) , (200, 47 , 112) , 2),
         Group((Block((0,1)), Block((1,0)) , Block((1,1)) , Block((2,1))) , (229, 240, 32) , 2),
         Group((Block((1,0)), Block((1,1)) , Block((1,2)) , Block((2,0))) , (240, 107, 32) , 2),
         Group((Block((0,0)), Block((0,1)) , Block((1,1)) , Block((2,1))) , (32, 209, 240) , 2),)
saves = SavedGroup()

class CurrentGroup():
    def __init__(self):
        self.group = groups[random.randint(0,len(groups) - 1)]
        self.y = -self.group.h
        self.x = 9
        self.tick = 10
        self.face = 0
        
    def draw(self) :
        self.group.draw((self.x , self.y))
        
    def fall(self) :
        self.y += 1
        self.hitBottom()
        
    def moveH(self):
        if self.face == 1 and self.x <= 19:
            self.x += 1
        elif self.face == 2 and self.x >= 0:
            self.x -= 1
        self.hitBlock()
        self.hitBlock()
        
            
    def hitBottom(self):
        if self.y > 39-self.group.h:
            saves.save(self)
            self.group = groups[random.randint(0 , len(groups) -1)]
            self.y = -self.group.h
            self.x = 9
            
    def hitBlock(self):
        for block in self.group.blocks:
            for tblock in saves.stuffs:
                if block.rel_pos[0]+self.x == tblock[0] and block.rel_pos[1]+self.y+1 == tblock[1]:
                    saves.save(self)
                    self.group = groups[random.randint(0 , len(groups) -1)]
                    self.y = -self.group.h
                    self.x = 9
                    

Body = CurrentGroup()

def acceDetect():
    global counter
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_DOWN]:
        Body.tick = 1
        
    else:
        Body.tick = 10
        
def horDetect():
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_RIGHT]:
        Body.face = 1
    elif keyPressed[pygame.K_LEFT]:
        Body.face = 2
    else :
        Body.face = 0

counter = 0
h_con = 0
while True :
    game_screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            acceDetect()
            horDetect()
    if counter >= Body.tick:
        Body.fall()
        counter = 0
    else:
        counter+=1
    if h_con >= 4:
        h_con +=1
        Body.moveH()
    else:
        h_con += 1
    Body.draw()
    saves.draw()
    pygame.display.flip()
    clock.tick(20)