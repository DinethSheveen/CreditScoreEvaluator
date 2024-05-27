#CREATING AND INITIALIZING VARIABLES
user=""
credit_pass=0
defer=0
fail=0
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0
fo=None
progress_list=[]
trailer_list=[]
retriever_list=[]
exclude_list=[]
tot_outcomes=0

fo=open("Evaluation_Sheet.txt","w")       #OPENING THE TEXT FILE

#MAIN PROGRAM

retry="y"
while(retry=="y"):
    display= "Progression Sheet"
    print()
    print(display.center(50,"*"))
    try:                                                            #EXCEPTION HANDLING       
        credit_pass=int(input("Enter your credits at pass :"))   
        if(credit_pass not in[0,20,40,60,80,100,120]):              #CHECKING WHTHER THE MARK ENTERED IS WITHIN THE RANGE 
            raise Exception
       
        defer=int(input("Enter your credits at defer :"))
        if(defer not in[0,20,40,60,80,100,120] ):               
            raise Exception

        fail=int(input("Enter your credits at fail :"))
        if(fail not in[0,20,40,60,80,100,120]):                    
            raise Exception

    except ValueError:                    #PRINTING A MESSAGE IF THE DATA TYPE IS INVALID
        print("Integer Required.")
        continue
    
    except Exception:
        print("Out of range.")             #PRINTING A MESSAGE IF THE MARK ENTERED IS OUT OF RANGE 
        continue
    
    #CHECKING FOR THE MARK INTERVALS
    if(credit_pass==120 and defer==0 and fail==0):              
        pass_status="Progress"
        progress_count+=1
        progress_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==100 and defer==20 and fail==0):
        pass_status="Progress(module trailer)"
        trailer_count+=1
        trailer_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==100 and defer==0 and fail==20):
        pass_status="Progress(module trailer)"
        trailer_count+=1
        trailer_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==80 and (defer==0 or defer==20 or defer==40) and (fail==0 or fail==20 or fail==40)):
        pass_status="Module retriever"
        retriever_count+=1
        retriever_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==60 and (defer==0 or defer==20 or defer==40 or defer==60) and (fail==0 or fail==20 or fail==40 or fail==60)):
        pass_status="Module retriever"
        retriever_count+=1
        retriever_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==40 and (defer==20 or defer==40 or defer==60 or defer==80) and (fail==0 or fail==20 or fail==40 or fail==60)):
        pass_status="Module retriever"
        retriever_count+=1
        retriever_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==40 and defer==0 and fail==80):
        pass_status="Exclude"
        exclude_count+=1
        exclude_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==20 and (defer==100 or defer==80 or defer==60 or defer==40) and (fail==0 or fail==20 or fail==40 or fail==60)):
        pass_status="Module retriever"
        retriever_count+=1
        retriever_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==20 and (defer==20 or defer==0) and (fail==80 or fail==100)):
        pass_status="Exclude"
        exclude_count+=1
        exclude_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==0 and (defer==120 or defer==100 or defer==80 or defer==60) and (fail==0 or fail==20 or fail==40 or fail==60)):
        pass_status="Module retriever"
        retriever_count+=1
        retriever_list.append([credit_pass,defer,fail])
        
    elif(credit_pass==0 and (defer==40 or defer==20 or defer==0) and (fail==80 or fail==100 or fail==120)):
        pass_status="Exclude"
        exclude_count+=1
        exclude_list.append([credit_pass,defer,fail])
        
    try:
        total=credit_pass+defer+fail
        if(total==120):
            print(end="")
        else:
            raise Exception
        
    except Exception:
        print("Total incorrect.")
        continue

    if(user.lower()=='student'):
        print(pass_status)
        break
    
    print(pass_status)    
    print("-"*100) #SEPERATING DATA SETS FROM ONE ANOTHER

    #ACCESSING THE TEXT FILE
    if(pass_status=="Progress"):
        fo.write(pass_status)
        fo.write(" - ")
        fo.write(str(progress_list[progress_count-1]))
        fo.write("\n")
                
    if(pass_status=="Progress(module trailer)"):
        fo.write(pass_status)
        fo.write(" - ")
        fo.write(str(trailer_list[trailer_count-1]))
        fo.write("\n")

    if(pass_status=="Module retriever"):
        fo.write(pass_status)
        fo.write(" - ")
        fo.write(str(retriever_list[retriever_count-1]))
        fo.write("\n")

    if(pass_status=="Exclude"):
        fo.write(pass_status)
        fo.write(" - ")
        fo.write(str(exclude_list[exclude_count-1]))
        fo.write("\n")
        
    retry=input("Would you like to enter another set of data?\nEnter 'y' for yes 'q' to quit and view results :")
    retry=retry.lower()
    while not(retry=='y' or retry=='q'):
        print("Please type 'y' or 'q'.")
        retry=input("Would you like to enter another set of data?\nEnter 'y' for yes 'q' to quit and view results :")
        
