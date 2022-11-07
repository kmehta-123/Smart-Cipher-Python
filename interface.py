import cipher
import smart_solve
from pickle_db import PickleDB
from database import Database
import os

debug = False

main_path = 'main.db'

def encode(db):
    text = input('Text: ').lower()
    offset = int(input('Offset: '))
    encoded = cipher.encode(text, offset)
    db.push(encoded, text)
    print('Encoded: ' + encoded)

def decode(db):
    text = input('Text: ').lower()
    offset = int(input('Offset: '))
    decoded = cipher.decode(text, offset)
    db.push(text, decoded)
    print('Decoded: ' + decoded)

def smart_solve_interface(db):
    text = input('Text: ')

    smart_solved = None

    if db.fetch(text) == None:
        smart_solved = smart_solve.smart_solve(text)
        db.push(text, smart_solved)
    else:
        smart_solved = db.fetch(text)

    print('Smart Solved: ' + smart_solved)


if __name__ == '__main__':

    os.system('cls')

    print(f"{'=' * 20} SMART SOLVER V 1.0 {'=' * 20}")

    main = Database(main_path)

    while True:
        print('[0]: Encode')
        print('[1]: Decode')
        print('[2]: Smart Solve')
        print('[3]: Quit')


        choice = int(input())

        if choice == 0:
            encode(main)
        if choice == 1:
            decode(main)
        if choice == 2:
            smart_solve_interface(main)
        if choice == 3:
            os.system('cls')
            break
        
        print()
        print('-' * 60)
        print()