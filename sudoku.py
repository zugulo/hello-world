import csv
import numpy as np

sudoku = [[0] * 9 for _ in range(9)]
reference_set = {0,1,2,3,4,5,6,7,8,9}
count_number = 0
scount_number = 2

def main():
    opensudoku()
    count_number = count_sudoku()
    for i in range (100):
        solve()
        rowsolve(0)
        rowsolve(3)
        rowsolve(6)
        #print(sudoku)
        count_number = count_sudoku()
    for i in range(9):
        print(sudoku[i])
    print(count_number)



def opensudoku():    
    with open(r'C:\Users\rasun\projects\sudoku\test2.csv') as file:
        reader = csv.reader(file)  
        count = 0 
        for row in reader:
            for i in range(9):
                 sudoku[count][i] = int(row[i])
            count += 1

def count_sudoku():
    count_zero = 0;
    for i in range (9):
        for j in range(9):
            if(sudoku[i][j] == 0):
                count_zero +=1
    return 81 - count_zero

def solve ():
    global count_number
    for i in range (9):
        for j in range(9):
            if(sudoku[i][j] != 0):
                continue
            numbers_nearby = {0}
            numbers_nearby.clear()
            for k in range (9):
                numbers_nearby.add(sudoku[i][k])
                numbers_nearby.add(sudoku[k][j])
            numbers_nearby.update(addcube(i,j))
            numbers_nearby.add(sudoku[i][j])
            if(len(numbers_nearby) == 9):
                x = reference_set.difference(numbers_nearby)
                print(x, i ,j)
                sudoku[i][j] = x.pop()
                count_number += 1
                
 # if a number is in 2 rows/columns in a 1/3rd of the whole sudoku 
 #  then check if only a certain space is valid by checking if the other 2 are blocked
            
def rowsolve (a):
    row1 = {0}
    row1.clear()
    row2 = {0}
    row2.clear()
    row3 = {0}
    row3.clear()
    for k in range (9):
        row1.add(sudoku[a][k])
        row2.add(sudoku[a+1][k])
        row3.add(sudoku[a+2][k])
    intersection1 = row1 & row2 # 
    intersection2 = row1 & row3
    intersection3 = row3 & row2
    intersection1,intersection2,intersection3.remove(0)
    for number in intersection1:
        if()

def check_column(column, value):
    for i in range(9):
        if(sudoku[i][column] == value):
            return True
    
    return False

def check

def check_row(row, value):
    for i in range(9):
        if(sudoku[row][i] == value):
            return True
    
    return False

def addcube(i, j):
    cube = set()
    if i < 3:
        if j < 3:
            for x in range(3):
                for y in range(3):
                    cube.add(sudoku[x][y])
        elif j < 6:
            for x in range(3):
                for y in range(3, 6):
                    cube.add(sudoku[x][y])
        else:
            for x in range(3):
                for y in range(6, 9):
                    cube.add(sudoku[x][y])
    elif i < 6:
        if j < 3:
            for x in range(3, 6):
                for y in range(3):
                    cube.add(sudoku[x][y])
        elif j < 6:
            for x in range(3, 6):
                for y in range(3, 6):
                    cube.add(sudoku[x][y])
        else:
            for x in range(3, 6):
                for y in range(6, 9):
                    cube.add(sudoku[x][y])
    else:
        if j < 3:
            for x in range(6, 9):
                for y in range(3):
                    cube.add(sudoku[x][y])
        elif j < 6:
            for x in range(6, 9):
                for y in range(3, 6):
                    cube.add(sudoku[x][y])
        else:
            for x in range(6, 9):
                for y in range(6, 9):
                    cube.add(sudoku[x][y])
    return cube

main()