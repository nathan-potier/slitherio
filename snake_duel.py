


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
        head_y, head_x = self.body[-1]
        dy, dx = self.direction
        new_head = (head_y + dy, head_x + dx)
        self.body.append(new_head)
        return new_head
    
    def change_direction(self, new_direction):
        #Empêcher d'aller en arrière directement
        if ( new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1] ):
            self.direction = new_direction
    
    def dead(self):
        """Fait mourir le serpent"""
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
    
    def display(self):
        """Faire l'affichage dans le terminal de la grille"""
        pass
    
    def all_alive(self):
        for snake in self.snakes:
            if not snake.alive :
                return False   
                
        return True


def get_touche():
    pass


def main():
    pass





if __name__ == "__main__" :
    main()
    
    
