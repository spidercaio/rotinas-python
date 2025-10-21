rotinas = {} # Inicializando o dicionário vazio em escopo global
def main(): # Função principal main
    menu_opcoes() 
    
def menu_opcoes(): # Definindo a função que exibe o menu de opções
    while True: # O menu continuará sendo exibido até o usuário inserir 0
        opcao = input("\n -------------------\n Olá! Seja bem vindo! Você deseja:\n 1 - Definir uma rotina \n 2 - Visualizar suas rotinas \n 0 - Sair \n ------------------- \n")
        if opcao == "1":
            definir_rotina() # Se opção 1, o usuário irá definir uma rotina
        elif opcao == "2":
            visualizar_rotina() # Se opção 2, o usuário irá visualizar as rotinas
        elif opcao == "0": 
            break # Se opção 0, o programa encerrará
        else:
            print("Opção inválida!") # Caso nenhuma das opções, uma mensagem de erro será exibida
        
def check_dia(dia): # Definição da função para checar se o dia já foi definido
    global rotinas
    if dia in rotinas: # Se o dia já estiver no dicionário de rotinas
        verificacao = input("Esse dia já foi definido, deseja modificar? s/n ").lower() # Avisa o usuário e pede uma confirmação
        if verificacao != "s":
            main() # Se o usuário inserir "n", retorna ao menu principal, se não, segue o código
            
def visualizar_rotina(): # Definição da função para visualizar as rotinas
    if len(rotinas) > 0: # Se houver rotinas registradas
        print("Essas são todas as rotinas registradas: ")
        for dia in rotinas: # Para cada dia no dicionário de rotinas
            print(f"Dia: {dia.capitalize()} \nRotina:", end=" ") # Exibe o dia
            for tarefa in rotinas[dia]: # Para cada tarefa relacionada ao dia
                if tarefa == rotinas[dia][-1]: # Se for a última tarefa, exibe um ponto final em vez de vírgula
                    print(f"{tarefa.capitalize().strip()}", end=".\n")
                else:
                    print(f"{tarefa.capitalize().strip()}", end=", ") # Se caso não for, exibe uma vírgula ao final da tarefa
    else:
        print("Ainda não há nenhuma rotina registrada! ") # Se o tamanho do dicionário for 0, exibe uma mensagem
        
def definir_rotina(): # Definição da função para definir uma rotina
    global rotinas
    while True: # Loop para garantir que o usuário insira um dia válido
        dia = input("Para qual dia você deseja definir a rotina? ").lower().strip()
        check_dia(dia) # Chama a função para checar se esse dia já foi definido anteriormente
        if dia in ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"): # Se o dia inserido estiver presente em alguma dessas opções
            break # Se for válido, encerra o loop
        else:
            print("Dia inválido, tente novamente!") # Caso contrário, exibe mensagem de erro e retorna ao começo do loop
    input_usuario = input("Digite a rotina, separada por vírgula: ")
    rotina = input_usuario.split(',') # Divide a string com as rotinas em uma lista a partir das vírgulas
    match dia: # Estrutura match case para definir a rotina no dia correspondente
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
    print(f"Sua rotina para {dia} foi definida com sucesso!") # Mensagem de confirmação
main()
