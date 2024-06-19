class TSPFileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.num_city = 0
        self.dist_mat = []
        

    def read_file(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        
        self.dist_mat = []
        for line in lines:
            line = line.strip()
            if line:
                distances = list(map(float, line.split()))
                self.dist_mat.append(distances)

            self.num_cidades = len(self.dist_mat)

    def get_num_cities(self):
        return self.num_cidades
    
    def get_dist_mat(self):
        return self.dist_mat