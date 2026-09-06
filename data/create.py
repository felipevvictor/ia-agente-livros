entrada = input().split()

transacoes_unicas = []

for text in entrada:
    if text not in transacoes_unicas:
        transacoes_unicas.append(text)

print(' '.join(transacoes_unicas))