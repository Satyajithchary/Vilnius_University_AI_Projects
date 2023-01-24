LHS=[]
RHS=[]
FACTS=[]
NEW_FACTS=[]
GOALS=[]
fi= ""
fo = ""
movecounter=1
new_facts_added=[]
finished=0
amongfacts=0

mystack=[]
usedrules=[]



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

def PrintData():        #function to print data    

    global GOALS

    print("Part 1. Data")
    print("Part 1. Data", file=fo)



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

def PrintResults():
    if finished==0:
        print('\n')
        print('\n', file=fo)

    print("PART 3. Results")
    print("PART 3. Results", file=fo)


    if amongfacts==1:
        print("  Goal ",GOALS[0]," among facts. Empty Path.")
        print("  Goal ",GOALS[0]," among facts. Empty Path.", file=fo)

        return
    
    if finished==0:
        print("  No path.")
        print("  No path.", file=fo)

        return
    
    if finished==1:
        print("  1) Goal ",GOALS[0]," achieved.", sep='') 
        print("  1) Goal ",GOALS[0]," achieved.", sep='', file=fo) 

        print("  2) Path: ",sep='',end='')
        print("  2) Path: ",sep='',end='', file=fo)

        usedrules.reverse()
        for i in range(0,len(usedrules)):
            print("R",usedrules[i]+1, ", " if i<=len(usedrules)-2 and len(usedrules)>1 else ".", sep='', end='')
            print("R",usedrules[i]+1, ", " if i<=len(usedrules)-2 and len(usedrules)>1 else ".", sep='', end='', file=fo)
        return





