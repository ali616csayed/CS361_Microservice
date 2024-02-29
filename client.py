import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        print("1. View Recipes")
        print("2. Save Recipe")
        print("3. Remove Recipe")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            socket.send_string("VIEW")
            recipes = socket.recv_string()
            print("-------------------------------------")
            print("Recipes:")
            print(recipes)
            print("-------------------------------------")
        elif choice == "2":
            recipe = input("Enter recipe to save: ")
            socket.send_string(f"SAVE {recipe}")
            response = socket.recv_string()
            print(response)
        elif choice == "3":
            recipe = input("Enter recipe to remove: ")
            socket.send_string(f"REMOVE {recipe}")
            response = socket.recv_string()
            print(response)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
