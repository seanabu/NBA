import MySQLdb
from lib import players

class Database:

    host = ''
    user = ''
    password = ''
    db = 'mydb'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":

    db = Database()

    #CleanUp Operation
    del_query = "DELETE FROM basic_python_database"
    db.insert(del_query)

    # Data Insert into the table
    query = """     INSERT  ('playerID', 'first_name', 'last_name', 'birthdate' , 'season_exp', 'current_team','position', 'height', 'from_year', 'to_year') INTO players  VALUES (203112, u'Quincy', u'Acy', u'1990-10-06T00:00:00', 3, 1610612758, u'Forward', u'6-7', u'2012', u'2015'),(203919, u'Jordan', u'Adams', u'1994-07-08T00:00:00', 1, 1610612763, u'Guard', u'6-5', u'2014', u'2015'),(203500, u'Steven', u'Adams', u'1993-07-20T00:00:00', 2, 1610612760, u'Center', u'7-0', u'2013', u'2015'),(202399, u'Jeff', u'Adrien', u'1986-02-10T00:00:00', 4, 0, u'', u'', u'2010', u'2014'),(201167, u'Arron', u'Afflalo', u'1985-10-15T00:00:00', 8, 1610612752, u'Guard', u'6-5', u'2007', u'2015')")
        """

    # db.query(query)
    db.insert(query)

    # Data retrieved from the table
    select_query = """
        SELECT * FROM basic_python_database
        WHERE age = 21
        """

    people = db.query(select_query)

    for person in people:
        print "Found %s " % person['name']