if(retry=="q"):
    from graphics import *
    def window(progress_count,trailer_count,retriever_count,exclude_count):
        win=GraphWin("Histogram Results",560,800) #OPENING THE WINDOW WITH THE DECLARED WIDTH AND HEIGHT 
        win.setBackground("mint cream")   #SETTING THE BACKGROUND COLOUR TO BLACK

        heading=Text(Point(150,50),"Histogram Results")  #DRAWING A TEXT IN THE WINDOW
        heading.setStyle("bold")    #SETTING FONT STYLE TO BOLD
        heading.draw(win)                 #DRAWING THE TEXT ON THE WINDOW 

        hr_line=Line(Point(20,550),Point(520,550))   #DRAWING THE HORIZONTAL AXIS (X AXIS)
        hr_line.draw(win)

        bar1=Rectangle(Point(50,550),Point(150,550-(progress_count*10)))     #INCREASING THE HEIGHT OF THE BARS
        bar1.setFill("green")                          #FILLING THE BARS WITH GREY COLOUR
        bar1.draw(win)

        msg2=Text(Point(100,565),"Progress")     #DISPLAYING THE PROGRESSING TYPE BELOW THE RESPECTIVE BAR 
        msg2.draw(win)

        bar2=Rectangle(Point(160,550),Point(260,550-(trailer_count*10)))
        bar2.setFill("gold")
        bar2.draw(win)

        msg3=Text(Point(205,565),"Trailer")
        msg3.draw(win)

        bar3=Rectangle(Point(270,550),Point(370,550-(retriever_count*10)))
        bar3.setFill("silver")
        bar3.draw(win)

        msg4=Text(Point(320,565),"Retriever")
        msg4.draw(win)

        bar4=Rectangle(Point(380,550),Point(480,550-(exclude_count*10)))
        bar4.setFill("grey")
        bar4.draw(win)

        msg5=Text(Point(425,565),"Excluded")
        msg5.draw(win)

        progress_result_count=Text(Point(100,550-(progress_count*10)-15),progress_count)        #DISPLAYING THE PORGRESS AMOUNT ABOVE THE RESPECTIVE BAR 
        progress_result_count.draw(win)

        trailer_result_count=Text(Point(205,550-(trailer_count*10)-15),trailer_count)
        trailer_result_count.draw(win)

        retriever_result_count=Text(Point(320,550-(retriever_count*10)-15),retriever_count)
        retriever_result_count.draw(win)

        exclude_result_count=Text(Point(425,550-(exclude_count*10)-15),exclude_count)
        exclude_result_count.draw(win)

        tot_outcomes=progress_count+trailer_count+retriever_count+exclude_count
        msg6=Text(Point(50,600),tot_outcomes)
        msg6.draw(win)

        msg7=Text(Point(140,600),"Outcomes in Total.")
        msg7.draw(win)

        win.getMouse()                   # WINDOW WILL DISSAPPEAR WITH A SINGLE CLICK ON THE WINDOW 
        win.close()
    window(progress_count,trailer_count,retriever_count,exclude_count)
    
    print("Progress",progress_list)
    print("Module Trailer",trailer_list)
    print("Module Retriever -",retriever_list)
    print("Exclude -",exclude_list)
  
#CLOSING THE TEXT FILE
fo.close()
