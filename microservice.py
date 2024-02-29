import zmq
import os

# Define the path to the recipe file
RECIPE_FILE = "recipes.txt"


# Function to load recipes from file
def load_recipes():
    if os.path.exists(RECIPE_FILE):
        with open(RECIPE_FILE, "r") as file:
            return [line.strip() for line in file]
    else:
        return []


# Function to save recipes to file
def save_recipes(recipes):
    with open(RECIPE_FILE, "w") as file:
        for recipe in recipes:
            file.write(recipe + "\n")


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    recipes = load_recipes()

    while True:
        message = socket.recv_string()

        # This is the logical block that handles the
        # different types of messages that can be sent by the client

        # VIEW command prints all the recipes in the text file in the
        # command line of the client
        if message.startswith("VIEW"):
            socket.send_string("\n".join(recipes))

        # SAVE command writes the recipe input in the client
        # command line input
        elif message.startswith("SAVE"):
            recipe = message.split(" ", 1)[1]
            recipes.append(recipe)
            save_recipes(recipes)
            socket.send_string("Recipe saved successfully.")
        # REMOVE command removes the input recipe from the
        # loaded recipes from the text file, then overwrites
        # the file with the remaining recipes
        elif message.startswith("REMOVE"):
            recipe = message.split(" ", 1)[1]
            if recipe in recipes:
                recipes.remove(recipe)
                save_recipes(recipes)
                socket.send_string("Recipe removed successfully.")
            else:
                socket.send_string("Recipe not found.")
        # Error handling for any invalid commands
        else:
            socket.send_string("Invalid command.")


if __name__ == "__main__":
    main()
