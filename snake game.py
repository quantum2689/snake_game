
from pygame.locals import *
import pygame
from random import randint
#create snake game
class Snake:
    #initialize snake
    def __init__(self):
        #create snake
        self.snake = [(100, 100), (90, 100), (80, 100)]
        #create direction
        self.direction_x = 0
        self.direction_y = 1
        #create score
        self.score = 0
    #check if snake is dead
    def is_dead(self):
        #check if snake is dead
        if self.snake[0][0] < 0 or self.snake[0][0] > 639 or self.snake[0][1] < 0 or self.snake[0][1] > 479:
            return True
        for i in range(1, len(self.snake)):
            if self.snake[0][0] == self.snake[i][0] and self.snake[0][1] == self.snake[i][1]:
                return True
        return False
    #check if snake ate food
    def ate_food(self, food):
        #check if snake ate food

        if (food.food_x - 10 <= self.snake[0][0] <= food.food_x + 10) and  food.food_y - 10  <= self.snake[0][1] <= food.food_y + 10:
            return True
        else:
            return False
    #change direction
    def change_direction(self, x, y):
        #change direction
        self.direction_x = x
        self.direction_y = y
    #draw snake
    def draw_snake(self, surface):
        #draw snake
        for i in range(len(self.snake)):
            pygame.draw.rect(surface, (0, 255, 0), (self.snake[i][0], self.snake[i][1], 10, 10))
    #move snake
    def move_snake(self):
        #move snake
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i - 1][0], self.snake[i - 1][1])
        self.snake[0] = (self.snake[0][0] + self.direction_x * 10, self.snake[0][1] + self.direction_y * 10)
    #add food
    def add_food(self, food):
        #add food
        self.snake.append((food.food_x, food.food_y))
    #increase score
    def increase_score(self):
        #increase score
        self.score += 1
    #get score
    def get_score(self):
        #get score
        return self.score
    

class Food():
    #initialize food
    def __init__(self):
        #create food
        self.food_x = 0
        self.food_y = 0
        #generate food
        self.generate_food()
    #generate food
    def generate_food(self):
        #generate food
        self.food_x = randint(0, 639)
        self.food_y = randint(0, 479)
    #draw food
    def draw_food(self, surface):
        #draw food
        pygame.draw.rect(surface, (255, 0, 0), (self.food_x, self.food_y, 10, 10))
    def get_food_x(self):
        #get food x
        return self.food_x
    def get_food_y(self):
        #get food y
        return self.food_y
    
def main():
    #initialize pygame
    pygame.init()
    #create screen
    screen = pygame.display.set_mode((640, 480))
    #set caption
    pygame.display.set_caption("Snake Game")
    #create surface
    surface = pygame.Surface((640, 480))
    #create snake
    snake = Snake()
    #create food
    food = Food()
    #create clock
    clock = pygame.time.Clock()
    #create game loop
    while True:
        #set fps
        clock.tick(10)
        #check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.change_direction(0, -1)
                elif event.key == K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == K_RIGHT:
                    snake.change_direction(1, 0)

        #check if snake is dead
        if snake.is_dead():
            print("Game Over")
            pygame.quit()
            return
        #check if snake ate food
        if snake.ate_food(food):
            food.generate_food()
            snake.add_food(food)
        #draw surface
        surface.fill((0, 0, 0))
        #draw food
        food.draw_food(surface)
        #draw snake
        snake.draw_snake(surface)
        #draw surface
        screen.blit(surface, (0, 0))
        #update screen
        snake.move_snake()
        pygame.display.update()

main()
