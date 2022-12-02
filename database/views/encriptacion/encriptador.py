from werkzeug.security import generate_password_hash, check_password_hash

def encriptarPassword(password):

    '''
    Nos permite llevar a cabo la incriptacón de las contraseñas ingresadas por los 
    usuario en :model: `database.Usuario`.
    '''
    passwordEncriptado = generate_password_hash(password, 'sha256',20)
    return passwordEncriptado

def comparePassword(passwordEncriptado,password):
    '''
    Hace la comparacion entre las contraseñas registradas por los usuarios en
    :model: `database.Usuario`, verifica su existencia y permite un acceso.
    '''
    return check_password_hash(passwordEncriptado,password)
