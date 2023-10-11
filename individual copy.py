import random
import networkx as nx

class Individual:
    def __init__(self, sets,graph):
        
        self.size = sum(len(s) for s in sets)
        # self.loci = [(None, None) for _ in range(self.size)]
        self.graph= graph
        self.loci = sorted(self.graph.edges())
        self.gene = {i:(None, None) for i in self.loci}
        # self.gene = [(None, None) for _ in range(self.size)]
        self._populate_individual(sets)

    def _populate_individual(self, sets):
        current_position = 0
        visited = {t: 0 for t in self.loci}

        for set in sets:
            # visited = {t: 0 for t in set}
            random_set = list(set)
            random_set.reverse()
            for cur_edge in set:
                value_assigned=False
                for other_edge in random_set:
                    if visited[other_edge] or other_edge == cur_edge: continue
                    if self.adjacent(cur_edge,other_edge):
                        self.gene[cur_edge]=other_edge
                        visited[other_edge]=1
                if not value_assigned:
                    for other_edge in random_set:
                        if not visited[other_edge]:
                            self.gene[cur_edge]=other_edge
                            visited[other_edge]=1


            # # random.shuffle(random_set)
            # for cur_tuple in set:
            #     value_assigned = False

            #     for other_tuple in random_set:
            #         if visited[other_tuple] or other_tuple == cur_tuple:
            #             continue
            #         if self.adjacent(cur_tuple, other_tuple):
            #             self.loci[current_position] = cur_tuple
            #             self.gene[current_position] = other_tuple
            #             current_position += 1
            #             value_assigned = True
            #             visited[other_tuple] = 1
            #             break

            #     if not value_assigned:
            #         for t in random_set:
            #             if(not visited[t]):
            #                 other_tuple = t
            #         self.loci[current_position] = cur_tuple
            #         self.gene[current_position] = other_tuple
            #         visited[cur_tuple] = 1
            #         current_position += 1

    def adjacent(self, t1, t2):
        if t1[0] == t2[0] or t1[0] == t2[1] or t1[1] == t2[0] or t1[1] == t2[1]:
            return True
        return False

    def decode(self):
        labels = {l: 0 for l in self.loci}
        c=1
        for locus, gene_value in self.gene:
            if labels[locus] == 0 and labels[gene_value]==0:
                labels[locus]=c
                labels[gene_value]=c
                c+=1
            elif labels[locus] == 0:
                labels[locus]= labels[gene_value]
            elif labels[gene_value] == 0:
                labels[gene_value]= labels[locus]
        
        # for i in range(self.size):
        #     if labels[self.loci[i]] == 0 and labels[self.gene[i]] == 0:
        #         labels[self.loci[i]]=c
        #         labels[self.gene[i]]=c
        #         c+=1
        #     elif labels[self.loci[i]] == 0:
        #         labels[self.loci[i]] = labels[self.gene[i]]
        #     elif labels[self.gene[i]] == 0:
        #         labels[self.gene[i]] = labels[self.loci[i]]

        value_to_keys = {}
        for key, value in labels.items():
            if value in value_to_keys:
                value_to_keys[value].add(key)
            else:
                value_to_keys[value] = {key}
        return list(value_to_keys.values())
            
    def get_gene(self,index):
        return self.loci[index],self.gene[index]
    
    def set_gene(self,index,loci_value,gene_value):
        self.gene[index]=gene_value
        self.loci[index]=loci_value

    def __eq__(self,other):
        for i in range(len(self.gene)):
            if (self.gene[i]!=other.gene[i] or self.loci[i]!=other.loci[i]) : return False
        return True

    def __str__(self):
        loci_str = ', '.join(map(str, self.loci))
        gene_str = ', '.join(map(str, self.gene))
        return f"Loci: [{loci_str}]\nGene: [{gene_str}]"

graph=nx.read_edgelist('graph.txt',nodetype=int)
# Example usage:
sets_list = [{(1, 2), (2, 3)}, {(4, 5), (5, 6), (4, 11)}, {(7, 8), (9, 10)}]
individual = Individual(sets_list)

# print(individual)
# print(individual1)
# print(individual2)

# # print(individual.decode())
# print(individual== individual1)
# print(individual== individual2)
# individual.set_gene(1,(11,22),(33,44))

print(individual)
