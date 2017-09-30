 
nota1=float(raw_input("digite uma nota "))
nota2=float(raw_input("digite outra nota "))
if nota1>10 or nota2>10:
	print "erro. nota maior do que 10"
	exit()
media=nota1+nota2
media=media/2
print "sua media eh ", media
if media<4:
	print "reprovado"
else:
	if media<7:
		print "exame"
	else:
		print "aprovado"

