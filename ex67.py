def valida_email(email):
   
    if email.count('@') != 1:
        return False

    usuario, dominio = email.split('@')

    
    if not usuario or not dominio:
        return False

    
    if '.' not in dominio:
        return False

   
    dominio_partes = dominio.split('.')
    if len(dominio_partes) < 2 or len(dominio_partes[-1]) < 2:
        return False

    return True
