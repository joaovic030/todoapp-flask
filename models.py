# 1.import sqlite
import sqlite3
# 2. create a connection to DB     
# conn = sqlite3.connect('todo.db')
# 3. Write your sql query   
# query = "<SQLite Query goes here>"
# 4. execute the query
# result = conn.execute(query)


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)    
    def create_user_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS "User" (
                _id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT,
                CreatedOn Date DEFAULT CURRENT_DATE
            );
        """
        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create(self, text, description):
        # print("\n \n --Text: "+text + "--- Description: "+description)
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'

        result = self.conn.execute(query)
        return result
    
    # def update()