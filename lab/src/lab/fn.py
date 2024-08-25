import firebase_admin
from firebase_admin import credentials,db
from datetime import datetime
import traceback 
import mysql.connector  
def dbs():
    if not firebase_admin._apps:
        cred=credentials.Certificate('F:\QT\lab\src\lab\mca-dmlp-firebase-adminsdk-5sboz-7539f33330.json')
        firebase_admin.initialize_app(cred,{'databaseURL':'https://mca-dmlp-default-rtdb.asia-southeast1.firebasedatabase.app/'})
    
    return db.reference('/')

def qn(qid,sub):
    ref=dbs()
    r=ref.child('Questions').child(sub).child('Q').child(qid).get()
    l=[]
    for i in r.values():
        l.append(i)
    return l

def qnss(roll):
    ref=dbs()
    l=[]
    d= datetime.now().strftime("%Y-%m-%d")
    r=ref.child("Exam").get()
    for i,j in r.items():
        if(j['Date']==d):
            sub=i
    s=ref.child("Subjects").get()
    for i,j in s.items():
        if i==sub:
            l.append(j['Sub_Name'])
            l.append(j['Sem'])
    if(roll==0):
        q1=qn("01",sub)
        q2=qn("02",sub)
    else:
        q1=qn("03",sub)
        q2=qn("04",sub)
    l.append(q1[0])
    l.append(q2[0])
    l.append(q1[1])
    l.append(q2[1])
    l.append(sub)
    return(l)

def langs(sub):
    ref=dbs()
    l=ref.child("Prog_Lang").child("20MCA201").get()
    return l

def login_user(username):
    ref=dbs()
    s=ref.child("Student").child(username).get()
    if s!=None:
        return s['Password']
    else:
        return ""
    

def admin():
    ref=dbs()
    qn=ref.child("Questions").get()
    sub=ref.child("Subjects").get()
    l=[]
    if(qn==None):
        return l
    for i,j in qn.items():
        for k in j.values():
            for y,x in k.items():
                l2=[]
                l2.append(x['Qn_Title'])
                l2.append(sub[i]['Sem'])
                l2.append(sub[i]['Sub_Name'])
                l2.append(y)
                l.append(l2)
    return (l)

def delete_qn(q):
    ref=dbs()
    qn_title = q[1]
    qn_ref=ref.child("Questions").get()
    for course_id, course_data in qn_ref.items():
        for qn_set_key, qn_set_data in course_data.items():
            for question_key, question_data in qn_set_data.items():
                if question_key == q[0] and question_data['Qn_Title'] == qn_title:
                    ref.child(f"Questions/{course_id}/{qn_set_key}/{question_key}").delete()
                    ref.child(f"Test_Case/{course_id}/{qn_set_key}/{question_key}").delete()
                    return


def add_qn(q,l):
    ref=dbs()
    sub=ref.child("Subjects").get()
    qns=ref.child("Questions").get()
    for i,j in sub.items():
        if(j['Sub_Name']==q[1]):
            id=i
    ref.child("Questions").child(id).child("Q").update({q[0]:{"Qn":q[2],"Qn_Title":q[3]}})

    tc=ref.child("Test_Case")
    for i in range(len(l)):
        if i==9:
            tid="10"
        else:
            tid="0"+str(i+1)
        tc.child(id).child("Q").child(q[0]).child("TC").update({tid:{"Input":l[i][0],"Output":l[i][1]}})

def subjects():
    ref=dbs()
    l=[]
    exm=ref.child("Exam").get()
    sub=ref.child("Subjects").get()
    if(exm==None):
        return l
    for i in exm:
        l.append(sub[i]["Sub_Name"])
    return l

def qids(val):
    ref=dbs()
    l=[]
    q=[]
    sub=ref.child("Subjects").get()
    qns=ref.child("Questions").get()
    id=""
    if qns==None:
        q=["0"+str(x) for x in range(1,5)]
        return q
    for i,j in sub.items():
        if(j['Sub_Name']==val):
            id=i
    if(id not in qns):
        q=["0"+str(x) for x in range(1,5)]
        return q
    for i in qns[id].values():
        for k in i:
            l.append(int(k))
    for i in range(1,5):
        if i not in l:
            s="0"+str(i)
            q.append(s)
    return q


def viewq(q):
    ref=dbs()
    qns=ref.child("Questions").get()
    l1=[]
    for i,j in qns.items():
        for x,y in j.items():
            for l,m in y.items():
                if l==q[0] and m['Qn_Title']==q[1]:
                    l1.append(q[0])
                    l1.append(i)
                    l1.append(m["Qn"])
                    l1.append(q[1])

    sub=ref.child("Subjects").get()
    tc=ref.child("Test_Case").get()
    for i,j in sub.items():
            if(j['Sub_Name']==q[2]):
                id=i
    for i,j in tc.items():
        if i==id:
            for k,l in j.items():
                for x,y in l.items():
                    if x==q[0]:
                        for o,p in y.items():
                                for q,w in p.items():
                                    t1=[]
                                    t1.append(w['Input'])
                                    t1.append(w['Output'])
                                    l1.append(t1)
    return l1

