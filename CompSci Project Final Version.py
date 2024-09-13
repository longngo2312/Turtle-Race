import turtle as trtl 
import random
print("Welcome to the All-Star Turtle Race")
budget = 100
print("your budget is $",budget)
while True:
    trtl.hideturtle()
    bet_value = int(input("How much dollar do you wanna bet? "))
    if bet_value <= budget:
        List_of_turtles = ["square","arrow","circle","turtle","triangle","classic"]
        Racers_name = ["Bob","Stuart","Ferb","Santonio","Kevin","Tom"]
        Vehicles = [] 
        color_vehicle = ["red","blue","orange","green","yellow","white"]
        number_of_racers = 6
        x = -500
        y = 300 
        screen = trtl.Screen()
        trtl.bgcolor("light blue")
        trtl.speed(0)   
        trtl.penup()
        trtl.goto(-100,350)
        trtl.pendown()
        trtl.pencolor("red")
        trtl.write("Turtle Race",font=("Times News Roman",40))
        trtl.penup()
        trtl.goto(x,y)
        trtl.pendown()
        trtl.pencolor("red")
        for i in range(4):
            trtl.forward(1000)
            trtl.right(90)
            trtl.forward(360)
            trtl.right(90)
        trtl.setheading(-90)
        z = 10 
        for i in range(9):
            trtl.penup()
            trtl.goto(x +100,y - 20)
            trtl.pendown()
            trtl.setheading(0)
            trtl.write(z)
            trtl.setheading(-90)
            trtl.forward(320)
            x = x + 100
            z = z + 10
        trtl.penup()
        trtl.goto(500,-100)
        trtl.pendown()
        trtl.setheading(0)
        trtl.write("FINISH LINE",font=("Times New Roman",13))
        x = -450 
        y = 280
        turtle_bet = screen.textinput(title="Make your bet!", prompt="Which turtle do you think will win? Enter a colour (red, white, blue, orange, yellow, green): ")
        for i in List_of_turtles:
            Vh = trtl.Turtle(shape=i)
            Vehicles.append(Vh)
            color = color_vehicle.pop()
            Vh.fillcolor(color)
            Vh.speed(7)
            Vh.penup()
            Vh.goto(x,y)
            Vh.pendown()
            Vh.penup()
            y = y - 60 
            Vh.pendown()
        FinishLine = False
        while FinishLine != True:
            for name in Racers_name:    
                for i in range(len(Vehicles)):
                    distance = random.randint(5,15)
                    Vehicles[i].forward(distance)
                    if Vehicles[i].xcor() > 510:
                        wining_turtle = Vehicles[i].fillcolor()
                        print(name,"won the race")
                        print(wining_turtle, "turtle won the race")
                        FinishLine = True
                        trtl.penup()
                        trtl.goto(-100,-200)
                        trtl.pendown() 
                        if turtle_bet == wining_turtle:
                            trtl.write("YOU WON", font=("Times News Roman",40))
                            print("YOU WON")
                            new_budget = 2*bet_value
                            print("You won",new_budget)
                            budget = budget + new_budget
                            print("Your current budget is:","$",budget)

                        else:
                            trtl.write("YOU LOST",font=("Times New Roman",40))
                            print("YOU LOST!") 
                            budget = budget - bet_value
                            print("Your current budget is:","$",budget)
                if FinishLine == True:
                    break
    else:
        print("Please type in the value within your budget")    
    if budget <= 0:
        print("Thanks for playing")
        print("You ran out of money")
        break
    else:
        again = input("Do you want to play again? (y) or (n) ").lower()
        trtl.clear()
        if again != "y":
            print("Thanks for playing the game")
            screen.bye()
            break
screen.mainloop()