from time import sleep, time
import pygame
from Map import Map

def main():
    # Define variables specific to pygame:
    title = "Terminal Submarine" # Title of the game window
    (width, height) = (1000, 700) # Width and height of the game window
    targetFPS = 60 # Target frames per second for the game loop

    # Define game specific variables:
    menu = "Main"
    map = Map("GameMap") # Create a Map object with the specified map file
    gameRunning = True # Variable to control the main loop
    prevTime = time() # Store the previous time for FPS calculation

    pygame.init() # Initialize the Pygame library
    pygame.display.set_caption(title) # Set the window title
    mainWindow = pygame.display.set_mode((width, height)) # Create the main window with the specified size

    drawGameWindow(mainWindow, width, height, menu, map) # Draw the first game window before entering the main loop
    while gameRunning: # Main Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the user closes window
                gameRunning = False # Exit the main loop
            isKeyPressed, menu = getUserInput(event, menu) # Call the function to handle user input
            if isKeyPressed: # Call the function to draw the game window if a key is pressed
                if menu == "Quit": # Check if the current menu is the quit menu
                    gameRunning = False # Exit the main loop
                else:
                    drawGameWindow(mainWindow, width, height, menu, map) # Call the function to draw the game window if a key is pressed

        # Handle FPS
        currentTime = time() # Get the current time
        diff = currentTime - prevTime # Calculate the time difference since the last frame
        delay = max(1.0 / targetFPS - diff, 0) # Calculate the delay needed to maintain target FPS
        sleep(delay) # Sleep for the calculated delay
        prevTime = time() # Update the previous time for the next iteration

    pygame.quit() # Quit Pygame when the main loop ends



def drawMainMenu(mainWindow, width, height):
    with open("MainMenu.txt", "r") as file: # Open the MainMenu.txt file in read mode
        menuContent = file.read() # Read the content of the file
        print(menuContent) # Print the content to the console (for debugging purposes)

    font = pygame.font.Font(None, 40) # Create a font object with size 40
    menuText = font.render(menuContent, True, (255, 255, 255)) # Render the menu textin white color

    mainWindow.blit(menuText, (width/2 - menuText.get_width()/2, height/2 - menuText.get_height()/2)) # Draw the menu text on the main window at the center of the window

def drawNavigationMenu(mainWindow, width, height, map):
    # font = pygame.font.Font("cour.ttf", 14) # Create a font object with size 14
    # font = pygame.font.SysFont("couriernew", 14) # Create a font object with size 14
    font = pygame.font.SysFont("lucidaconsole", 14) # Create a font object with size 14
    optionsFont = pygame.font.Font(None, 40) # Create a font object with size 40
    navigationText = font.render(map.returnMap(), True, (255, 255, 255)) # Render the menu textin white color
    mainWindow.blit(navigationText, (width/2 - navigationText.get_width()/2, 5)) # Draw the navigation text on the main window at the center of the window
    optionsText = "Press 'b' to return to the main menu\nPress 'w' to set a waypoint"
    optionsTextSurface = optionsFont.render(optionsText, True, (11, 224, 0)) # Render the options text in green color
    mainWindow.blit(optionsTextSurface, (width/2 - optionsTextSurface.get_width()/2, navigationText.get_height() + (height - navigationText.get_height())/2 - optionsTextSurface.get_height()/2)) # Draw the options text on the main window at the center of the space below the map.

def getUserInput(event, menu):
    # If no key is pressed, dont update the window.
    # Check if a key is pressed in the main menu
    if event.type == pygame.KEYDOWN and menu == "Main":
        if event.key == pygame.K_s: # Identify which key is pressed, what to do, and update the window accordingly.
            print("s key pressed")
        if event.key == pygame.K_n:
            print("n key pressed")
            menu = "Navigation" # Change the current menu to the navigation menu
        if event.key == pygame.K_w:
            print("w key pressed")
        if event.key == pygame.K_q:
            print("q key pressed")
            menu = "Quit" # Change the current menu to the quit menu
        return (True, menu) # If a key is pressed, return True.

    # Check if a key is pressed in the navigation menu
    if event.type == pygame.KEYDOWN and menu == "Navigation":
        if event.key == pygame.K_b: # Identify which key is pressed, what to do, and update the window accordingly.
            print("b key pressed")
            menu = "Main" # Change the current menu back to the main menu
        if event.key == pygame.K_w:
            print("w key pressed")
        return (True, menu) # If a key is pressed, return True.

    return (False, menu) # If no key is pressed, return False.

def drawGameWindow(mainWindow, width, height, menu, map):
    mainWindow.fill((0, 0, 0)) # Fill the window with black color
    # Drawing code goes in here:
    if menu == "Main": # Check if the current menu is the main menu
        drawMainMenu(mainWindow, width, height) # Call the function to draw the main menu
    if menu == "Navigation": # Check if the current menu is the navigation menu
        drawNavigationMenu(mainWindow, width, height, map) # Call the function to draw the navigation menu
    pygame.display.flip() # Update the display

if __name__ == "__main__":
    main() # Call the main function to start the game
