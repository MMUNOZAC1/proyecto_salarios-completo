def calcular_salario(horas, categoria):
    tarifas = {1: 12000, 2: 17000, 3: 22000}
    if horas < 0:
        raise ValueError("Horas inválidas: deben ser >= 0")
    if categoria not in tarifas:
        raise ValueError("Categoría inválida: debe ser 1, 2 o 3")
    tarifa = tarifas[categoria]
    if horas > 40:
        extras = horas - 40
        return 40 * tarifa + extras * tarifa * 1.25
    return horas * tarifa
