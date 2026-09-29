from sistema_estoque import SistemaEstoque
from constantes import TITULO_SISTEMA, MENU_PRINCIPAL, MSG_PRODUTO_CADASTRADO
def main():
    sistema = SistemaEstoque()

    while True:
        print(TITULO_SISTEMA)
        print(MENU_PRINCIPAL)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = int(input("Código:"))
            nome = input("Nome:")
            preco = float(input("Preço:"))
            quantidade = int(input("Quantidade:"))

            # Modificação
            sistema.cadastrar_produto(
                codigo,
                nome,
                preco,
                quantidade
            )

            print(MSG_PRODUTO_CADASTRADO)

        elif opcao == "2":
            codigo = int(input("Código a ser consultado: "))
            resultado = sistema.consultar_produto(codigo)


            if resultado:
                print("Codigo: ")
                if len(str(resultado.codigo)) < 3:
                    print("0"*(3 - len(str(resultado.codigo))) + str(resultado.codigo))

                else:
                    print(resultado.codigo)

                for info in resultado.produto:
                    print(info, resultado.produto[info])
                    
        elif opcao == "3":
            sistema.listar_catalogo()

        elif opcao == "4":
            print(f"Valor Total do estoque: R$ {sistema.calcular_valor_total_estoque() :.2f}")

        elif opcao == "5":
            sistema.produtos_estoque_baixo()
        elif opcao == "6":
            codigo = int(input("Código a ser removido: "))
            sistema.remover_produto(codigo)

        elif opcao == "7":
            print('Altura da árvore do estoque:', sistema.diagnostico())

        elif opcao == "8":
            codigo = input("Código do produto a ser atualizado: ") 
            nome = input("Novo nome: ") 
            preco = float(input("Novo preço: ") )
            quantidade = int(input("Nova quantidade:"))

            sistema.atualizar_valores(codigo, nome, preco, quantidade)

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
        
if __name__ == "__main__":
    main()
