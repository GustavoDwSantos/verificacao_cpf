"""
Validaçao do CPF

Os dois dígitos de verificação do CPF (constituído de 9 dígitos) são calculados através de um complicado algoritmo:

Etapa 1: cálculo de DV1
    Soma 1: soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro).
    Multiplique a soma 1 por 10 e calcule o resto da divisão do resultado por 11. Se der 10, DV1 é zero,caso contrário o DV1 é o próprio resto.

Etapa 2: cálculo de DV2
    Soma 2: soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa.
    Adicione a Soma 2 ao dobro do DV1, multiplique por 10 e calcule o resto da divisão do resultado por 11.
    Se der 10, DV2 é zero, caso contrário o DV2 é o próprio resto.

Etapa 3: Multiplique DV1 por 10, some com DV2 e você tem o número de controle do CPF.

Exemplo: para o CPF 398 136 146, temos:

Etapa 1: 2x6 + 3x4 + 4x1 + 5x6 + 6x3 + 7x1 + 8x8 + 9x9 + 10x3 = 258
2580 mod 11 = 6, portanto, DV1 = 6

Etapa 2: 3x6 + 4x4 + 5x1 + 6x6 + 7x3 + 8x1 + 9x8 + 10x9 + 11x3 = 299
(299 + 6x2)x10 mod 11 = 3150 mod 11 = 8, portanto DV2 = 8

Etapa 3: DV1x10 + DV2 = 6x10 + 8 = 68, que é o número procurado.
"""



def calculo_dv1(cpf):
    resultado = 0
    for i, digito in enumerate (cpf[::-1]):
        resultado += int(digito) * (i+2)
    resultado = resultado *10 % 11 
    return resultado if resultado < 10 else 0

def calculo_dv2(cpf):
    resultado = 0 
    for i, digito in enumerate(cpf[::-1]):
        resultado += int(digito) * (i+3)
    resultado = (resultado + calculo_dv1(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0

def calculo_dv(cpf):
    return calculo_dv1(cpf) * 10 + calculo_dv2(cpf)

def valida_cpf(cpf_completo):

    dv = calculo_dv(cpf_completo[:-2])
    return dv == int(cpf_completo[-2:])





