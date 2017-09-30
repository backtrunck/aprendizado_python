

i = raw_input("digite um numero binario: ")

print i

if len([j for j in i if j != '1' and j!='0']) > 0:
	print 'numero binario invalido'
	exit(1)
else :
    
    lista =  [int(j) for j in i]
    lista.reverse()
    numDec = 0
    potencia = 0
    for  potencia,algarismo in list(enumerate(lista)):
	numDec = numDec + (algarismo * (2 ** potencia))

    print "o numero em decimal eh %d \n" % numDec    


