import math


def verify_sum_to_1(probability_distribution):
    return round(sum([i[1] for i in probability_distribution]), 5) == 1.00


def find_mean(probability_distribution):
    total = 0
    for item in probability_distribution:
        total += item[0] * item[1]
    return total


def find_stddev(probability_distribution):
    mean = find_mean(probability_distribution)
    variance = 0.0
    for item in probability_distribution:
        variance += (item[0] - mean) ** 2 * item[1]
    stddev = math.sqrt(variance)
    return stddev
