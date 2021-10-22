import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="python", db="python",port=3305 , charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        #print("DaoEmp:__init__")
        
    def myselect(self):
        sql = "select * from emp"
    
        self.curs.execute(sql)
    
        rows = self.curs.fetchall()
    
        return rows
    
    def myinsert(self,emp_id,emp_name,tel,address):    
        sql = f"""insert into emp values('{emp_id}',{emp_name},{tel},{address})"""
    
        result = self.curs.execute(sql)
        
        return result
    
    def myupdate(self,emp_id,emp_name,tel,address):
        sql = f"""update emp set emp_name = '{emp_name}',
                                 tel = '{tel}',
                                 address = '{address}'
                                 where emp_id = '{emp_id}' """
    
        result = self.curs.execute(sql)
    
        return result
    
    def mydelete(self, emp_id):
        sql = f"""delete from emp where emp_id = {emp_id} """
    
        result = self.curs.execute(sql)
    
        return result
    
    def __del__(self):
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        #print("DaoEmp:__del__")
        
if __name__ == '__main__':
    de = DaoEmp()
    # lst = de.myselect()
    # for row in lst:
    #     print(row)
    
    #cnt = de.myinsert("12", "12", "12", "12")
    #print(cnt)