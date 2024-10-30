if __name__ == '__main__':
    nombre = input("Proporciona un nombre: ")
    nom = " "
    match nombre:
        case "bertha": nom = "30-04-2004"
        case "esmeralda": nom = "30-06-2006"
        case "nayely": nom = "04-03-1981"
        case "manuel": nom = "08-02-1971"
        case " ": nom = "???????????"
    print(f"la fecha de nacimiento de {nombre} es: {nom}")
