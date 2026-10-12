class CanCalculator:
    def __init__(self):
        self.cans = 0
        self.height_can = 0
        self.needed_cans = 0
        self.height = 0

    def printResult(self):
        # Print the bottom layer input
        print(f"Bottom Layer: {self.cans}")
        # Print the amount of cans needed to finish the pyramid
        print(f"Cans needed to finish pyramid: {self.needed_cans}")
        # Check if height has been supplied
        if self.height == 0:
            # Return if not
            return 0
        else: # If it has been supplied do
            if float(self.height) < 1: # If it is below 100cm do
                self.height = f"{round(float(self.height) * 100, 3)} cm" # Round it to 3 digits (ex. 0.17304938475 * 100 → 17.304938475 round 3 digits → 17.3 add "cm" → 17.3 cm)
                print(f"Height: {self.height}") # Print the result
            else: # If it is above 100cm do
                self.height = f"{round(float(self.height), 3)} m" # Round it to 3 digits (ex. 1.7364938475 → 1.74 add "m" → 1.74 m)
                print(f"Height: {self.height}") # Print the calculated result

    def calculateCansNeeded(self):
        # Calculate the cans needed for the whole pyramid
        layers_to_add = [] # List of layers to add in total
        for i in range(self.cans): # For the amount of cans on the bottom layer
            layers_to_add.append(int(i) + 1) # Append the index (for example: 14 → 13 → 12 → 11 → ...)

        self.needed_cans += sum(layers_to_add) # Summarize all of them together (14 + 13 + 12 + 11 + ... = 105)

        if self.height_can: # If the height of one can was supplied do
            self.calculateHeight() # Fire calculateHeight
        else: # If not do
            self.printResult() # Go straight to printing the result

    def calculateHeight(self): # Definition of calculate height
        if self.height_can == 0: # If the single can height was not supplied (safety buffer) do
            self.printResult() # Go straight to printing the result
            return # Safely return out of the function

        res = self.cans * float(self.height_can) / 100 # If the above if was false, calculate the height in m using formula h = cans * single can height / 100 so for example h = 14 * 17 = 238 cm / 100 = 2.38 m

        self.height = res # Safe the value of the result that was calculated above

        self.printResult() # Go to print result

    def askInput(self): # Ask the for the user's input (entry point)
        bottom_layer = input("How many cans are in the bottom layer?\n>>> ") # Ask user how long the bottom layer is
        height_single_can = input("How tall is one singular can (cm)? (Optional)\n>>> ") # Ask user how tall one can is

        if not isinstance(int(bottom_layer), int): # If bottom layer extracted integer is not an integer do:
            print("Please supply a valid number.") # Inform user of mistake
            return 1; # Exit safely.. in this case it crashes but i dont care to fix it

        self.cans = int(bottom_layer) # Define and save the bottom layer value as integer (since input returns string, we have to cast int to it.)
        self.height_can = height_single_can # The height of a single can, we do not cast float to this value yet because we don't know if the user typed bogus crap

        self.calculateCansNeeded() # Proceed to calculateCansNeeded() function.

CanCalculator().askInput() # Entry point to start the program.
