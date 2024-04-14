# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    pattern = r"\(\d{2}\) \d{4}-\d{4}"
    
    if re.fullmatch(pattern, phone_number):
        return "Numero de telefone válido."

    else:
        return "Número de telefone inválido."
   
    
phone_number = input()  

validate_numero_telefone(phone_number)