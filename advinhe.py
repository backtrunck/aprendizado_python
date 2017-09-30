from random import randrange
import os

os.system('clear')

numero_secreto = randrange(0, 5)

print "Em 3 tentativas tente advinhar o numero que eu estou pensando entre 0 e 4"
for i in range(3):
	print "%d tentativa"%(i+1)

	palpite = int(raw_input(""))
	
	if numero_secreto == palpite :
		print "Acertou, Miseravel"
		exit()
	else:
		print "Errou, desgracado"


print "Vc perdeu, o numero era %d, tente de novo"%numero_secreto




