from models.tspinstance import *
from models.city import *
class TSPParser:
    def __init__(self, tsp_file_path, solution_file_path):
        self.tsp_file_path = tsp_file_path
        self.solution_file_path = solution_file_path

    def parse_tsp_file(self):
        with open(self.tsp_file_path, 'r') as f:
            lines = f.readlines()

        name = lines[0].split(":")[1].strip()
        tsp_type = lines[1].split(":")[1].strip()
        comment = lines[2].split(":")[1].strip()
        dimension = int(lines[3].split(":")[1].strip())
        edge_weight_type = lines[4].split(":")[1].strip()
        edge_weight_format = lines[5].split(":")[1].strip()
        display_data_type = lines[6].split(":")[1].strip()

        tsp_instance = TSPInstance(name, comment, dimension, edge_weight_type, edge_weight_format, display_data_type)

        # Parse edge weights
        edge_weights = []
        edge_weight_section_start = lines.index('EDGE_WEIGHT_SECTION\n') + 1
        edge_weight_section_end = lines.index('DISPLAY_DATA_SECTION\n')

        for i in range(edge_weight_section_start, edge_weight_section_end):
            edge_weights.append(list(map(int, lines[i].strip().split())))
        
        tsp_instance.set_edge_weights(edge_weights)

        # Parse cities
        display_data_section_start = edge_weight_section_end + 1
        for i in range(display_data_section_start, len(lines)):
            city_data = lines[i].strip().split()
            if len(city_data) == 3:
                city = City(int(city_data[0]), float(city_data[1]), float(city_data[2]))
                tsp_instance.add_city(city)
            else:
                print(f"Skipping invalid line: {lines[i]}")

        return tsp_instance

    def parse_solution_file(self):
        with open(self.solution_file_path, 'r') as f:
            solution = [list(map(int, line.strip().split())) for line in f]

        return solution