# Break statement : When a break statement is introduced in a loop then that loops treminate all the iterartion after that break statement.

# continue statement : When a continue statement is introduced in a loop then that particular loop's iteration will be skipped.

for i in range(100) :
    if ( i % 2 == 0 ) :
        continue
    print(i)
    if( i % 100 == 0 ) :
        break

# do-while loop is not present in python, but a do while loop can be created by creating a infinite while loop.

i = 0
while(True) :
    print(i+1) 
    i = i + 1
    if ( i == 100 ) :
        break;