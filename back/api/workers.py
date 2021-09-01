from back.models                      import Candidates, Workers, Workers_Role 
from datetime                         import date

#TODO korekta dużych liter 
def add_worker(name:str,login:str,surname:str,birthday,worker_role:str):
    if worker_role=="":
        Workers.objects.create(Name=name,Login=login,Surname=surname,Birthdate=birthday,ID_Workers_Role=None)
    else:
        role_obj, exist= Workers_Role.objects.get_or_create(Name=worker_role)
        Workers.objects.create(Name=name,Login=login,Surname=surname,Birthdate=birthday,ID_Workers_Role=role_obj)

def get_worker(id:int):
    return Workers.objects.get(pk=id)

def get_worker_by_username(_username:str):
    return Workers.objects.get(Login=_username)

def delete_worker():
    pass

def search_workers():
    pass