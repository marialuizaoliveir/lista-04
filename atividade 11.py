class Pessoa:
    def _init_(self,nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        if isinstance (nome,str) and len(nome) > 0:
            self.__nome = nome
        else:
            print('Nome Invalido')

# Testar a função
abc = Pessoa('Joaqui 5555666n')
print(abc.get_nome())

abc.set_nome('Maria Joaquina')
print(abc.get_nome())

class ContaBancaria:
    def _init_(self, saldo):
        self.__saldo = saldo if saldo >= 0 else 0  # Inicializa o saldo, garantindo que não seja negativo

    # Método para depositar valor na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor depositado inválido")

    # Método para sacar valor da conta
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Valor de saque inválido!")
    
    # Método para obter o saldo atual
    def get_saldo(self):
        return self.__saldo

# Testar código pela entrada de dados
conta = ContaBancaria(1000)  # Inicializa a conta com saldo de 1000
conta.depositar(500)  # Deposita 500 na conta
print(conta.get_saldo())  # Exibe o saldo atual: 1500

conta.sacar(2000)  # Tenta sacar 2000, mas o saldo é insuficiente

print(conta.get_saldo())  # Exibe o saldo atual: 1500

#///////////////////////////////////////////////////////////////////
# lista 04///////////////////////////////////////////

#ex1////////////////////////////////////////////////////////////////////////////////
class Pessoa:
    def _init_(self, nome):
        self._nome = nome

    def nome(self):
        return self._nome

    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome não pode estar vazio.")
        self._nome = novo_nome


p = Pessoa("Ana")
print(p.nome)   

p.nome = "Paul"  
print(p.nome) 

try:
    p.nome = ""  
except ValueError as e:
    print(e)  
    
#ex5//////////////////////////////////////////////////////////////////////
class Aluno:
    def _init_(self, nome, nota):
        self._nome = nome
        self._nota = nota

    # Getter e Setter para nome
    
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para nota
    
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nova_nota):
        if not (0 <= nova_nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        self._nota = nova_nota

# Exemplo de uso
aluno = Aluno("Carlos", 8)
print(aluno.nome)  
print(aluno.nota)  

aluno.nome = "Ana"
aluno.nota = 9
print(aluno.nome)  
print(aluno.nota)  

try:
    aluno.nota = 11  
except ValueError as e:
    print(e)  

#ex4/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class ContaBancaria():
       def _init_(self, nome, deposito):
     self.saldo = 1000
     self. nome = nome
     self.deposito = deposito

   def saida(self):
      print(f"O saldo da conta da {self.nome} é R${self.saldo + self.deposito}")

#ex7///////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Livro:
    def _init_(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor

    
    
    def titulo(self):
        return self._titulo

    def titulo(self, novo_titulo):
        if not novo_titulo:
            raise ValueError("O título não pode estar vazio.")
        self._titulo = novo_titulo

    
    def autor(self):
        return self._autor

    def autor(self, novo_autor):
        if not novo_autor:
            raise ValueError("O autor não pode estar vazio.")
        self._autor = novo_autor


livro = Livro("Crepúsculo", "Sthephenie Meyer")
print(livro.titulo)  
print(livro.autor)  

livro.titulo = "Amanhcer"
livro.autor = "Sthephenie Meyer"
print(livro.titulo)  
print(livro.autor)   

try:
    livro.titulo = ""  
except ValueError as e:
    print(e)  

#ex8/////////////////////////////////////////////////////////////////////////////////////////////
class Funcionario:
    def _init_(self, salario):
        self.salario = salario 

    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= 0:
            raise ValueError("O salário deve ser um valor positivo.")
        self._salario = novo_salario


funcionario = Funcionario(3000)
print(funcionario.salario)  #3000

funcionario.salario = 4500
print(funcionario.salario)  # 4500

#ex9///////////////////////////////////////////////////////////////////////////////////////////
class Casa:
    def _init_(self, endereco, valor):
        self._endereco = endereco
        self._valor = valor

    # Getter para o atributo endereco
    def endereco(self):
        return self._endereco

    # Setter para o atributo endereco
    def endereco(self, novo_endereco):
        if not novo_endereco:
            raise ValueError("O endereço não pode estar vazio.")
        self._endereco = novo_endereco

    # Getter para o atributo valor
    
    def valor(self):
        return self._valor


    def valor(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O valor deve ser um número positivo.")
        self._valor = novo_valor

# Exemplo de uso
casa = Casa("Avenida São Paulo , 123", 250000)
print(casa.endereco)  
print(casa.valor)     # 250000

casa.endereco = "Avenida palmeira , 456"
casa.valor = 300000
print(casa.endereco)  # Avenida Palmeira, 456
print(casa.valor)     # 300000

try:
    casa.valor = -50000  # Tenta definir um valor negativo
except ValueError as e:
    print(e)  # "O valor deve ser um número positivo."
    
#ex10//////////////////////////////////////////////////////////////////////////////////////////////////////
class Celular:
    def _init_(self, marca):
        self._marca = marca

    # Getter para o atributo marca
    def marca(self):
        return self._marca
    
    def marca(self, nova_marca):
        if not nova_marca:
            raise ValueError("A marca não pode estar vazia.")
        self._marca = nova_marca

# Exemplo de uso
celular = Celular("Samsung")
print(celular.marca)  # Samsung

celular.marca = "Motorola"
print(celular.marca)  # Motorola

try:
    celular.marca = ""  # Tenta definir uma marca vazia
except ValueError as e:
    print(e)  # "A marca não pode estar vazia."
    
#ex11///////////////////////////////////////////////////////////////////////////////////////
class Animal:
    def _init_(self, idade):
        self.idade = idade  # Usa o setter para aplicar a validação

    # Getter para o atributo idade
    def idade(self):
        return self._idade

    # Setter para o atributo idade com validação
    def idade(self, nova_idade):
        if not isinstance(nova_idade, int) or nova_idade <= 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")
        self._idade = nova_idade

# Exemplo de uso
animal = Animal(5)
print(animal.idade)  # 5

animal.idade = 7
print(animal.idade)  # 7

try:
    animal.idade = -2  
except ValueError as e:
    print(e)  
    
    animal.idade = "dez" 
except ValueError as e:
    print(e)  

#ex12//////////////////////////////////////////////////////////////////////////////////////////////////
class Estudante:
    def _init_(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome não pode estar vazio.")
        self._nome = novo_nome


    def matricula(self):
        return self._matricula
r
    def matricula(self, nova_matricula):
        if not isinstance(nova_matricula, str) or len(nova_matricula) == 0:
            raise ValueError("A matrícula deve ser uma string não vazia.")
        self._matricula = nova_matricula

# Exemplo de uso
estudante = Estudante("Luiza", "12345")
print(estudante.nome)       # João Silva
print(estudante.matricula)  # 12345

# Modificando os atributos usando os setters
estudante.nome = "Maria Oliveira"
estudante.matricula = "67890"

print(estudante.nome)       # Maria Oliveira
print(estudante.matricula)  # 67890

# Tentando atribuir um nome vazio
try:
    estudante.nome = ""  # Nome vazio
except ValueError as e:
    print(e)  # "O nome não pode estar vazio."

# Tentando atribuir uma matrícula inválida
try:
    estudante.matricula = ""  # Matrícula vazia
except ValueError as e:
    print(e)  # "A matrícula deve ser uma string não vazia."
    
#ex13///////////////////////////////////////////////////////////////////////////////////////////////
class Veiculo:
    def _init_(self, velocidade_maxima):
        self._velocidade_maxima = velocidade_maxima

    def velocidade_maxima(self):
        return self._velocidade_maxima

veiculo = Veiculo(200)
print(veiculo.velocidade_maxima)  

#ex14////////////////////////////////////////////////////////////////////////////////////////////////////////
class Computador:
    def _init_(self, memoria_ram):
        self.memoria_ram = memoria_ram  


    def memoria_ram(self):
        return self._memoria_ram

    
    def memoria_ram(self, nova_memoria_ram):
        if nova_memoria_ram <= 0:
            raise ValueError("A memória RAM deve ser maior que zero.")
        self._memoria_ram = nova_memoria_ram

computador = Computador(8)  # 8 GB de memória RAM
print(computador.memoria_ram)  # 8

computador.memoria_ram = 16  # Modificando a memória RAM
print(computador.memoria_ram)  # 16

#ex15////////////////////////////////////////////////////////////////////////////////////
class Filme:
    def _init_(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento

    # Getter e Setter para o atributo titulo
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if not novo_titulo:
            raise ValueError("O título não pode estar vazio.")
        self._titulo = novo_titulo

    # Getter e Setter para o atributo ano_lancamento
    def ano_lancamento(self):
        return self._ano_lancamento

    def ano_lancamento(self, novo_ano):
        if not isinstance(novo_ano, int) or novo_ano < 1888:  # O primeiro filme foi lançado em 1888
            raise ValueError("O ano de lançamento deve ser um número inteiro maior ou igual a 1888.")
        self._ano_lancamento = novo_ano

filme = Filme("Inception", 2010)
print(filme.titulo)          
print(filme.ano_lancamento)  

filme.titulo = "Interstellar"
filme.ano_lancamento = 2014
print(filme.titulo)          
print(filme.ano_lancamento)  

#ex16////////////////////////////////////////////////////////////////////////////////////////////
class Jogo:
    def _init_(self, pontuacao):
        self.pontuacao = pontuacao  


    def pontuacao(self):
        return self._pontuacao

    def pontuacao(self, nova_pontuacao):
        if nova_pontuacao < 0:
            raise ValueError("A pontuação não pode ser negativa.")
        self._pontuacao = nova_pontuacao


jogo = Jogo(100)
print(jogo.pontuacao)  # 100

# Modificando a pontuação
jogo.pontuacao = 200
print(jogo.pontuacao)  # 200

#ex17///////////////////////////////////////////////////////////////////////////////////////
class Empresa:
    def _init_(self, nome, numero_funcionarios):
        self.nome = nome
        self.numero_funcionarios = numero_funcionarios

    # Getter e Setter para o atributo nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome da empresa não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo numero_funcionarios
    @property
    def numero_funcionarios(self):
        return self._numero_funcionarios

    @numero_funcionarios.setter
    def numero_funcionarios(self, novo_numero):
        if novo_numero < 0:
            raise ValueError("O número de funcionários deve ser um valor não negativo.")
        self._numero_funcionarios = novo_numero

# Exemplo de uso
empresa = Empresa("Tech Solutions", 50)
print(empresa.nome)              # Tech Solutions
print(empresa.numero_funcionarios)  # 50

# Modificando os atributos usando os setters
empresa.nome = "Innovative Tech"
empresa.numero_funcionarios = 60
print(empresa.nome)              # Innovative Tech
print(empresa.numero_funcionarios)  # 60

# Tentando definir um nome vazio
try:
    empresa.nome = ""  # Nome vazio
except ValueError as e:
    print(e)  # "O nome da empresa não pode estar vazio."

# Tentando definir um número negativo de funcionários
try:
    empresa.numero_funcionarios = -5  # Número negativo de funcionários
except ValueError as e:
    print(e)  # "O número de funcionários deve ser um valor não negativo."

#ex18/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Filme:
    def _init_(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento

    # Getter e Setter para o atributo titulo
    
    def titulo(self):
        return self._titulo

    def titulo(self, novo_titulo):
        if not novo_titulo:
            raise ValueError("O título não pode estar vazio.")
        self._titulo = novo_titulo

    # Getter e Setter para o atributo ano_lancamento

    def ano_lancamento(self):
        return self._ano_lancamento

    @ano_lancamento.setter
    def ano_lancamento(self, novo_ano):
        if not isinstance(novo_ano, int) or novo_ano < 1888:  # O primeiro filme foi lançado em 1888
            raise ValueError("O ano de lançamento deve ser um número inteiro maior ou igual a 1888.")
        self._ano_lancamento = novo_ano

# Exemplo de uso
filme = Filme("Inception", 2010)
print(filme.titulo)          # Inception
print(filme.ano_lancamento)  # 2010

# Modificando os atributos usando os setters
filme.titulo = "Interstellar"
filme.ano_lancamento = 2014
print(filme.titulo)          # Interstellar
print(filme.ano_lancamento)  # 2014

# Tentando definir um título vazio
try:
    filme.titulo = ""  # Título vazio
except ValueError as e:
    print(e)  # "O título não pode estar vazio."

# Tentando definir um ano inválido
try:
    filme.ano_lancamento = 1800  # Ano anterior ao primeiro filme
except ValueError as e:
    print(e)  # "O ano de lançamento deve ser um número inteiro maior ou igual a 1888."

#ex19//////////////////////////////////////////////
class Cidade:
    def _init_(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

    # Getter e Setter para o atributo nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome da cidade não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo populacao
    @property
    def populacao(self):
        return self._populacao

    @populacao.setter
    def populacao(self, nova_populacao):
        if not isinstance(nova_populacao, int) or nova_populacao < 0:
            raise ValueError("A população deve ser um número inteiro positivo.")
        self._populacao = nova_populacao

# Exemplo de uso
cidade = Cidade("São Paulo", 12300000)
print(cidade.nome)         # São Paulo
print(cidade.populacao)    # 12300000

# Modificando os atributos usando os setters
cidade.nome = "Rio de Janeiro"
cidade.populacao = 6748000
print(cidade.nome)         # Rio de Janeiro
print(cidade.populacao)    # 6748000

# Tentando definir um nome vazio
try:
    cidade.nome = ""  # Nome vazio
except ValueError as e:
    print(e)  # "O nome da cidade não pode estar vazio."

# Tentando definir uma população negativa
try:
    cidade.populacao = -5000  # População negativa
except ValueError as e:
    print(e)  # "A população deve ser um número inteiro positivo."

#ex20///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Professor:
    def _init_(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    # Getter e Setter para o atributo nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome:
            raise ValueError("O nome do professor não pode estar vazio.")
        self._nome = novo_nome

    # Getter e Setter para o atributo disciplina
    @property
    def disciplina(self):
        return self._disciplina

    @disciplina.setter
    def disciplina(self, nova_disciplina):
        if not nova_disciplina:
            raise ValueError("A disciplina não pode estar vazia.")
        self._disciplina = nova_disciplina

# Exemplo de uso
professor = Professor("João Silva", "Matemática")
print(professor.nome)        # João Silva
print(professor.disciplina)  # Matemática

# Modificando os atributos usando os setters
professor.nome = "Maria Oliveira"
professor.disciplina = "Física"
print(professor.nome)        # Maria Oliveira
print(professor.disciplina)  # Física

# Tentando definir um nome vazio
try:
    professor.nome = ""  # Nome vazio
except ValueError as e:
    print(e)  # "O nome do professor não pode estar vazio."
