from module import Movement

def main():
    print("""This is Printed Movement (PM)
    v.0.1
    by Ignacy Bojarski
    (this project is mostly for educational purposes)
    
    Use WSAD to control your +.
    To quit use Q key""")

    m = Movement()

    m.createPlayer()
    while True:
        playerInput = input()
        playerInput.lower()
        if playerInput == "w":
            m.moveUp()
        elif playerInput == "s":
            m.moveDown()
        elif playerInput == "a":
            m.moveLeft()
        elif playerInput == "d":
            m.moveRight()
        elif playerInput == "q":
            print("Exiting program...")
            break
        else:
            print("Invalid key")


if __name__ == "__main__":
    main()