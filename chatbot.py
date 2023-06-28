import ai21

ai21.api_key = 'dDG2hQfD5KPjyi3dugkSkDPxqz6Xm1rF'

contexto = """Um assistente virtual que sabe de tudo. Tudo que o usuario pede o assistente responde.
usuario: conte uma curiosidade
assistente: A cada minuto, cerca de 72 horas de conteúdo são enviadas ao site de vídeos Youtube.
usuario: me conte uma curiosidade
assistente: Estima-se que, a cada ano, o monte Everest cresça 4 milímetros.
"""


def executar(prompt):
    resposta = ai21.Completion.execute(
        model="j2-mid",
        prompt=prompt,
        numResults=1,
        maxTokens=200,
        temperature=0.5,
        topKReturn=0,
        topP=0.9,
        countPenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        frequencyPenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        presencePenalty={
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        stopSequences=["\n"],
    )
    return resposta['completions'][0]['data']['text']


if __name__ == '__main__':
    print('=' * 80)
    conversa = ''
    while True:
        prompt = input('usuario: ').strip()
        conversa += 'usuario: '+prompt+'\n'
        prompt_completo = contexto+conversa+'assistente:'
        resposta = executar(prompt_completo).strip()
        conversa += 'assistente: '+resposta+'\n'
        print('assistente: '+resposta)
