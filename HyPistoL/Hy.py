from abc import ABC, abstractmethod # Faz a Importação do abstractmethod 

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = None
        self._idade = None
        self.nome = nome
        self.idade = idade

    @property    
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property    
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    @abstractmethod
    def exibir_informacoes(self):
        pass

class Sala(ABC):
    def __init__(self, numero, capacidade):
        self.numero = numero  # usa o setter
        self.capacidade = capacidade  # usa o setter

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if isinstance(valor, int) and valor > 0:
            self._numero = valor
        else:
            raise ValueError("O número da sala deve ser um inteiro positivo.")

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor):
        if isinstance(valor, int) and valor > 0:
            self._capacidade = valor
        else:
            raise ValueError("A capacidade da sala deve ser um inteiro maior que zero.")

    @abstractmethod
    def exibir_informacoes(self):
        pass


class Paciente(Pessoa):
    def __init__(self, nome, idade, numero_utente):
        super().__init__(nome, idade)
        self._numero_utente = numero_utente
        self._historico_medico = []

    @property
    def numero_utente(self):
        return self._numero_utente

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nº Utente: {self.numero_utente}")
        print(f"Histórico médico: {self._historico_medico if self._historico_medico else 'Nenhum registro'}")



#----------------------------------------------------------------------------#

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self._salario = None
        self.salario = salario
        


    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        try:
            valor = float(valor)
            if valor >= 0:
                self._salario = valor
            else:
                raise ValueError("O salário deve ser um valor positivo.")
        except ValueError:
            print("Erro: salário inválido. Deve ser um número positivo.")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: €{self.salario:.2f}")

    def pagamento(self):
        print("-------------------------------------")
        print("         PAGAMENTO FUNCIONÁRIO        ")
        print(f"Cargo: {self.cargo}")
        print(f"Salário base: €{self.salario:.2f}")
        print(f"Pagamento total: €{self.salario:.2f}")
        print("-------------------------------------")
        return self.salario

    def aplicar_aumento(self, percentual):
        if percentual > 0:
            aumento = self.salario * (percentual / 100)
            self.salario += aumento
            print(f"Aumento aplicado: +{aumento:.2f}€")
            print(f"Novo salário: €{self.salario:.2f}")
        else:
            raise ValueError("O percentual de aumento deve ser positivo.")
        
#----------------------------------------------------------------------------------#

class Medico(Pessoa):
    def __init__(self, nome, idade, salario_base, especialidade):
        super().__init__(nome, idade)
        self._salario_base = salario_base
        self._especialidade = None
        self.especialidade = especialidade  # usa o setter para validar
        self._pacientes = []

    @property
    def salario_base(self):
        return self._salario_base

    @property
    def especialidade(self):
        return self._especialidade
    
    @especialidade.setter
    def especialidade(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._especialidade = valor.strip()
        else:
            raise ValueError("Especialidade deve ser uma string não vazia.")

    def adicionar_paciente(self, paciente):
        if paciente not in self._pacientes:
            self._pacientes.append(paciente)

    def listar_pacientes(self):
        if self._pacientes:
            print("Pacientes atendidos:")
            for i, paciente in enumerate(self._pacientes, 1):
                print(f"{i}. {paciente.nome} ({paciente.idade} anos)")
        else:
            print("Nenhum paciente atendido ainda.")

    def calcular_pagamento(self):
        valor_por_paciente = 50
        adicional = len(self._pacientes) * valor_por_paciente
        pagamento_total = self._salario_base + adicional
        print("-------------------------------------")
        print("             PAGAMENTO MÉDICO             ")
        print(f"Salário base: €{self._salario_base:.2f}")
        print(f"Pacientes atendidos: {len(self._pacientes)}")
        print(f"Adicional por paciente: €{adicional:.2f}")
        print(f"Pagamento total: €{pagamento_total:.2f}")
        print("-------------------------------------")
        return pagamento_total

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Número de pacientes atendidos: {len(self._pacientes)}")

#----------------------------------------------------------------------------------#

class Enfermeiro(Pessoa):
    def __init__(self, nome, idade, salario_base, turno):
        super().__init__(nome, idade)
        self._salario_base = salario_base
        self._turno = None
        self.turno = turno  # usa o setter para validar
        self._pacientes = []

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        if valor.lower() in ["dia", "noite"]:
            self._turno = valor.lower()
        else:
            raise ValueError("Turno inválido. Use 'dia' ou 'noite'.")

    def adicionar_paciente(self, paciente):
        self._pacientes.append(paciente)

    def listar_pacientes(self):
        if self._pacientes:
            print("Pacientes sob responsabilidade:")
            for i, paciente in enumerate(self._pacientes, 1):
                print(f"{i}. {paciente.nome} ({paciente.idade} anos)")
        else:
            print("Nenhum paciente sob responsabilidade.")

    def calcular_pagamento(self):
        adicional = 100 if self.turno == "noite" else 100
        adicional = 100 if self.turno == "dia" else 50
        pagamento_total = self._salario_base + adicional
        print("-------------------------------------")
        print("             PAGAMENTO ENFERMEIRO             ")
        print(f"Salário base: €{self._salario_base:.2f}")
        print(f"Turno: {self.turno}")
        print(f"Adicional por turno: €{adicional:.2f}")
        print(f"Pagamento total: €{pagamento_total:.2f}")
        print("-------------------------------------")
        return pagamento_total

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Turno: {self.turno}")
        print(f"Número de pacientes sob cuidado: {len(self._pacientes)}")

#----------------------------------------------------------------------------------#

class Administrativo(Pessoa):
    def __init__(self, nome, idade, salario_base, setor):
        super().__init__(nome, idade)
        self._salario_base = salario_base
        self._setor = None
        self.setor = setor  # usa o setter para validar
        self._horas_trabalhadas = 0

    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, valor):
        setores_validos = ["financeiro", "recursos humanos", "logística", "atendimento"]
        if valor.lower() in setores_validos:
            self._setor = valor.lower()
        else:
            raise ValueError(f"Setor inválido. Escolha entre: {', '.join(setores_validos)}")

    def registrar_horas(self, horas):
        if horas > 0:
            self._horas_trabalhadas += horas
        else:
            raise ValueError("Horas devem ser um valor positivo.")

    def calcular_pagamento(self):
        valor_por_hora = 10
        adicional = self._horas_trabalhadas * valor_por_hora
        pagamento_total = self._salario_base + adicional
        print("-------------------------------------")
        print("           PAGAMENTO ADMINISTRATIVO           ")
        print(f"Salário base: €{self._salario_base:.2f}")
        print(f"Horas registradas: {self._horas_trabalhadas}")
        print(f"Adicional por horas: €{adicional:.2f}")
        print(f"Pagamento total: €{pagamento_total:.2f}")
        print("-------------------------------------")
        return pagamento_total

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Setor: {self.setor}")
        print(f"Horas trabalhadas: {self._horas_trabalhadas}")

