import board
from time import sleep
import random
import pwmio
import servo
from analogio import AnalogIn


turn = 0 # whose turn it is, 0 is player, 1 is AI
round = 1 # which round of the game it is
end = 0 # if the game has ended
plan = 0 # where the AI is planning to move
extend = 0 # how far out the arm is
twist = 0 # angle of turn of the arm
offset = 3
armProg = 96
colorBase = 0
scanN = 1

pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.A5, duty_cycle=2 ** 15, frequency=50)
uppy = pwmio.PWMOut(board.D7, duty_cycle=0, frequency=50, variable_frequency=True) # Sets up a PWM output for the magnet servo as there are no more A timers
#uppy = pwmio.PWMOut(board.A0, duty_cycle=2 ** 15, frequency=50, variable_frequency=True)
color = AnalogIn(board.A2)


theBoard = {'7': ' ' , '8': ' ' , '9': ' ' , # The visual board, keeps track of placed X's and O's
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

distBoard = {'7': 170 , '8': 157 , '9': 170 , # Holds all of the distance data to the board
            '4': 110 , '5': 96 , '6': 110 ,
            '1': 58 , '2': 30 , '3': 58 , '0': 112}
angleBoard = {'7': 110 , '8': 90 , '9': 70 , # Holds all of the angle data to the board
            '4':  122, '5': 90 , '6': 61 ,
            '1': 150 , '2': 90 , '3': 42 , '0': 170}
arm = servo.Servo(pwm) # The extendy arm servo
spinny = servo.Servo(pwm2) # The twisty servo
#                                                  ARM SERVO SHOULD HAVE ONE TOOTH SHOWING IN THE BACK WHEN AT '5' POSITION

def printBoard(board):
    print("")
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def checkWin():
            global end
            if theBoard['7'] == theBoard['8'] == theBoard['9'] and theBoard['9'] != ' ': # across the top
                end += 1      
                print("Across Top")     
            
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] and theBoard['6'] != ' ': # across the middle
                end += 1
                print("Across Mid")       
            
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] and theBoard['3'] != ' ': # across the bottom
                end += 1
                print("Across Bottom")
                
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] and theBoard['7'] != ' ': # down the left side
                end += 1
                print("Down Left")
                
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] and theBoard['8'] != ' ': # down the middle
                end += 1
                print("Down Mid")
                
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] and theBoard['9'] != ' ': # down the right side
                end += 1
                print("Down Right")
                 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] and theBoard['3'] != ' ': # diagonal
                end += 1
                print("Diagonal 7-3")
                
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] and theBoard['9'] != ' ': # diagonal
                end += 1
                print("Diagonal 9-1")

def grab(direction): # Code to pick up and drop the magnet
    if direction == 0: # 0 Picks Up
        uppy.duty_cycle = (3800) # This motor goes from 0 to 65535, but <4800 is clockwise, >4800 is counter clockwise
        sleep(1)
        uppy.duty_cycle = (0)
        sleep(.25)
        uppy.duty_cycle = (5800)
        sleep(1)
    elif direction == 1: # 1 Drops
        uppy.duty_cycle = (5800)
        sleep(.35)
        uppy.duty_cycle = (3800)
        sleep(.35)
    uppy.duty_cycle = (0)

def place(spot): # Code to move the arm to a specified place on the board
    armProg = arm.angle
    sleep(.25)
    while arm.angle != distBoard['0']: # code to move arm smoothly
        if abs(armProg - distBoard['0']) < 2:
            arm.angle = (distBoard['0'])
            break
        elif armProg < distBoard['0']:
            armProg += 1
        elif armProg > distBoard['0']:
            armProg -= 1
        arm.angle = (armProg) 
        sleep(.0001)
    armProg = spinny.angle
    spinny.angle = (angleBoard['0'] + offset)
    while spinny.angle != angleBoard['0'] + offset: # code to move arm turn smoothly
        if abs(armProg - angleBoard['0'] + offset) < 2:
            spinny.angle = (angleBoard['0'] + offset)
            break
        elif armProg < angleBoard['0'] + offset:
            armProg += 1
        elif armProg > angleBoard['0'] + offset:
            armProg -= 1
        spinny.angle = (armProg) 
        sleep(.0001)
    sleep(1.25)
    #   PICKUP
    grab(0)
    print("Pickup")

    
    theBoard[str(spot)] = "O"
    armProg = spinny.angle
    while spinny.angle != angleBoard[str(spot)] + offset: # code to move arm turn smoothly
        if abs(armProg - (angleBoard[str(spot)] + offset)) < 2:
            spinny.angle = (angleBoard[str(spot)] + offset)
            break
        elif armProg < angleBoard[str(spot)] + offset:
            armProg += 1
        elif armProg > angleBoard[str(spot)] + offset:
            armProg -= 1
        spinny.angle = (armProg) 
        print(str(angleBoard[str(spot)]) + "   " + str(armProg))
        sleep(.0001)
    print("moved")
    sleep(.25)
    armProg = arm.angle
    while arm.angle != distBoard[str(spot)]:#             Extend
        if abs(armProg - distBoard[str(spot)]) < 2:
            arm.angle = (distBoard[str(spot)] * 0.86925636203 + 5)
            break
        elif armProg < distBoard[str(spot)]:
            armProg += 1
        elif armProg > distBoard[str(spot)]:
            armProg -= 1
        arm.angle = (armProg * 0.86925636203 + 5) 
        sleep(.0001)

    #   DROP
    grab(1)
    print("Drop")

    armProg = arm.angle
    sleep(.25)
    while arm.angle != distBoard['0']: # code to move arm smoothly
        if abs(armProg - distBoard['0']) < 2:
            arm.angle = (distBoard['0'])
            break
        elif armProg < distBoard['0']:
            armProg += 1
        elif armProg > distBoard['0']:
            armProg -= 1
        arm.angle = (armProg) 
        sleep(.0001)
    armProg = spinny.angle
    spinny.angle = (angleBoard['0'] + offset)
    while spinny.angle != angleBoard['0'] + offset: # code to move arm turn smoothly
        if abs(armProg - angleBoard['0'] + offset) < 2:
            spinny.angle = (angleBoard['0'] + offset)
            break
        elif armProg < angleBoard['0'] + offset:
            armProg += 1
        elif armProg > angleBoard['0'] + offset:
            armProg -= 1
        spinny.angle = (armProg) 
        sleep(.0001)

