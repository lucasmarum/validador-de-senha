import re


def verificar_senha(txt):
    if len(txt) < 8:
        return False, "A senha deve conter no minimo 8 caracteres"
    if not re.search(r'[A-Z]', senha):
        return False, "A senha deve conter no minimo uma letra maiuscula"
    if not re.search(r'[a-z]', senha):
        return False, "A senha deve conter no minimo uma letra minuscula"
    if not re.search(r'\d', senha):
        return False, "A senha deve conter no minimo um número"
    return True, "A senha é robusta"


senha = input("Digite a sua senha: ")
resultado, mensagem = verificar_senha(senha)
print(mensagem)