import random  
NUMBER_OF_BULLSHIT = 10


with open('text') as f:
    content = f.readlines()


clause = []
counter =0
for i in content:
    if not len(i)<20:
        ti = i.split('\\',500)
        for j in ti:
            if len(j)>1:
                clause = clause+[j]
                #print counter,' : ',j
                counter = counter+1

my_randoms=[]  
  
for i in range (NUMBER_OF_BULLSHIT):    
    my_randoms.append(random.randrange(0,len(clause)))    

#print my_randoms
finaloutput=''

for i in range (len(my_randoms)):
    finaloutput = finaloutput + clause[my_randoms[i]]
    
    if random.randrange(0,3) == 0 or i == len(my_randoms)-1:
        finaloutput = finaloutput + '\xE3\x80\x82'
    elif random.randrange(0,3) == 1:
        finaloutput = finaloutput + '\xEF\xBC\x81'
    else:
        finaloutput = finaloutput + '\xEF\xBC\x8C'

print finaloutput

#'\xE3\x80\x82' = 'o'
#'\xEF\xBC\x81' = '!'
#'\xEF\xBC\x8C' = ','
#
#