def scan():
    scanN = 1
    while scanN < 10:
        if theBoard[str(scanN)] != 'X' and theBoard[str(scanN)] != 'O':
            arm.angle = distBoard[str(scanN)]
            sleep(.25)
            spinny.angle = angleBoard[str(scanN)]
            sleep(.4)
            if (color.value - colorBase) > 3000:
                theBoard[str(scanN)] = 'X'
                break
            print(scanN)


        if scanN < 3:
            scanN += 1
        elif scanN == 3:
            scanN = 6
        elif scanN > 4 and scanN < 7:
            scanN -= 1
        elif scanN == 4:
            scanN = 7
        elif scanN > 6:
            scanN += 1


arm.angle = distBoard['5']
spinny.angle = 90 + offset
sleep(.3)
for i in range(10):
    colorBase += color.value
    sleep(.05)
colorBase /= 10
print(colorBase)
scan()
print("Move with the numpad.")
sleep(1)

uppy.duty_cycle = (0)


for i in range(5): # The main tic tac toe loop
    plan = 0
    print("Round " + str(round) + ", Your Turn")
    turn = 0
    printBoard(theBoard)
    print("--------------------------------")

# Start Removal
    print("Where Would you like to move?")
    move = input("")

    try:
        if move == "]":
            uppy.duty_cycle = (5800)
            sleep(.125)
            uppy.duty_cycle = (0)
            i-=1
            continue
        elif move == "[":
            uppy.duty_cycle = (3800)
            sleep(.125)
            uppy.duty_cycle = (0)
            i -=1
            continue
        elif int(move) < 10 and  int(move) > 0 and theBoard[move] == " ":
            theBoard[str(move)] = "X"
            round += 1
        else:
            print("Invalid move, try again")
            i -= 1
            continue
    except:
        print("Invalid move, try again")
        continue
