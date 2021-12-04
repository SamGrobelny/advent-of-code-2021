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

def main():
    print(measure_depth('data/day-1-input.txt'))

if __name__ == '__main__':
    main()