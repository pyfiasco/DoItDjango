import os, sys
from pathlib import Path
import time

path = Path('c:/projects/mysite')
os.chdir(path)



'''
os.system("python manage.py runserver")
os.system("python manage.py runserver")
os.system("python manage.py runserver")
'''
def migrate(app='pages'):    
    os.system("python manage.py makemigrations")
    time.sleep(5)
    os.system(f"python manage.py makemigrations {app}")
    time.sleep(5)
    os.system(f"python manage.py migrate {app}")


def run():
    os.system("python manage.py runserver")

def collectstatic():
    # static 파일 모으기
    os.system("python manage.py collectstatic")

if __name__ == "__main__":
    '''
    migrate()  
    collectstatic()      
    '''






    '''
    run()   
    '''