#----------------------------------------------------------------------------------#

class EnfermeiroChefe(Pessoa):
    def __init__(self, nome, idade, salario_base, turno, setor, bonus_chefia):
        super().__init__(nome, idade)
        self._salario_base = salario_base
        self._turno = None
        self.turno = turno  # usa o setter
        self._setor = None
        self.setor = setor  # usa o setter
        self._bonus_chefia = None
        self.bonus_chefia = bonus_chefia  # usa o setter
        self._pacientes = []

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        if valor.lower() in ["dia", "noite"]:
            self._turno = valor.lower()
        else:
            raise ValueError("Turno inválido. Use 'dia' ou 'noite'.")

    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, valor):
        setores_validos = ["emergência", "pediatria", "cirurgia", "clínica geral"]
        if valor.lower() in setores_validos:
            self._setor = valor.lower()
        else:
            raise ValueError(f"Setor inválido. Escolha entre: {', '.join(setores_validos)}")

    @property
    def bonus_chefia(self):
        return self._bonus_chefia

    @bonus_chefia.setter
    def bonus_chefia(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._bonus_chefia = valor
        else:
            raise ValueError("O bônus de chefia deve ser um número positivo.")

    def adicionar_paciente(self, paciente):
        self._pacientes.append(paciente)

    def listar_pacientes(self):
        if self._pacientes:
            print("Pacientes sob responsabilidade:")
            for i, paciente in enumerate(self._pacientes, 1):
                print(f"{i}. {paciente.nome} ({paciente.idade} anos)")
        else:
            print("Nenhum paciente sob responsabilidade.")

    def calcular_pagamento(self):
        adicional_turno = 100 if self.turno == "noite" else 50
        pagamento_total = self._salario_base + adicional_turno + self.bonus_chefia
        print("-------------------------------------")
        print("         PAGAMENTO ENFERMEIRO CHEFE         ")
        print(f"Salário base: €{self._salario_base:.2f}")
        print(f"Turno: {self.turno}")
        print(f"Adicional por turno: €{adicional_turno:.2f}")
        print(f"Bônus de chefia: €{self.bonus_chefia:.2f}")
        print(f"Pagamento total: €{pagamento_total:.2f}")
        print("-------------------------------------")
        return pagamento_total

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Turno: {self.turno}")
        print(f"Setor: {self.setor}")
        print(f"Número de pacientes sob cuidado: {len(self._pacientes)}")
        
#----------------------------------------------------------------------------------#

class SalaConsulta(Sala):
    def __init__(self, numero, capacidade, medico_responsavel):
        super().__init__(numero, capacidade)
        self._medico_responsavel = None
        self.medico_responsavel = medico_responsavel
        self._pacientes_agendados = []

    @property
    def medico_responsavel(self):
        return self._medico_responsavel

    @medico_responsavel.setter
    def medico_responsavel(self, valor):
        if isinstance(valor, Medico):
            self._medico_responsavel = valor
        else:
            raise TypeError("O responsável deve ser uma instância da classe Medico.")

    @property
    def pacientes_agendados(self):
        return self._pacientes_agendados

    def agendar_consulta(self, paciente):
        if len(self._pacientes_agendados) < self.capacidade:
            self._pacientes_agendados.append(paciente)
            self.medico_responsavel.adicionar_paciente(paciente)
        else:
            print("Sala cheia. Não é possível agendar mais pacientes.")

    def exibir_informacoes(self):
        print(f"Sala de Consulta nº {self.numero}")
        print(f"Capacidade: {self.capacidade}")
        print(f"Médico responsável: {self.medico_responsavel.nome}")
        print("Pacientes agendados:")
        if self._pacientes_agendados:
            for i, p in enumerate(self._pacientes_agendados, 1):
                print(f"{i}. {p.nome} ({p.idade} anos)")
        else:
            print("Nenhum paciente agendado.")

    def detalhar_sala(self):
        print("=== Sala de Consulta ===")
        print(f"Número da sala: {self.numero}")
        print(f"Capacidade: {self.capacidade}")
        print(f"Médico responsável: {self.medico_responsavel.nome}")
        print("Pacientes agendados:")
        if self._pacientes_agendados:
            for i, paciente in enumerate(self._pacientes_agendados, 1):
                print(f"{i}. {paciente.nome} ({paciente.idade} anos)")
        else:
            print("Nenhum paciente agendado.")

    def exibir_informacoes(self):
        self.detalhar_sala()
#----------------------------------------------------------------------------------#

class SalaCirurgia(Sala):
    def __init__(self, numero, capacidade, medico_responsavel):
        super().__init__(numero, capacidade)
        self._medico_responsavel = None
        self.medico_responsavel = medico_responsavel  # usa o setter
        self._pacientes_agendados = []

    @property
    def medico_responsavel(self):
        return self._medico_responsavel

    @medico_responsavel.setter
    def medico_responsavel(self, valor):
        if isinstance(valor, Medico):
            self._medico_responsavel = valor
        else:
            raise TypeError("O responsável deve ser uma instância da classe Medico.")

    def agendar_consulta(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("O paciente deve ser uma instância da classe Paciente.")

        if len(self._pacientes_agendados) < self.capacidade:
            self._pacientes_agendados.append(paciente)
            self.medico_responsavel.adicionar_paciente(paciente)
            print(f"Cirurgia agendada para {paciente.nome}.")
        else:
            print("Capacidade máxima da sala atingida. Não é possível agendar mais cirurgias.")

    def detalhar_sala(self):
        print("=== Sala de Cirurgia ===")
        print(f"Número da sala: {self.numero}")
        print(f"Capacidade: {self.capacidade}")
        print(f"Médico responsável: {self.medico_responsavel.nome}")
        print("Pacientes agendados:")
        if self._pacientes_agendados:
            for i, paciente in enumerate(self._pacientes_agendados, 1):
                print(f"{i}. {paciente.nome} ({paciente.idade} anos)")
        else:
            print("Nenhum paciente agendado.")

    def exibir_informacoes(self):
        self.detalhar_sala()
#----------------------------------------------------------------------------------#

class Consulta:
    def __init__(self, medico, paciente, data, tipo, sala=None):
        self._sala = sala
        if not isinstance(medico, Medico):
            raise TypeError("O médico deve ser uma instância da classe Medico.")
        if not isinstance(paciente, Paciente):
            raise TypeError("O paciente deve ser uma instância da classe Paciente.")
        if not isinstance(data, str) or not data.strip():
            raise ValueError("A data deve ser uma string não vazia.")
        self._medico = medico
        self._paciente = paciente
        self._data = data.strip()
        self._tipo = None
        self.tipo = tipo  # usa o setter

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        tipos_validos = ["rotina", "emergência", "especialidade", "urgência"]
        if isinstance(valor, str) and valor.strip().lower() in tipos_validos:
            self._tipo = valor.strip().lower()
        else:
            raise ValueError(f"Tipo de consulta inválido. Escolha entre: {', '.join(tipos_validos)}")

    @property
    def medico(self):
        return self._medico

    @property
    def paciente(self):
        return self._paciente

    @property
    def data(self):
        return self._data

    def exibir_detalhes(self):
        print("=== Detalhes da Consulta ===")
        print(f"Data: {self.data}")
        print(f"Tipo: {self.tipo}")
        print(f"Médico: {self.medico.nome} ({self.medico.especialidade})")
        print(f"Paciente: {self.paciente.nome}, {self.paciente.idade} anos")