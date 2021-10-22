import pymysql

class DaoMember:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="python", db="python",port=3305 , charset="utf8")
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        #print("DaoEmp:__init__")
        
    def myselect(self):
        sql = f"""select m_id,
                         m_name,
                         mobile,
                         up_date,
                         in_date
                  from member"""
    
        self.curs.execute(sql)
    
        rows = self.curs.fetchall()
    
        return rows
    
    def myinsert(self,m_id,m_name,mobile,in_date):    
        sql = f"""insert into member(m_id, m_name, mobile, in_date) values({m_id},'{m_name}','{mobile}',{in_date})"""
    
        result = self.curs.execute(sql)
        
        return result
    
    def myupdate(self,m_id,m_name,mobile,up_date):
        sql = f"""update member set m_name = '{m_name}',
                                 mobile = '{mobile}',
                                 up_date = {up_date}
                                 where m_id = {m_id} """
    
        result = self.curs.execute(sql)
    
        return result
    
    def mydelete(self, m_id):
        sql = f"""delete from member where m_id = {m_id} """
    
        result = self.curs.execute(sql)
    
        return result
    
    def __del__(self):
        self.conn.commit()
        self.curs.close()
        self.conn.close()
        #print("DaoEmp:__del__")
        
if __name__ == '__main__':
    de = DaoMember()
    print(de.myselect())
    #cnt = de.myinsert(m_id=1, m_name='1', mobile="010-4855-6457", up_date="DATE_FORMAT(NOW(),'%y%c%e')", in_date="DATE_FORMAT(NOW(),'%y%c%e')")
    #print(cnt)
    #lst = de.myselect()
    #for row in lst:
    #    print(row)
    
    #cnt = de.myinsert("12", "12", "12", "12")
    #print(cnt)