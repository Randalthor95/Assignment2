import networkx as nx
import os


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
