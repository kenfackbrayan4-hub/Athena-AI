from brain.brain import AthenaBrain


def main():

    athena = AthenaBrain()

    print("Athena AI started.")
    print("Type exit to close.")

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            break

        answer = athena.think(user)

        print("Athena:", answer)



if __name__ == "__main__":
    main()