def retorna_bicho(valor):
    if valor == 0 | valor > 97:
        nome = "Vaca"
    elif valor > 93:
        nome = "Veado"
    elif valor > 89:
        nome = "Urso"
    elif valor > 85:
        nome = "Tigre"
    elif valor > 81:
        nome = "Touro"
    elif valor > 77:
        nome = "Peru"
    elif valor > 73:
        nome = "Pavao"
    elif valor > 69:
        nome = "Porco"
    elif valor > 65:
        nome = "Macaco"
    elif valor > 61:
        nome = "Leao"
    elif valor > 57:
        nome = "Jacare"
    elif valor > 53:
        nome = "Gato"
    elif valor > 49:
        nome = "Galo"
    elif valor > 45:
        nome = "Elefante"
    elif valor > 41:
        nome = "Cavalo"
    elif valor > 37:
        nome = "Coelho"
    elif valor > 33:
        nome = "Cobra"
    elif valor > 29:
        nome = "Camelo"
    elif valor > 25:
        nome = "Carneiro"
    elif valor > 21:
        nome = "Cabra"
    elif valor > 17:
        nome = "Cachorro"
    elif valor > 13:
        nome = "Borboleta"
    elif valor > 9:
        nome = "Burro"
    elif valor > 5:
        nome = "Aguia"
    elif valor > 1:
        nome = "Avestrus"
    else:
        nome = "Invalido"
    return nome

class Resultado():
    def __init__(self):
        self.premio = ''
        self.resultado = ''
        self.nomeBicho = ''
        self.valor = ''    

    def printar(self):
        s = "%s premio: %s (%s) - Valor: R$%s\n" % (self.premio, self.resultado, self.nomeBicho, self.valor)
        return s

    def set_resultado(self, pResultado):
        self.resultado = pResultado
        final = pResultado[3]+ pResultado[4]
        self.nomeBicho = retorna_bicho(int(final))