def updt_qn(q,l):
    ref = dbs()
    qid = str(q[0])
    qns = ref.child("Questions").child(q[1]).child("Q").child(qid)
    qns.update({
        "Qn": q[2],
        "Qn_Title": q[3]
    })
    tc=ref.child("Test_Case")
    for i in range(len(l)):
        if i==9:
            tid="10"
        else:
            tid="0"+str(i+1)
        tc.child(q[1]).child("Q").child(q[0]).child("TC").update({tid:{"Input":l[i][0],"Output":l[i][1]}})


def admin_sub(n,id):
    ref=dbs()
    l1=[]
    xm=ref.child("Exam").get()
    qns=ref.child("Subjects").get()
    if(xm==None):
        return l1
    if(n==0):
        for x,y in xm.items():
            for i,j in qns.items():
                l=[]
                if i==x:
                    l.append(j['Sem'])
                    l.append(j['Sub_Name'])
                    l.append(y['Date'])
                    l1.append(l)
    else:
        st=ref.child("Student").child(id).get()
        sem=(st['Semester'])
        for x,y in xm.items():
            for i,j in qns.items():
                l=[]
                if i==x and j['Sem']==sem:
                    l.append(j['Sem'])
                    l.append(j['Sub_Name'])
                    l.append(y['Date'])
                    l1.append(l)
    return l1
    

def subname(sem):
    ref=dbs()
    l=[]
    sub=ref.child("Subjects").get()
    for i in sub.values():
        if(i['Sem']==int(sem)):
            l.append(i['Sub_Name'])
    return l


def in_ex(sub1,date):
    ref=dbs()
    sub=ref.child("Subjects").get()
    for i,j in sub.items():
        if(j['Sub_Name']==sub1):
            id=i
    exm=ref.child("Exam")
    exm.update({
        id:{"Date":date}
    })

def delete_sub(q):
    ref=dbs()
    sub=ref.child("Subjects").get()
    xm=ref.child("Exam").get()
    id=""
    for i,j in sub.items():
        if j['Sub_Name']==q[0]:
            for x in xm:
                if x==i:
                    ref.child("Exam").child(x).delete()
                    ref.child("Questions").child(x).delete()

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
    msg(l,otp)

def update_pass(ktuid,p):
    ref=dbs()
    ref.child("Student").child(ktuid).update({"Password":p})

def editsubj(q):
    ref=dbs()
    sub=ref.child("Subjects").get()
    exm=ref.child("Exam").get()
    l=[]
    id=""
    for j,i in sub.items():
        if(i['Sub_Name']==q[0]):
            l.append(i['Sem'])
            l.append(i['Sub_Name'])
            id=j
    for i,j in exm.items():
        if(i==id):
            l.append(j['Date'])
    return l

def update_exm(q):
    ref=dbs()
    sub=ref.child("Subjects").get()
    for j,i in sub.items():
            if(i['Sub_Name']==q[0]):
                id=j
    ref.child("Exam").child(id).update({"Date":q[1]})

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
    ref=dbs()
    tc=ref.child("Test_Case").get()
    l=[]
    s="0"+str(q[0])
    for i,j in tc.items():
        if i==q[1]:
            for k in j.values():
                for x,y in k.items():
                    if x==s:
                        for q in y.values():
                            for w in q.values():
                                l.append(w['Input'])
                                l.append(w['Output'])
    return l

def run_code(code,q):
    l=testcase(q)
    r=[]
    code=code+"""\nresult = fn(args['num'])"""
    for i in range(0,len(l),2):
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
    ref=dbs()
    l=[]
    stud=ref.child("Student").get()
    for i,j in stud.items():
        if(i==id):
            l.append(j['Name'])
            l.append(str(j['Phno']))
            l.append(j['Gender'])
            l.append(j['Email'])
            l.append(j['DOB'])
    return l




def stud_sub(id):
    ref=dbs()
    l=[]
    sem=""
    stud=ref.child("Student").get()
    tr=ref.child("Faculty").get()
    for i,j in stud.items():
        if(i==id):
            sem=j['Semester']
    sub=ref.child("Subjects").get()

    for i,j in sub.items():
        l2=[]
        if(j['Sem']==sem):
            l2.append(j['Sub_Name'])
            for x,y in tr.items():
                if(x==j['Tr_id']):
                    l2.append(y['Name'])
        l.append(l2)
    return l

