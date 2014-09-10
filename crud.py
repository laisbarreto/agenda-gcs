class Crud():
	def __init__(self):
        pass

    def pesquisar_contato(self, agenda, nome):
        resultado = []
        nome = nome.lower()
        for chave in agenda.iterkeys():
            contato = agenda.get(chave)
            if contato != None:
                contato.nome = contato.nome.lower()
                if contato.nome.find(nome) != -1:
                    resultado.append(contato)

        return resultado
