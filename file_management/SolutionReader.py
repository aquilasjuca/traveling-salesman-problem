class BestSolutionReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.best_solution = []

    def read_file(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        
        self.best_solution = [int(line.strip()) for line in lines]

    def get_best_solution(self):
        return self.best_solution
