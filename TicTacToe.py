# -*- coding: utf-8 -*-
"""
Dan Foster Python Project - Tic Tac Toe Game
"""


def tictactoe():
    top = '    1   2   3 '
    row_a = ['A',['|',' ','|',' ','|',' ','|']]
    row_b = ['B',['|',' ','|',' ','|',' ','|']]
    row_c = ['C',['|',' ','|',' ','|',' ','|']]
    moves = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
    played = []
    underb = '_________________'
    undera = '_________________'

    def game_over():
        z = input('GAME OVER, PRESS ENTER TO RESTART:\n\n')
        if z != None:
            tictactoe()

    def player_2_wins():
        print('\n\nPLAYER 2 WINS!')
        make_board()
        game_over()
    def player_1_wins():
        print('\n\nPLAYER 1 WINS!')
        make_board()
        game_over()
    def test_win():

        #WIN CONDITIONS
        #top row horizontal win conditions

        if row_a[1][1] == row_a[1][3] and row_a[1][3]== row_a[1][5]:
            if row_a[1][1] == 'X':
                player_1_wins()
            elif row_a[1][1] == '0':
                player_2_wins()
        #mid row horizontal win conditions
        elif row_b[1][1] == row_b[1][3] and row_b[1][3]== row_b[1][5]:
            if row_b[1][5] == 'X':
                player_1_wins()
            elif row_b[1][5]=='0':
                player_2_wins()
        #bottom row horizontal win conditions
        elif row_c[1][1] == row_c[1][3] and row_c[1][3]== row_c[1][5]:
            if row_c[1][5]== 'X':
                player_1_wins()
                make_board()
                game_over()
            elif row_c[1][5] == '0':
                player_2_wins()
        #left column vertical win conditions
        elif row_c[1][1] == row_b[1][1] and row_b[1][1] == row_a[1][1]:
            if row_a[1][1] == 'X':
                player_1_wins()
                make_board()
                game_over()
            elif row_a[1][1] == '0':
                player_2_wins()
        #left colum
        #mid column vertical win conditions
        elif row_c[1][3] == row_b[1][3] and row_b[1][3]== row_a[1][3]:
            if row_c[1][3] == 'X':
                player_1_wins()
                make_board()
                game_over()
            elif row_c[1][3] == '0':
                player_2_wins()
        #right column vertical win conditions
        elif row_c[1][5] == row_b[1][5] and row_b[1][5] == row_a[1][5]:
            if row_a[1][5] == 'X':
                player_1_wins()
                make_board()
                game_over()
            elif row_a[1][5] == '0':
                player_2_wins()
        #diagonal win conditions
        elif row_c[1][1] == row_b[1][3] and row_b[1][3] == row_a[1][5]:
            if row_c[1][1] == 'X':
                player_1_wins()
            elif row_c[1][1] == '0':
                player_2_wins()
        elif row_c[1][5] == row_b[1][3] and row_b[1][3] == row_a[1][1]:
            if row_c[1][5] == 'X':
                player_1_wins()
            elif row_c[1][5] == '0':
                player_2_wins()
        #Draw
        elif len(played) == len(moves):
            print('\n\nDRAW')
            make_board()
            game_over()
        else:
            pass

    def update_p1():
        if player1go == 'a1':
            row_a[1][1] = 'X'
        elif player1go == 'a2':
            row_a[1][3] = 'X'
        elif player1go == 'a3':
            row_a[1][5] = 'X'
        elif player1go == 'b1':
            row_b[1][1] = 'X'
        elif player1go == 'b2':
            row_b[1][3] = 'X'
        elif player1go == 'b3':
            row_b[1][5] = 'X'
        elif player1go == 'c1':
            row_c[1][1] = 'X'
        elif player1go == 'c2':
            row_c[1][3] = 'X'
        elif player1go == 'c3':
            row_c[1][5] = 'X'
        pass

    def update_p2():
        if player2go == 'a1':
            row_a[1][1] = '0'
        elif player2go == 'a2':
            row_a[1][3] = '0'
        elif player2go == 'a3':
            row_a[1][5] = '0'
        elif player2go == 'b1':
            row_b[1][1] = '0'
        elif player2go == 'b2':
            row_b[1][3] = '0'
        elif player2go == 'b3':
            row_b[1][5] = '0'
        elif player2go == 'c1':
            row_c[1][1] = '0'
        elif player2go == 'c2':
            row_c[1][3] = '0'
        elif player2go == 'c3':
            row_c[1][5] = '0'
        pass
        test_win()
    def make_board():
        a = str(row_a)
        a = a.replace('[','').replace(']','').replace("'",'').replace(',','')
        b = str(row_b)
        b = b.replace('[','').replace(']','').replace("'",'').replace(',','')
        c = str(row_c)
        c = c.replace('[','').replace(']','').replace("'",'').replace(',','')
        print('\n\n')
        print(top)
        print(a)
        print(undera)
        print(b)
        print(underb)
        print(c)
        print('\n\n')

    make_board()
    while True:
        player1go = input('Player 1, choose your coordinates:').lower()
        while player1go not in moves or player1go in played:
             player1go = input('Player 1, choose your coordinates:').lower()
        played.append(player1go)
        update_p1()
        test_win()
        make_board()
        player2go = input('Player 2, choose your coordinates:').lower()
        while player2go not in moves or player2go in played:
             player2go = input('Player 2, choose your coordinates:').lower()
        played.append(player2go)
        update_p2()
        test_win()
        make_board()


tictactoe()
