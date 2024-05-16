import sqlite3
import os

class dbContext:
    def __init__(self):
        self.filePath = "~/playground"
        self.fileName = "settings.db"
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath) 
    @property
    def fullFilePath(self):
        return os.path.join(self.filePath, self.fileName)
        
    @property
    def connection(self):
        return sqlite3.connect(self.fullFilePath)
    
    @property
    def cursor(self):
        return self.connection.cursor()
    
    def executeQuery(self, query:str, *args):
        cursor = self.cursor
        try:
            cursor.execute(query, args)
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()
            
    def tableExists(self, tableName):
        cursor = self.cursor
        try:
            response = cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ", (tableName, ))
            return cursor.fetchone()[0] == 1
        finally:
            cursor.close()