import re

def part_one(filename: str) -> int:
    lines = process_file(filename)
    int_lines = [(re.sub('\D','',line.strip())) for line in lines]
    return sum([int(line[-1]) for line in int_lines])+10*sum([int(line[0]) for line in int_lines])

def part_two(filename: str) -> int:
    lines = process_file(filename)
    total = 0
    for line in lines:
        sum_line = sum(find_nums(line))
        print(sum_line)
        total += sum_line
    return total


def find_nums(line: str) -> list[int]:
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine","1","2","3","4","5","6","7","8","9"]
    print(line)
    min_ind = len(line)
    first_num = ""
    last_num = ""
    max_ind = -1
    for number in numbers:
        index = 0
        while index < len(line):
            ind = line.find(number, index)
            if ind == -1:
                break
            else:
                index += 1
            if ind!=-1 and ind<min_ind:
                min_ind=ind
                first_num = number
            if ind!=-1 and ind>max_ind:
                max_ind=ind
                last_num = number


    return [10*str_to_num(first_num),str_to_num(last_num)]

def str_to_num(str_num:str) -> int:
    numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    try:
        return numbers.index(str_num)
    except:
        return int(str_num)
    



def process_file(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().split("\n")

    return lines


if __name__ == "__main__":
    input_path = "test.txt"

    print("---Part One---")
    print(part_one(input_path))

    input_path = "real.txt"
    print("---Part Two---")
    print(part_two(input_path))