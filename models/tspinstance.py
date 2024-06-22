class TSPInstance:
    def __init__(self, name, comment, dimension, edge_weight_type, edge_weight_format, display_data_type):
        self.name = name
        self.comment = comment
        self.dimension = dimension
        self.edge_weight_type = edge_weight_type
        self.edge_weight_format = edge_weight_format
        self.display_data_type = display_data_type
        self.cities = []
        self.edge_weights = []

    def add_city(self, city):
        self.cities.append(city)

    def set_edge_weights(self, weights):
        self.edge_weights = weights

    def distance(self, city_index_1, city_index_2):
        if city_index_1 < 0 or city_index_1 >= len(self.edge_weights):
            raise IndexError(f"City index 1 out of range: {city_index_1}")
        if city_index_2 < 0 or city_index_2 >= len(self.edge_weights[city_index_1]):
            raise IndexError(f"City index 2 out of range: {city_index_2}")
        return self.edge_weights[city_index_1][city_index_2]

    def __str__(self):
        return f"TSP Instance: {self.name}, {self.comment}, {self.dimension} cities"