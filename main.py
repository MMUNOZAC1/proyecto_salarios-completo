from salarios import calcular_salario
if __name__ == "__main__":
    try:
        h = float(input("Horas trabajadas: "))
        c = int(input("Categoría (1,2,3): "))
        salario = calcular_salario(h, c)
        print(f"Salario calculado: {salario:,.0f}")
    except ValueError as e:
        print("Error:", e)
    except Exception:
        print("Error: Entrada no válida.")
