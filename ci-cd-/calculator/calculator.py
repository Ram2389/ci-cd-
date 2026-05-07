#calculator for the CI-CD

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Operazioni disponibili: +, -, *, /")
    operation = input("Operazione: ")
    a = float(input("Primo numero: "))
    b = float(input("Secondo numero: "))

    if operation == "+":
        print(f"Risultato: {add(a, b)}")
    elif operation == "-":
        print(f"Risultato: {subtract(a, b)}")
    elif operation == "*":
        print(f"Risultato: {multiply(a, b)}")
    elif operation == "/":
        try:
            print(f"Risultato: {divide(a, b)}")
        except ValueError as e:
            print(f"Errore: {e}")
    else:
        print("Operazione non riconosciuta")
