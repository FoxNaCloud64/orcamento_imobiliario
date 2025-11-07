import csv

class Imovel:
    def __init__(self):
        self.valor_contrato = 2000.00
        self.aluguel_mensal = 0.0
    
    def mostrar_orcamento_final(self):
        print("\n--- ORÇAMENTO GERADO ---")
        print(f"Aluguel Mensal: R$ {self.aluguel_mensal:.2f}")
        print(f"Taxa de Contrato: R$ {self.valor_contrato:.2f} (em até 5x)")
        print("--------------------------")

    def gerar_csv(self):
        print("Gerando 'orcamento_anual.csv'...")
        with open('orcamento_anual.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Mês", "Valor Aluguel"])
            for i in range(1, 13):
                writer.writerow([f"Mês {i}", f"R$ {self.aluguel_mensal:.2f}"])
        print("Arquivo gerado com sucesso!")


class Apartamento(Imovel):
    def __init__(self, num_quartos, tem_garagem, sem_criancas):
        super().__init__()
        self.aluguel_mensal = 700.00 
        
        if num_quartos == 2:
            self.aluguel_mensal += 200.00
        
        if tem_garagem:
            self.aluguel_mensal += 300.00
            
        if sem_criancas:
            self.aluguel_mensal *= 0.95

            
class Casa(Imovel):
    def __init__(self, num_quartos, tem_garagem):
        super().__init__()
        self.aluguel_mensal = 900.00
        
        if num_quartos == 2:
            self.aluguel_mensal += 250.00
            
        if tem_garagem:
            self.aluguel_mensal += 300.00

            
class Estudio(Imovel):
    def __init__(self, vagas_estacionamento):
        super().__init__()
        self.aluguel_mensal = 1200.00
        if vagas_estacionamento == 2:
            self.aluguel_mensal += 250.00
        elif vagas_estacionamento > 2:
            self.aluguel_mensal += 250.00
            vagas_extras = vagas_estacionamento - 2
            self.aluguel_mensal += (vagas_extras * 60.00)


def main():
    print("---------------------------------------------")

    print(" Bem-vindo ao Sistema de Orçamento R.M.")
    print("---------------------------------------------")
    
    print("Qual tipo de imóvel você deseja?")
    print("1: Apartamento")
    print("2: Casa")
    print("3: Estúdio")
    
    tipo_imovel = ""
    while tipo_imovel not in ['1', '2', '3']:
        tipo_imovel = input("Digite o número (1, 2 ou 3): ")
    
    imovel_orcado = None # Inicializa a variável fora dos blocos if/elif
    
    if tipo_imovel == '1':
        print("\n--- Apartamento ---")
        quartos = int(input("Quantos quartos? (1 ou 2): "))
        garagem = input("Deseja vaga de garagem? (s/n): ").lower() == 's'
        criancas = input("Possui crianças? (s/n): ").lower() == 's'
        imovel_orcado = Apartamento(num_quartos=quartos, 
                                    tem_garagem=garagem, 
                                    sem_criancas=not criancas)

    elif tipo_imovel == '2':
        print("\n--- Casa ---")
        quartos = int(input("Quantos quartos? (1 ou 2): "))
        garagem = input("Deseja vaga de garagem? (s/n): ").lower() == 's'
        imovel_orcado = Casa(num_quartos=quartos, tem_garagem=garagem)

    elif tipo_imovel == '3':
        print("\n--- Estúdio ---")
        vagas = int(input("Quantas vagas de estacionamento deseja? (0, 2 ou mais): "))
        imovel_orcado = Estudio(vagas_estacionamento=vagas)

    
    if imovel_orcado:
        imovel_orcado.mostrar_orcamento_final()
        
        gerar_csv = input("\nDeseja gerar o arquivo .csv com 12 parcelas? (s/n): ").lower()
        if gerar_csv == 's':
            imovel_orcado.gerar_csv()

if __name__ == "__main__":
    main()