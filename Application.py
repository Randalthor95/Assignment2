import Graph_Maker as gm
import Simulator
import CSV_Maker
import Chart_Maker

b = 'Barabasi'
e = 'Erdos'
w = 'Watts'

nodes = 1000
edges = 2
seed = 3
watts_p = .5
graph_type = b

infect_p = .2
infect_node_zero = 2


cure_node_zero = 500
cure_p = .5


current_file = graph_type + '_' + str(nodes) + '_' + str(edges) + '_' + str(infect_p) + '_' + str(infect_node_zero)
if cure_node_zero is not -1:
    current_file += '_' + str(cure_node_zero) + '_' + str(cure_p)

current_path = 'F:/Documents/College/Colorado State/Security/Assignment 2 Sheets/' + graph_type + \
               '/' + current_file + '/'



# if graph_type is 'Barabasi':
#     gm.make_barabasi_albert(current_path, current_file, nodes, edges, seed)
# elif graph_type is 'Erdos':
#     gm.make_erdos_renyi(current_path, current_file, nodes, edges, seed)
# elif graph_type is 'Watts':
#     gm.make_watts_strogatz(current_path, current_file, nodes, edges, watts_p, seed)

current_file_csv = current_path + current_file + '.csv'
if cure_node_zero is -1:

    infect_file = current_path + current_file + '_infect'
    lists = Simulator.simulate_infection(current_file_csv, infect_p, infect_node_zero)
    CSV_Maker.make_csv_from_infection(infect_file, lists)
    Chart_Maker.make_infected_charts(infect_file)

else:
    cure_file = current_path + current_file + '_cure'
    lists = Simulator.simulate_cure(current_file_csv, infect_p, cure_p, infect_node_zero, cure_node_zero)
    CSV_Maker.make_csv_from_cure(cure_file, lists)

    Chart_Maker.make_cured_charts(cure_file)
