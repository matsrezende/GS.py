# GlobalSolution.py
O projeto em Python simula o consumo de energia de veículos elétricos, calcula distâncias percorridas e otimiza o consumo quando a distância ultrapassa 100 km. Além disso, grava dados em arquivo e oferece um menu interativo para simulação, visualização e otimização do consumo, visando uma mobilidade mais eficiente.

# Explicação do Código:
Veículos e Consumo de Energia:
Cada veículo tem um consumo por quilômetro e uma distância percorrida. O dicionário veiculos contém essas informações.

Simulação de Viagem:
A função simular_viagem() calcula o consumo de energia de um veículo com base na distância percorrida.

Otimização de Consumo:
A função otimizar_consumo() reduz o consumo de energia de um veículo em 10% quando a distância percorrida ultrapassa 100 km. Isso é uma simulação de otimização com base no uso contínuo.

Gravação de Dados em Arquivo:
A função gravar_em_arquivo() salva os dados de consumo em um arquivo consumo_energia_log.txt.

Exibição dos Dados:
A função exibir_dados_veiculos() mostra as distâncias percorridas e o consumo de cada veículo.

Interface do Usuário:
O programa oferece um menu interativo para que o usuário escolha entre simular uma viagem, visualizar dados dos veículos, otimizar o consumo de energia ou gravar os dados em um arquivo.

Identificação do Problema e Solução Proposta:

Identificação do Problema: Os veículos elétricos têm ganhado destaque como uma alternativa para a redução da emissão de gases poluentes e a preservação de recursos naturais.Mas, um dos principais desafios é a eficiência no uso de energia, já que uma gestão inadequada pode comprometer a autonomia dos veículos e aumentar o consumo de energia. Portanto, é necessário monitorar e otimizar o consumo de energia desses veículos para promover uma mobilidade mais eficiente e sustentável.

# Solução Proposta: 
O sistema desenvolvido visa monitorar o consumo de energia dos veículos elétricos, calcular o impacto das viagens e otimizar o consumo com base em condições pré-definidas (como a distância percorrida). O sistema simula viagens, registra o consumo energético e otimiza o uso de energia quando o veículo alcança uma certa distância. O usuário pode visualizar dados detalhados e salvar o histórico de consumo em um arquivo para análise posterior.
