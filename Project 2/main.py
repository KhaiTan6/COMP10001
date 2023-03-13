# Question 1
def navigate(program, start):
    """Takes a list of actions of strings as program and a tuple of location 
    (integer for coordinate and direction for string) as start. The function 
    then returns a tuple corresponding to the final location of the vehicle 
    after executing the program starting from the inital location "start"."""
    
    xcoordinate = start[0]
    ycoordinate = start[1]
    direction = start[2]
    # executes the command from the list of program one at a time.
    for command in program:
        if command == "Drive" and direction == "N":
            ycoordinate += 1
            continue
        if command == "Drive" and direction == "E":
            xcoordinate += 1
            continue
        if command == "Drive" and direction == "S":
            ycoordinate -= 1
            continue
        if command == "Drive" and direction == "W":
            xcoordinate -= 1
            continue
        if command == "TurnR" and direction == "N":
            direction = "E"
            continue
        if command == "TurnR" and direction == "E":
            direction = "S"
            continue
        if command == "TurnR" and direction == "S":
            direction = "W"
            continue
        if command == "TurnR" and direction == "W":
            direction = "N"
            continue
        if command == "TurnL" and direction == "N":
            direction = "W"
            continue
        if command == "TurnL" and direction == "E":
            direction = "N"
            continue
        if command == "TurnL" and direction == "S":
            direction = "E"
            continue
        if command == "TurnL" and direction == "W":
            direction = "S"
            continue
    return (xcoordinate, ycoordinate, direction)

# Question 2
def collision(program1, start1, program2, start2):
    """ Takes a list of actions of strings as program1 and a tuple of location 
    (integer for coordinate and direction for string) as start1 for one 
    vehicle,and the same for program2 and start2 for another vehicle. 
    The function then returns a tuple of (x,y) coordinates of the cell where
    both vehicle collide or None if they do not collide."""
    
    # checks whether both the vehicles start from the same cell
    if (start1[0], start1[1]) == (start2[0], start2[1]):
        return (start1[0], start1[1])
    
    xcoordinate1 = start1[0]
    ycoordinate1 = start1[1]
    direction1 = start1[2]
    location_list1 = []
    location_list1.append((xcoordinate1, ycoordinate1))
    
    # excecutes the command from  the list of program1 one at a time to 
    # determine the location and append the coordinates into a list.
    for command1 in program1:
        if command1 == "Drive" and direction1 == "N":
            ycoordinate1 += 1
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "Drive" and direction1 == "E":
            xcoordinate1 += 1
            location_list1.append((xcoordinate1, ycoordinate1))  
            continue
        if command1 == "Drive" and direction1 == "S":
            ycoordinate1 -= 1
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "Drive" and direction1 == "W":
            xcoordinate1 -= 1
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnR" and direction1 == "N":
            direction1 = "E"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnR" and direction1 == "E":
            direction1 = "S"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnR" and direction1 == "S":
            direction1 = "W"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnR" and direction1 == "W":
            direction1 = "N"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnL" and direction1 == "N":
            direction1 = "W"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnL" and direction1 == "E":
            direction1 = "N"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnL" and direction1 == "S":
            direction1 = "E"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        if command1 == "TurnL" and direction1 == "W":
            direction1 = "S"
            location_list1.append((xcoordinate1, ycoordinate1))
            continue
        
    xcoordinate2 = start2[0]
    ycoordinate2 = start2[1]
    direction2 = start2[2]
    location_list2 = []
    location_list2.append((xcoordinate2, ycoordinate2))
    
    # excecutes the command from  the list of program2 one at a time to 
    # determine the location.
    for command2 in program2:
        if command2 == "Drive" and direction2 == "N":
            ycoordinate2 += 1
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "Drive" and direction2 == "E":
            xcoordinate2 += 1
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "Drive" and direction2 == "S":
            ycoordinate2 -= 1
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "Drive" and direction2 == "W":
            xcoordinate2 -= 1
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnR" and direction2 == "N":
            direction2 = "E"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnR" and direction2 == "E":
            direction2 = "S"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnR" and direction2 == "S":
            direction2 = "W"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnR" and direction2 == "W":
            direction2 = "N"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnL" and direction2 == "N":
            direction2 = "W"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnL" and direction2 == "E":
            direction2 = "N"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnL" and direction2 == "S":
            direction2 = "E"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
        if command2 == "TurnL" and direction2 == "W":
            direction2 = "S"
            location_list2.append((xcoordinate2, ycoordinate2))
            continue
            
    from itertools import zip_longest
    # compares the coordinates of both vehicles after each command executed to 
    # check for collision.
    for coordinate1, coordinate2 in zip_longest(location_list1, location_list2,
                                               fillvalue=location_list2[-1]):
        if coordinate1 == coordinate2:
            return coordinate1
        
    # checks the final location of both vehicle whether they collide.
    if location_list1[-1] == location_list2[-1]:
        return location_list1[-1]
    return None

