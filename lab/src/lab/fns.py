import mysql.connector  
from  wapp import *
import traceback 
# question for a particular subject
def qn(qid,sub):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')

    mycursor = mydb.cursor()
    sql = "SELECT qn,qn_title FROM qns WHERE q_id = %s AND sub_id = %s"
    values = (qid, sub)

    mycursor.execute(sql, values)
    result = mycursor.fetchall()
    return(result[0][0],result[0][1])

def qnss(roll):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    l = []
    mycursor = mydb.cursor()
    d= "select CURDATE()"
    mycursor.execute(d,)
    result = mycursor.fetchall()
    d=result[0][0]
    s1= "select sub_id from exam where date= %s"
    mycursor.execute(s1,(d,))
    result = mycursor.fetchall()
    sub=result[0][0]
    sql = "SELECT sub_name,sem FROM subjects WHERE sub_id= %s"
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
    l.append(sub)
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
    sql = "SELECT qn_title,sem,sub_name,q_id FROM qns join subjects on qns.sub_id=subjects.sub_id order by sem,sub_name"
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
    s="select sub_id from subjects where sub_name= %s"
    mycursor.execute(s,(q[1],))
    result = mycursor.fetchall()
    for i in result:

        for j in i:
            id=j
    sql = "insert into qns values(%s,%s,%s,%s)"
    mycursor.execute(sql, (q[0],id,q[2],q[3],))
    mydb.commit()

# subject id
def subjects():
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT sub_name FROM subjects where sub_id in (select sub_id from exam);"
    mycursor.execute(sql,)
    result = mycursor.fetchall()
    for i in result:

        for j in i:
            l.append(j)
    #print(l)
    return l

#qids
def qids(val):
    l=[]
    q=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT q_id FROM qns join subjects on qns.sub_id=subjects.sub_id where sub_name= %s"
    mycursor.execute(sql,(val,))
    result = mycursor.fetchall()
    for i in result:

        for j in i:
            l.append(j)
    #print(l)
    for i in range (1,5):
        if i not in l:
            q.append(str(i))
    return q


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
    sql = "SELECT sem,sub_name,date FROM subjects join exam on exam.sub_id=subjects.sub_id order by date"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        #for j in i:
        l.append(i)
    return(l)

#list of subjects in sem
def subname(sem):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT sub_name FROM subjects where sem= %s"
    mycursor.execute(sql,(sem,))
    result = mycursor.fetchall()
    for i in result:

        for j in i:
            l.append(j)
    #print(l)
    return l


def in_ex(sub,date):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT sub_id FROM subjects where sub_name= %s"
    mycursor.execute(sql,(sub,))
    result = mycursor.fetchall()
    for i in result:
        for j in i:
            l.append(j)
    sql = "insert into exam values(%s,%s)"
    mycursor.execute(sql, (l[0],date,))
    mydb.commit()



def delete_sub(q):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "delete from exam where sub_id in (select sub_id from subjects where sub_name= %s)"
    mycursor.execute(sql, (q[0],))
    mydb.commit()


def wa_msg(otp,id):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT phno FROM student where ktuid= %s"
    mycursor.execute(sql,(id,))
    result = mycursor.fetchall()
    for i in result:

        for j in i:
            l.append(j)
    #print(l)
    msg(l,otp)


def update_pass(ktuid,p):
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "update student set password= %s where ktuid= %s"
    mycursor.execute(sql, (p,ktuid,))
    mydb.commit()


def editsubj(q):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "select sem,sub_name,date from exam join subjects on subjects.sub_id = exam.sub_id where sub_name= %s"
    mycursor.execute(sql, (q[0],))
    result = mycursor.fetchall()
    for i in result:

        for j in i:
            l.append(j)
    return l


def update_exm(q):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "SELECT sub_id FROM subjects where sub_name= %s"
    mycursor.execute(sql,(q[0],))
    result = mycursor.fetchall()
    for i in result:
        for j in i:
            l.append(j)
    sql = "update exam set date= %s where sub_id= %s"
    mycursor.execute(sql, (q[1],l[0],))
    mydb.commit()


def run_embedded_python_code(code, args):
    local_context = {"args": args}
    
    try:
        exec(code, {}, local_context)
    except Exception:
        tb = traceback.format_exc().strip().split('\n')
        error_msg = '\n'.join(tb[4:]) if len(tb) > 4 else '\n'.join(tb)
        return {'error': error_msg}

    return local_context

def testcase(q):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "select inp, output from test_case where qid= %s and sub_id= %s"
    mycursor.execute(sql, (q[0],q[1],))
    result = mycursor.fetchall()
    for i in result:
        for j in i:
            l.append(j)
    return l


def run_code(code,q):
    l=testcase(q)
    r=[]
    code=code+"""\nresult = fn(args['num'])"""
    for i in range(0,3,2):
        arguments = {"num": int(l[i])}
        result = run_embedded_python_code(code, arguments)

        if 'error' in result:
            r.append([result['error'],0])
        else:
            try:
                r.append([result.get('result', 'Key not found in context'),1])
            except KeyError:
                r.append(["Key 'result' not found in context.",1])
    r.append(l)
    return r


def stud_profile(id):
    l=[]
    mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Vyshnav@2002",database='labsys')
    mycursor = mydb.cursor()
    sql = "select * from student where ktuid= %s "
    mycursor.execute(sql, (id,))
    result = mycursor.fetchall()
    for i in result:
        for j in i:
            l.append(j)
    return l