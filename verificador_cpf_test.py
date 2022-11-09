from verificador_cpf import _calculo_dv, _calculo_dv1, _calculo_dv2, valida_cpf,tamanho_cpf,limpar_mascara,_gerador_digitos, adiciona_dv, gerador_cpf_aleatorio, adicionar_mascara

def test_calculo_dv1():
    assert _calculo_dv1("398136146") == "6"
    assert _calculo_dv1("511379278") == "0"
    assert _calculo_dv1("123456789") == "0"

def test_calculo_dv2():
    assert _calculo_dv2("398136146") == "8"
    assert _calculo_dv2("511379278") == "1"
    assert _calculo_dv2("123456789") == "9"

def test_calculo_dv():
    assert _calculo_dv("398136146") == "68"
    assert _calculo_dv("511379278") == "01"
    assert _calculo_dv("123456789") == "09"

def test_valida_cpf():
    assert valida_cpf("39813614668") == True
    assert valida_cpf("51137927801") == True
    assert valida_cpf("12345678987") == False
    assert valida_cpf("12345678909") == True
    assert valida_cpf("12345678990") == False

def test_tamanho_cpf():
    assert tamanho_cpf("39813614668") == True
    assert tamanho_cpf("12314") == False
    assert tamanho_cpf("511.379.278-01") == True

def test_limpar_mascara():
    assert limpar_mascara("511.379.278-01") == "51137927801"
    assert limpar_mascara("123.456.789-09") == "12345678909"
    assert limpar_mascara("398.136.146.68") == "39813614668"    
    assert limpar_mascara("000.000.000-00") == "00000000000"
    assert limpar_mascara("...-") == ""
    assert limpar_mascara("") == ""

def test_gerador_digitos():
    assert len(_gerador_digitos()) == 9
    assert _gerador_digitos().isdigit() == True

def test_adiciona_dv():
    assert adiciona_dv("511379278") == "51137927801"
    assert adiciona_dv("398136146") == "39813614668"
    assert adiciona_dv("123456789") == "12345678909"

def test_gerador_cpf():
    assert len(gerador_cpf_aleatorio()) == 11
    assert valida_cpf (gerador_cpf_aleatorio()) == True

def test_adicionar_mascara():
    assert adicionar_mascara("12345678909") == '123.456.789-09' 
    