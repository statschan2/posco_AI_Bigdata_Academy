#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open("students.txt","r")

data = f.readlines()

for i in range(0,len(data)) :
    data[i] = data[i].split("\t")

for i in range(0, len(data)) :
    data[i][3] = data[i][3][:2]

for i in range(0, len(data)) :
    data[i].append((int(data[i][2]) + int(data[i][3]))/2)

for i in range(0, len(data)) :
    if data[i][4] >= 90 :
        data[i].append("A")
    elif data[i][4] >= 80 :
        data[i].append("B")
    elif data[i][4] >= 70 :
        data[i].append("C")
    elif data[i][4] >= 60 :
        data[i].append("D")
    else : 
        data[i].append("F")

data.sort(key = lambda e : e[5])

print("%+10s %+15s %10s %10s %10s %10s" %("Student","Name","Midterm","Final","Average","Grade"))
print("-"*70)
for i in range(len(data)) :
    print("%+10s %+15s %8s %11s %9s %10s" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))


# In[2]:


def show_function() :
    data.sort(key = lambda e : e[4], reverse = True)
    
    print("%+10s %+15s %10s %10s %10s %10s" %("Student","Name","Midterm","Final","Average","Grade"))
    print("-"*70)
    for i in range(len(data)) :
        print("%+10s %+15s %8s %11s %9s %10s" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
    
def search_function() :
    stu_id = input("Student ID : ")
    
    for i in range(0, len(data)) :
        if data[i][0] == stu_id :
            print("%+10s %+15s %10s %10s %10s %10s" %("Student","Name","Midterm","Final","Average","Grade"))
            print("-"*70)
            print("%+10s %+15s %8s %11s %9s %10s" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
            return
    
    print("NO SUCH PERSON.")
    
def changescore_function() :
    stu_id = input("Student ID : ")
    
    for i in range(0, len(data)) :
        if data[i][0] == stu_id :
            question = input("Mid/Final? ")
            if question == "mid" :
                newscore = int(input("Input new score : "))
                if (newscore < 101) & (newscore >= 0) :
                    print("%+10s %+15s %10s %10s %10s %10s" %("Student","Name","Midterm","Final","Average","Grade"))
                    print("-"*70)
                    print("%+10s %+15s %8s %11s %9s %10s" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
                    
                    data[i][2] = newscore
                    data[i][4] = (int(data[i][2]) + int(data[i][3]))/2
                    
                    if data[i][4] >= 90 :
                        data[i][5] = "A"
                    elif data[i][4] >= 80 :
                        data[i][5] = "B"
                    elif data[i][4] >= 70 :
                        data[i][5] = "C"
                    elif data[i][4] >= 60 :
                        data[i][5] = "D"
                    else : 
                        data[i][5] = "F"
                    
                    print("Score changed.")
                    print("%+10s %+15s %8s %11s %9s %10s" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
            elif question == "final" :
                newscore = int(input("Input new score : "))
                if (newscore < 101) & (newscore >= 0) :
                    print("%+10s %+15s %10s %10s %10s %10s" %("Student","Name","Midterm","Final","Average","Grade"))
                    print("-"*70)
                    print("%+10s %+15s %8s %11s %9s %10s" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
                    
                    data[i][3] = newscore
                    data[i][4] = (int(data[i][2]) + int(data[i][3]))/2
                    
                    if data[i][4] >= 90 :
                        data[i][5] = "A"
                    elif data[i][4] >= 80 :
                        data[i][5] = "B"
                    elif data[i][4] >= 70 :
                        data[i][5] = "C"
                    elif data[i][4] >= 60 :
                        data[i][5] = "D"
                    else : 
                        data[i][5] = "F"
                    
                    print("Score changed.")
                    print("%+10s %+15s %8s %11s %9s %10s" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
            return
                    
    print("NO SUCH PERSON.")
    
def add_function() :
    stu_id = input("Student ID : ")
    
    idlist = []
    for i in range(0,len(data)) :
        idlist.append(data[i][0])
    
    if stu_id not in idlist :
        new_name = input("Name : ")
        new_mid = input("Midterm Score : ")
        new_final = input("Final Score : ")
        new_avg = (int(new_mid) + int(new_final))/2
        if new_avg >= 90 :
            new_grade = "A"
        elif new_avg >= 80 :
            new_grade = "B"
        elif new_avg >= 70 :
            new_grade = "C"
        elif new_avg >= 60 :
            new_grade = "D"
        else : 
            new_grade = "F"
            
        data.append([stu_id,new_name,new_mid,new_final,new_avg,new_grade])
        
        print("Student added.")
        return
    
    print("ALREADY EXISTS.")
    
def searchgrade_function() :
    stu_grade = input("Grade to search : ")
    glist = []
    for i in range(0,len(data)) :
        glist.append(data[i][5])
    
    new_list = []
    if stu_grade in glist :
        
        for i in range(0,len(data)) :
            if data[i][5] == stu_grade :
                new_list.append(data[i])
            else : 
                new_list = new_list

        print("%+10s %+15s %10s %10s %10s %10s" %("Student","Name","Midterm","Final","Average","Grade"))
        print("-"*70)        
        for j in range(0,len(new_list)) :
            print("%+10s %+15s %8s %11s %9s %10s" %(new_list[j][0], new_list[j][1], new_list[j][2], new_list[j][3], new_list[j][4], new_list[j][5]))
        
    elif stu_grade not in ["A","B","C","D","F"] :
        pass
    else :
        return print("NO RESULTS.")
    
def remove_function() :
    if len(data) == 0 :
        print("List is empty.")
        return 0
           
    stu_id = input("Student ID : ")
    
    for i in range(0,len(data)) :
        if data[i][0] == stu_id :
            del data[i]
            print("Student removed.")
            return
    
    print("NO SUCH PERSON.")
    
def quit_function() :
    command = input("Save data?[yes/no] ")
    
    if command == "yes" :
        fname = input("File name : ")
        fname.replace(' ','')
        
        f = open(fname,"w")
        data.sort(key = lambda e : e[4], reverse = True)
        
        for i in range(len(data)) :
            dataset = "%+10s %+15s %10s %10s %10s %10s\n" %(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5])
            f.write(dataset)
        print("$")
    else :
        print("$")
    f.close() 


# In[3]:


while True:
    command = input("# ")
    if command == "show" :
        show_function()
        
    elif command == "search" :
        search_function()
        
    elif command == "changescore" :
        changescore_function()
        
    elif command == "add" :
        add_function()
        
    elif command == "searchgrade" :
        searchgrade_function()
        
    elif command == "remove" :
        remove_function()
    
    elif command == "quit" :
        quit_function()
        break
    else:
        print("wrong input!")

