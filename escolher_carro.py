# Lista de carros disponíveis e suas características
carros = [
    {"nome": "Toyota Corolla", "tipo": "sedan", "combustivel": "gasolina", "preco": 120000},
    {"nome": "Honda HR-V", "tipo": "SUV", "combustivel": "gasolina", "preco": 150000},
    {"nome": "Renault Kwid", "tipo": "hatch", "combustivel": "gasolina", "preco": 80000},
    {"nome": "Chevrolet Onix", "tipo": "hatch", "combustivel": "flex", "preco": 90000},
    {"nome": "Jeep Compass", "tipo": "SUV", "combustivel": "diesel", "preco": 180000},
    {"nome": "Fiat Argo", "tipo": "hatch", "combustivel": "flex", "preco": 95000},
    {"nome": "Volkswagen Polo", "tipo": "hatch", "combustivel": "gasolina", "preco": 98000},
]

print("Bem-vindo ao sistema de escolha de carro novo!")
print("Responda algumas perguntas para receber uma sugestão:")

tipo = input("Qual tipo de carro você prefere? (sedan/hatch/SUV): ").strip().lower()
combustivel = input("Qual tipo de combustível você prefere? (gasolina/flex/diesel): ").strip().lower()
preco_max = int(input("Qual o valor máximo que você quer pagar? (em reais): "))

print("\nCarros sugeridos para você:")

encontrados = False
for carro in carros:
    if (
        carro["tipo"] == tipo
        and carro["combustivel"] == combustivel
        and carro["preco"] <= preco_max
    ):
        print(f"- {carro['nome']} ({carro['tipo']}, {carro['combustivel']}) - R${carro['preco']}")
        encontrados = True

if not encontrados:
    print("Nenhum carro encontrado com as suas preferências.")
