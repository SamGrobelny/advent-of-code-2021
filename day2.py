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

def control_sub_accurate(filename):
    with open(filename) as file:
        horizontal = 0
        depth = 0
        curr_aim = 0
        for line in file:
            line_arr = line.strip().split()
            command = line_arr[0]
            amount = int(line_arr[1])
            if command == 'forward':
                horizontal += amount
                depth += curr_aim * amount
            elif command == 'up':
                curr_aim -= amount
            elif command == 'down':
                curr_aim += amount
    return depth * horizontal

def main():
    # print(control_sub('data/day-2-input.txt'))
    print(control_sub_accurate('data/day-2-input.txt'))

if __name__ == '__main__':
    main()