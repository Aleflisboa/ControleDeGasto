while True:
    ENTRADA = float(input("ENTRADA DO MÊS: "))
    if ENTRADA >= 0:
        break
    print("")


while True:
    try:
     ALIMENTACAO = float(input("ENTRADA DA ALIMENTAÇÃO: "))
     if ALIMENTACAO >= 0:
      break
     print("Valor Invalido")
    except ValueError:
     print("Apenas numero")
     
while True:
    try:
     DESPESAS = float(input("ENTRADA DAS DESPESAS: "))
     if DESPESAS >= 0:
        break
     print("Valor Invalido")
    except ValueError:
     print("Apenas numero")

while True:
    try:
     LAZER = float(input("ENTRADA DO LAZER: "))
     if LAZER >= 0:
       break
     print("Valor Invalido")
    except ValueError:
     print("Apenas número")

while True:
    try:
     TRANSPORTE = float(input("ENTRADA DO TRANSPORTE: "))
     if TRANSPORTE >= 0:
      break
     print("Valor Invalido")
    except ValueError:
        print("Apenas número")

def total_despesas(alimentacao, despesas, lazer, transporte):
    total = alimentacao + despesas + lazer + transporte
    return total

# Calculando as porcentagens
P_ALIMENTACAO = (ALIMENTACAO / ENTRADA) * 100
P_DESPESAS = (DESPESAS / ENTRADA) * 100
P_LAZER = (LAZER / ENTRADA) * 100
P_TRANSPORTE = (TRANSPORTE / ENTRADA) * 100
# Calculando o total
total = total_despesas(ALIMENTACAO, DESPESAS, LAZER, TRANSPORTE)

# Calculando o saldo restante
saldo = ENTRADA - total

# Calculando a porcentagem total
porcentagem_total = (total / ENTRADA) * 100

def PE(saldo):
    if saldo > 0:
        P_EMERGENCIA = (saldo * 50) / 100
        INVESTIMENTO = (saldo / 100) * 34.9
    else:
        P_EMERGENCIA = 0
        INVESTIMENTO = 0
        
    saldo_final = saldo - P_EMERGENCIA - INVESTIMENTO
    
    return P_EMERGENCIA, INVESTIMENTO, saldo_final

emergencia, investimento, restante= PE(saldo)

gastos = []
gasto = {
    "descricao": "Almoço",
    "categoria": "Alimentação",
    "valor": 25.00,
    "data": "08/11/2026"
}

gastos.append(gasto)


print(f"\nAlimentação: R$ {ALIMENTACAO:.2f} ({P_ALIMENTACAO:.2f}%)")
print(f"Despesas: R$ {DESPESAS:.2f} ({P_DESPESAS:.2f}%)")
print(f"Lazer: R$ {LAZER:.2f} ({P_LAZER:.2f}%)")
print(f"Transporte: R$ {TRANSPORTE:.2f} ({P_TRANSPORTE:.2f}%)")

print("=" * 50)
print(f"\nTOTAL GASTO: R$ {total:.2f}")
print(f"PORCENTAGEM GASTA: {porcentagem_total:.2f}%")
print(f"SALDO RESTANTE: R$ {saldo:.2f}")
print(f"SALDO DO INVESTIMENTO: R$ {investimento:.2f}")
print(f"DINHEIRO DA EMERGENCIA: R$ {emergencia:.2f}")

print("=" * 50)
print(f"SALDO RESTANTE: R$ {restante:.2f}")