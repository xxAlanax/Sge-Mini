from no_produto import NoProduto
from constantes import ESTOQUE_MINIMO_PADRAO

class SistemaEstoque:
    def __init__(self):
        self.raiz = None
    def esta_vazio(self):
        return self.raiz is None
    def cadastrar_produto(self, codigo, nome, preco, quantidade):
        produto = {"Nome": nome, "Preço:":preco, "Quantidade":quantidade}
        NoProduto(codigo, produto)
    # TODO: criar/inserir um NoProduto respeitando a regra da ABP
    # (codigo menor -> esquerda, codigo maior -> direita).
    # Se o código já existir, decida e documente o comportamento
    # (ex.: atualizar o cadastro existente).
        pass
    def consultar_produto(self, codigo):
    # TODO: retornar os dados do produto com esse código,
    # ou None se o código não existir no estoque.
        pass
    def listar_catalogo(self):
    # TODO: retornar uma lista de produtos ordenada por código
    # (do menor para o maior).
        pass
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
