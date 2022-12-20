import math

car_probability = ((0, 0.09),
                   (1, 0.36),
                   (2, 0.35),
                   (3, 0.13),
                   (4, 0.05),
                   (5, 0.02))

benfords_law = ((1, 0.301),
                (2, 0.176),
                (3, 0.125),
                (4, 0.097),
                (5, 0.079),
                (6, 0.067),
                (7, 0.058),
                (8, 0.051),
                (9, 0.046))


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


def main():
    print(find_mean(benfords_law))


if __name__ == '__main__':
    main()