# End Removal

    checkWin()
    if end == 1:
        i = 6
        break
    elif round == 10:
        turn = 2
        break

    printBoard(theBoard)
    sleep(1)
    turn = 1
    if True:
        if theBoard['7'] == theBoard['8'] == "O" and theBoard['9'] == ' ': # across the top
            place(9)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['8'] == "O" and theBoard['7'] == ' ': # across the top
            place(7)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['9'] == "O" and theBoard['8'] == ' ': # across the top
            place(8)
            round += 1
            turn += 1
        elif theBoard['4'] == theBoard['5'] == "O" and theBoard['6'] == ' ': # across mid
            place(6)
            round += 1
            turn += 1
        elif theBoard['6'] == theBoard['5'] == "O" and theBoard['4'] == ' ': # across mid
            place(4)
            round += 1
            turn += 1
        elif theBoard['4'] == theBoard['6'] == "O" and theBoard['5'] == ' ': # across mid
            place(5)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['2'] == "O" and theBoard['3'] == ' ': # across bottom
            place(3)
            round += 1
            turn += 1
        elif theBoard['3'] == theBoard['2'] == "O" and theBoard['1'] == ' ': # across bottom
            place(1)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['3'] == "O" and theBoard['2'] == ' ': # across bottom
            place(2)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['4'] == "O" and theBoard['1'] == ' ': # down left
            place(1)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['4'] == "O" and theBoard['7'] == ' ': # down left
            place(7)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['1'] == "O" and theBoard['4'] == ' ': # down left
            place(4)
            round += 1
            turn += 1
        elif theBoard['8'] == theBoard['5'] == "O" and theBoard['2'] == ' ': # down mid
            place(2)
            round += 1
            turn += 1
        elif theBoard['2'] == theBoard['5'] == "O" and theBoard['8'] == ' ': # down mid
            place(8)
            round += 1
            turn += 1
        elif theBoard['8'] == theBoard['2'] == "O" and theBoard['5'] == ' ': # down mid
            place(5)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['6'] == "O" and theBoard['3'] == ' ': # down right
            place(3)
            round += 1
            turn += 1
        elif theBoard['3'] == theBoard['6'] == "O" and theBoard['9'] == ' ': # down right
            place(9)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['3'] == "O" and theBoard['6'] == ' ': # down right
            place(6)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['5'] == "O" and theBoard['1'] == ' ': # right diagonal
            place(1)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['1'] == "O" and theBoard['5'] == ' ': # right diagonal
            place(5)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['5'] == "O" and theBoard['9'] == ' ': # right diagonal
            place(9)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['5'] == "O" and theBoard['3'] == ' ': # left diagonal
            place(3)
            round += 1
            turn += 1
        elif theBoard['3'] == theBoard['5'] == "O" and theBoard['7'] == ' ': # left diagonal
            place(7)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['3'] == "O" and theBoard['5'] == ' ': # left diagonal
            place(5)
            round += 1
            turn += 1

        elif theBoard['7'] == theBoard['8'] == "X" and theBoard['9'] == ' ': # across the top
            place(9)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['8'] == "X" and theBoard['7'] == ' ': # across the top
            place(7)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['9'] == "X" and theBoard['8'] == ' ': # across the top
            place(8)
            round += 1
            turn += 1
        elif theBoard['4'] == theBoard['5'] == "X" and theBoard['6'] == ' ': # across mid
            place(6)
            round += 1
            turn += 1
        elif theBoard['6'] == theBoard['5'] == "X" and theBoard['4'] == ' ': # across mid
            place(4)
            round += 1
            turn += 1
        elif theBoard['4'] == theBoard['6'] == "X" and theBoard['5'] == ' ': # across mid
            place(5)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['2'] == "X" and theBoard['3'] == ' ': # across bottom
            place(3)
            round += 1
            turn += 1
        elif theBoard['3'] == theBoard['2'] == "X" and theBoard['1'] == ' ': # across bottom
            place(1)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['3'] == "X" and theBoard['2'] == ' ': # across bottom
            place(2)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['4'] == "X" and theBoard['1'] == ' ': # down left
            place(1)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['4'] == "X" and theBoard['7'] == ' ': # down left
            place(7)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['1'] == "X" and theBoard['4'] == ' ': # down left
            place(4)
            round += 1
            turn += 1
        elif theBoard['8'] == theBoard['5'] == "X" and theBoard['2'] == ' ': # down mid
            place(2)
            round += 1
            turn += 1
        elif theBoard['2'] == theBoard['5'] == "X" and theBoard['8'] == ' ': # down mid
            place(8)
            round += 1
            turn += 1
        elif theBoard['8'] == theBoard['2'] == "X" and theBoard['5'] == ' ': # down mid
            place(5)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['6'] == "X" and theBoard['3'] == ' ': # down right
            place(3)
            round += 1
            turn += 1
        elif theBoard['3'] == theBoard['6'] == "X" and theBoard['9'] == ' ': # down right
            place(9)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['3'] == "X" and theBoard['6'] == ' ': # down right
            place(6)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['5'] == "X" and theBoard['1'] == ' ': # right diagonal
            place(1)
            round += 1
            turn += 1
        elif theBoard['9'] == theBoard['1'] == "X" and theBoard['5'] == ' ': # right diagonal
            place(5)
            round += 1
            turn += 1
        elif theBoard['1'] == theBoard['5'] == "X" and theBoard['9'] == ' ': # right diagonal
            place(9)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['5'] == "X" and theBoard['3'] == ' ': # left diagonal
            place(3)
            round += 1
            turn += 1
        elif theBoard['3'] == theBoard['5'] == "X" and theBoard['7'] == ' ': # left diagonal
            place(7)
            round += 1
            turn += 1
        elif theBoard['7'] == theBoard['3'] == "X" and theBoard['5'] == ' ': # left diagonal
            place(5)
            round += 1
            turn += 1

        else:
            if round == 2 and theBoard['5'] == ' ':
                if random.randint(1,2) == 1:
                    place(5)
                else:
                    place(random.randint(1,9))
                round += 1
            else:
                while plan != 10:
                    plan = random.randint(1,9)
                    if theBoard[str(plan)] == ' ':
                        place(plan)
                        plan = 10
                        round += 1

    checkWin()
    if end == 1:
        i = 6
        break

printBoard(theBoard)
print("\nGame Over.\n")   
if turn == 0:             
    print(" ****  You  win. ****")
elif turn == 2:
    print(" ****  AI  wins. ****")
    
else:
    print("0 wuns")