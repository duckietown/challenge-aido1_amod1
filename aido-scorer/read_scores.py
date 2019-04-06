import math


def read_scores_data(filename):
    data = open(filename).read().strip()
    lines = data.split('\n')
    last = lines[-1]

    scores_data = last.split(',')[1:]

    def interpret(x):
        return float(x)

    scores_data = list(map(interpret, scores_data))

    stats = {}
    stats['steps'] = len(lines)

    scores = {}
    scores['service_quality'] = scores_data[0]
    scores['efficiency'] = scores_data[1]
    scores['fleet_size'] = scores_data[2]

    if math.isinf(scores['fleet_size']):
        scores['fleet_size'] = -1000*1000*1000


    return stats, scores


if __name__ == '__main__':
    print(read_scores_data('example-aidoScoresIntg.csv'))
