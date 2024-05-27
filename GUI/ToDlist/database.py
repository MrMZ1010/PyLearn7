# MohammadAli Mirzaei ####

import sqlite3

class Database:
    def __init__(self):
        # Establish a connection to the SQLite database file named "todolist.db"
        self.conn = sqlite3.connect("todolist.db")
        # Create a cursor object to execute SQL queries
        self.cursor=self.conn.cursor() 

    def get_task(self):
        # SQL query to select all rows from the 'tasks' table
        query="SELECT * FROM tasks"
        # Execute the SQL query
        result=self.cursor.execute(query)
        # Fetch all rows returned by the query
        tasks=result.fetchall()
        # Return the fetched rows
        return tasks
    
    def add_new_tasks(self,new_title,new_description,priority,time):
        try:
            # SQL query to insert a new task into the 'tasks' table
            query= f"INSERT INTO tasks('title','description','priority') VALUES('{new_title}','{new_description}\n{time}',{priority})"
            # Execute the SQL query
            self.cursor.execute(query)
            # Commit the changes to the database
            self.conn.commit()
            # Return True to indicate successful insertion
            return True
        except:
            # Return False if an error occurs during insertion
            return False

    def remove_task(self,id_num,obj):
        # SQL query to delete a task from the 'tasks' table based on its ID
        query=f"DELETE FROM tasks WHERE id={id_num}" 
        # Execute the SQL query
        self.cursor.execute(query)
        # Commit the changes to the database
        self.conn.commit()
        # Call the 'read_from_database' method of the passed object to refresh the data
        obj.read_from_database()

    def task_done(self,id_num,r):
        if r==2:
            # If the 'r' parameter is 2, change it to 1
            r=1
        # SQL query to update the 'is_done' column of a task based on its ID
        query=f"UPDATE tasks SET is_done='{r}' WHERE id={id_num}"
        # Execute the SQL query
        self.cursor.execute(query)
        # Commit the changes to the database
       
