# import os 

# from Hy import Paciente
# from Hy import Funcionario
# from Hy import Medico
# from Hy import Enfermeiro
# from Hy import Administrativo
# from Hy import EnfermeiroChefe
# from Hy import SalaConsulta
# from Hy import SalaCirurgia
# from Hy import Consulta

# def excluir():
#     os.system('cls' if os.name == 'nt' else 'clear')

# excluir()
# while True:
    
#     excluir()
#     print("\n=== Hyspytol ===")
#     print("1 - Cadastrar")
#     print("2 - Salas")
#     print("3 - Consulta")
#     print("4 - Encerrar programa")
#     try:
#         op = int(input("Escolha uma opção (1-5): "))
#     except ValueError:
#         print("Opção inválida. Tente novamente.")
#         input("Pressione Enter para continuar...")
#         continue

#     match op:
#         case 1:
#             excluir()
#             while True:
#                 print("----CADASTRAR----")
#                 print("1 - Paciente")
#                 print("2 - Funcionário")
#                 print("3 - Médico")
#                 print("4 - Enfermeiro")
#                 print("5 - Administrador")
#                 print("6 - Enfermeiro chefe")
#                 print("7 - Voltar")
#                 try:
#                     op = int(input("Escolha uma opção (1-5): "))
#                 except ValueError:
#                     print("Opção inválida. Tente novamente.")
#                     input("Pressione Enter para continuar...")
#                     excluir()
#                     continue
#                 match op:
#                     case 1:
#                         excluir()
#                         p1 = Paciente("Kauã", 25, 1200)
#                         p1.exibir_informacoes()
#                         input()
#                         excluir()
#                     case 2:
#                         excluir()
#                         f1 = Funcionario("Kauã", 25, "Técnico de TI", 1200)
#                         f1.exibir_informacoes()
#                         f1.aplicar_aumento(10)
#                         input()
#                         excluir()
#                     case 3:
#                         excluir()
#                         me = Medico("Jonas,",29,5000,"Plástica")
#                         me.adicionar_paciente(Paciente("João", 30, "123456"))
#                         me.adicionar_paciente(Paciente("Maria", 28, "654321"))
#                         me.exibir_informacoes()
#                         me.listar_pacientes()
#                         me.calcular_pagamento()
#                         input()
#                         excluir()
#                     case 4:
#                         excluir()
#                         e1 = Enfermeiro("Kauã", 25, 1300, "noite")
#                         e1.adicionar_paciente(Paciente("João", 30, "123456"))
#                         e1.adicionar_paciente(Paciente("Maria", 28, "654321"))
#                         e1.exibir_informacoes()
#                         e1.listar_pacientes()
#                         e1.calcular_pagamento()
#                         input()
#                         excluir()
#                     case 5:
#                         excluir()
#                         a1 = Administrativo("Kauã", 25, 1000, "financeiro")
#                         a1.registrar_horas(12)
#                         a1.exibir_informacoes()
#                         a1.calcular_pagamento()
#                         input()
#                         excluir()
#                     case 6:
#                         excluir()
#                         ec = EnfermeiroChefe("Kauã", 28, 1800, "noite", "cirurgia", 300)
#                         ec.adicionar_paciente(Paciente("João", 30, "123456"))
#                         ec.exibir_informacoes()
#                         ec.listar_pacientes()
#                         ec.calcular_pagamento()
#                         input()
#                         excluir()
#                     case 7:
#                         break
#         case 2:
#             excluir()
#             while True:
#                 print("----Salas----")
#                 print("1 - Sala de Consulta")
#                 print("2 - Sala de Cirurgia")
#                 print("3 - Voltar")
#                 try:
#                     op = int(input("Escolha uma opção (1-3): "))
#                 except ValueError:
#                     print("Opção inválida. Tente novamente.")
#                     input("Pressione Enter para continuar...")
#                     excluir()
#                     continue
#                 match op:
#                     case 1:
#                         excluir()
#                         medico = Medico("Dra. Ana", 45, 3000, "Cardiologia")
#                         pacientes = [
#                                     {
#                                     "Nome": "Kauã",
#                                     "Idade":  23 ,
#                                     "Utente":"654321"
#                                     },
#                                     {
#                                     "Nome": "Willian",
#                                     "Idade":  19 ,
#                                     "Utente":"324328" 
#                                     }
#                                     ]
#                         pacientes_objetos = []

#                         for dados in pacientes:
#                             paciente = Paciente(dados["Nome"], dados["Idade"], dados["Utente"])
#                             pacientes_objetos.append(paciente)

