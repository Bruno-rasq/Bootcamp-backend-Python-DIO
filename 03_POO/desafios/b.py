# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self, nome, saldo):
      self._nome = nome
      self._saldo = saldo

    @property
    def nome(self):
      return self._nome

    @property
    def saldo(self):
      return self._saldo

# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
    def verificar_saldo(self):
      mensagem = ''

      if self.saldo < 10:
        mensagem = "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
      elif self.saldo >= 50:
        mensagem = "Parabéns! Continue aproveitando seu plano sem preocupações."
      else:
        mensagem = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

      return self.mensagem_personalizada(mensagem)

# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 
    def mensagem_personalizada(self, mensagem):
      return mensagem

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def verificar_saldo(self):
      return self.plano.verificar_saldo()



# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = 'João'
nome_plano = 'Essencial '
saldo_inicial = 9

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)