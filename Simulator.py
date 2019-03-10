import Graph_Maker as gm;
import random
import networkx as nx


def simulate_infection(file, p, node_zero):
    G = gm.make_graph_from_file(file, True, False)
    infected_count = 1
    G.nodes[node_zero]['infected'] = True
    infected_per_round = [1];
    total_infected = [1]
    while infected_count < G.number_of_nodes():
        infected_nodes = []
        for i, node in enumerate(G):
            if G.nodes[i]['infected']:
                infected_nodes.append(i)

        infected_this_round_count = 0;
        for node in infected_nodes:
            for neighbor in G.adj[node]:
                if G.nodes[neighbor]['infected'] is False and (random.uniform(0, 1) <= p):
                    G.nodes[neighbor]['infected'] = True
                    infected_count += 1
                    infected_this_round_count += 1
        infected_per_round.append(infected_this_round_count)
        total_infected.append(infected_count)

    return [infected_per_round, total_infected]


def simulate_cure(file, p, p_prime, infected_node_zero, cure_node_zero):
    if infected_node_zero == cure_node_zero:
        return AssertionError('infected node zero cannot be the same as cure node zero')

    G = gm.make_graph_from_file(file, True, True)
    print(nx.is_connected(G))
    G.nodes[infected_node_zero]['infected'] = True
    G.nodes[cure_node_zero]['cured'] = True

    ever_infected_count = 1
    current_infected_count = 1
    cured_count = 1
    infected_per_round = [1]
    cured_per_round = [1]
    total_ever_infected = [1]
    total_current_infected = [1]
    total_cured = [1]

    while cured_count < G.number_of_nodes():
        infected_nodes = []
        for i, node in enumerate(G):
            if G.nodes[i]['infected'] and not G.nodes[i]['cured']:
                infected_nodes.append(i)

        infected_this_round_count = 0
        for node in infected_nodes:
            for neighbor in G.adj[node]:
                if G.nodes[neighbor]['cured'] is False and G.nodes[neighbor]['infected'] is False and (
                        random.uniform(0, 1) <= p):
                    G.nodes[neighbor]['infected'] = True
                    ever_infected_count += 1
                    infected_this_round_count += 1
                    current_infected_count +=1
        infected_per_round.append(infected_this_round_count)
        total_ever_infected.append(ever_infected_count)
        print('ever_infected_count: ' + str(ever_infected_count))

        cured_nodes = []
        for i, node in enumerate(G):
            if G.nodes[i]['cured']:
                cured_nodes.append(i)

        cured_this_round_count = 0
        for node in cured_nodes:
            for neighbor in G.adj[node]:
                if G.nodes[neighbor]['cured'] is False and (random.uniform(0, 1) <= p_prime):
                    if G.nodes[neighbor]['infected']:
                        current_infected_count -= 1
                        G.nodes[neighbor]['infected'] = False
                    G.nodes[neighbor]['cured'] = True
                    cured_count += 1
                    cured_this_round_count += 1
        cured_per_round.append(cured_this_round_count)
        total_cured.append(cured_count)
        total_current_infected.append(current_infected_count)
        print('cured_count: ' + str(cured_count))

    return [infected_per_round, total_ever_infected, total_current_infected, cured_per_round, total_cured]
