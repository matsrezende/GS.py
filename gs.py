import random

# Dados de veículos elétricos e seus consumos
veiculos = {
    'Carro Elétrico 1': {'consumo_por_km': 0.2, 'distancia_percorrida': 0},
    'Carro Elétrico 2': {'consumo_por_km': 0.25, 'distancia_percorrida': 0},
    'Carro Elétrico 3': {'consumo_por_km': 0.18, 'distancia_percorrida': 0},
    'Carro Elétrico 4': {'consumo_por_km': 0.3, 'distancia_percorrida': 0}
}

# Função para calcular o consumo total de energia de um veículo
def calcular_consumo_energia(veiculo):
    return veiculos[veiculo]['consumo_por_km'] * veiculos[veiculo]['distancia_percorrida']

# Função para simular o consumo dos veículos em uma viagem
def simular_viagem(veiculo, distancia):
    veiculos[veiculo]['distancia_percorrida'] += distancia
    consumo = calcular_consumo_energia(veiculo)
    print(f'{veiculo} percorreu {distancia} km e consumiu {consumo:.2f} kWh.')
    return consumo

# Função para otimizar o consumo energético
def otimizar_consumo(veiculo):
    # Se a distância percorrida for muito alta, vamos otimizar o consumo reduzindo-o em 10%
    if veiculos[veiculo]['distancia_percorrida'] > 100:
        veiculos[veiculo]['consumo_por_km'] *= 0.9  # Reduzir 10% no consumo
        print(f'O consumo do {veiculo} foi otimizado em 10%. Novo consumo por km: {veiculos[veiculo]["consumo_por_km"]:.2f} kWh/km')

# Função para registrar os dados de consumo em um arquivo
def gravar_em_arquivo():
    try:
        with open("consumo_energia_log.txt", "w") as arquivo:
            for veiculo in veiculos:
                consumo_total = calcular_consumo_energia(veiculo)
                arquivo.write(f'{veiculo}: {consumo_total:.2f} kWh\n')
        print('Dados gravados com sucesso em consumo_energia_log.txt')
    except Exception as e:
        print(f'Erro ao gravar os dados: {e}')

# Função para exibir os dados de consumo
def exibir_dados_veiculos():
    for veiculo in veiculos:
        consumo = calcular_consumo_energia(veiculo)
        print(f'{veiculo} - Distância Percorrida: {veiculos[veiculo]["distancia_percorrida"]} km, Consumo: {consumo:.2f} kWh')

# Função principal para gerenciar o sistema
def sistema_de_monitoramento():
    print("Sistema de Monitoramento de Consumo de Energia para Veículos Elétricos")
    while True:
        print("\nEscolha uma opção:")
        print("1. Simular Viagem de um Veículo")
        print("2. Exibir Dados dos Veículos")
        print("3. Otimizar Consumo de Energia")
        print("4. Gravar Dados em Arquivo")
        print("5. Sair")
        
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            veiculo = input("Escolha um veículo (Carro Elétrico 1, Carro Elétrico 2, Carro Elétrico 3, Carro Elétrico 4): ")
            distancia = float(input("Digite a distância percorrida (em km): "))
            simular_viagem(veiculo, distancia)

        elif opcao == '2':
            exibir_dados_veiculos()

        elif opcao == '3':
            veiculo = input("Escolha um veículo para otimizar o consumo: ")
            otimizar_consumo(veiculo)

        elif opcao == '4':
            gravar_em_arquivo()

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Rodando o sistema de monitoramento
sistema_de_monitoramento()
