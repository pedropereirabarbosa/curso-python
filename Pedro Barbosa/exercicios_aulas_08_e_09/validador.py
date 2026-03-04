def validar_email(email:str):
    if email.count("@") >=1 or email.count(".") >= 1:
        return True
    else:
        return False

def validar_senha(senha):
    if len(senha) > 8:
        return True
    else:
        return False