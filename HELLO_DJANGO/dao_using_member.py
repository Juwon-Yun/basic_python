from HELLO_DJANGO.dao_member import DaoMember

de = DaoMember()


# x = 13
# for i in range(1,10):    
#     value1 = x      
#     value2 = x    
#     value3 = x    
#     value4 = x    
#     cnt = de.myinsert(emp_id=value1, emp_name=value2, tel=value3, address=value4)
#     x += 1
#     print(cnt)


de.myinsert(m_id=1, m_name="윤주원", mobile="010-4855-6457", in_date="DATE_FORMAT(NOW(),'%Y%c%e')")
#de.myupdate(m_id=1, m_name="윤윤윤", mobile="010-1111-1111", up_date="DATE_FORMAT(NOW(),'%Y%c%e')")
#de.mydelete(m_id=1)
lst = de.myselect()
for row in lst:
    print(row)
