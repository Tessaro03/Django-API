from validate_docbr import CPF


def nome_valido(nome):
    return nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def cpf_valido(cpf_validate):
    cpf = CPF()
    return cpf.validate(cpf_validate)