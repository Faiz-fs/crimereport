from flask import Flask, render_template, request
import csv
from os import path
import time
import random


app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/crime')
def ret():
    return render_template('crime.html')
@app.route('/comfirm',methods=['POST'])
def save():
    area=request.form.get('area')
    situation=request.form.get('situation')
    a=time.time()
    current_time=time.ctime(a)
    gc = []
    def complaintcheck():
        m=random.randint(10000,10000000)
        if m in gc:
            complaintcheck()
        else:
            gc.append(m)
            return m
    complaint_no=complaintcheck()

    l=['complaint_no','area','situation','current_time']
    if path.isfile('D:\\Faisal\\Documents\\flask\\templates\\crimedata.csv'):
        with open('D:\\Faisal\\Documents\\flask\\templates\\crimedata.csv','a+',newline='') as f:
            read=csv.reader(f)
            w=csv.DictWriter(f,fieldnames=l)
            w.writerow({'complaint_no':complaint_no,'area':area,'situation':situation,'current_time':current_time})
    else:
        with open('D:\\Faisal\\Documents\\flask\\templates\\crimedata.csv', 'w', newline='') as fa:
            writer = csv.DictWriter(fa, fieldnames=l)
            writer.writeheader()
            writer.writerow({'complaint_no':complaint_no,'area': area, 'situation': situation,'current_time':current_time})
    return render_template('confirm.html',area=area,cr=situation,fs=complaint_no)
@app.route('/report')
def report():
    with open('D:\\Faisal\\Documents\\flask\\templates\\crimedata.csv','r') as re:
        read=csv.reader(re)
        item=[]
        for i in read:
            l=len(i)
            if i[(l-1)]=='solved' or (not i[(l-1)].isalpha()):
                item.append(i)
    return render_template('report.html',li=item)
@app.route('/checkstatus')
def s():
    return render_template('checkstatus.html')
@app.route('/status',methods=['POST'])
def check():
    c_no=request.form.get('cno')
    with open('D:\\Faisal\\Documents\\flask\\templates\\crimedata.csv','r') as kl:
        read=csv.reader(kl)
        for i in read:
            if i[0]==c_no:
                l=len(i)
                if i[(l-1)].isalpha():
                    b=i[(l-1)]
                else:
                    b='investigation not started '    return render_template('result.html',status=b)

if __name__=='__main__':
    app.run(debug=True)
                                    ▪ 
