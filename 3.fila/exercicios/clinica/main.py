from entites import Cliente,Fila
import os 

def menu():
    print('''
Clinica Medica - Atendimento
=============
1. Incluir paciente
2. Realizar chamada
3. Consultar a posição atual
4. Listar a quantidade de pacientes atendidos
5. Sair
    ''')
    op = int(input('Digite a opcao desejada: '))
    return op

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    fila = Fila()
    contador = 0
    while True:
        limpar_tela()
        op = menu()
        if op == 1:
            nome = input('Digite o nome do paciente: ')
            cpf = input('Digite o CPF do paciente: ')
            plano = input('Digite o plano do paciente(ou "n" para nenhum): ')
            if plano == 'n':
                paciente = Cliente(nome,cpf)
                fila.adicionar(paciente)
            else:
                paciente = Cliente(nome,cpf,plano)
                fila.adicionar(paciente)
            contador += 1

        elif op == 2:
            paciente = fila.remover()
            contador += 1
            print(f'Paciente {paciente.nome} atendido')
        elif op == 3:
            print(f'Posicao atual: {fila.posicao_atual(paciente.cpf)}')
            voltar = input('Pressione ENTER para voltar ao menu')
        elif op == 4:
            print(f'Quantidade de pacientes atendidos: {contador}')
            voltar = input('Pressione ENTER para voltar ao menu')
        elif op == 5:
            break
        
    print('Programa encerrado')
    print(fila)

if __name__ == '__main__':
    main()