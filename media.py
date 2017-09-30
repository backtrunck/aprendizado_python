qt_notas = raw_input("Digite a quantidade de notas ")
nota = 0
nota_temp = 0 
for i in range(int(qt_notas)):
    nota_temp = float(raw_input("Digite a Nota "))
    if nota_temp > 10:
        print "A nota tem que ser menor do que 10"
        exit()
    nota = nota + nota_temp 
            
print "A media eh: %f"%float(nota/int(qt_notas))
