import os
import time
import threading
import random
import sys

try :
    import msvcrt #que pour windows
except :
    import tty
    import termios




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
#couple : (y , x)
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTION_KEYS = {
    'z' : UP, 's' : DOWN, 'q' : LEFT, 'd': RIGHT
}



class Snake:
    
    def __init__(self, head:tuple, symbol:str, direction:tuple):
        self.body = [head]
        self.symbol = symbol
        self.direction = direction
        self.alive = True

    def move(self):
        head_y, head_x = self.body[-1]
        dy, dx = self.direction
        new_head = (head_y + dy, head_x + dx)
        self.body.append(new_head)
        return new_head
    
    def change_direction(self, new_direction):
        #Empêcher d'aller en arrière directement
        

        if ( new_direction[0] != -(self.direction[0]) or new_direction[1] != -(self.direction[1]) ):
            self.direction = new_direction
    
    def dead(self):
        """Fait mourir le serpent"""
        self.alive = False
    
    
class Map :
    
    
    def __init__(self, height:int, width:int, snakes:list[Snake]):
        self.height = height
        self.width = width
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.snakes = snakes
        
        for snake in snakes :
            for y, x in snake.body :
                self.grid[y][x] = snake.symbol
    
    
    def is_empty(self, position):
        """
        renvoie un bouléan en fonction de si la case est vide ou non 
        """
        y , x = position
        return self.grid[y][x] == ' ' 
    
    def is_inside(self, position):
        """renvoie un bouléan en fonciton de : es ce que la position est bien dans la range du tableau"""
        y , x = position
        
        
        if  0 <= y < self.height and 0 <= x < self.width :
            return True
        return False   

    def update(self):
        """faire déplacer tout les serpant en vérifiant qu'ils soit en vie . 
            a la suite de ce déplacement regarder si le serpent est mtn mort ( mort si en dehors de la map ou sur une case non vide)
            et s'il n'est pas mort alors le déplacer dans la grille"""
        
        for snake in self.snakes :
            if not snake.alive :
                continue
            
            new_head = snake.move()
            if not self.is_inside(new_head) or not self.is_empty(new_head) : 
                snake.alive = False
            else:
                y, x = new_head
                self.grid[y][x] = snake.symbol

    
    def display(self):
        """Faire l'affichage dans le terminal de la grille"""
        
        print("+" + "-" * self.width + "+")
        for row in self.grid :
            print("|" + "".join(row) + "|")      
        print("+" + "-" * self.width + "+")

    def all_alive(self):
        for snake in self.snakes:
            if not snake.alive :
                return False   
                
        return True


def get_touche():
    pass


def main():
    height, width = 15, 30
    mode = input("Mode (1 = solo, 2 = coop):")
    
    snakes = []
    
    if mode == "2" :
        s1 = Snake((5, 5),  "1", RIGHT)
        s2 = Snake((10, 10),  "2", LEFT)
        snakes = [s1, s2]
    else:
        s1 = Snake((7, 15), "1",  RIGHT)
        snakes = [s1]


    game_map = Map(height, width, snakes)
    
    
    #start l'écoute des touches 
    
    
    while(game_map.all_alive()):
        dir = input()
        
        pos = DIRECTION_KEYS[dir]
        s1.change_direction(pos)
                     
        game_map.update()
        game_map.display()
        time.sleep(0.2)
    
    
    
    print("Game Over!!!!")
    
    
if __name__ == "__main__" :
    main()




