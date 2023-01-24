import time
LHS=[]
RHS=[]
FACTS=[]
GOALS=[]
usedrules=[]
finish=0
iteration=1
fi= ""
fo = ""

def TakeInput ():       #function to take input
    global LHS
    global RHS
    global FACTS
    global GOALS
    global fo
    global fi

    filename = input("Name of the input file: ")
    fi = open(filename, "r")
    filename2 = input("Name of the output file: ")
    fo = open(filename2, "w")
    print("\n\n")

    #BEGINS TAKING RULES IN INPUT
    i=0
    goaway=0
    currentrule=[]  #rule in current line
    currentline=[]  #lhs + rhs in current line

    for line in fi:
        if i>=3 and goaway==0:  #skip first two lines and skip lines if rules are finished
            if(line=="2) Facts\n"):     #break when you finish rules
                goaway=1
            if goaway!=1:
                for word in line.split(): #take every word in input
                    if word=="//":  #when you get // it means you've finished to take rule and rules goals
                        break   
                    else:
                        currentline.append(word)    #add word to currentline

                for j in range (1,len(currentline)):        #put each word, except first one which is goal, in rules
                    currentrule.append(currentline[j])     #insert rules that lead to the goal
                
                if currentline:
                    LHS.append(currentrule)  #insert 
                    RHS.append(currentline[0])      #insert goal of the rule in list of rules' goals
                currentrule=[]     #empty currentrule
                currentline=[]      #empty currentline
        i=i+1
    #FINISHES TAKING RULES IN INPUT, everything works


    #BEGINS TAKING FACTS IN INPUT
    fi.close()
    fi = open(filename, "r")
    gettingfacts=0


    for line in fi:
        if gettingfacts==1:
            for word in line.split():
                FACTS.append(word)
            gettingfacts=0

        if line=="2) Facts\n":
            gettingfacts=1


    #FINISHES TAKING FACTS IN INPUT, everything works


    #BEGINS TAKING GOAL IN INPUT

    fi.close()
    fi = open(filename, "r")
    gettinggoal=0

    for line in fi:
        if gettinggoal==1:
            for word in line.split():
                GOALS.append(word)
            gettinggoal=0
        
        if line=="3) Goal\n":
            gettinggoal=1



    #FINISHES TAKING GOAL IN INPUT
    


def PrintData():        

    global GOALS

    print("Part 1. Data\n")
    print("Part 1. Data\n", file=fo)



    #begins printing rules

    print("  1) Rules")
    print("  1) Rules", file=fo)

    for i in range(0,len(LHS)):
        print("     R", i+1, ": ", sep='', end='')
        print("     R", i+1, ": ", sep='', end='', file=fo)

        for j in range(0,len(LHS[i])):
            if j<=len(LHS[i])-2 and len(LHS[i])!=1:
                print(LHS[i][j],", ", end='', sep='')
                print(LHS[i][j],", ", end='', sep='', file=fo)

            else:
                print(LHS[i][j]," -> ", RHS[i], sep='')
                print(LHS[i][j]," -> ", RHS[i], sep='', file=fo)


    #finishes printing rules

    #begins printing facts

    print("  2) Facts ", sep='', end='')
    print("  2) Facts ", sep='', end='', file=fo)

    for i in range(0,len(FACTS)):
        if i<=len(FACTS)-2 and len(FACTS)!=1:
            print(FACTS[i], ", ", sep='', end='') 
            print(FACTS[i], ", ", sep='', end='', file=fo) 

        else:
            print(FACTS[i],".", sep='')
            print(FACTS[i],".", sep='', file=fo)


    #finishes printing facts

    #begins printing goal

    print("  3) Goal ", sep='', end='')
    print("  3) Goal ", sep='', end='', file=fo)

    print(GOALS[0],".\n", sep='')
    print(GOALS[0],".\n", sep='', file=fo)

    #finishes printing goal




def PrintResults():
    print("PART 3. Results")
    print("PART 3. Results", file=fo)

    
    if finish==1:
        if iteration>1:
            print("  1) Goal ", GOALS[0], " achieved.", sep='')
            print("  1) Goal ", GOALS[0], " achieved.", sep='', file=fo)

            print("  2) Path ",sep='', end='')
            print("  2) Path ",sep='', end='', file=fo)

            for i in range(0,len(usedrules)):
                print("R",usedrules[i]+1, ", " if i<=len(usedrules)-2 and len(usedrules)>1 else ".", sep='', end='')
                print("R",usedrules[i]+1, ", " if i<=len(usedrules)-2 and len(usedrules)>1 else ".", sep='', end='', file=fo)

        else: 
            print("  Goal ", GOALS[0], " in facts. Empty Path.")
            print("  Goal ", GOALS[0], " in facts. Empty Path.", file=fo)


    else:
        print("  Goal not achieved. Empty path")
        print("  Goal not achieved. Empty path", file=fo)








