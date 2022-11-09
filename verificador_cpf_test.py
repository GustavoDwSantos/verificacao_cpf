from verificador_cpf import calculo_dv, calculo_dv1, calculo_dv2, valida_cpf

def test_calculo_dv1():
    assert calculo_dv1("398136146") == 6
    assert calculo_dv1("511379278") == 0
    assert calculo_dv1("123456789") == 0

def test_calculo_dv2():
    assert calculo_dv2("398136146") == 8
    assert calculo_dv2("511379278") == 1
    assert calculo_dv2("123456789") == 9

def test_calculo_dv():
    assert calculo_dv("398136146") == 68
    assert calculo_dv("511379278") == 1
    assert calculo_dv("123456789") == 9

def test_valida_cpf():
    assert valida_cpf("39813614668") == True
    assert valida_cpf("51137927801") == True
    assert valida_cpf("12345678987") == False
    assert valida_cpf("12345678909") == True
    assert valida_cpf("12345678990") == False


    
    
