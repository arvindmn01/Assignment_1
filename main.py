from fastapi import FastAPI , Request, Form
from fastapi.templating import Jinja2Templates

app=FastAPI()
templates=Jinja2Templates(directory='Templates')
from typing import Optional


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Column,Integer,String
# SQLALCHEMY_DATABASE_URL='sqlite:///./database.db'

# engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

# Sessionmaker=sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base=declarative_base()

# class Task(Base):
#     __tablename__='task'
#     id=Column(Integer,primary_key=True,index=True)
#     task_name=Column(String)
#     completed=Column(String)

@app.get('/')
def home(request:Request):
    return templates.TemplateResponse('base.html',context={'request':request})
add_list=[]
completed_task=[]
pending=[]
@app.post('/')
def home(request:Request,Add_task:Optional[str]=Form(None),task1:Optional[str]=Form(None),submit:Optional[str]=Form(None),delete:Optional[str]=Form(None)):

    print(delete)
    
    if Add_task!=None and Add_task not in add_list:

        add_list.append(Add_task)
    if (submit=='Mark as Completed' and task1!=None) and (task1 not in completed_task):
        completed_task.append(task1)
        pending.remove(task1)
    if delete=='Delete' and task1!=None:
        add_list.remove(task1)
    
    for i in add_list:
        if i not in completed_task and i not in pending:
            pending.append(i)
   
    return templates.TemplateResponse('base.html',context={'request':request,'add_list':add_list,'completed_task':completed_task,'pending':pending})
