print "Tax Calculator".center(80)
salary=int(input("Enter your Gross salary in Rupees:"))
age=int(input("Enter your age:"))
if 0<=salary<=250000 and age<60:
 print "No Tax"
elif 251000<=salary<=500000 and age<60:
 tax1=(salary/100)*5
 aftax1=salary-tax1
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax1,"INR as income tax"
 print "Your total income after paying tax is",aftax1,"INR"
elif 500001<=salary<=1000000 and age<60:
 tax2=(salary/100)*20
 aftax2=salary-tax2
 print "Your gross salary is",salary
 print "you need to pay",tax2,"INR as income tax"
 print "Your total income after paying tax is",aftax2,"INR"
elif 1000001<=salary<=5000000 and age<60:
 tax1=(salary/100)*30
 aftax3=salary-tax3
 print "Your gross salary is",salary
 print "you need to pay",tax3,"INR as income tax"
 print "Your total income after paying tax is",aftax3,"INR"
elif 5000001<=salary<=10000000 and age<60:
 tax4=(salary/100)*30
 surcharge=(tax4/100)*10
 surtax=tax4+surcharge
 cess=(surtax/100)*3
 surtcess=surtax+cess
 aftax4=salary-surtcess
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax4,"INR as income tax"
 print "you also have to pay 10% surcharge that is",surcharge,"INR"
 print "cess on your gross income is",cess,"INR"
 print "Your total income after paying tax is",aftax4,"INR"
elif 10000001<=salary<=50000000000000 and age<60:
 tax5=(salary/100)*30
 surcharge=(tax5/100)*15
 surtax=tax5+surcharge
 cess=(surtax/100)+3
 surtcess=surtax+cess
 aftax5=salary-surtcess
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax5,"INR as income tax"
 print "You have to pay 15% surcharge that is",surcharge,"INR"
 print "cess on your gross income is",cess,"INR"
 print "Your total income after paying tax is",aftax5,"INR"
elif 0<=salary<=300000 and 61<=age<=80:
 print "No Tax"
elif 300001<=salary<=500000 and 61<=age<=80:
 tax1=(salary/100)*5
 aftax1=salary-tax1
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax1,"INR as income tax"
 print "Your total income after paying tax is",aftax1,"INR"
elif 500001<=salary<=1000000 and 61<=age<=80:
 tax2=(salary/100)*20
 aftax2=salary-tax2
 print "Your gross salary is",salary
 print "you need to pay",tax2,"INR as income tax"
 print "Your total income after paying tax is",aftax2,"INR"
elif 1000001<=salary<=5000000 and 61<=age<=80:
 tax3=(salary/100)*30
 aftax3=salary-tax3
 print "Your gross salary is",salary
 print "you need to pay",tax3,"INR as income tax"
 print "Your total income after paying tax is",aftax3,"INR"
elif 5000001<=salary<=10000000 and 61<=age<=80:
 tax4=(salary/100)*30
 surcharge=(tax4/100)*10
 surtax=tax4+surcharge
 cess=(surtax/100)*3
 surtcess=surtax+cess
 aftax4=salary-surtcess
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax4,"INR as income tax"
 print "you also have to pay 10% surcharge that is",surcharge,"INR"
 print "cess on your gross income is",cess,"INR"
 print "Your total income after paying tax is",aftax4,"INR"
elif 10000001<=salary<=50000000000000 and 61<=age<=80:
 tax5=(salary/100)*30
 surcharge=(tax5/100)*15
 surtax=tax5+surcharge
 cess=(surtax/100)*3
 surtcess=surtax+cess
 aftax5=salary-surtcess
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax5,"INR as income tax"
 print "You have to pay 15% surcharge that is",surcharge,"INR"
 print "cess on your gross income is",cess,"INR"
 print "Your total income after paying tax is",aftax5,"INR"
elif 0<=salary<=500000 and age>=81:
 print "No Tax"
elif 500001<=salary<=1000000 and age>=81:
 tax2=(salary/100)*20
 aftax2=salary-tax2
 print "Your gross salary is",salary
 print "you need to pay",tax2,"INR as income tax"
 print "Your total income after paying tax is",aftax2,"INR"
elif 1000001<=salary<=10000000 and age>=81:
 tax4=(salary/100)*30
 aftax4=salary-surtcess
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax4,"INR as income tax"
 print "Your total income after paying tax is",aftax4,"INR"
elif 10000001<=salary<=50000000000000 and age>=81:
 tax5=(salary/100)*30
 surcharge=(tax5/100)*15
 surtax=tax5+surcharge
 cess=(surtax/100)*3
 surtcess=surtax+cess
 aftax5=salary-surtcess
 print "Your gross salary is",salary,"INR"
 print "you need to pay",tax5,"INR as income tax"
 print "You have to pay 15% surcharge that is",surcharge,"INR"
 print "cess on your gross income is",cess,"INR"
 print "Your total income after paying tax is",aftax5,"INR"
else:
 print "invalid input"

