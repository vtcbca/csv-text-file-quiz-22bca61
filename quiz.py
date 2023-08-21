import csv
csv_rowlist=[['sid','sname','salary'],
             [1,'siya',3000],
             [2,'om',4000],
             [3,'nisha',4500],
             [4,'disha',5000],
             [5,'sai',4200]]
with open('c:\\sqlite3\\csv\\salary.csv','w') as file:
    w= csv.writer(file)
    w.writerows(csv_rowlist)



    
