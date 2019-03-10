def make_csv_from_infection(file, lists):
    f = open(file + '_infected_per_round.csv', 'a')
    separator = ', '
    f.write(separator.join(str(x) for x in lists[0]))
    f.write('\n')
    f.close()

    f = open(file + '_total_infected.csv', 'a')
    separator = ', '
    f.write(separator.join(str(x) for x in lists[1]))
    f.write('\n')
    f.close()


def make_csv_from_cure(file, lists):
    f = open(file + '_infected_per_round.csv', 'a')
    separator = ', '
    f.write(separator.join(str(x) for x in lists[0]))
    f.write('\n')
    f.close()

    f = open(file + '_total_ever_infected.csv', 'a')
    separator = ', '
    f.write(separator.join(str(x) for x in lists[1]))
    f.write('\n')
    f.close()

    f = open(file + '_total_current_infected.csv', 'a')
    separator = ', '
    f.write(separator.join(str(x) for x in lists[2]))
    f.write('\n')
    f.close()

    f = open(file + '_cured_per_round.csv', 'a')
    separator = ', '
    f.write(separator.join(str(x) for x in lists[3]))
    f.write('\n')
    f.close()

    f = open(file + '_total_cured.csv', 'a')
    separator = ', '
    f.write(separator.join(str(x) for x in lists[4]))
    f.write('\n')
    f.close()


def read_csv(file):
    lines = []
    with open(file) as f:
        for line in f:
            lines.append([int(n) for n in line.split(',')])

    return lines
