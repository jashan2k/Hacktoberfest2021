"""
In this puzzle we are given Two water jugs of diffrent sizes.
We are then given a quantity lesser than or equal to the size of the two jugs 
and our goal is to find our automate the process of getting the desired quantity.

rule:
1.each fill,transfer and empty process is a step
2.we cannot fill until a certain quantity and just add them i.e if a jug is filler then it is filled to the fullest, 
in transfer, we have to transfer water until either jugs become full or empty
and in empty we have to empty the entire quantity of the jug.
"""
#getting the required variables
print("Please ensure that u give a natural number as the size")
i=int(input("Enter the quantity of jug1 in litres"))
j=int(input("Enter the quantity of jug2 in litres"))
n=int(input("Enter the required quantity(in litres) that u want to get"))
if i+j<n and i==j :
    print("The given quantity cannot be achieved with %d and %d litre jugs"%(i,j))
elif i%2==0 and j%2==0 and n%2!=0:
    print("The given quantity cannot be achieved with %d and %d litre jugs"%(i,j))
elif i+j==n:
    #if the sum gets us the desired quantity
    print("fill both of them")
else:
    #loop for  filling, transfering and emptying
    x=0
    y=0
    t=0
    step=1
    while y+x!=n and x!=n and y !=n and t<10:
        t+=1
        if x==0:
            #if the first jug is empty fill it
            x=i
            print("Step - %d"%(step))
            step+=1
            print("fill %d litres jug"%(i))
        if y==j:
            #if the second jug is full empty it
            y=0
            print("Step - %d"%(step))
            step+=1
            print("empty %d litres jug" %(j))
            if x>j-y and y+x!=n and x!=n and y !=n :
                #if 1st jug has more litres that 2nd jug original quantity - 2nd jug present or actual quantity
                #transfering water from 1st jug to 2nd jug
                y+=j
                x-=j
                print("Step - %d"%(step))
                step+=1
                print("Tansfer %d litres jug to %d litres jug"%(i,j))
            elif y+x!=n and x!=n and y !=n :
                #transfering water from 1st jug to 2nd jug
                y+=x
                x-=y
                print("Step - %d"%(step))
                step+=1
                print("Tansfer %d litres jug to %d litres jug"%(i,j))
        elif x>j-y and y+x!=n and x!=n and y !=n :
            #here y is not emptied yet
            #transfering water from 1st jug to 2nd jug
            z=j-y
            y+=z
            x-=z
            print("Step - %d"%(step))
            step+=1
            print("Tansfer %d litres jug to %d litres jug"%(i,j))
        elif y+x!=n and x!=n and y !=n :
            #transfering water from 1st jug to 2nd jug
            z=x
            y+=z
            x-=z
            print("Step - %d"%(step))
            step+=1
            print("Tansfer %d litres to %d litres"%(i,j))
    print("Voila now u have a jug with %d litres i.e the sum of jug1 and jug2 gives us %d litres"%(n,n))        
        

            
