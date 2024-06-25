class BestSolutionReader:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def read_file(self):
        with open(self.file_name, 'r') as file:
            dados = file.read().split()
            caminho = [int(valor) -1 for valor in dados]
            return caminho
   
            