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

Copy code
python microservice.py
Open another terminal window and navigate to the same directory.

Run the client:

Copy code
python client.py

# Usage
Once both the server and client are running, you can use the client to interact with the microservice using the following commands:

View Recipes: Lists all recipes currently stored in the system.
Save Recipe: Adds a new recipe to the system.
Remove Recipe: Deletes a recipe from the system.
Exit: Quits the client application.
Follow the prompts on the client side to select an action and provide necessary inputs such as recipe name.

# Notes
Recipes are stored in a local text file named recipes.txt.
Each recipe should be on a separate line in the text file.

# UML Diagram

# Contributors
Ali A

# License
This project is licensed under the MIT License.


