# Flask-Database
This is a basic flask-database template that will mange databases with sqlalchemy

## Make a database in postgres:

### login:
$ psql postgres

### create new db:
postgres=# CREATE DATABASE flask_database;  

### create database URL (for postgres):
String Form:  
"|sql you are using|://|user|:|password|@localhost|/|dbname|"  
Ex:
"postgresql://bbearce:password@localhost/flask_database"  
  
### paste this in app.py
...  
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bbearce:password@localhost/flask_database"  
... 

### open terminal and create db and tables defined in app.py

$ python  
.>>> from app import db  
.>>> db.create_all()  
.>>> db.session.commit()  

### open postgres and see tables

$ psql flask_database  
flask_database=# \dt  
        List of relations  
 Schema | Name  | Type  |  Owner    
--------+-------+-------+---------  
 public | roles | table | bbearce   
 public | users | table | bbearce  
(2 rows)  
