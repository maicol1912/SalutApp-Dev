from werkzeug.security import generate_password_hash, check_password_hash

def encriptarPassword(password):
    passwordEncriptado = generate_password_hash(password, 'sha256',20)
    return passwordEncriptado

def comparePassword(passwordEncriptado,password):
    return check_password_hash(passwordEncriptado,password)
