""" 
This module performs basic arithmetic operations. 
"""

def suorita_laskutoimitus(p_operaatio, p_luku1, p_luku2):
    """ 
    Adds, subtracts, multiplies or divides two numbers 
    based on the given operation.
    The operation will be performed on the first number 
    using the second number."
    
    Args: 
        p_operaatio(str): The operation to perform ('+', '-', '*', '/'). 
        p_luku1 (float): The first number. 
        p_luku2 (float): The second number. 
    Returns: 
        float: the result of the calculation or
        string: "Tällä ohjelmalla ei pääse äärettömyyteen" 
            when given operation is divide ('/') and the divisor is 0.
    """
    tulos = "Tällä ohjelmalla ei pääse äärettömyyteen"
    if p_operaatio == "+":
        tulos =  p_luku1 + p_luku2
    elif p_operaatio == "-":
        tulos =  p_luku1 - p_luku2
    elif p_operaatio == "*":
        tulos =  p_luku1 * p_luku2
    elif p_operaatio == "/":
        if p_luku2 != 0:
            tulos = p_luku1 / p_luku2
    return tulos

operaatio = input("Valitse operaatio (+, -, *, /):  ")
if operaatio in ('+', '-', '*', '/'):
    try:
        luku1 = float(input("Anna luku1:  "))
        luku2 = float(input("Anna luku2:  "))

    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Tulos: ", suorita_laskutoimitus(operaatio, luku1, luku2))
else:
    print("Operaatiota ei ole olemassa")
