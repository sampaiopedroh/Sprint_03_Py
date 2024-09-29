# Simulador de Corrida de Fórmula E - Sprint 3

import time
import os

def criar_carro(velocidade_base, bateria_inicial, desgaste_pneu_inicial):
    """Cria um dicionário representando um carro com suas características."""
    return {
        "velocidade": velocidade_base,
        "bateria": bateria_inicial,
        "desgaste_pneu": desgaste_pneu_inicial
    }

def atualizar_carro(carro, tempo_corrida):
    """Atualiza as características do carro com base no tempo de corrida."""
    carro["velocidade"] -= tempo_corrida * 0.1  # Diminui a velocidade com o tempo
    carro["bateria"] -= tempo_corrida * 0.05  # Diminui a bateria com o tempo
    carro["desgaste_pneu"] += tempo_corrida * 0.02  # Aumenta o desgaste dos pneus com o tempo
    if carro["desgaste_pneu"] > 1:  # Se o desgaste dos pneus passar de 1, diminui a velocidade
        carro["velocidade"] -= 0.2

def exibir_estado_corrida(carros, tempo_corrida):
    """Exibe o estado atual da corrida."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela
    print(f"Tempo de corrida: {tempo_corrida} segundos")
    print("-" * 20)
    for i, carro in enumerate(carros):
        print(f"Carro {i+1}:")
        print(f"  Velocidade: {carro['velocidade']:.2f}")
        print(f"  Bateria: {carro['bateria']:.2f}%")
        print(f"  Desgaste do Pneu: {carro['desgaste_pneu']:.2f}")
        print("-" * 20)

def main():
    """Função principal do programa."""
    num_carros = int(input("Digite o número de carros na corrida: "))
    carros = []
    for i in range(num_carros):
        carros.append(criar_carro(100 + i * 5, 100, 0))

    tempo_corrida = 0
    while tempo_corrida < 100:  # Tempo total da corrida é 100
        exibir_estado_corrida(carros, tempo_corrida)
        
        # Interação do usuário para avançar o tempo
        input("Pressione Enter para avançar 1 segundo... \n") 

        carros.sort(key=lambda carro: carro["velocidade"], reverse=True)
        for carro in carros:
            atualizar_carro(carro, 1)
        tempo_corrida += 1

    print("\nCorrida finalizada!")

if __name__ == "__main__":
    main()
