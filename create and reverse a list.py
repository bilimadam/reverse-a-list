
print ('Welcome to the bilimadam\'s codes.', end='\n' )
print ('...', end='\n')
print ('...', end='\n')
print ('...', end='\n')

def createbody(x):
    try:
        x.append (int(input('How long do you want to create a list = ')))
        return x
    except ValueError:
         print ('Please give a integer !', end='\n')
         createbody(listsize)

def intcontrol(x):
    try:
        a = int(x)
        return True
    except ValueError:
        return False

def floatcontrol(x):
    try:
        a = float(x)
        return True
    except ValueError:
        return False

def listcreate():
    a = []
    control1 = ''
    
    while (control1 != 'end'):
        control2 = input('Do you want to add a list in list ?''\n''if yes, write \'yes\'''\n''Answer = ')
        if control2 == 'yes':
            a.append(listcreate())
            control1 = input('To finish this section, write \'end\'''\n''if dont want to finish just enter''\n''Answer = ')
            continue
        
        x = input('Input : ')
        fcontrol = floatcontrol(x)
        icontrol = intcontrol(x)
        
        if x == 'True' or x == 'False':
            if x == 'True':
                a.append(True)
            else:
                a.append(False)
        elif icontrol == True:
            a.append(int(x))
        elif fcontrol == True:
            a.append(float(x))
        else:
            a.append(x)
        control1 = input('To finish this section, write \'end\'''\n''if dont want to finish just enter''\n''Answer = ')
    
    return a

def reverser (l):
    if type(l) == list:
        if len(l) != 0:
            for i in range(len(l)):
                if type(l[i]) == list:
                    reverser(l[i])
            return l.reverse()

            
yourlist = []
listsize = []
createbody(listsize)
#print (listsize)

for _ in range (listsize[0]):
    control = input('Do you want to add a list in list ?''\n''if yes, write \'yes\'''\n''Answer = ')
    if control == 'yes':
        yourlist.append(listcreate())
        print('\n', 'Your list now appering like : ', yourlist, '\n')
        continue
    
    x = input('Input : ')
    fcontrol = floatcontrol(x)
    icontrol = intcontrol(x)
        
    if x == 'True' or x == 'False':
        if x == 'True':
            yourlist.append(True)
        else:
            yourlist.append(False)
    elif icontrol == True:
        yourlist.append(int(x))
    elif fcontrol == True: 
        yourlist.append(float(x))
    else:
        yourlist.append(x)
    

print ('\n', 'Yourlist is = ', yourlist, '\n')

reversedlist = yourlist.copy()
reverser(reversedlist)
#print (reversedlist[0])
#print (reversedlist[1])
#print (type(reversedlist))

#for i in range (len(reversedlist)):
#    if type(reversedlist[i]) == list:
#        reverser(reversedlist[i])
                
print ('\n', f'The reversed list is = {reversedlist}', '\n')