#                         sala = SalaConsulta(101, 2, medico)

#                         for paciente in pacientes_objetos:
#                             sala.agendar_consulta(paciente)

#                         sala.detalhar_sala()
#                         input()
#                         excluir()
#                     case 2:
#                         excluir()
#                         medico = Medico("Dr. Carlos", 50, 5000, "Cirurgia Geral")
#                         paciente1 = Paciente("João", 40, "123456")
#                         paciente2 = Paciente("Ana", 35, "654321")

#                         pacientes = [
#                                     {
#                                     "Nome": "Kauã",
#                                     "Idade":  23 ,
#                                     "Utente":"654321"
#                                     },
#                                     {
#                                     "Nome": "Willian",
#                                     "Idade":  19 ,
#                                     "Utente":"324328" 
#                                     }
#                                     ]
#                         pacientes_objetos = []

#                         for dados in pacientes:
#                             paciente = Paciente(dados["Nome"], dados["Idade"], dados["Utente"])
#                             pacientes_objetos.append(paciente)

#                         sala = SalaConsulta(101, 2, medico)

#                         for paciente in pacientes_objetos:
#                             sala.agendar_consulta(paciente)

#                         sala.detalhar_sala()
#                         input()
#                         excluir()
#                     case 3:
#                         break
#         case 3: 
#             excluir()
#             medico = Medico("Dra. Ana", 45, 3000, "Cardiologia")
#             paciente = Paciente("Kauã", 23, "654321")
#             sala = SalaCirurgia(201, 2, medico)

#             consulta = Consulta(paciente, medico, sala)
#             consulta.adicionar_equipamento("Estetoscópio")
#             consulta.adicionar_equipamento("Monitor cardíaco")
#             consulta.detalhar_consulta()
#             input()
#             excluir()
#         case 4: 
#             excluir()
#             print("Sistema encerrado.")
#             break
#         case _:
#             excluir()
#             input()
#             print("Acerte animal")
#             input()
#             excluir()

import os
from Hy import (
    Paciente, Medico, Enfermeiro, EnfermeiroChefe, Funcionario, Administrativo,
    SalaConsulta, SalaCirurgia, Consulta
)

# Listas de armazenamento
pacientes_cadastrados = []
medicos_cadastrados = []
enfermeiros_cadastrados = []
chefes_cadastrados = []
funcionarios_cadastrados = []
administradores_cadastrados = []
consultas_realizadas = []

