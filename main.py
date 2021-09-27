from setup_pc import SistemaGeral

menu_head = "MENU DE FERRAMENTAS"
print("-"*27)
print(menu_head.center(27, " "))
print("-"*27)
print("1| Ver configurações do PC\n2| Teste de velocidade\n3| Temperatura")

escolha = int(input("Digite o valor correspondente a opção:  "))

print(" "*len(str(escolha)))

if escolha == 1:
    SistemaGeral.info_geral()
elif escolha == 2:
    print("Calculando a velocidade da internet...")
    SistemaGeral.internet_speed()   
elif escolha == 3:
    print("escolheu 3")

