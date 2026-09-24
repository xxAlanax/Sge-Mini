from no_produto import NoProduto
from constantes import ESTOQUE_MINIMO_PADRAO, MSG_PRODUTO_NAO_ENCONTRADO

class SistemaEstoque:
    def __init__(self):
        self.raiz = None

    def esta_vazio(self):
        return self.raiz is None
    
    def cadastrar_produto(self, codigo, nome, preco, quantidade):
        produto = {"Nome:": nome, "Preço:":preco, "Quantidade":quantidade}

        novo_produto = NoProduto(codigo, produto)

        if self.esta_vazio():
            self.raiz = novo_produto

        else:
            self._cadastrar(self.raiz, novo_produto)

    def _cadastrar(self, no_atual, no):
        if no.codigo < no_atual.codigo:
            if no_atual.esquerda is None:
                no_atual.esquerda = no

            else:
                self._cadastrar(no_atual.esquerda, no)

        elif no.codigo > no_atual.codigo:
            if no_atual.direita is None:
                no_atual.direita = no
                
            else:
                self._cadastrar(no_atual.direita, no)

        else:
            no_atual.produto = no.produto

    def consultar_produto(self, codigo):
        return self._buscar(self.raiz,codigo)

    def _buscar(self, no, codigo):
        if no is None:
            print(MSG_PRODUTO_NAO_ENCONTRADO)
            return None
        
        elif no.codigo == codigo:
            return no

        elif codigo < no.codigo:
            return self._buscar(no.esquerda, codigo)

        else:
            return self._buscar(no.direita, codigo)


    def listar_catalogo(self):
        return self._listar(self.raiz)

    def _listar(self, no):
        if no is None:
            return None
        
        else:
            self._buscar(no.esquerda)
            print(no.codigo, no.produto)
            self._buscar(no.direita)

    def calcular_valor_total_estoque(self):
    # TODO: retornar o valor total do estoque
    # (soma de preco * quantidade de todos os produtos).
        pass
    def produtos_estoque_baixo(self, minimo=ESTOQUE_MINIMO_PADRAO):
    # TODO: retornar a lista de produtos cuja quantidade
    # é menor que 'minimo'.
        pass
    def remover_produto(self, codigo):
    # TODO: remover o produto com esse código, mantendo
    # a propriedade da ABP para os produtos restantes.
        pass
    def diagnostico(self):
    # TODO: retornar a altura da árvore.
    # Serve para monitorar se o estoque está bem distribuído
    # (uma árvore muito "torta" deixa a busca mais lenta).
        pass
