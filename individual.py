import random


class Individual:
    def __init__(self, sets):
        self.size = sum(len(s) for s in sets)
        self.loci = [(None, None) for _ in range(self.size)]
        self.gene = [(None, None) for _ in range(self.size)]
        self._populate_individual(sets)

    def _populate_individual(self, sets):
        current_position = 0
        for set in sets:
            visited = {t: 0 for t in set}
            random_set = list(set)
            random.shuffle(random_set)
            for cur_tuple in set:
                value_assigned = False
                
                for other_tuple in random_set:
                    if visited[other_tuple] or other_tuple == cur_tuple:
                        continue
                    if self.adjacent(cur_tuple, other_tuple):
                        self.loci[current_position] = cur_tuple
                        self.gene[current_position] = other_tuple
                        current_position += 1
                        value_assigned = True
                        visited[other_tuple] = 1
                        break

                if not value_assigned:
                    for t in random_set:
                        if(not visited[t]): other_tuple=t 
                    self.loci[current_position] = cur_tuple
                    self.gene[current_position] = other_tuple
                    visited[cur_tuple] = 1
                    current_position += 1

    def adjacent(self, t1, t2):
        if t1[0] == t2[0] or t1[0] == t2[1] or t1[1] == t2[0] or t1[1] == t2[1]:
            return True
        return False

    def __str__(self):
        # Convert the loci and gene arrays to strings and format them
        loci_str = ', '.join(map(str, self.loci))
        gene_str = ', '.join(map(str, self.gene))

        # Return a formatted string
        return f"Loci: [{loci_str}]\nGene: [{gene_str}]"


# Example usage:
sets_list = [{(1, 2), (2, 3)}, {(4, 5), (5, 6), (4, 11)}, {(7, 8), (9, 10)}]
individual = Individual(sets_list)
print(individual)
