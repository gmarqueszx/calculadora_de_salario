import os

class Salary:
    def __init__(self, ganho_por_hora, horas_mes):
        self.ganho_por_hora = ganho_por_hora
        self.horas_mes = horas_mes

    def salario_bruto(self):
        return self.ganho_por_hora * self.horas_mes
    
    def pagoAoINSS(self):
        return self.salario_bruto() * 0.11
    
    def pagoAoSindicato(self):
        return self.salario_bruto() * 0.05
    
    def salarioLiquido(self):
        return self.salario_bruto() - self.pagoAoINSS() - self.pagoAoSindicato()

def obter_entrada_usuario():
    while True:
        try:
            ganho_por_hora = float(input('Quanto você recebe por hora: '))
            if ganho_por_hora <= 0:
                raise ValueError("O valor deve ser positivo.")
            
            horas_mes = float(input('Quantas horas você trabalha por mês: '))
            if horas_mes <= 0:
                raise ValueError("O valor deve ser positivo.")
            
            return Salary(ganho_por_hora, horas_mes)
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

def menu_principal(salario): 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('RH Conectsol - Salários \n')

        print('1. Salário Bruto')
        print('2. Pago ao INSS')
        print('3. Pago ao Sindicato')
        print('4. Salário Líquido')
        print('5. Sair\n')

        opcao_escolhida = input('Digite a opção escolhida de 1 a 5: ')

        if opcao_escolhida == '1':
            print(f'O seu salário bruto mensal é: R${salario.salario_bruto():.2f}')
        elif opcao_escolhida == '2':
            print(f'Você paga por mês ao INSS: R${salario.pagoAoINSS():.2f}')
        elif opcao_escolhida == '3':
            print(f'Você paga por mês ao Sindicato: R${salario.pagoAoSindicato():.2f}')
        elif opcao_escolhida == '4':
            print(f'O seu salário líquido mensal é: R${salario.salarioLiquido():.2f}')
        elif opcao_escolhida == '5':
            print('Saindo do sistema...')
            break
        else:
            print('Resposta inválida.')

        input('Pressione qualquer tecla para continuar: ')

def main():
    salario = obter_entrada_usuario()
    menu_principal(salario)

if __name__ == '__main__':
    main()
        