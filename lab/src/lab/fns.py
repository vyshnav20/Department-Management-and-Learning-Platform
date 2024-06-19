import mysql.connector  

# question for a particular subject
def qn(qid,sub):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')

    mycursor = mydb.cursor()
    sql = "SELECT qn,qn_title FROM qns WHERE q_id = %s AND sub_id = %s"
    values = (qid, sub)

    mycursor.execute(sql, values)
    result = mycursor.fetchall()
    return(result[0][0],result[0][1])

def qnss(sub,roll):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    l = []
    mycursor = mydb.cursor()
    
    sql = "SELECT sub_name,sem FROM subjects WHERE sub_id = %s"
    mycursor.execute(sql, (sub,))
    result = mycursor.fetchall()
    l.append(result[0][0])
    l.append(result[0][1])
    if(roll==0):
        q1=qn(1,sub)
        q2=qn(2,sub)
    else:
        q1=qn(3,sub)
        q2=qn(4,sub)
    l.append(q1[0])
    l.append(q2[0])
    l.append(q1[1])
    l.append(q2[1])
    return(l)
    
# languages supported for a subject
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

# display list of questions in db
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

#delete qn from db
def delete_qn(q):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "delete from qns where q_id=%s and qn_title=%s"
    mycursor.execute(sql, (q[0],q[1],))
    mydb.commit()

# insert qn to db
def add_qn(q):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "insert into qns values(%s,%s,%s,%s)"
    mycursor.execute(sql, (q[0],q[1],q[2],q[3],))
    mydb.commit()

# subject id
def subjects():
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT sub_id FROM subjects"
    mycursor.execute(sql,)
    result = mycursor.fetchall()
    for i in result:

        for j in i:
            l.append(j)
    #print(l)
    return l

# details of qn in db
def viewq(q):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT * FROM qns where q_id=%s and qn_title=%s"
    mycursor.execute(sql, (q[0],q[1],))
    result = mycursor.fetchall()
    for i in result:
        for j in i:
            l.append(j)
    #print(l)
    return l

# update qn to db
def updt_qn(q):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "update qns set qn= %s, qn_title=%s where q_id=%s and sub_id=%s"
    mycursor.execute(sql, (q[2],q[3],q[0],q[1],))
    mydb.commit()

# list exam dates
def admin_sub():
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT sem,sub_name,date FROM subjects"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        #for j in i:
        l.append(i)
    return(l)