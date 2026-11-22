from time import sleep, time
import pygame

def main():
    # Define variables specific to pygame:
    title = "Terminal Submarine" # Title of the game window
    (width, height) = (1000, 700) # Width and height of the game window
    targetFPS = 60 # Target frames per second for the game loop

    pygame.init() # Initialize the Pygame library
    pygame.display.set_caption(title) # Set the window title
    mainWindow = pygame.display.set_mode((width, height)) # Create the main window with the specified size

    running = True # Variable to control the main loop
    prevTime = time() # Store the previous time for FPS calculation



    while running: # Main Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the user closes window
                running = False # Exit the main loop
            if getUserInput(event): # Call the function to handle user input
                drawGameWindow(mainWindow, width, height) # Call the function to draw the game window if a key is pressed

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
    pass

def getUserInput(event):
    # If no key is pressed, dont update the window.
    if event.type == pygame.KEYDOWN: # Check if a key is pressed
        if event.key == pygame.K_s: # Identify which key is pressed, what to do, and update the window accordingly.
            print("s key pressed")
        if event.key == pygame.K_n:
            print("n key pressed")
        if event.key == pygame.K_w:
            print("w key pressed")

        return True # If a key is pressed, return True.
    return False # If no key is pressed, return False.

def drawGameWindow(mainWindow, width, height):
    mainWindow.fill((0, 0, 0)) # Fill the window with black color
    # Drawing code goes in here:
    drawMainMenu(mainWindow, width, height) # Call the function to draw the main menu
    pygame.display.flip() # Update the display
    pass

if __name__ == "__main__":
    main() # Call the main function to start the game
