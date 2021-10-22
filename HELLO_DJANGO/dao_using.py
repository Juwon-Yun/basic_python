from HELLO_DJANGO.dao_emp import DaoEmp

de = DaoEmp()


# x = 13
# for i in range(1,10):    
#     value1 = x      
#     value2 = x    
#     value3 = x    
#     value4 = x    
#     cnt = de.myinsert(emp_id=value1, emp_name=value2, tel=value3, address=value4)
#     x += 1
#     print(cnt)

de.myupdate(emp_id=13, emp_name=1, tel=1, address=1)
de.mydelete(emp_id=15)

lst = de.myselect()
for row in lst:
    print(row)