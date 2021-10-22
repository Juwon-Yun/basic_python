import pymysql
import numpy as np


class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="python", db="_stock_old",port=3305 , charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        #print("DaoEmp:__init__")
        
    def myinsert(self,s_code,s_name,price,g_time):    
        sql = """insert into stock
        (s_code,s_name,price,g_time) 
        values
        (%s,%s,%s,%s)"""
    
        result = self.curs.execute(sql,(s_code,s_name,price,g_time))
        
        return result
    def myCount(self):
        sql = """select count(*) from stock"""
        
        #fetch_all, execute X
        
        result = self.curs.execute(sql)
        
        rows = self.curs.fetchall()    
        print(rows)

        for row in rows:
            print(row)
            print(row)
            
        
        return result
    
    def mySamsung(self,s_name):
        arr = []
        sql = f"""
        SELECT price FROM stock
        where s_name like '{s_name}'
        order by price
        """
        self.curs.execute(sql)
        result = self.curs.fetchall()
        for i in result:
            arr.append(i['price'])
        
        return arr
    
    def mySelect100(self,s_name):
        arr = []
        sql = f"""
        SELECT price FROM stock
        where s_name like '{s_name}'
        order by price
        """
        self.curs.execute(sql)
        result = self.curs.fetchall()
        for i in result:
            arr.append(i['price'])

        retarr = []
        
        for a in arr:
            #값이 0인 데이터는 0.9로 입력해준다
            if arr[0] == 0:
                retarr.append(0.98)
            else:
                retarr.append(a / arr[0])
        
        return retarr
    
    #넘피를 이용한 방법
    def mySelect100n(self,s_name):
        arr = []
        sql = f"""
        SELECT price FROM stock
        where s_name like '{s_name}'
        order by price
        """
        self.curs.execute(sql)
        result = self.curs.fetchall()
        for i in result:
            arr.append(i['price'])

        arr_n = np.array(arr)
        arr_n = arr_n / arr_n[0]
        return arr_n
    
    def stock_old(self):
        sql = """SELECT s000020 FROM stock_sync_0121"""
        
        self.curs.execute(sql)
        arr = self.curs.fetchall()
        
        return arr
    
    def getAllNames(self):
        arr = []
        sql = f"""
        SELECT distinct s_name FROM stock
        """
        self.curs.execute(sql)
        result = self.curs.fetchall()
        #fetchall에서 s_name들의 값만 필요하기때문에 반복문으로 arr 배열에 value값을 넣어준다
        for i in result:
            arr.append(i['s_name'])
        
        return arr
    
    def mycommit(self):
        self.conn.commit()
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        #print("DaoEmp:__del__")
        
if __name__ == '__main__':
    ds = DaoStock()
    price = ds.stock_old();
    print(price)
    #de = DaoEmp()
    # lst = de.myselect()
    # for row in lst:
    #     print(row)
    
    #cnt = de.myinsert("12", "12", "12", "12")
    #print(cnt)