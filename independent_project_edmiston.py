def practice_plan(position): #defining the function
    team_practice = ("4. Team batting practice (1 hour)\n5. Situational work (1 hour)\n6. Bunt and 1st and 3rd Defense (30 minutes)")  #variable to assign the team schedule and able to use it in all individual schedules

    if position == "Infielder":   #selection statement if infielder is chosen it will print out outfielders schedule
        print(f"\nPractice plan for {position}:")
        print("1. Ground balls drill (30 minutes)")
        print("2. Throwing across infield (20 minutes)")
        print("3. Base running practice (30 minutes)")
        print(team_practice)

    elif position == "Outfielder":  #selection statement if outfielder is chosen it will print out outfielders schedule
        print(f"\nPractice plan for {position}:") #says what position is receiving this plan
        print("1. Fly balls drill (30 minutes)") #individual drills for each one
        print("2. Quick reactions drill/Ladder drill (20 minutes)")
        print("3. Base running practice (30 minutes)")
        print(team_practice) #printing variable of the entire team practice for each position

    elif position == "Pitcher": #selection statement if pitcher is chosen it will print out outfielders schedule
        print(f"\nPractice plan for {position}:") 
        print("1. Pitching mechanics review (30 minutes)")
        print("2. Bullpen session (30 minutes)")
        print("3. Pitcher fielding practice (20 minutes)")
        print(team_practice) #printing variable of the entire team practice for each position

    elif position == "Catcher":   #selection statement if catcher is chosen it will print out outfielders schedule
        print(f"\nPractice plan for {position}:")
        print("1. Receiving drills (30 minutes)")
        print("2. Blocking drills (20 minutes)")
        print("3. Throwing out runners (30 minutes)")
        print(team_practice) #printing variable of the entire team practice for each position

    else:  #if position isnt selected it will let them restart
        print("Invalid position selected.")


name = input("What is your name? ") #input to get the users name to welcome them to the practice plan
print(f"Hello, {name}! Let's create your practice plan.") 

position_type = ["Infielder", "Outfielder", "Pitcher", "Catcher"] # list of the positions

while True:
        pick_position = input("\nPick your position\nType '0' for Infielder\nType '1' for Outfielder\nType '2' for Pitcher\nType '3' for Catcher\nType here: ")
        #input for the user to choose the position
        if pick_position in ['0', '1', '2', '3']:
            position = position_type[int(pick_position)]
            practice_plan(position)  #calls the function with parameter
            break #breaks loop
        else:
            print("Invalid choice. Please select a position number.")  #Resets the loop if a position isnt picked

