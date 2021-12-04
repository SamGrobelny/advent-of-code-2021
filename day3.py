from types import CodeType


def find_gamma(filename):
    with open(filename) as file:
        result = [] # list of lists; first = 0 count, second = 1 count
        for _ in range(12):
            result.append([0,0])
        for line in file:
            line_list = list(line.strip())
            for i in range(len(line_list)):
                val = int(line_list[i])
                if val == True:
                    result[i][1] += 1
                else:
                    result[i][0] += 1
        gamma_code = []
        for element in result:
            if element[0] > element[1]:
                gamma_code.append(0)
            elif element[1] > element[0]:
                gamma_code.append(1)
    return gamma_code

def find_epsilon(gamma_code:list):
    epsilon_code = []
    for value in gamma_code:
        if value == 1:
            epsilon_code.append(0)
        elif value == 0:
            epsilon_code.append(1)
    return epsilon_code

def list_to_string(a_list:list):
    string = ''
    for value in a_list:
        string += str(value)
    return string
    

def main():
    gamma_code = find_gamma('data/day-3-input.txt')
    epsilon_code = find_epsilon(gamma_code)
    print(gamma_code)
    print(epsilon_code)
    gamma_string = list_to_string(gamma_code)
    epsilon_string = list_to_string(epsilon_code)
    gamma_int = int(gamma_string, 2)
    epsilon_int = int(epsilon_string, 2)
    print(gamma_int * epsilon_int)

if __name__ == '__main__':
    main()