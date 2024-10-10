print(" ")
print("Alvaro Campechano 3W")
print(" ")
def es_email_valido(email):
    """
    Verifica si una dirección de correo electrónico es válida.
    
    Args:
    email (str): La dirección de correo electrónico a verificar.
    
    Returns:
    bool: True si es válida, False si no lo es.
    """
    return '@' in email

# Captura de la dirección de email
email_input = input("Por favor, ingresa tu dirección de correo electrónico: ")

# Verificación de la dirección de email
if es_email_valido(email_input):
    print("La dirección de correo electrónico es válida.")
else:
    print("La dirección de correo electrónico no es válida.")

