# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    @property
    def nome(self):
      return self._nome

    @property
    def numero(self):
      return self._numero

    @property 
    def plano(self):
      return self._plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):

      custo_chamada = self.plano.custo_chamada(duracao)
      if self.plano.verificar_saldo(custo_chamada):
        saldo_atual = self.plano.deduzir_saldo(custo_chamada)
        return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_atual:.2f}"
      return f"Saldo insuficiente para fazer a chamada." 

# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':

# TODO: Verifique se o saldo do plano é suficiente para a chamada.

# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.

# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self, custo_chamada):
      if self.saldo > custo_chamada:
        return True
      return False

# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, duracao):
      custo_por_minuto = 0.10
      return custo_por_minuto * duracao

# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self, custo_chamada):
      self.saldo = self.saldo - custo_chamada
      return self.saldo

# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = 'Rodrigo'
numero = '(00) 90000-0000'
saldo_inicial = 10

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = '(33) 93333-3333'
duracao = 120

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))