def entrada_obrigatoria(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        else:
            print("Este campo não pode ficar vazio. Digite um valor válido.")

def adicionar_historico(self, descricao):
    if isinstance(descricao, str) and descricao.strip():
        self._historico_medico.append(descricao.strip())

def entrada_obrigatoria(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        else:
            print("Este campo não pode ficar vazio.")

def registrar_consulta():
    excluir()
    print("=== Registrar Nova Consulta ===")

    if not pacientes_cadastrados or not medicos_cadastrados:
        print("Cadastre pelo menos 1 paciente e 1 médico.")
        input("Pressione Enter para continuar...")
        return

    # Escolher paciente
    print("\nPacientes disponíveis:")
    for i, p in enumerate(pacientes_cadastrados, 1):
        print(f"{i}. {p.nome} ({p.idade} anos)")
    try:
        idx_paciente = int(input("Escolha o número do paciente: "))
        paciente = pacientes_cadastrados[idx_paciente - 1]
    except (ValueError, IndexError):
        print("Paciente inválido.")
        input("Pressione Enter para continuar...")
        return

    # Escolher médico
    print("\nMédicos disponíveis:")
    for i, m in enumerate(medicos_cadastrados, 1):
        print(f"{i}. {m.nome} ({m.especialidade})")
    try:
        idx_medico = int(input("Escolha o número do médico: "))
        medico = medicos_cadastrados[idx_medico - 1]
    except (ValueError, IndexError):
        print("Médico inválido.")
        input("Pressione Enter para continuar...")
        return

    # Data e tipo
    data = entrada_obrigatoria("Data da consulta (ex: 24/10/2025): ")
    tipos_validos = ["rotina", "emergência", "especialidade", "urgência"]
    while True:
        tipo = entrada_obrigatoria("Tipo de consulta (rotina/emergência/especialidade/urgência): ").lower()
        if tipo in tipos_validos:
            break
        else:
            print("Tipo inválido. Escolha entre:", ", ".join(tipos_validos))

    # Criar e registrar consulta
    consulta = Consulta(medico, paciente, data, tipo)
    consultas_realizadas.append(consulta)
    print("\nConsulta registrada com sucesso!")
    consulta.exibir_detalhes()
    input("\nPressione Enter para continuar...")
    

def calcular_pagamento(lista, titulo):
    excluir()
    print(f"=== Pagamentos de {titulo} ===")
    if lista:
        for i, pessoa in enumerate(lista, 1):
            print(f"\n{i}. {pessoa.nome}")
            try:
                valor = pessoa.calcular_pagamento()
                print(f"Pagamento total: €{valor:.2f}")
            except Exception as e:
                print(f"Erro ao calcular pagamento: {e}")
    else:
        print("Nenhum cadastro encontrado.")
    input("\nPressione Enter para continuar...")

def pagamento(lista, titulo):
    excluir()
    print(f"=== Pagamentos de {titulo} ===")
    if lista:
        for i, pessoa in enumerate(lista, 1):
            print(f"\n{i}. {pessoa.nome}")
            try:
                valor = pessoa.pagamento()
                print(f"Pagamento total: €{valor:.2f}")
            except Exception as e:
                print(f"Erro ao calcular pagamento: {e}")
    else:
        print("Nenhum cadastro encontrado.")
    input("\nPressione Enter para continuar...")

def alterar_pagamento(lista, titulo):
    excluir()
    print(f"=== Alterar Pagamento de {titulo} ===")
    if not lista:
        print("Nenhum cadastro encontrado.")
        input("Pressione Enter para continuar...")
        return

    for i, pessoa in enumerate(lista, 1):
        print(f"{i}. {pessoa.nome}")

    try:
        escolha = int(input("\nEscolha o número da pessoa para alterar o pagamento: "))
        pessoa = lista[escolha - 1]
    except (ValueError, IndexError):
        print("Escolha inválida.")
        input("Pressione Enter para continuar...")
        return

    # Detecta tipo de pessoa e altera o valor correspondente
    try:
        if hasattr(pessoa, "salario"):
            novo = float(input("Novo salário: "))
            pessoa.salario = novo
        elif hasattr(pessoa, "salario_base"):
            novo = float(input("Novo salário base: "))
            pessoa._salario_base = novo
        if hasattr(pessoa, "bonus_chefia"):
            alterar_bonus = input("Deseja alterar o bônus de chefia? (s/n): ").lower()
            if alterar_bonus == "s":
                novo_bonus = float(input("Novo bônus de chefia: "))
                pessoa.bonus_chefia = novo_bonus
        print("\nPagamento atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao alterar pagamento: {e}")

    input("Pressione Enter para continuar...")


def excluir():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funções de cadastro
def cadastrar_paciente():
    excluir()
    print("=== Cadastro de Paciente ===")
    nome = entrada_obrigatoria("Nome: ")
    while True:
        idade = int(entrada_obrigatoria("Idade: "))
        if idade < 120 and idade >0:
                break
        else:
            print("Insira um valor positivo dentro dos padrões do século")
    while True:
        utente = entrada_obrigatoria("Número do Utente: ").strip()
        if len(utente) == 9 and utente.isdigit():
                break
        else:
            print("O número do utente deve ter pelo menos 9 dígitos numéricos.")
    paciente = Paciente(nome, idade, utente)
    pacientes_cadastrados.append(paciente)
    print("\nPaciente cadastrado com sucesso:")
    paciente.exibir_informacoes()
    input("Pressione Enter para continuar...")

def cadastrar_medico():
    excluir()
    print("=== Cadastro de Médico ===")
    nome = entrada_obrigatoria("Nome: ")
    while True:
        idade = int(entrada_obrigatoria("Idade: "))
        if idade < 120 and idade >0:
                break
        else:
            print("Insira um valor positivo dentro dos padrões do século")
    while True:
        salario = float(entrada_obrigatoria("Salário base: "))
        if salario < 10000000 and salario > 0:
                break
        else:
            print("Insira um valor positivo dentro do que o governo pode pagar!")
    especialidade = entrada_obrigatoria("Especialidade: ")
    medico = Medico(nome, idade, salario, especialidade)
    medicos_cadastrados.append(medico)
    print("\nMédico cadastrado com sucesso:")
    medico.exibir_informacoes()
    input("Pressione Enter para continuar...")

def cadastrar_enfermeiro():
    excluir()
    print("=== Cadastro de Enfermeiro ===")
    nome = entrada_obrigatoria("Nome: ")
    while True:
        idade = int(entrada_obrigatoria("Idade: "))
        if idade < 120 and idade > 0:
                break
        else:
            print("Insira um valor positivo dentro dos padrões do século")
    while True:
        salario = float(entrada_obrigatoria("Salário base: "))
        if salario < 10000000 and salario > 0:
                break
        else:
            print("Insira um valor positivo dentro do que o governo pode pagar!")
    while True:
        turno = entrada_obrigatoria("Turno (dia/noite): ").lower()
        if turno in ["dia", "noite"]:
            break
        else:
            print("Turno inválido. Digite 'dia' ou 'noite'.")
    enfermeiro = Enfermeiro(nome, idade, salario, turno)
    enfermeiros_cadastrados.append(enfermeiro)
    print("\nEnfermeiro cadastrado com sucesso:")
    enfermeiro.exibir_informacoes()
    input("Pressione Enter para continuar...")

def cadastrar_enfermeiro_chefe():
    excluir()
    print("=== Cadastro de Enfermeiro Chefe ===")
    nome = entrada_obrigatoria("Nome: ")
    while True:
        idade = int(entrada_obrigatoria("Idade: "))
        if idade < 120 and idade >0:
                break
        else:
            print("Insira um valor positivo dentro dos padrões do século")
    while True:
        salario = float(entrada_obrigatoria("Salário base: "))
        if salario < 10000000 and salario > 0:
                break
        else:
            print("Insira um valor positivo dentro do que o governo pode pagar!")
    while True:
        turno = entrada_obrigatoria("Turno (dia/noite): ")
        if turno == "dia" and turno == "noite":
                break
        else:
            print("Os turnos estão entre o dia/noite")
    setores_validos = ["emergência", "pediatria", "cirurgia", "clínica geral"]
    while True:
        setor = entrada_obrigatoria(f"Setor: [emergência, pediatria, cirurgia, clinica geral] ").lower()
        if setor in setores_validos:
            break
        else:
            print("Setor inválido. Tente: emergência, pediatria, cirurgia, clínica geral.")
    while True:
        bonus = float(entrada_obrigatoria("Bónus de chefia: (Até 1.000€) "))
        if bonus < 1000 and bonus > 0:
            break
        else:
            print("Bonus invalido.")
    chefe = EnfermeiroChefe(nome, idade, salario, turno, setor, bonus)
    chefes_cadastrados.append(chefe)
    print("\nEnfermeiro Chefe cadastrado com sucesso:")
    chefe.exibir_informacoes()
    input("Pressione Enter para continuar...")

def cadastrar_funcionario():
    excluir()
    print("=== Cadastro de Funcionário ===")
    nome = entrada_obrigatoria("Nome: ")
    while True:
        idade = int(entrada_obrigatoria("Idade: "))
        if idade < 120 and idade >0:
                break
        else:
            print("Insira um valor positivo dentro dos padrões do século")
    cargo = input("Cargo: ")
    while True:
        salario = float(entrada_obrigatoria("Salário base: "))
        if salario < 10000000 and salario > 0:
                break
        else:
            print("Insira um valor positivo dentro do que o governo pode pagar!")
    funcionario = Funcionario(nome, idade, cargo, salario)
    funcionarios_cadastrados.append(funcionario)
    print("\nFuncionário cadastrado com sucesso:")
    funcionario.exibir_informacoes()
    input("Pressione Enter para continuar...")

def cadastrar_administrador():
    excluir()
    print("=== Cadastro de Administrador ===")
    nome = entrada_obrigatoria("Nome: ")
    while True:
        idade = int(entrada_obrigatoria("Idade: "))
        if idade < 120 and idade >0:
                break
        else:
            print("Insira um valor positivo dentro dos padrões do século")
    salario = float(input("Salário: "))
    setores_validos = ["financeiro", "recursos humanos", "logística", "atendimento"]
    while True:
        setor = input(f"Setor: [financeiro, recursos humanos, logística, atendimento] ").lower()
        if setor in setores_validos:
            break
        else:
            print("Setor inválido. Tente: financeiro, recursos humanos, logística ou atendimento.")
    while True:
        horas = int(entrada_obrigatoria("Horas trabalhadas: (até 500hrs) "))
        if horas < 500 and horas > 0:
            break
        else:
            print("Suas horas não são validas.")
    administrador = Administrativo(nome, idade, salario, setor)
    administrador.registrar_horas(horas)
    administradores_cadastrados.append(administrador)
    print("\nAdministrador cadastrado com sucesso:")
    administrador.exibir_informacoes()
    administrador.calcular_pagamento()
    input("Pressione Enter para continuar...")


def listar(lista, titulo):
    excluir()
    print(f"=== {titulo} Cadastrados ===")
    if lista:
        for i, pessoa in enumerate(lista, 1):
            print(f"\n{i}.")
            try:
                pessoa.exibir_informacoes()
            except AttributeError:
                print(f"{pessoa.nome} ({pessoa.idade} anos)")
                print("Obs: método exibir_informacoes() não implementado.")
    else:
        print("Nenhum cadastro encontrado.")
    input("\nPressione Enter para continuar...")

while True:
    excluir()
    print("\n=== Hyspytol ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Pagamentos")
    print("4 - Criar Sala (Tipos)")
    print("5 - Consultas")
    print("6 - Encerrar programa")
    try:
        op = int(input("Escolha uma opção (1-6): "))
    except ValueError:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")
        continue

        
    match op:
        case 1 : 
            excluir()
            while True:
                excluir()
                print("\n=== Cadastrar ===")
                print("1 - Cadastrar Pacientes")
                print("2 - Cadastrar Médicos")
                print("3 -Cadastrar Enfermeiros")
                print("4 - Cadastrar Enfermeiro Chefe")
                print("5 - Cadastrar Funcionários")
                print("6 - Cadastrar Administradores")
                print("7 - voltar")
                try:
                    op = int(input("Escolha uma opção (1-7): "))
                except ValueError:
                    print("Opção inválida. Tente novamente.")
                    input("Pressione Enter para continuar...")
                    continue

                match op:
                    case 1: cadastrar_paciente()
                    case 2: cadastrar_medico()
                    case 3: cadastrar_enfermeiro()
                    case 4: cadastrar_enfermeiro_chefe()
                    case 5: cadastrar_funcionario()
                    case 6: cadastrar_administrador()
                    case 7: break
                    case _:
                        print("Opção inválida.")
                        input("Pressione Enter para continuar...")
                
        case 2 :
            excluir()
            while True:
                excluir()
                print("\n=== Listagem ===")
                print("1 - Listagem Pacientes")
                print("2 - Listagem Médicos")
                print("3 - Listagem Enfermeiros")
                print("4 - Listagem Enfermeiro Chefe")
                print("5 - Listagem Funcionários")
                print("6 - Listagem Administradores")
                print("7 - voltar")
                try:
                    op = int(input("Escolha uma opção (1-7): "))
                except ValueError:
                    print("Opção inválida. Tente novamente.")
                    input("Pressione Enter para continuar...")
                    continue

                match op:
                    case 1: listar(pacientes_cadastrados, "Pacientes")
                    case 2: listar(medicos_cadastrados, "Médicos")
                    case 3: listar(enfermeiros_cadastrados, "Enfermeiros")
                    case 4: listar(chefes_cadastrados, "Enfermeiros Chefes")
                    case 5: listar(funcionarios_cadastrados, "Funcionários")
                    case 6: listar(administradores_cadastrados, "Administradores")
                    case 7: break
                    case _:
                        print("Opção inválida.")
                        input("Pressione Enter para continuar...")
        case 3 :
            excluir()
            while True:
                excluir()
                print("\n=== Pagamentos ===")
                print("1 - Pagamentos Funcionários")
                print("2 - Pagamentos Médicos")
                print("3 - Pagamentos Enfermeiros")
                print("4 - Pagamento Enfermeiro Chefe")
                print("5 - Pagamento Administradores")
                print("6 - Alterar Pagamentos")
                print("7 - voltar")
                try:
                    op = int(input("Escolha uma opção (1-7): "))
                except ValueError:
                    print("Opção inválida. Tente novamente.")
                    input("Pressione Enter para continuar...")
                    continue

                match op:
                    case 1: pagamento(funcionarios_cadastrados, "Funcionários")
                    case 2: calcular_pagamento(medicos_cadastrados, "Médicos")
                    case 3: calcular_pagamento(enfermeiros_cadastrados, "Enfermeiros")
                    case 4: calcular_pagamento(chefes_cadastrados, "Enfermeiros Chefes")
                    case 5: calcular_pagamento(administradores_cadastrados, "Administradores")
                    case 6:
                        excluir()
                        print("\n=== Alterar Pagamentos ===")
                        print("1 - Funcionários")
                        print("2 - Médicos")
                        print("3 - Enfermeiros")
                        print("4 - Enfermeiros Chefes")
                        print("5 - Administradores")
                        print("6 - Voltar")
                        try:
                            sub_op = int(input("Escolha uma opção (1-6): "))
                        except ValueError:
                            print("Opção inválida.")
                            input("Pressione Enter para continuar...")
                            continue

                        match sub_op:
                            case 1: alterar_pagamento(funcionarios_cadastrados, "Funcionários")
                            case 2: alterar_pagamento(medicos_cadastrados, "Médicos")
                            case 3: alterar_pagamento(enfermeiros_cadastrados, "Enfermeiros")
                            case 4: alterar_pagamento(chefes_cadastrados, "Enfermeiros Chefes")
                            case 5: alterar_pagamento(administradores_cadastrados, "Administradores")
                            case 6: pass
                            case _: 
                                print("Opção inválida.")
                                input("Pressione Enter para continuar...")
                    case 7: break
                    case _:
                        print("Opção inválida.")
                        input("Pressione Enter para continuar...")
        case 4 :
            excluir()
            while True:
                excluir()
                print("\n=== Salas ===")
                print("1 - Ocupar Sala de Consulta")
                print("2 - Ocupar Sala de Cirurgia")
                print("3 - Desocupar Sala de Consulta")
                print("4 - Desocupar Sala de Cirugia")
                print("5 - voltar")
                try:
                    op = int(input("Escolha uma opção (1-5): "))
                except ValueError:
                    print("Opção inválida. Tente novamente.")
                    input("Pressione Enter para continuar...")
                    continue

                match op:
                    case 1:
                        sala_consulta_ocupada = None
                        sala_cirurgia_ocupada = None
                        excluir()
                        if not medicos_cadastrados or len(pacientes_cadastrados) < 1:
                            print("Cadastre pelo menos 1 médico e 1 paciente.")
                            input("Pressione Enter para continuar...")
                            continue

                        medico = medicos_cadastrados[0]
                        sala_consulta_ocupada = SalaConsulta(101, 1, medico)
                        for paciente in pacientes_cadastrados[:1]:
                            sala_consulta_ocupada.agendar_consulta(paciente)
                        sala_consulta_ocupada.exibir_informacoes()
                        input("Pressione Enter para continuar...")
                    case 2:
                        excluir()
                        if not medicos_cadastrados or not pacientes_cadastrados:
                            print("Cadastre pelo menos 1 médico e 1 paciente.")
                            input("Pressione Enter para continuar...")
                            continue
                        medico = medicos_cadastrados[0]
                        sala_cirurgia_ocupada = SalaCirurgia(101, 1, medico)
                        for paciente in pacientes_cadastrados[:1]:
                            sala_cirurgia_ocupada.agendar_consulta(paciente)
                        sala_cirurgia_ocupada.exibir_informacoes()
                        input("Pressione Enter para continuar...")
                    case 3:  # Desocupar Sala de Consulta
                        excluir()
                        if not medicos_cadastrados or len(pacientes_cadastrados) < 1:
                            print("Cadastre pelo menos 1 médico e 1 paciente.")
                            input("Pressione Enter para continuar...")
                            continue

                        if sala_consulta_ocupada:
                            sala_consulta_ocupada._pacientes_agendados.clear()
                            print("Sala de consulta desocupada com sucesso.")
                            sala_consulta_ocupada.exibir_informacoes()
                        else:
                            print("Nenhuma sala de consulta está ocupada.")
                        input("Pressione Enter para continuar...")

                    case 4:  # Desocupar Sala de Cirurgia
                        excluir()
                        if not medicos_cadastrados or not pacientes_cadastrados:
                            print("Cadastre pelo menos 1 médico e 1 paciente.")
                            input("Pressione Enter para continuar...")
                            continue

                        if sala_cirurgia_ocupada:
                            sala_cirurgia_ocupada._equipamentos.clear()
                            print("Sala de cirurgia desocupada com sucesso.")
                            sala_cirurgia_ocupada.exibir_informacoes()
                        else:
                            print("Nenhuma sala de cirurgia está ocupada.")
                        input("Pressione Enter para continuar...")
                    case 5: break
                    case _:
                        print("Opção inválida.")
                        input("Pressione Enter para continuar...")
        case 5:
            excluir()
            registrar_consulta()
            if sala_consulta_ocupada:
                paciente.adicionar_historico(f"Consulta com Dr. {medico.nome} em sala {sala_consulta_ocupada.numero}")
            else:
                print("Nenhuma sala de consulta está ocupada.")
        case 6:
            excluir()
            print("Sistema encerrado.")
            break
        case _:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")
