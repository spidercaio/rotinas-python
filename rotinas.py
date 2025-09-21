rotinas = {}
def main():
    menu_opcoes() 
    
def menu_opcoes():
    while True:
        opcao = input("\n -------------------\n Olá! Seja bem vindo! Você deseja:\n 1 - Visualizar suas rotinas \n 2 - Definir uma rotina \n 0 - Sair \n ------------------- \n")
        if opcao == "1":
            visualizar_rotina()
        elif opcao == "2":
            definir_rotina()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
        
def check_dia(dia):
    global rotinas
    if dia in rotinas:
        verificacao = input("Esse dia já foi definido, deseja modificar? s/n ").lower()
        if verificacao != "s":
            main()
            
def visualizar_rotina():
    if len(rotinas) > 0:
        print(f"Essas são todas as rotinas registradas: \n {rotinas}")
    else:
        print("Ainda não há nenhuma rotina registrada! ")
        
def definir_rotina():
    global rotinas
    while True:
        dia = input("Para qual dia você deseja definir a rotina? ").lower().strip()
        check_dia(dia)
        if dia in ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"):
            break
        else:
            print("Dia inválido, tente novamente!")
    input_usuario = input("Digite a rotina, separada por vírgula: ")
    rotina = input_usuario.split(',')
    match dia:
        case "segunda":
            rotinas["segunda"] = rotina
        case "terça":
            rotinas["terça"] = rotina
        case "quarta":
            rotinas["quarta"] = rotina
        case "quinta":
            rotinas["quinta"] = rotina
        case "sexta":
            rotinas["sexta"] = rotina
        case "sábado":
            rotinas["sábado"] = rotina
        case "domingo":
            rotinas["domingo"] = rotina
    print(f"Sua rotina para {dia} foi definida com sucesso!")
main()