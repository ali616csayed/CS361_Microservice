# CS361_Microservice
# Recipe Management Microservice
This microservice allows clients to interact with a recipe management system over ZeroMQ. Clients can view, save, and remove recipes stored in a local text file through simple commands.

# Prerequisites
Python 3.x installed on your system.
ZeroMQ library (pyzmq) installed. You can install it via pip:
Copy code
pip install pyzmq

# Getting Started
Clone this repository to your local machine or download the files directly.

Open a terminal window and navigate to the directory containing the microservice files.

Run the server:

Copy code python microservice.py

Open another terminal window and navigate to the same directory.

Run the client:

Copy code
python client.py

# Usage
Once both the server and client are running, you can use the client to interact with the microservice using the following commands:

View Recipes: Lists all recipes currently stored in the system.
socket.send_string("VIEW") to the microservice will return all the recipes stored.


Save Recipe: Adds a new recipe to the system.
socket.send_string(f"SAVE {recipe}") to the microservice will save the new recipe.

Remove Recipe: Deletes a recipe from the system.
socket.send_string(f"REMOVE {recipe}") to the microservice will remove the recipe.

Exit: Quits the client application.

Follow the prompts on the client side to select an action and provide necessary inputs such as recipe name.

# Notes
Recipes are stored in a local text file named recipes.txt.
Each recipe should be on a separate line in the text file.

# UML Diagram
![UML Diagram](https://github.com/ali616csayed/CS361_Microservice/assets/91701542/132e145b-b411-4c50-89a0-62082b0d5d58)


# Contributors
Ali A

# License
This project is licensed under the MIT License.


