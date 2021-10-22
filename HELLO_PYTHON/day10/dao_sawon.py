import pymysql

class DaoMovie:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="python", db="python",port=3305 , charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        #print("DaoEmp:__init__")
        
    def myinsert(self,title,link,image,subtitle,pubDate,director,actor,userRating):    
        sql = """insert into movie
        (title,link,image,subtitle,pubDate,director,actor,userRating) 
        values
        (%s,%s,%s,%s,%s,%s,%s,%s)"""
    
        result = self.curs.execute(sql,(title,link,image,subtitle,pubDate,director,actor,userRating))
        
        return result
    
    def __del__(self):
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        #print("DaoEmp:__del__")
        
if __name__ == '__main__':
    pass
    #de = DaoEmp()
    # lst = de.myselect()
    # for row in lst:
    #     print(row)
    
    #cnt = de.myinsert("12", "12", "12", "12")
    #print(cnt)