import random

def get_randomInt():
	random_number = random.randrange(1,13)
	return random_number
# randrange() nunca va a mostrar el ultimo, es como hacer un .length -1 por lo cual por eso hay que poner un rango de numero más en este caso 13
# si pongo 12 nunca se va a leer, primer valor si lo va a leer pero el ultimo no, solo anterior


print(get_randomInt())