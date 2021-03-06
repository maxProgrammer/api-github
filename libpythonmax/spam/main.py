class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.enviador = enviador
        self.sessao = sessao

    def enviar_emails(self, rementente, assunto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                rementente,
                usuario.email,
                assunto,
                corpo
            )
