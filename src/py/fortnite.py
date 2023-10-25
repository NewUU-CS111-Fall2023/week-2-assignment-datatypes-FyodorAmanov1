class play:
    def Dead_Alive():   
        characters = int(input("How many characters are in the game ? "))

        list_x = []
        list_y = []
        total_dist = 0

        for i in range(characters):
            x = int(input("So what is x of character " + str(i+1) + " "))
            y = int(input("So what is y of character " + str(i+1) + " "))
            list_x.append(x)
            list_y.append(y)

        x_dec = int(input("Okay what is your x coordinate "))
        y_dec = int(input("Okay what is your y coordinate "))

        for i in range(characters):
            dist = ((list_x[i] - x_dec)**2 + (list_y[i] - y_dec)**2)**(1/2)
            total_dist += dist

        if (total_dist < characters):
            print("Died")
        else:
            print("It's ok, you are Alive")