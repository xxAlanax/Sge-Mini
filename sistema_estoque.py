from no_produto import NoProduto
from constantes import ESTOQUE_MINIMO_PADRAO, MSG_PRODUTO_REMOVIDO, MSG_PRODUTO_NAO_ENCONTRADO

class SistemaEstoque:
    def __init__(self):
        self.raiz = None

    def esta_vazio(self):
        return self.raiz is None
    
    def cadastrar_produto(self, codigo, nome, preco, quantidade):
        produto = {"Nome:": nome, "Preço:":preco, "Quantidade:":quantidade}

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
        if no is not None:
            self._listar(no.esquerda)

            print(no.codigo, end = " - ")
            print(no.produto['Nome:'], end = " - ")
            print('R$',no.produto['Preço:'], end = " - ")
            print(no.produto['Quantidade:'], 'un')

            self._listar(no.direita)



    def calcular_valor_total_estoque(self):
        return self._calcular(self.raiz)

    def _calcular(self, no):
        if no is None:
            return 0
        
        else:
            esquerda = self._calcular(no.esquerda)
            direita = self._calcular(no.direita)
            valor = no.produto['Preço:'] * no.produto['Quantidade:']

            return esquerda + valor + direita        
            
    def produtos_estoque_baixo(self, minimo=ESTOQUE_MINIMO_PADRAO):
        return self._minimo(self.raiz, minimo)
    
    def _minimo(self, no, minimo):
        if no is not None:
            self._minimo(no.esquerda, minimo)

            if no.produto["Quantidade:"] < minimo:
                print(no.codigo, end = " - ")
                print(no.produto['Nome:'], end = " - ")
                print('R$',no.produto['Preço:'], end = " - ")
                print(no.produto['Quantidade:'], 'un')
        
            self._minimo(no.direita, minimo)
    
    def remover_produto(self, codigo):
        self.raiz = self._remover(self.raiz, codigo)
    
    def _remover(self, no, codigo):
        if no is None:
            print(MSG_PRODUTO_NAO_ENCONTRADO)
            return None
        
        elif no.codigo == codigo:
            # 1
            if no.esquerda == None and no.direita == None:
                print(MSG_PRODUTO_REMOVIDO)
                return None


            # 2
            elif no.direita == None:
                print(MSG_PRODUTO_REMOVIDO)
                return no.esquerda

            elif no.esquerda == None:
                print(MSG_PRODUTO_REMOVIDO)
                return no.direita

            # 3
            else:
                sucessor = self._menor(no.direita)
                no.direita = self._remover(no.direita, sucessor.codigo)

                no.codigo = sucessor.codigo
                no.produto = sucessor.produto

                return no
            

        elif codigo < no.codigo:
            no.esquerda = self._remover(no.esquerda, codigo)

        else:
            no.direita = self._remover(no.direita, codigo)

        return no

    def _menor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual
        

    def diagnostico(self):
        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return 0

        
        esquerda = self._altura(no.esquerda)
        direita = self._altura(no.direita)

        return 1 + max(esquerda, direita)

    def atualizar_valores (self, codigo, nome, preco, quantidade):
        self._atualizar(self.raiz, codigo, nome, preco, quantidade)

    def _atualizar (self, no, codigo, nome, preco, quantidade):
        if no is None:
            print(MSG_PRODUTO_NAO_ENCONTRADO)
            return None
                
        elif no.codigo == codigo:
                no.produto['Nome:'] = nome
                no.produto['Preço:'] = preco
                no.produto['Quantidade:'] = quantidade
        
        elif codigo < no.codigo:
            return self._atualizar(no.esquerda, codigo)
        
        else:
            return self._atualizar(no.direita, codigo)
        
