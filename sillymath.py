right_count=0

l=[]
for n30 in range(11):
    for n20 in range(21):
        for n10 in range(31):
            sum=10*n10+20*n20+30*n30
            if sum==600:
                right_count+=1
                l.append([n10, n20, n30])
                
            
        
            
print(l)