def FCAlgorithm():

    print("PART 2. Trace\n")
    print("PART 2. Trace\n", file=fo)

    global usedrules
    global finish
    global iteration


    k=0     #rules counter
    newFACTS=[]
    apprules=[]     #already applied rules
    lr = len(LHS)
    newit=0         #flag to say whether to write "ITEARATION" or not
    goon=0
    finish=0
    pn=0

    for i in range(0,lr): #set applied rules to 0 for each rule; 0 not applied, 1 applied
        apprules.append(0)


    if GOALS[0] in FACTS:
        finish=1
        return

    while(k<lr):

        goon=0

        if(pn==1):
            print("\n")
            print("\n", file=fo)

        pn=0

        if finish==1:
            break

        goon=0

        if newit==0:
            print("  ITERATION ", iteration, sep='')
            print("  ITERATION ", iteration, sep='', file=fo)

        newit=1     #set to 1, to avoid writing ITERATION everytime you check a rule

        #printing Rk+1:X->Y
        print("    R",k+1,":", sep='',end='')
        print("    R",k+1,":", sep='',end='', file=fo)

        for i in range(0,len(LHS[k])):
            print(LHS[k][i], "," if i<=len(LHS[k])-2 and len(LHS[k])!=1 else "->", end='', sep='')
            print(LHS[k][i], "," if i<=len(LHS[k])-2 and len(LHS[k])!=1 else "->", end='', sep='', file=fo)

        print(RHS[k], end='', sep='')
        print(RHS[k], end='', sep='', file=fo)


        if apprules[k]==1:      #check if rule has already been applied
            print(" skip, because flag1 raised.")
            print(" skip, because flag1 raised.", file=fo)

            goon=1
            k=k+1   #go next rule
            if(k==lr):
                        print("")
                        print("", file=fo)

                        return

        if apprules[k]==2 and goon==0:      #check if it's already been checked that RHS is in facts
            goon=1
            print(" skip, because flag2 raised.")
            print(" skip, because flag2 raised.", file=fo)

            k=k+1   #go next rule
            if(k==lr):
                        print("")
                        print("", file=fo)

                        return
        
        if apprules[k]==0 and goon==0:  #if rule hasn't been applied yet
            check=0

            for i in range(0,len(LHS[k])):       

                if (LHS[k][i] not in FACTS and LHS[k][i] not in newFACTS) and goon==0:      #fix this: when you go to next rule, i has to go back to 0
                    print(" not applied, because of lacking ", LHS[k][i], ".", sep='')
                    print(" not applied, because of lacking ", LHS[k][i], ".", sep='', file=fo)

                    k=k+1
                    goon=1
                    if(k==lr):
                        print("")
                        print("", file=fo)
                        return
                    break

                elif (LHS[k][i] in FACTS or LHS[k][i] in newFACTS) and goon==0:
                    check+=1
                
            if check==len(LHS[k]) and goon==0:      #if we have all the facts to apply the rule
                if RHS[k] in FACTS or RHS[k] in newFACTS:
                    print(" not applied, because RHS in facts. Raise flag2.")
                    print(" not applied, because RHS in facts. Raise flag2.", file=fo)

                    apprules[k]=2
                    k=k+1
                    if(k==lr):
                        print("")
                        print("", file=fo)

                        return
                else:
                    newFACTS.append(RHS[k])
                    apprules[k]=1
                    usedrules.append(k)
                    print(" apply. Raise flag1. Facts ", sep='', end='')
                    print(" apply. Raise flag1. Facts ", sep='', end='', file=fo)

                    for i in range(0,len(FACTS)):
                        print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else " and ", sep='', end='')
                        print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else " and ", sep='', end='', file=fo)

                    for i in range(0,len(newFACTS)):
                        print(newFACTS[i], ", " if i<=len(newFACTS)-2 and len(newFACTS)!=1 else ".", sep='', end='')
                        print(newFACTS[i], ", " if i<=len(newFACTS)-2 and len(newFACTS)!=1 else ".", sep='', end='', file=fo)


                    check2=0
                    for i in range(0,len(FACTS)):
                        if FACTS[i] in GOALS:
                            check2+=1
                    for i in range(0,len(newFACTS)):
                        if newFACTS[i] in GOALS:
                            check2+=1

                    if check2==len(GOALS):
                        print(" Goal Achieved.")
                        print(" Goal Achieved.", file=fo)

                        finish=1
                        

                    k=0
                    newit=0
                    iteration+=1
                    pn=1





TakeInput()
PrintData()
FCAlgorithm()
PrintResults()