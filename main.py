import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt


pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',10)
pd.set_option('display.max_colwidth',100)
pd.set_option('display.width',None)

print('---------------------------------------Welcome To School Management System---------------------------------------')
print(' \t\t\t\t\t\t\t\t   ~ Priyanshu Kumar')
now=dt.datetime.now()
print('Current Date & Time :',now.strftime('%Y-%m-%d %I:%M:%S'))
def main():
    while True:
        print('\n1.  Student Section')
        print('2.  Faculty Section')
        print('3.  Management Section')
        print('4.  Exit')
        n=input('Choose a no. : ')

        #Student Section
        
        if n=='1':
            df=pd.read_csv('Book.csv')
            print('\n1.  To Check Admission No.')
            print('2.  To Check Student Info')
            print('3.  To Update Student Info')
            print('4.  To Add a New Student')
            print('5.  To Display Recent Record')
            print('6.  To Check All Record')
            print('7.  To Delete a Record')
            print('8.  To Show Total Amount')
            print('9.  To Show Graph')
            print('10. To Back')
           
            n=input('Choose a no. : ')
            if n=='1':
                while True:
                    rn = int(input('Enter Student Roll No. : '))
                    if 1 <= rn <= len(df):
                        an = df['Addmission No.'][df['Roll No.'] == rn].values[0]
                        print(f"Addmission No. of Roll No. {rn} is {an}")
                        ans = input("Do you want to continue (y/n) : ")
                        if ans.lower() != 'y':
                            break
                    else:
                        print('Oops....! This Roll No. Not Exist')
            elif n=='2':
                while True:
                    rn=int(input('Enter Student Roll No. : '))
                    if 1<=rn<=len(df):
                        print(df.loc[rn-1])
                        ans = input("Do you want to continue (y/n) : ")
                        if ans.lower() != 'y':
                            break
                    else:
                        print('Oops....! This Roll No. Not Exist')
            elif n=='3':
                while True:
                    print('1. Update Name')
                    print('2. Update Class')
                    print('3. Update DOB')
                    print('4. Update Father Name')
                    print('5. Update Fee')
                    print('6. Update Mobile No.')
                    u=int(input('Choose a no. : '))
                    if 0<u<7:
                        while True:
                            a=int(input('Enter Student Roll No. : '))
                            if 1<=a<=len(df):
                                break
                            else:
                                print('Oops....! This Roll No. Not Exist')
                        if u==1:
                            b=input('Enter Name : ')
                            while True:
                                c=input('Enter Gender(M/F) : ')
                                if c=='M' or c=='m' or c=='F' or c=='f':
                                    break
                                else:
                                    print('Oops....! Please Enter Valid Data')
                            d=b.upper()
                            e=c.upper()
                            df.loc[a-1,'Name']=d
                            df.loc[a-1,'Gender']=e
                            print('Name,Gender Updated....!')
                        elif u==2:
                            while True:
                                b=int(input('Enter Class : '))
                                if 1<=b<=12:
                                    df.loc[a-1,'Class']=b
                                    print('Class Updated....!')
                                    break
                                else:
                                    print('Oops....! This Class not exist')
                        elif u==3:
                            b=input('Enter DOB(dd/mm/yyyy) : ')
                            df.loc[a-1,'DOB']=b
                            print('DOB Updated....!')
                        elif u==4: 
                            b=input('Enter Father Name : ')
                            c=b.upper()
                            df.iloc[a-1,5]=c
                            print('Father Name Updated....!')
                        elif u==5:
                            b=float(input('Enter Fee: '))
                            df.loc[a-1,'Fee']=b
                            print('Fee Updated....!')
                        elif u==6:
                            while True:
                                try:
                                    b=input('Enter Mobile No. : ') 
                                    l=str(b)     
                                    if len(l)==10:
                                        df.loc[a-1,'Mobile No.']=b
                                        print('Mobile No. Updated....!')
                                        break
                                    else:
                                        print('Oops....! Mobile No. is Inncorrect')
                                except:
                                    print('Oops....! Please Enter Valid Mobile No.')
                        ans = input("Do you want to continue (y/n) : ")
                        if ans.lower() != 'y':
                            break
                    else:
                        print('Please Enter Valid Value')
            elif n=='4':
                a=df.iloc[-1,0]
                b=df.iloc[-1,1]
                c=input('Enter Student Name : ').upper()
                while True:
                    d=int(input('Enter Class : '))
                    if 1<=d<=12:
                        break
                    else:
                        print('Oops....! This Class not exist')
                e=input('Enter DOB(dd/mm/yyyy) : ')
                f=input('Enter Father Name : ').upper()
                while True:
                    g=input('Enter Gender(M/F) : ')
                    if g=='M' or g=='m':
                        g='M'
                        break
                    elif g=='F' or g=='f':
                        g='F'
                        break
                    else:
                        print('Oops....! Please Enter Valid Data')
                if d==12:
                    Fee=3800
                elif d==11:
                    Fee=3500
                elif d==10:
                    Fee=3000
                elif d==9:
                    Fee=2800
                elif d==8:
                    Fee=2500
                elif d==7:
                    Fee=2300
                elif d==6:
                    Fee=2000
                elif d==5:
                    Fee=1800
                elif d==4:
                    Fee=1600
                elif d==3:
                    Fee=1300
                elif d==2:
                    Fee=1200
                elif d==1:
                    Fee=1000
                h=Fee
                while True:
                    i=input('Enter Mobile No. : ')
                    if len(i)==10:
                        break
                    else:
                        print('Oops....! Mobile No. is Inncorrect')
                j=[a+1,b+1,c,d,e,f,g,h,i]
                df.loc[-1]=j
                df.reset_index(drop=True,inplace=True)  
                print('Record Added....!')
            elif n=='5':
                print(df.tail(1))
            elif n=='6':
                df2=df.copy()
                print(df2.to_string(index=False))
            elif n=='7':
                while True:
                    rn=int(input('Enter Roll No. : '))
                    if 1<=rn<=len(df):
                        df.drop(rn-1,inplace=True)
                        print('Record Deleted....!')
                        break
                    else:
                        print('Oops....! This Roll No. Not Exist')
            elif n=='8':
                print('Total Amount is',df.Fee.sum())  
            elif n=='9':
                print('1. No. of Student Graph')
                print('2. Fee Graph')
                print('3. Total Amount Graph')
                print('4. Male & Female Student Graph') 
                while True:
                    g=int(input('Choose a no. : '))
                    if g==1:
                        a=['12','11','10','9','8','7','6','5','4','3','2','1']
                        b=[len(df[df.Class==12]),len(df[df.Class==11]),\
                           len(df[df.Class==10]),len(df[df.Class==9]),\
                           len(df[df.Class==8]),len(df[df.Class==7]),\
                           len(df[df.Class==6]),len(df[df.Class==5]),\
                           len(df[df.Class==4]),len(df[df.Class==3]),\
                           len(df[df.Class==2]),len(df[df.Class==1])]
                        c=['r','b','k','g','y','m','c']
                        plt.bar(a,b,width=0.8,color=c)
                        plt.title('No. of Students From Each Class')
                        plt.xlabel('Classes')
                        plt.ylabel('No. of Students')
                        plt.show()
                        break
                    elif g==2:
                        d=['12','11','10','9','8','7','6','5','4','3','2','1']
                        b=[]
                        for i in range(12,0,-1):
                            a=df.Fee[df.Class==i].iloc[-1]
                            b.append(a)
                        plt.plot(d,b,marker='d',markeredgecolor='red')
                        plt.title('Fee Chart According to the Class')
                        plt.xlabel('Class')
                        plt.ylabel('Fee')
                        plt.show()
                        break
                    elif g==3:
                        b=[]
                        for n in range(12,0,-1):
                            total=df.Fee[df.Class==n]
                            a=total.sum()
                            b.append(a)
                        d=['12','11','10','9','8','7','6','5','4','3','2','1']
                        c=['r','b','k','g','y','m','c']
                        plt.bar(d,b,width=0.8,color=c)
                        plt.title('Total Amount From Each Classes')
                        plt.xlabel('Classes')
                        plt.ylabel('Total Fee')
                        plt.show()
                        break
                    elif g==4:
                        a=['Male','Female']
                        b=[len(df[df.Gender=='M']),len(df[df.Gender=='F'])]
                        plt.bar(a,b,width=0.15,color=['r','g'])
                        plt.title('No. of Male & Female Student')
                        plt.xlabel('Gender')
                        plt.ylabel('No. of Students')
                        plt.show()
                        break
                    else :
                        print('Please Enter Valid Value')
            elif n=='10':
                main()
            else:
                print('Please Enter Valid Value')

            df.to_csv(r'Book.csv',index=False)

        #Faculty Section
        elif n=='2':
            df=pd.read_csv('EmployeeData.csv')
            print('1.  To Check Employee Info')
            print('2.  To Update Employee Info')
            print('3.  To Add a New Employee')
            print('4.  To Display Recent Record')
            print('5.  To Check All Record')
            print('6.  To Delete a Record')
            print('8.  To Show Total Amount')
            print('9.  To Show Graph')
            print('10. To Back')
            n=input('Choose a no. : ')
    
            if n=='1':
                while True:
                    rn=input('Enter Employer ID : ')
                    index=df[['Employer ID','Gender']][df['Employer ID']==rn].index[0]
                    print(df.loc[index])
                    break
            elif n=='2':
                print('1. Update Name')
                print('2. Update Department')
                print('3. Update Position')
                print('4. Update DOB')
                print('5. Update Hire Date')
                print('6. Update Address')
                print('7. Update Email')
                print('8. Update Mobile No.')
                print('9. Update Salary')
                while True:
                    u=int(input('Choose a no. : '))
                    if 0<u<10:
                        while True:
                            try:
                                a=input('Enter Employee ID : ')
                                if len(a)==4:
                                    a=int(a[1:])
                                    if 1<=a<=len(df):
                                        break
                                    else:
                                        print('Oops....! This ID Not Exist')
                                else:
                                    print('Oops....! Please Enter Valid ID')
                            except:
                                print('Oops....! Please Enter Valid ID')
                        if u==1:
                            b=input('Enter Name : ')
                            while True:
                                c=input('Enter Gender(M/F) : ')
                                if c=='M' or c=='m' or c=='F' or c=='f':
                                    break
                                else:
                                    print('Oops....! Please Enter Valid Data')
                            df.loc[a-1,'Employee Name']=b
                            df.loc[a-1,'Gender']=c
                            print('Name,Gender Updated....!')
                        elif u==2:
                            while True:
                                b=input('Enter Department : ')
                                df.loc[a-1,'Department']=b
                                print('Department Updated....!')
                                break
                        elif u==3: 
                            b=input('Enter Position : ')
                            df.loc[a-1,'Position']=b
                            print('Position Updated....!')
                            break
                        elif u==4:
                            b=input('Enter DOB(dd/mm/yyyy) : ')
                            df.loc[a-1,'Date of Birth']=b
                            print('DOB Updated....!')
                            break
                        elif u==5:
                            b=input('Enter DOH(dd/mm/yyyy) : ')
                            df.loc[a-1,'Hire Date']=b
                            print('DOH Updated....!')
                            break
                        elif u==6:
                            b=input('Enter Address : ')
                            df.loc[a-1,'Address']=b
                            print('Address Updated....!')
                            break
                        elif u==7:
                            b=input('Enter Email : ')
                            df.loc[a-1,'Email']=b
                            print('Email Updated....!')
                            break
                        elif u==8:
                            while True:
                                try:
                                    b=int(input('Enter Mobile No. : ')) 
                                    l=str(b)     
                                    if len(l)==10:
                                        df.loc[a-1,'Phone Number']=b
                                        print('Mobile No. Updated....!')
                                        break
                                    else:
                                        print('Oops....! Mobile No. is Inncorrect')
                                except:
                                    print('Oops....! Please Enter Valid Mobile No.')
                            break
                        elif u==9:
                            b=float(input('Enter Salary: '))
                            df.loc[a-1,'Salary']=b
                            print('Salary Updated....!')
                            break
                        else:
                            print('Please Enter Valid Value')
                        df.to_csv(r'EmployeeData.csv',index=False)
            elif n=='3':
                a=df.iloc[-1,0]
                a=int(a[1:])
                a=a+1
                a='E0'+str(a)
                while True:
                    b=input('Enter Employee Name : ')
                    if b:
                        try:
                            if int(b):
                                print('Oops....! Please Enter Valid Name')
                        except:
                            break
                    if b==0:
                        print('Oops....! Please Enter Valid Name')
                    else:    
                        print('Oops....! Name is Empty')
                while True:
                    c=input('Enter Gender(M/F) : ')
                    if c=='M' or c=='m':
                        c='M'
                        break
                    elif c=='F' or c=='f':
                        c='F'
                        break
                    else:
                        print('Oops....! Please Enter Valid Data')
                d=input('Enter Department : ')
                e=input('Enter Position : ')
                f=input('Enter DOB(dd/mm/yyyy) : ')
                g=input('Enter DOH(dd/mm/yyyy) : ')
                h=input('Enter Address : ')
                i=input('Enter Email : ')
                while True:
                    try:
                        j=int(input('Enter Mobile No. : ')) 
                        l=str(j)     
                        if len(l)==10:
                            break
                        else:
                            print('Oops....! Mobile No. is Inncorrect')
                    except:
                        print('Oops....! Please Enter Valid Mobile No.')
                while True:
                    try:
                        k=float(input('Enter Salary: '))
                        k=str(k)
                        break
                    except:
                        print('Please Enter Valid Value')
                n=[a,b,c,d,e,f,g,h,i,j,k]
                df.loc[-1]=n
                df.reset_index(drop=True,inplace=True)
                print('Record Added....!')

            df.to_csv(r'EmployeeData.csv',index=False)
                                                                      
        #Management Section
        elif n=='3':
            print("Under Development")

        #Exit
        elif n=='4':
            break
        else:
            print('Please Enter Valid Value')

main()
                

        
