from blessings import Terminal
from openai import OpenAI
import json

client = OpenAI(
    api_key=''
)

def gerar_questao(topico):
    resposta = client.chat.completions.create(
        model ="gpt-3.5-turbo",
        menssages=[{
            "role": "system",
            "content":"""
                Você é um desenvolvedor muito experiente com conhecimento em diferentes 
                stacks e conceitos teóricos sobre programação e engenharia de software.
                Você está trabalahndo em um processo de contratação e seu trabalho agora é escrever perguntas
                para uma entrevista. Cada pergunta deve ter quarto respostas possíveis e uma delas 
                deve ser a correta. Escreva essas perguntas no seguinte formato:
                '{"pergunta": "Pergunta", "opcoes": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"], "certa": "Opção 1"}'
            """
        }, {
            "role": "user",
            "content": f"Gere uma questão sobre {topico}."

        }]
    )

    conteudo = resposta.choices[0].message.content
    return json.loads(conteudo)


pontos = 0
term = Terminal()
topico = input("Sobre qual tópico você quer responder? ")

while topico:
    print("Carregando...")
    questao = gerar_questao(topico)


    print(term.clear)
    print(term.bold_underline(questao['pergunta']))

    for i, opcao in enumerate(questao['opcoes'], start =1):
        print(f"{i}) {opcao}")

    resposta = int(input("Escolha uma opção[1-4]: ")) - 1

    escolhida = questao['opcoes'] [resposta].lower()
    certa = questao['certa'].lower()

    if escolhida == certa:
        pontos += 1
        print(term.green(f'Você acertou! Agora você tem {pontos} pontos\n'))
    else:
        print(
            term.red(f'Você errou! A resposta correta era: "{certa}"\n'))
        
    continuar = input("Quer continuar? (S/n) ")

    if continuar. lower() == 'n':
        break

print('Fim do programa')


#print(term.red('Mensagem de erro!'))
#print(term.green('Mensagem de sucesso!'))