from typing import NamedTuple


class Rule(NamedTuple):
    number: int
    consequent: chr
    antecedents: list
    flag1: bool
    flag2: bool

    def __getitem__(self, item):
        if isinstance(item, int):
            item = self._fields[item]
        return getattr(self, item)

    def get(self, item, default=None):
        try:
            return self[item]
        except (KeyError, AttributeError, IndexError):
            return default



rules = []
facts = []
goal = ''
path = []
initialFacts = []
newFacts = []

def checkIfGoalAchieved():
    if goal in facts:
        return True
    return False

def checkRules():
    iterationTrace = ""
    for rule in rules:
        iterationTrace += "\t\tR"+str(rule["number"])+":"+','.join(rule["antecedents"])+"->"+rule["consequent"]+" "
        if all(elem in facts for elem in rule["antecedents"]):
            if not rule["flag1"]:
                if not rule["flag2"]:
                    if rule["consequent"] in facts:
                        rules[rule["number"]-1] = rule._replace(flag2=True)
                        iterationTrace += "not applied, because RHS in facts. Raise flag2.\n"
                        continue
                    else:
                        rules[rule["number"]-1] = rule._replace(flag1=True)
                        facts.append(rule["consequent"])
                        newFacts.append(rule["consequent"])
                        path.append("R"+str(rule["number"]))
                        iterationTrace += "apply. Raise flag1. Facts " + ','.join(initialFacts)+ " and "+ ','.join(newFacts) + "\n"
                        return True, iterationTrace
                else:
                    iterationTrace += "skip, because flag2 raised.\n"
                    continue
            else:
                iterationTrace += "skip, because flag1 raised. \n"
                continue
        else:
            iterationTrace += "not applied, because of lacking " + ','.join(set(rule["antecedents"])-set(facts)) + ".\n"
            continue
    
    return False, iterationTrace


def doForwardChaining(f):
    result_text = ""
    if checkIfGoalAchieved(): 
        result_text += ("\nPart 3.  Results \n")
        result_text += ("\t\t Goal "+ goal +" is in facts. Path is empty")
        f.write(result_text)
        return
    if len(rules) == 0:
        return
    result_text += ("\nPart 2.  Trace \n")
    for i in range(len(rules)):
        result_text += ("\n\tITERATION "+str(i+1)+"\n")
        applied, iterationTrace =  checkRules()
        result_text += iterationTrace
        if not applied:
            result_text += ("\nPart 3.  Results \n")
            result_text += ("\t\t Goal "+ goal +" is not achievable. Path is none")
            break 
        if checkIfGoalAchieved():
            result_text += "\t\tGoal achieved\n"
            result_text += ("\nPart 3.  Results \n")
            result_text += ("\t1)\t Goal "+ goal +" achieved.\n")
            result_text += ("\t2)\t Path "+ ', '.join(path) +".\n")
            break

    f.write(result_text)

def readRules(data):
    for i in range(len(data)):
        if len(data[i]) < 3:
            return data[i+1:]
        else:
            l = list(data[i].replace(" ", ""))
            if l[0] in facts:
                flag2 = True
            else:
                flag2 = False
            rule = Rule(i+1, l[0], l[1:], False, flag2)
            rules.append(rule)

def readFacts(data):
    if data[0][:2]=="2)":
        l = list(data[1].replace(" ",""))
        for fact in l:
            facts.append(fact)
            initialFacts.append(fact)
    return data[2:]

def readGoal(data):
    for i in range(len(data)):
        if data[i][:2]=="3)":
            global goal
            goal = data[i+1][0]
            break


print("Which test file to solve?")
file = str(input())

with open(file, 'r') as f:
    data = f.read().splitlines()

for i in range(len(data)):
    if data[i][:2] == "//":
        continue
    elif data[i][:2] == "1)":
        nextLines = readRules(data[i+1:])
        nextLines = readFacts(nextLines)
        readGoal(nextLines)
        break


def printData(f):
    result_text = ""
    result_text= result_text + ("\nPart 1.  Data \n\t1)\tRules\n")
    for rule in rules:
        result_text += "\t\tR"+str(rule["number"])+":"+','.join(rule["antecedents"])+"->"+rule["consequent"]+"\n"
    result_text += ("\t2)\tFacts "+','.join(facts)+".\n")
    result_text += ("\t3)\tGoal "+goal+".\n")
    f.write(result_text)

f = open("out-forwardChaining.txt", "w")
printData(f)
doForwardChaining(f)
f.close()
print("The results are printed to out-forwardChaining.txt")


