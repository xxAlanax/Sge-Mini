from no_produto import NoProduto
# modificação
from constantes import ESTOQUE_MINIMO_PADRAO, MSG_PRODUTO_REMOVIDO, MSG_PRODUTO_NAO_ENCONTRADO, MSG_PRODUTO_ATUALIZADO, ARQUIVO_EXPORTACAO

class SistemaEstoque:
    def __init__(self):
        self.raiz = None

    def esta_vazio(self):
        return self.raiz is None
    
# Cadastrando Produto
    def cadastrar_produto(self, codigo, nome, preco, quantidade):
        produto = {"Nome:": nome, "Preço:":preco, "Quantidade:":quantidade}
        # Objeto
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

# Consulta
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

# Listar Catalogo
    def listar_catalogo(self):
        catalogo = []
        self._listar(self.raiz, catalogo)
        return catalogo

    def _listar(self, no, catalogo):
        if no is not None:
            self._listar(no.esquerda, catalogo)
            catalogo.append([no.codigo, no.produto['Nome:'], no.produto['Preço:'], no.produto['Quantidade:']])
            self._listar(no.direita, catalogo)

# Calculo do valor do Estoque
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
        
# Estoque baixo            
    def produtos_estoque_baixo(self, minimo=ESTOQUE_MINIMO_PADRAO):
        baixo = []
    #Modificação
        self._minimo(self.raiz, minimo, baixo)
        return baixo
    
    def _minimo(self, no, minimo, baixo):
        if no is not None:
            self._minimo(no.esquerda, minimo, baixo)

            if no.produto['Quantidade:'] < minimo:
                baixo.append([no.codigo, no.produto['Nome:'], no.produto['Preço:'], no.produto['Quantidade:']])
                
            self._minimo(no.direita, minimo, baixo)
    
# Remover produtos
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


# Atualizar preco
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
            # Modificação
                print(MSG_PRODUTO_ATUALIZADO)
# Modificação
        elif codigo < no.codigo:
            return self._atualizar(no.esquerda, codigo, nome, preco, quantidade)
        
        else:
            return self._atualizar(no.direita, codigo, nome, preco, quantidade)
        
# Exportar catalogo para .txt (modificação)
    def exportar_catalogo(self, arq_exportado=ARQUIVO_EXPORTACAO):
        catalogo = self.listar_catalogo()

        with open(arq_exportado, "w", encoding="utf-8") as arquivo:
            arquivo.write("CÓDIGO - NOME - PREÇO - QUANTIDADE\n")

            for codigo, nome, preco, quantidade in catalogo:
                arquivo.write(f"{codigo:03d} - {nome} - R$ {preco:.2f} - {quantidade} un\n")

        return len(catalogo)
