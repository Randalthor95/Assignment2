import matplotlib.pyplot as plt
import CSV_Maker
import numpy as np
import matplotlib.patches as mpatches


def flatten_list_of_lists(lists):
    new_list = []
    for list in lists:
        for item in list:
            new_list.append(item)

    return new_list

def make_scatter_chart_from_file(file,  x_label, y_label, title):
    lists = CSV_Maker.read_csv(file)
    ax = plt.subplot()
    times = []
    for list in lists:
        time = []
        for x, val in enumerate(list):
            time.append(x)
        times.append(time)

    lists = flatten_list_of_lists(lists)
    times = flatten_list_of_lists(times)
    ax.scatter(times, lists)
    plt.plot(np.unique(times), np.poly1d(np.polyfit(times, lists, 5))(np.unique(times)))

    infected_label = mpatches.Patch(color='red', label='Infected')
    plt.legend([infected_label], ["Infected"])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.savefig(file[0:int(len(file) - 4)] + '.png', bbox_inches='tight')




def make_overlay_scatter_chart_from_files(infected_file, cured_file, x_label, y_label, title):

    ax = plt.subplot()

    lists = CSV_Maker.read_csv(cured_file)
    times = []
    for list in lists:
        time = []
        for x, val in enumerate(list):
            time.append(x)
        times.append(time)

    lists = flatten_list_of_lists(lists)
    times = flatten_list_of_lists(times)
    ax.scatter(times, lists, c='b')
    plt.plot(np.unique(times), np.poly1d(np.polyfit(times, lists, 5))(np.unique(times)), c = 'b')

    lists = CSV_Maker.read_csv(infected_file)
    times = []
    for list in lists:
        time = []
        for x, val in enumerate(list):
            time.append(x)
        times.append(time)

    lists = flatten_list_of_lists(lists)
    times = flatten_list_of_lists(times)
    ax.scatter(times, lists, c='r')
    plt.plot(np.unique(times), np.poly1d(np.polyfit(times, lists, 5))(np.unique(times)), c='r')

    infected_label = mpatches.Patch(color='red', label='Infected')
    cured_label = mpatches.Patch(color='blue', label='Cured')
    plt.legend([infected_label, cured_label], ["Infected", "Cured"])

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(infected_file[0:int(len(cured_file) - 4)] + '.png', bbox_inches='tight')
    plt.close()


def make_infected_charts(file):
    make_scatter_chart_from_file(file + '_total_infected.csv',
                                 'Round#/Time',
                                 'Number Infected',
                                 'Total Infected')

    make_scatter_chart_from_file(file + '_infected_per_round.csv',
                                                      'Round#/Time',
                                                      'Number Infected',
                                                      'Infected Per Round')

def make_cured_charts(file):
    make_overlay_scatter_chart_from_files(file + '_total_ever_infected.csv',
                                                      file + '_total_cured.csv',
                                                      'Round#/Time',
                                                      'Total Number Ever Infected/Cured',
                                                      'Total Number of Ever Infected and Cured')

    make_overlay_scatter_chart_from_files(file + '_total_current_infected.csv',
                                          file + '_total_cured.csv',
                                          'Round#/Time',
                                          'Total Number of Current Infected/Cured',
                                          'Total Number of Current Infected and Cured')

    make_overlay_scatter_chart_from_files(file + '_infected_per_round.csv',
                                          file + '_cured_per_round.csv',
                                          'Round#/Time',
                                          'Number Infected/Cured',
                                          'Infected and Cured Per Round')