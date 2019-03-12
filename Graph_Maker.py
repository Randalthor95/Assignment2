import networkx as nx
import os
import Graph_Maker as gm
import Simulator
import CSV_Maker
import Chart_Maker


def make_graph_from_file(file, infected, cure):
    G = nx.Graph()

    with open(file) as f:
        lines = f.readlines()

        for num, line in enumerate(lines):
            if num == 0:
                line2 = line[0:int(len(line) - 2)]
                for x in range(int(line2)):
                    if infected:
                        if cure:
                            G.add_node(x, infected=False, cured=False)
                        else:
                            G.add_node(x, infected=False)
            else:
                if line.strip() != '':
                    ints = line.strip().split(',')
                    G.add_edge(int(ints[0]), int(ints[1]))

    return G


def make_erdos_renyi(directory, file, n, m, seed):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file = directory + file + '.csv'

    f = open(file, 'w')
    f.write(str(n))
    f.write(',\n')
    G = nx.gnm_random_graph(n, m, seed)
    count = 1;
    while not nx.is_connected(G):
        print('fail')
        G = nx.gnm_random_graph(n, m, seed + count)
        count += 1
    edges = G.edges
    for edge in edges:
        line = str(edge[0]) + ',' + str(edge[1]) + '\n'
        f.write(line)

    print('file written')


def make_barabasi_albert(directory, file, n, m, seed):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file = directory + file + '.csv'

    f = open(file, 'w')
    f.write(str(n))
    f.write(',\n')
    G = nx.barabasi_albert_graph(n, m, seed)
    count = 1;
    while not nx.is_connected(G):
        print('fail')
        G = nx.barabasi_albert_graph(n, m, seed + count)
        count += 1

    edges = G.edges
    for edge in edges:
        line = str(edge[0]) + ',' + str(edge[1]) + '\n'
        f.write(line)

    print('file written')


def make_watts_strogatz(directory, file, n, k, p, seed):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file = directory + file + '.csv'

    f = open(file, 'w')
    f.write(str(n))
    f.write(',\n')
    G = nx.watts_strogatz_graph(n, k, p, seed)
    count = 1;
    while not nx.is_connected(G):
        print('fail')
        G = nx.watts_strogatz_graph(n, k, p, seed + count)
        count += 1

    edges = G.edges
    for edge in edges:
        line = str(edge[0]) + ',' + str(edge[1]) + '\n'
        f.write(line)

    print('file written')


def make_graphs(nodes, edges, seed, watts_p, infect_p, infect_node_zero, cure_node_zero, cure_p, times_to_run):
    b = 'Barabasi'
    e = 'Erdos'
    w = 'Watts'

    for i in range(3):
        if i is 0:
            graph_type = b
        elif i is 1:
            graph_type = w
        else:
            graph_type = e
            edges = edges * nodes


        for x in range(5):
            current_file = graph_type + '_' + str(nodes) + '_' + str(edges) + '_' + str(infect_p) + '_' + str(
                infect_node_zero)
            if cure_node_zero is not -1:
                current_file += '_' + str(cure_node_zero) + '_' + str(cure_p)

            current_path = 'F:/Documents/College/Colorado State/Security/Assignment 2 Sheets/' + graph_type + \
                           '/' + current_file + '/'

            current_file_csv = current_path + current_file + '.csv'
            if not os.path.isfile(current_file_csv):
                if graph_type is 'Barabasi':
                    gm.make_barabasi_albert(current_path, current_file, nodes, edges, seed)
                elif graph_type is 'Erdos':
                    gm.make_erdos_renyi(current_path, current_file, nodes, edges, seed)
                elif graph_type is 'Watts':
                    gm.make_watts_strogatz(current_path, current_file, nodes, edges, watts_p, seed)

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
            print(graph_type + ' Round: ' + str(x))