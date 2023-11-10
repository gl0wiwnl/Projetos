class bombaCombustivel: 
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel): 
        self.tipoCombutivel = tipoCombustivel 
        self.valorLitro = valorLitro 
        self.quantidadeCombustivel = quantidadeCombustivel 
    
    def abastecePorValor(self, valor): 
        quantidade_litro = valor / self.valorLitro 
        if quantidade_litro <= self.quantidadeCombustivel: 
            self.quantidadeCombustivel -= quantidade_litro
            print (f"A quantidade de litros que foi colocada no veiculo é de {quantidade_litro: .2f}L \n") 
            print(f"A quantidade de litros na bomba é de {self.quantidadeCombustivel}L") 

        else: 
            print ("Bomba com quantidade de combustivel insuficiente") 
            print(f"A quantidade de litros na bomba é de {self.quantidadeCombustivel}L") 

    def abastecerPorLitro(self, litros1): 
        valorTotal = litros1 * self.valorLitro  
        if litros1 <= self.quantidadeCombustivel: 
            self.quantidadeCombustivel -= litros1 
            print (f"O valor a ser pago pelo cliente é de R${valorTotal: .2f} \n") 
            print(f"A quantidade de litros na bomba é de {self.quantidadeCombustivel}L") 

        else: 
            print ("Bomba com quantidade de combustivel insuficiente") 
            print(f"A quantidade de litros na bomba é de {self.quantidadeCombustivel}L") 

    
    def alterarValor(self, novoValor): 
        self.valorLitro = novoValor 
        print(self.valorLitro) 

    def alterarCombustivel(self, novoTipo): 
        self.tipoCombutivel = novoTipo 
        print(self.tipoCombutivel) 

    def alterarQuantidadeCombustivel(self, novaQuantidade): 
        self.quantidadeCombustivel = novaQuantidade 
        print(f"A quantidade de litros na bomba é de {self.quantidadeCombustivel}L") 
 