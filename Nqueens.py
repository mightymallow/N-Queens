

import time
import os
import math


def make_queen_sat(N):
    tempStringArray = []
    totalClauses = 0
    totalArguments = N*N
    file1 = open("Queen_SAT.txt","w+")
    

    # Creating row constraints in string array
    for i in range(0,N):
        tempStringAll = ""
        multiplier = i*N
        for j in range(0,N):
            tempStringAll += str(multiplier+j+1) + " "
            for k in range(j+1,N):
                tempString = str(-(multiplier+j+1)) + " " + str(-(multiplier+k+1)) + " " + str(0) + "\n"
                tempStringArray.append(tempString)
                totalClauses += 1
        tempStringArray.append(tempStringAll)
        tempStringArray += str(0) + "\n"
        totalClauses += 1
    #print(tempStringArray)

    # Creating column constraints in string array
    for i in range(0,N):
        tempStringAll = ""
        for j in range(0,N):
            multiplier = j*N
            tempStringAll += str(multiplier+i+1) + " "
            for k in range(j+1,N):
                tempMultiplier = k*N
                tempString = str(-(multiplier+i+1)) + " " + str(-(tempMultiplier+i+1)) + " " + str(0) + "\n"
                tempStringArray.append(tempString)
                totalClauses += 1
        tempStringArray.append(tempStringAll)
        tempStringArray += str(0) + "\n"
        totalClauses += 1
    #print(tempStringArray)

    # Creating diagonal constraints from top left to bottom right in string array
    for i in range(0,N-1):
        iMultiplier = i*N
        for j in range(0,N-1):
            tempCounter = 0
            for k in range(j+1,N):
                tempCounter += 1
                tempMultiplier = tempCounter*(N+1)
                checkNumber = iMultiplier + tempMultiplier + j + 1
                if checkNumber <= totalArguments:
                    tempString = str(-(iMultiplier+j+1)) + " " + str(-(iMultiplier+tempMultiplier+j+1)) + " " + str(0) + "\n"
                    tempStringArray.append(tempString)
                    totalClauses += 1
                else:
                    continue

    # Creating diagonal constraints from top right to bottom left in string array
    for i in range(0,N-1):
        iMultiplier = i*N
        for j in range(1,N):
            tempCounter = 0
            for k in range(0,j):
                tempCounter += 1
                tempMultiplier = tempCounter*(N-1)
                checkNumber = iMultiplier + tempMultiplier + j + 1
                if checkNumber <= totalArguments:
                    tempString = str(-(iMultiplier+j+1)) + " " + str(-(iMultiplier+tempMultiplier+j+1)) + " " + str(0) + "\n"
                    tempStringArray.append(tempString)
                    totalClauses += 1
                else:
                    continue

    initialization = "p" + " " + "cnf" + " " + str(totalArguments) + " " + str(totalClauses) + "\n"
    file1.write(initialization)
    file1.writelines(tempStringArray)



def analyze_output(out):
    file2 = open(out)
    # https://stackoverflow.com/questions/15718068/search-file-and-find-exact-match-and-print-line
    for line in file2:
        if line.rstrip() == "UNSATISFIABLE":
            sol = "No solution"
            return sol
        if line.rstrip() == "SATISFIABLE":
            continue
        sol = line.rstrip()
    file2.close
    # change string to int and remove trailing 0 from list
    sol = sol.split()
    sol.pop()
    #print(sol)
    return sol



def draw_queen_sat_sol(sol):
    length = math.sqrt(len(sol))
    counter = 0
    if sol == "No solution":
        print("No solution")
    else:
        for x in sol:
            counter += 1
            if int(x) <= 0:
                print(".", end = " ")
            else:
                print("Q", end = " ")
            if counter == length:
                print()
                counter = 0
    print()



def main_program():
    N = 2
    elapsed_time = 0
    NArray = []
    timeArray = []
    while elapsed_time <= 10:
        sol = make_queen_sat(N)
        start_time = time.time()
        os.system('minisat Queen_SAT.txt SAT')
        elapsed_time = time.time() - start_time
        NArray.append(str(N) + "\n")
        timeArray.append(str(elapsed_time) + "\n")
        if N <= 40:
            sol = analyze_output("SAT")
            draw_queen_sat_sol(sol)
        else:
            print()
            print("Too big: N must be less than 40")
            print()
        N += 1
    print("The maximum N reached was " + str(N))
    print()
    file3 = open("a3_q1_N.txt", "w+")
    file3.writelines(NArray)
    file4 = open("a3_q1_times.txt", "w+")
    file4.writelines(timeArray)


main_program()

