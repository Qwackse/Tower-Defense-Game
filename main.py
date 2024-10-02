import pygame, sys, os

#Setting the FPS and window size.
FPS = 60 
fpsClock = pygame.time.Clock()
window_width = 800
window_height = 600


pygame.display.set_caption('Tower Defense Game') #This basically sets the title of the window, above the game instance. 
pygame.init() #This is how we initialize pygame. 
window = pygame.display.set_mode((window_width, window_height)) #Sets the window to be stored inside of a variable. This has to be referenced in order to change anything on the screen.

#Class for the start screen. Handles rendering and checking for clicks to change the scene.
class StartScreen:
    def __init__(self, window):
        self.window = window
        self.background = pygame.image.load(os.path.join('game_assests', 'start_screen_background.jpg')) #Loads the background image, uses the image path, the os module allows python to access your files.
        self.background = pygame.transform.scale(self.background, (window_width, window_height)) #Scales the image to the size of the window (might not always look good depending on original image size)
        self.font = pygame.font.SysFont(None, 55) #Sets the font to be used by text. 
        self.title_text = self.font.render('Tower Defense Game', True, (255, 255, 255)) #Creates the text that is rendered. 
        self.start_text = self.font.render('Click to Start', True, (255, 255, 255))  

    def render(self):
        self.window.blit(self.background, (0, 0)) #blit draws the image on the window. In this case it is the background image.
        self.window.blit(self.title_text, (window_width // 2 - self.title_text.get_width() // 2, 100)) #Draws the title text on the window, the math is to center the text.
        start_text_rect = self.start_text.get_rect(center=(window_width // 2, 400)) #Creates a rectangle around the text.

        #Math to calculate the size of the rectangle with padding around the text, probably needs to be bigger.
        rect_x = start_text_rect.x - 10 
        rect_y = start_text_rect.y - 10
        rect_width = start_text_rect.width + 20
        rect_height = start_text_rect.height + 20

        pygame.draw.rect(self.window, (39, 145, 39), (rect_x, rect_y, rect_width, rect_height)) #Draws the rectangle around the text.
        self.window.blit(self.start_text, start_text_rect.topleft) #Draws the start text on the window.
        pygame.display.update() #Updates the window to show the changes.

    def check_for_click(self):
        for event in pygame.event.get(): #Here we are checking for "events". Events are things like mouse clicks, key presses, etc.
            if event.type == pygame.QUIT: #This branch detects if the user clicks the X button. Very important or you literally cant close the game.
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #This branch just checks for a mouse click, will change later so they have to click the box.
                return True
        return False #If no events are detected, the function returns false.

#Class for the main game screen. Handles rendering aswell. 
class MainGameScreen:
    def __init__(self, window):
        self.window = window #Sets the window to be used by the class.
        self.background = pygame.image.load(os.path.join('game_assests', 'map_one.png')) #Loads the background image.
        self.background = pygame.transform.scale(self.background, (window_width, window_height)) #Scales the image to the window size.
 
    def render(self):
        #We will need to update this later to draw the map, towers, enemies, etc.
        self.window.blit(self.background, (0, 0)) #Draws the background image on the window.
        pygame.display.update() #Updates the window to show the changes.
    
    def check_for_click(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #checks to see if the user clicks the X button.
                pygame.quit()
                sys.exit()
        return False


def main():
    start_screen = StartScreen(window) #Creates an instance of the start screen class.
    main_game_screen = MainGameScreen(window) #Creates an instance of the main game screen class.
    game_state = 'start_screen' #Sets the initial game state to the start screen.
    
    while True: #This is the main game loop. It will run until the game is closed.
        if game_state == 'start_screen': #This branch checks the game state and renders the appropriate screen.
            start_screen.render() #Renders the start screen using the function we created in the class.
            if start_screen.check_for_click(): #Checks for a click on the start screen, uses class function.
                game_state = 'main_game' #If a click is detected, the game state is changed to the main game.
                
        elif game_state == 'main_game': #This branch checks the game state and renders the appropriate screen.
            main_game_screen.render() #Renders the main game screen using the function we created in the class.
            main_game_screen.check_for_click() #Checks for a click on the main game screen, uses class function.

        fpsClock.tick(FPS) #This controls the FPS of the game.


if __name__ == '__main__':
    main()
