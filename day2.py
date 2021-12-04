def control_sub(filename):
    with open(filename) as file:
        horizontal = 0
        depth = 0
        for line in file:
            line_arr = line.strip().split()
            command = line_arr[0]
            amount = int(line_arr[1])
            if command == 'forward':
                horizontal += amount
            elif command == 'up':
                depth -= amount
            elif command == 'down':
                depth += amount
        return depth * horizontal

def main():
    print(control_sub('data/day-2-input.txt'))

if __name__ == '__main__':
    main()