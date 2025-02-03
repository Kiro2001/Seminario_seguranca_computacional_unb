from geradorChave import criarChaves, lerChaves
from assinador import assinar_documento, assinar_msg
from verificador import verificar_documento, verificar_msg

if __name__ == "__main__":
    print("Escolha uma opção para executar:\n")
    print("\t1 - Gerar chaves")
    print("\t2 - Assinar documento")
    print("\t3 - Verificar assinatura")
    print("\t4 - Demostração com inputs sem OAEP e sem arquivos")
    opcao = input("Opção: ")
    match opcao:
        case "1":
            chave_publica, chave_privada = criarChaves(1024)
            with open("public.pem", "w") as f:
                f.write(f"{chave_publica[0]}\n{chave_publica[1]}")
            with open("private.pem", "w") as f:
                f.write(f"{chave_privada[0]}\n{chave_privada[1]}")
        case "2":
            chave_publica, chave_privada = lerChaves("public.pem", "private.pem")
            msg = input("Digite a mensagem a ser assinada: ")
            nome_arquivo = input("Digite o nome do arquivo a ser salvo: ")
            assinar_documento(
                mensagem_claro=msg,
                chave_publica=chave_publica,
                chave_privada=chave_privada,
                nome_arquivo=nome_arquivo,
            )
        case "3":
            chave_publica, chave_privada = lerChaves("public.pem", "private.pem")
            nome_arquivo = input("Digite o nome do arquivo a ser verificado: ")
            verificacao = verificar_documento(
                nome_arquivo, chave_publica, chave_privada
            )
            print("Assinatura válida" if verificacao else "Assinatura inválida")
            
        case "4":
            msg = input("Digite a sua mensagem:")
            print("")
            chave_publica, chave_privada = criarChaves(1024)
            assinatura = assinar_msg(msg, chave_privada)
            print(assinatura)
            print("")

            print(f"Verificação:{verificar_msg(msg,chave_publica,assinatura)}")
            print("")
            mud= input("DIgite qual mudança na string para demostrar a propriedade de integridade:")
            print("")
            msg=msg + mud
            print(msg)
            print("")
            print(f"Verificação:{verificar_msg(msg,chave_publica,assinatura)}")
            print("")

            print("Retornando a string ao normal \n")
            msg=msg[0:-len(mud)]
            print(msg)
            print("")
            print(f"Verificação:{verificar_msg(msg,chave_publica,assinatura)}")

        case _:
            print("Opção inválida")
        