def bchaining(g, tr):

    global LHS
    global RHS
    global FACTS
    global NEW_FACTS
    global GOALS
    global movecounter
    global new_facts_added
    global finished
    global usedrules
    global amongfacts

    print(" " if movecounter <10 else "", movecounter,") ", sep='', end='')
    print(" " if movecounter <10 else "", movecounter,") ", sep='', end='', file=fo)

    for t in range (0,tr):
        print("-", sep='', end='')
        print("-", sep='', end='', file=fo)

    print("Goal ",g, ". ", sep='' ,end='')
    print("Goal ",g, ". ", sep='' ,end='', file=fo)

    movecounter=movecounter+1

    atr = 0


    if g in FACTS:
        print("Fact (initial), as facts are ", sep='' ,end='')
        print("Fact (initial), as facts are ", sep='' ,end='', file=fo)

        for i in range(0,len(FACTS)):
            print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else ".", sep='', end='')
            print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else ".", sep='', end='', file=fo)

        print(" ",end='')
        print(" ",end='', file=fo)

        if g==GOALS[0]:
            amongfacts=1
        return True
    
    if g in NEW_FACTS:
        print("Fact (earlier inferred), as facts ", sep='' ,end='')
        print("Fact (earlier inferred), as facts ", sep='' ,end='', file=fo)

        for i in range(0,len(FACTS)):
            print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else " and ", sep='', end='')
            print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else " and ", sep='', end='', file=fo)

        for i in range(0,len(NEW_FACTS)):
            print(NEW_FACTS[i], ", " if i<=len(NEW_FACTS)-2 and len(NEW_FACTS)!=1 else ". ", sep='', end='')
            print(NEW_FACTS[i], ", " if i<=len(NEW_FACTS)-2 and len(NEW_FACTS)!=1 else ". ", sep='', end='', file=fo)

        if g==GOALS[0]:
            finished=1
        return True
    
    if g in mystack:
        print("Cycle. ", end='')
        print("Cycle. ", end='', file=fo)

        return False
    
    mystack.insert(0, g)

    for rule in range(0,len(LHS)):
        if RHS[rule]==g:
            if atr==1:
                print(" " if movecounter <10 else "", movecounter,") ", sep='', end='')
                print(" " if movecounter <10 else "", movecounter,") ", sep='', end='', file=fo)

                for t in range (0,tr):
                    print("-", sep='', end='')
                    print("-", sep='', end='', file=fo)

                print("Goal ",g, ". ", sep='' ,end='')
                print("Goal ",g, ". ", sep='' ,end='', file=fo)

                movecounter=movecounter+1
            atr=1
            print("Find R", rule+1, ":", sep='', end='')
            print("Find R", rule+1, ":", sep='', end='', file=fo)



            for j in range(0,len(LHS[rule])):
                if j<=len(LHS[rule])-2 and len(LHS[rule])!=1:
                    print(LHS[rule][j],",", end='', sep='')
                    print(LHS[rule][j],",", end='', sep='', file=fo)

                else:
                    print(LHS[rule][j],"->", RHS[rule], end='', sep='')
                    print(LHS[rule][j],"->", RHS[rule], end='', sep='', file=fo)


            
            newgoals=LHS[rule]

            print(". New goals ", end='', sep='', file=fo)
            print(". New goals ", end='', sep='', file=fo)


            for i in range(0,len(newgoals)):
                print(newgoals[i], ", " if i<=len(newgoals)-2 and len(newgoals)!=1 else ".", sep='',end='')
                print(newgoals[i], ", " if i<=len(newgoals)-2 and len(newgoals)!=1 else ".", sep='',end='', file=fo)

            print()
            print('',file=fo)


            fake_newgoals=[]
            for fng in range(0,len(newgoals)):
                fake_newgoals.append(newgoals[fng])


            for ng in range(len(fake_newgoals)):
                if ng>0:
                    print()
                    print('', file=fo)

                val=bchaining(fake_newgoals[ng], tr+1)
                if val==True:
                    newgoals.remove(fake_newgoals[ng])
                else:
                    break
                


            print("Back", end='', sep='')
            if len(newgoals)==0:
                usedrules.insert(0,rule)
                print(", OK.")
                print(", OK.", file=fo)

                #NEW_FACTS.insert(0,g)
                NEW_FACTS.append(g)
                new_facts_added.insert(0,g)
                print(" " if movecounter <10 else "", movecounter,") ", sep='', end='')
                print(" " if movecounter <10 else "", movecounter,") ", sep='', end='', file=fo)

                for t in range (0,tr):
                    print("-", sep='', end='')
                    print("-", sep='', end='', file=fo)

                print("Goal ",g, ". ", sep='' ,end='')
                print("Goal ",g, ". ", sep='' ,end='', file=fo)

                movecounter=movecounter+1

            else:
                if len(usedrules)>0:    
                    usedrules.pop(0)
                print(" FAIL.")
                print(" FAIL.", file=fo)

                

            if g in NEW_FACTS:
                print("Fact (presently inferred). FACTS ", sep='' ,end='')
                print("Fact (presently inferred). FACTS ", sep='' ,end='', file=fo)

                for i in range(0,len(FACTS)):
                    print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else " and ", sep='', end='')
                    print(FACTS[i], ", " if i<=len(FACTS)-2 and len(FACTS)!=1 else " and ", sep='', end='', file=fo)

                for i in range(0,len(NEW_FACTS)):
                    print(NEW_FACTS[i], ", " if i<=len(NEW_FACTS)-2 and len(NEW_FACTS)!=1 else ". ", sep='', end='')
                    print(NEW_FACTS[i], ", " if i<=len(NEW_FACTS)-2 and len(NEW_FACTS)!=1 else ". ", sep='', end='', file=fo)

                if (g==GOALS[0]):
                    print("OK.\n")
                    print("OK.\n", file=fo)

                    finished=1
                mystack.remove(g)
                return True
            
            # else:
            #     print("FAIL.")
    
    if(atr==0):
        print("No rules. ", end='', sep='')
        print("No rules. ", end='', sep='', file=fo)

        if len(usedrules)>0 :    
            usedrules.pop(0)
        mystack.remove(g)
        for nfa in range(0,len(new_facts_added)):
            if new_facts_added[nfa] in NEW_FACTS:
                NEW_FACTS.remove(new_facts_added[nfa])
        if g==GOALS[0]:
            finished=0
        return False
    
    if(atr==1):
        print(" " if movecounter <10 else "", movecounter,") ", sep='', end='')
        print(" " if movecounter <10 else "", movecounter,") ", sep='', end='', file=fo)

        for t in range (0,tr):
            print("-", sep='', end='')
            print("-", sep='', end='', file=fo)

        print("Goal ",g, ". ", sep='' ,end='')
        print("Goal ",g, ". ", sep='' ,end='', file=fo)

        movecounter=movecounter+1
        print("No more rules. ", end='', sep='')
        print("No more rules. ", end='', sep='', file=fo)

        if len(usedrules)>0:    
            usedrules.pop(0)
        mystack.remove(g)
        for nfa in range(0,len(new_facts_added)):
            if new_facts_added[nfa] in NEW_FACTS:
                NEW_FACTS.remove(new_facts_added[nfa])
        if g==GOALS[0]:
            finished=0
        return False


TakeInput()
PrintData()
print("PART 2. Trace")
print("PART 2. Trace", file=fo)
bchaining(GOALS[0], 0)
PrintResults()


