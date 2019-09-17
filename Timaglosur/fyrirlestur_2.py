# bool segð, segð(expression) skilar gildi
3>2 #skilar gildinni true
#notaðaar í if setningum
num= int(input('Sláðu inn tölu: ')) # fæ streng
if num == 0:
    print('Zero')
elif num == 1:
    print('One')
else:
    print('Something else')



if num ==0 or num==1: #aðeins önnur þarf að vera true til að heildar verði true
    print('Zero or one')



num1=int(input('Sláðu inn tölu: '))
num2=int(input('Sláðu inn tölu: '))
   
if num1 ==1 and num==2: #allir hlutar þurfa að vera true
    print('One and two')
else:
    print('Glatað')

if not num1 ==1 and num==2: #ef bæði verður true þá kemur samt false því if not
    print('One and two')
else:
    print('Annað')
    
