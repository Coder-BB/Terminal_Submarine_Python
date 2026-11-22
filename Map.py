class Map:
    def __init__(self, name):
        self.name = name
        self.maps = []
        self.load_map() # Call the load_map method to load the map data from the file


    def load_map(self):
        with open("Maps.txt", "r") as file:
            self.maps = file.read().split("***") # The delimiter "***" is used to separate different maps in the file. This will allow for multiple maps to be stored in a single file.
            self.mapRows = [None] * len(self.maps) # Initialize the mapRows list with the same length as the maps
            self.mapRows = self.maps[0].splitlines() # Grabs the strings from the first map. This will need to be updated to allow for multiple maps in the future.

    def getMapElement(self, row, col):
        return self.mapRows[row][col] # Return the character at the specified row and column in the map

    def printMap(self):
        headder = "     A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z "
        print(headder) # Print the column headers for the map at the top of the map for reference
        i = 0 # Initialize a counter for the row numbers
        for row in self.mapRows:
            print(f"{i:02d} |", end="") # Print the row number with leading zeros and a separator
            j = 0 # Initialize a counter for the column numbers
            for col in row:
                if j == len(row) - 1: # Check if the current column is the last column in the row
                    print(" " + col, end="") # Print the last character in the row
                    print(" | " + f"{i:02d}", end="") # Print the row number again at the end of the row for reference
                else:
                    print(" " + col + " |", end="") # Print the character in the row with a separator and no newline
                j += 1 # Increment the column counter
            print() # Print a newline after each row to format the map correctly
            i += 1 # Increment the row counter
        print(headder) # Print the column headers again at the bottom of the map for reference

    def returnMap(self):
        headder = "     A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z "
        mapString = headder + "\n" # Store the column headers for the map at the top of the map for reference
        i = 0 # Initialize a counter for the row numbers
        for row in self.mapRows:
            mapString += f"{i:02d} |" # Store the row number with leading zeros and a separator
            j = 0 # Initialize a counter for the column numbers
            for col in row:
                if j == len(row) - 1: # Check if the current column is the last column in the row
                    mapString += " " + col # Store the last character in the row
                    mapString += " | " + f"{i:02d}" # Store the row number again at the end of the row for reference
                else:
                    mapString += " " + col + " |" # Store the character in the row with a separator and no newline
                j += 1 # Increment the column counter
            mapString += "\n" # Store a newline after each row to format the map correctly
            i += 1 # Increment the row counter
        mapString += headder + "\n" # Store the column headers again at the bottom of the map for reference
        return mapString # Return the complete map string

# testMap = Map("NewMap") # Create a Map object with the specified map file
