def faculty(x):
    x_fac=1
    for ii in range(x):
        x_fac=x_fac*(ii+1)
    return(x_fac)

def binomial_coefficient(n,k):

    #Ueberpruefen ob n und k beide positiv sind und ob sie ganze Zahlen sind
    if n<0 or k<0 or isinstance(n,float) or isinstance(k,float):
        print ("Fehler")
    
    else:

        result= faculty(n)/faculty(k)/faculty(n-k)
    return (result)