#Question 3
def tolling(program, start, tolls):
    """Takes a list of actions of strings as program, a tuple of location 
    (integer for coordinate and direction for string) as start and a dictionary
    containing a tuple of two integers corresponding to the (x,y) coordinates 
    of a cell while the values of the dictionary will be the integer toll of 
    the cell. The function then returns the total amount of tolls incurred by 
    the program for entering a cell with toll."""
    
    xcoordinate = start[0]
    ycoordinate = start[1]
    direction = start[2]
    location_list = []
    # excecutes the command from  the list of program one at a time to 
    # determine the location and append the coordinates into a list only for 
    # "drive" command.
    for command in program:
        if command == "Drive" and direction == "N":
            ycoordinate += 1
            location_list.append((xcoordinate, ycoordinate))
            continue
        if command == "Drive" and direction == "E":
            xcoordinate += 1
            location_list.append((xcoordinate, ycoordinate))  
            continue
        if command == "Drive" and direction == "S":
            ycoordinate -= 1
            location_list.append((xcoordinate, ycoordinate))
            continue
        if command == "Drive" and direction == "W":
            xcoordinate -= 1
            location_list.append((xcoordinate, ycoordinate))
            continue
        if command == "TurnR" and direction == "N":
            direction = "E"
            continue
        if command == "TurnR" and direction == "E":
            direction = "S"
            continue
        if command == "TurnR" and direction == "S":
            direction = "W"
            continue
        if command == "TurnR" and direction == "W":
            direction = "N"
            continue
        if command == "TurnL" and direction == "N":
            direction = "W"
            continue
        if command == "TurnL" and direction == "E":
            direction = "N"
            continue
        if command == "TurnL" and direction == "S":
            direction = "E"
            continue
        if command == "TurnL" and direction == "W":
            direction = "S"
            continue
    
    # sums up the total amount of tolls incurred.
    totaltoll = 0
    for location in location_list:
        if location in tolls:
            totaltoll += tolls[location]
    return totaltoll

#Question 4
# incomplete
def whiley(program, location):
    """Takes a list of actions of strings as program and a tuple of location 
    (integer for coordinate and direction for string) as start. The function 
    then returns a tuple corresponding to the final location of the vehicle 
    after executing the program starting from the inital location "start"."""
    
    xcoordinate = location[0]
    ycoordinate = location[1]
    direction = location[2]
    # executes the command from the list of program one at a time.
    for command in program:
        if command == "Drive" and direction == "N":
            ycoordinate += 1
            continue
        if command == "Drive" and direction == "E":
            xcoordinate += 1
            continue
        if command == "Drive" and direction == "S":
            ycoordinate -= 1
            continue
        if command == "Drive" and direction == "W":
            xcoordinate -= 1
            continue
        if command == "TurnR" and direction == "N":
            direction = "E"
            continue
        if command == "TurnR" and direction == "E":
            direction = "S"
            continue
        if command == "TurnR" and direction == "S":
            direction = "W"
            continue
        if command == "TurnR" and direction == "W":
            direction = "N"
            continue
        if command == "TurnL" and direction == "N":
            direction = "W"
            continue
        if command == "TurnL" and direction == "E":
            direction = "N"
            continue
        if command == "TurnL" and direction == "S":
            direction = "E"
            continue
        if command == "TurnL" and direction == "W":
            direction = "S"
            continue
        
        if command == "Whiley":
            continue
               
    return (xcoordinate, ycoordinate, direction)