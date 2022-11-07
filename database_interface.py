from database import Database
import os
import time

def run():

    os.system('cls')

    print(f"{'=' * 20} DATABASE INTERFACE V 1.0 {'=' * 20}")

    db_path = input('New/Existing Database Path: ')

    while db_path.strip().rstrip() == '':
        db_path = input('New/Existing Database Path: ')

    db = Database(db_path)

    if not os.path.exists(db_path):
        print('[Creating new database]')


    options = ['Size', 'Reset', 'Peek', 'Change Database', 'New Database', 'Delete', 'Quit']

    while True:
        print(f"{'<' * 20} {db.get_path()} {'>' * 20}")
        for i in range(len(options)):
            print(f'[{i}]: {options[i]}')
        
        choice = int(input())

        if choice == 0:
            print(f'Size: {db.size()}')
        
        elif choice == 1:
            db.reset()
            print('[Database reset]')
        
        elif choice == 2:
            key = input('Key: ')
            val = db.fetch(key)

            if val == None:
                print('[Key not found]')
            else:
                print('Value: ' + db.fetch(key))
        
        elif choice == 3:
            db_new_path = input('Database Path: ')
            if not os.path.exists(db_new_path):
                print('[Database not found]')
            else:
                db = Database(db_new_path)
        
        elif choice == 4:
            new_path = input('New Database Path: ')
            Database(new_path)
            print('[New database created]')

        elif choice == 5:
            choice = input('Are you sure? Program will exit [y/n]: ')

            if choice == 'y':
                db.close()
                os.remove(db.get_path())
                db = None
                print('[Database erased]')
                print('[Program exiting...]')
                os.system('cls')
                break

        else:
            break
        
        time.sleep(0.5)
        print()

    if db != None:       
        db.close()




if __name__ == '__main__':
    run()