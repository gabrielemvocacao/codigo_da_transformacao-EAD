from datetime import datetime

nome = input("Digite seu nome: ")

hora = datetime.now().hour

print("Oi,", nome, "! Agora são", hora, "horas.")