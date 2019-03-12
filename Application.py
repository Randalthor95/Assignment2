import Graph_Maker as gm
import Simulator
import CSV_Maker
import Chart_Maker
import os

# file1 = 'F:/Documents/College/Colorado State/Security/Assignment 2 Sheets/' \
#         'Barabasi/Barabasi_1000_2/Barabasi_1000_2_infect_infected_per_round.csv'
# file2 ='F:/Documents/College/Colorado State/Security/Assignment 2 Sheets/' \
#        'Erdos/erdos_10000_40000/erdos_10000_40000_infect_infected_per_round.csv'
#
# t_stat, p_val = CSV_Maker.t_test_from_files(file1, file2)
# print(t_stat)
# print (p_val)


nodes = 1000
edges = 5
seed = 3
watts_p = .5

infect_p = .5
infect_node_zero = 2

cure_node_zero = 500
cure_p = .5

times_to_run = 5

gm.make_graphs(nodes, edges, seed, watts_p, infect_p, infect_node_zero, cure_node_zero, cure_p, times_to_run)
