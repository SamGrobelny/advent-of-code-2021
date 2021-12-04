def measure_depth(filename):
    with open(filename) as file:
        num_inc = 0
        prev = next(file).strip()
        for line in file:
            stripped = line.strip()
            if int(stripped) > int(prev):
                num_inc += 1
            prev = stripped
        return num_inc

def sliding_measure(filename):
    with open(filename) as file:
        inc_count = 0
        three_one = []
        three_two = []
        three_one_sum = 0
        three_two_sum = 0
        for i in range(3):
            three_one.append(int(next(file).strip()))
            three_one_sum += three_one[i]
        for line in file:
            stripped = line.strip()
            three_two = list(three_one)
            three_two.pop(0)
            three_two.append(int(stripped))
            three_two_sum = sum(three_two)
            if three_two_sum > three_one_sum:
                inc_count += 1
            three_one = list(three_two)
            three_one_sum = sum(three_one)
    return inc_count

        

def main():
    # print(measure_depth('data/day-1-input.txt'))
    print(sliding_measure('data/day-1-input.txt'))

if __name__ == '__main__':
    main()