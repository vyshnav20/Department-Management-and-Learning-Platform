import mysql.connector  

#to fetch subject name and other question details from database
def qn(qid,sub):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')

    mycursor = mydb.cursor()
    sql = "SELECT qn,qn_title FROM qns WHERE q_id = %s AND sub_id = %s"
    values = (qid, sub)

    mycursor.execute(sql, values)
    result = mycursor.fetchall()
    return(result[0][0],result[0][1])

def qnss(sub):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    l = []
    mycursor = mydb.cursor()
    
    sql = "SELECT sub_name,sem FROM subjects WHERE sub_id = %s"
    mycursor.execute(sql, (sub,))
    result = mycursor.fetchall()
    l.append(result[0][0])
    l.append(result[0][1])
    q1=qn(1,sub)
    q2=qn(2,sub)
    l.append(q1[0])
    l.append(q2[0])
    l.append(q1[1])
    l.append(q2[1])
    return(l)
    

def langs(sub):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT lang FROM prg_lang WHERE sub_id = %s"
    mycursor.execute(sql, (sub,))
    result = mycursor.fetchall()
    for i in result:
        for j in i:
            l.append(j)
    #print(l)
    return l


# Login Authentication
def login_user(username):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT password FROM student WHERE ktuid = %s"
    mycursor.execute(sql, (username,))
    result = mycursor.fetchall()
    for i in result:
        for j in i:
            l.append(j)
    #print(l)
    if not l:
        return ""
    else:
        return l[0]


def admin():
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT qn_title,sem,sub_name,q_id FROM qns join subjects on qns.sub_id=subjects.sub_id order by sub_name"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        #for j in i:
        l.append(i)
    return(l)

