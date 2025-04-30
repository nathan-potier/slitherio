


"""
class : 

Map:
    init
    apartion_point
    déplacement
Snake





description : 

dans un premier temps affichage dans le terminal 

un jeux ou le joueur controle un serpant dans une partie ( comme le jeux du snake ) sauf que :
le serpent avance tout seul tout le temps et ses directions sont controler par l'utilisateur . 
chaque case traverser devient le serpent et donc on ne peut plus y passer . 
si le serpant veut aller sur une case qui n'est pas vide alors il perd . 

ajout du mode coop meme jeux mais avec 2 serpents chacun controlés par un joueur différent . 


faire affichage graphgique 
"""

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RGIHT = (0, 1)

DIRECTION_KEYS = {
    'z' : UP, 's' : DOWN, 'q' : LEFT, 'd': RGIHT
}



class Snake:
    
    def __init__(self, head:tuple, symbol:str, direction:tuple):
        self.body = [head]
        self.symbol = symbol
        self.direction = direction
        self.alive = True
        
    def move(self):
        pass
    
    
    def cahnge_direction(self):
        pass
    
    def dead(self):
        self.alive = False
    
    
class Map :
    
    
    def __init__(self, height:int, width:int, snakes:Snake):
        self.height = height
        self.width = width
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.snakes = snakes
        
        for snake in snakes :
            for y, x in snake.body :
                self.grid[y][x] = snake.symbol
    
    
    def is_empty(self):
        pass
    
    def is_inside(self):
        pass
    
    def update(self):
        pass
    
    def display(self):
        pass
    
    def all_alive(self):
        pass
    
    
