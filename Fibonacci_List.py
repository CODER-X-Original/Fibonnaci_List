number_of_terms = int(input(" number of terms : "))

def fibo():
    x = 0
    y = 1
    tmp = 0
    counter = 0   
    while counter < number_of_terms:
        print(x)
        tmp = x+y
        x = y
        y = tmp
        counter = counter + 1

fibo()