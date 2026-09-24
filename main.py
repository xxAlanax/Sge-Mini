from sistema_estoque import SistemaEstoque
from constantes import TITULO_SISTEMA, MENU_PRINCIPAL
def main():
    sistema = SistemaEstoque()

    while True:
        print(TITULO_SISTEMA)
        print(MENU_PRINCIPAL)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código:")
            nome = input("Nome:")
            preco = float(input("Preço:"))
            qtd = int(input("Quantidade:"))
            sistema.cadastrar_produto(codigo, nome, preco, qtd)

            # Modificação
            sistema.cadastrar_produto(
                codigo,
                nome,
                preco,
                quantidade
            )

            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            codigo = int(input("Código a ser consultado:"))
            resultado = sistema.consultar_produto(codigo)

            if resultado:
                if len(str(resultado.codigo)) < 3:
                    print("0"*(3 - len(str(resultado.codigo))) + str(resultado.codigo))

                else:
                    print(resultado.codigo)

                for info in resultado.produto:
                    print(info, resultado.produto[info])
                    
        elif opcao == "3":
            pass # TODO: chamar sistema.listar_catalogo()
        elif opcao == "4":
            pass # TODO: chamar sistema.calcular_valor_total_estoque()
        elif opcao == "5":
            pass # TODO: chamar sistema.produtos_estoque_baixo()
        elif opcao == "6":
            pass # TODO: chamar sistema.remover_produto(...)
        elif opcao == "7":
            pass # TODO: chamar sistema.diagnostico()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
        
if __name__ == "__main__":
    main()

