# src/hotel_ai/main.py

from hotel_ai.crew import crew

def testar_localmente():
    # Apenas para testes locais
    entrada = "A luz do quarto 302 está piscando constantemente."
    result = crew.kickoff(inputs={"mensagem_cliente": entrada})
    print(f"\nResposta gerada:\n{result}\n")

if __name__ == "__main__":
    testar_localmente()
