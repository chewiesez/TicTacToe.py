# -*- coding: utf-8 -*-
"""
Spyder Editor

Dan Foster Python Boot Camp Milestone Project 1 - Tic Tac Toe Game
"""




def game_over():
    z = input('GAME OVER, PRESS ENTER TO RESTART:')
    if z != None:
        tictactoe()

def tictactoe():
    top = '          1    2    3 '
    row_a = [['A'],[' ',' ',' ']]
    row_b = [['B'],[' ',' ',' ']]
    row_c = [['C'],[' ',' ',' ']]
    print(top)
    print(row_a)
    print(row_b)
    print(row_c)
    list_1 = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    list_2 = []
    a = row_a
    b = row_b
    c = row_c
    go = 1



    def test():
        condition_1 = '\n\nPlayer 1 Wins!\n\n'
        condition_2 = '\n\nPlayer 2 Wins!\n\n'


        if a[1][0]==b[1][0] and c[1][0] == b[1][0]:#vertical

            if a[1][0] == 'X':
                print(condition_1)
                game_over()
                go = 2
            elif a[1][0] == 'O':
                print(condition_2)
                game_over()
                go = 2
            else:
                pass

        elif a[1][1]==b[1][1] and c[1][1] == b[1][1]:#vertical

            if a[1][1] == 'X':
                print(condition_1)
                game_over()
                go = 2
            elif a[1][1] == 'O':
                print(condition_2)
                game_over()
                go = 2
            else:
                pass

        elif a[1][2]==b[1][2] and c[1][2] == b[1][2]:#vertical

            if a[1][2] == 'X':
                print(condition_1)
                game_over()
                go = 2
            elif a[1][2] == 'O':
                print(condition_2)
                game_over()
                go = 2
            else:
                pass

        elif a[1][0] == b[1][1] and b[1][1]==c[1][2]:#diagonal1
            if a[1][0] == 'X':
                print(condition_1)
                game_over()
                go = 2
            elif a[1][0] == 'O':
                print(condition_2)
                game_over()
                go = 2
            else:
                pass

        elif a[1][2] == b[1][1] and b[1][1]==c[1][0]:#diagonal2
            if c[1][0] == 'X':
                print(condition_1)
                game_over()
                go = 2
            elif c[1][0] == 'O':
                print(condition_2)
                game_over()
                go = 2
            else:
                pass

        elif a[1] == ['X','X','X']:#horizontal
            print(condition_1)
            game_over()
            go = 2
        elif a[1] == ['O','O','O']:#horizontal
            print(condition_2)
            game_over()
            go = 2

        elif b[1] == ['X','X','X']:#horizontal
            print(condition_1)
            game_over()
            go = 2

        elif b[1] == ['O','O','O']:#horizontal
            print(condition_2)
            game_over()
            go = 2

        elif c[1] == ['X','X','X']:#horizontal
            print(condition_1)
            game_over()
            go = 2

        elif c[1] == ['O','O','O']:#horizontal
            print(condition_2)
            game_over()
            go = 2

        elif len(list_1) == len(list_2):
            game_over()
            go = 2
        else:
            pass
    while True:

        if go < 2:
            x = input('Player 1, choose the coordinates to place your X: ')
            move = x.upper()
        else:
            break
        if  move not in list_1:
            while move not in list_1:
                x = input('Player 1, choose a valid coordinate to place your X: ')
                move = x.upper()
                if  move in list_2:
                    while move in list_2:
                        x = input('Player 1, choose a valid coordinate to place your X: ')
                        move = x.upper()
        if  move in list_2:
            while move in list_2:
                x = input('Player 1, choose a valid coordinate to place your X: ')
                move = x.upper()
                if  move not in list_1:
                    while move not in list_1:
                        x = input('Player 1, choose a valid coordinate to place your X: ')
                        move = x.upper()
        if move == 'A1':
            a[1][0] = 'X'
            list_2.append('A1')
        elif move == 'B1':
            b[1][0] = 'X'
            list_2.append('B1')
        elif move == 'C1':
            c[1][0] = 'X'
            list_2.append('C1')
        elif move == 'A2':
            a[1][1] = 'X'
            list_2.append('A2')
        elif move == 'B2':
            b[1][1] = 'X'
            list_2.append('B2')
        elif move == 'C2':
            c[1][1] = 'X'
            list_2.append('C2')
        elif move == 'A3':
             a[1][2] = 'X'
             list_2.append('A3')
        elif move == 'B3':
             b[1][2] = 'X'
             list_2.append('B3')
        elif move == 'C3':
             c[1][2] = 'X'
             list_2.append('C3')
        print('\n\n')
        print(top)
        print(a)
        print(b)
        print(c)
        print('\n\n')
        test()

        if go < 2:
            y = input('Player 2, choose the coordinates to place your O: ')
            move2 = y.upper()
        else:
            break
        if  move2 not in list_1:
            while move2 not in list_1:
                x = input('Player 2, choose the coordinates to place your O: ')
                move2 = x.upper()
                if  move2 in list_2:
                    while move2 in list_2:
                        x = input('Player 2, choose the coordinates to place your O: ')
                        move2 = x.upper()
        if  move2 in list_2:
            while move2 in list_2:
                x = input('Player 2, choose the coordinates to place your O: ')
                move2 = x.upper()
                if  move2 not in list_1:
                    while move2 not in list_1:
                        x = input('Player 2, choose the coordinates to place your O: ')
                        move2 = x.upper()
        elif move2 == 'A1':
            a[1][0] = 'O'
            list_2.append('A1')
        elif move2 == 'B1':
            b[1][0] = 'O'
            list_2.append('B1')
        elif move2 == 'C1':
            c[1][0] = 'O'
            list_2.append('C1')
        elif move2 == 'A2':
            a[1][1] = 'O'
            list_2.append('A2')
        elif move2 == 'B2':
            b[1][1] = 'O'
            list_2.append('B2')
        elif move2 == 'C2':
            c[1][1] = 'O'
            list_2.append('C2')
        elif move2 == 'A3':
             a[1][2] = 'O'
             list_2.append('A3')
        elif move2 == 'B3':
             b[1][2] = 'O'
             list_2.append('B3')
        elif move2 == 'C3':
             c[1][2] = 'O'
             list_2.append('C3')
        print('\n\n')
        print(top)
        print(a)
        print(b)
        print(c)
        print('\n\n')
        test()

tictactoe()
    
