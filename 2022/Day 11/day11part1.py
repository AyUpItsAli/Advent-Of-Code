from typing import Callable


class Monkey:
    monkeys = []

    def __init__(self, starting_items: list, operation: Callable, test: Callable, success_monkey: int, fail_monkey: int):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.success_monkey = success_monkey
        self.fail_monkey = fail_monkey
        self.inspections = 0
        Monkey.monkeys.append(self)

    def inspect_items(self):
        for i in range(len(self.items)):
            item = self.items[i]
            self.items[i] = self.operation(item)
            self.inspections += 1

    def throw_items(self):
        for item in self.items:
            if self.test(item):
                Monkey.monkeys[self.success_monkey].items.append(item)
            else:
                Monkey.monkeys[self.fail_monkey].items.append(item)
        self.items = []


def create_operation(op: list) -> Callable:
    if op[0] == "*":
        if op[1] == "old":
            return lambda x: x * x
        y = int(op[1])
        return lambda x: x * y
    elif op[0] == "+":
        if op[1] == "old":
            return lambda x: x + x
        y = int(op[1])
        return lambda x: x + y
    return lambda x: x


def create_test(divisor: int) -> Callable:
    return lambda x: x % divisor == 0


def read_input():
    out = []
    with open("day11input.txt", "r") as file:
        line = file.readline()
        while line:
            if line.startswith("Monkey"):
                line = file.readline()
                starting_items: list
                operation: Callable
                test: Callable
                success_monkey: int
                fail_monkey: int
                while line != "\n" and line != "":
                    line = line.strip(" ").strip("\n")
                    if line.startswith("Starting items"):
                        starting_items = [int(x) for x in line.replace("Starting items: ", "").split(", ")]
                    elif line.startswith("Operation"):
                        op = line.replace("Operation: new = old ", "").split(" ")
                        operation = create_operation(op)
                    elif line.startswith("Test"):
                        divisor = int(line.replace("Test: divisible by ", ""))
                        test = create_test(divisor)
                        line = file.readline().strip(" ").strip("\n")
                        success_monkey = int(line.replace("If true: throw to monkey ", ""))
                        line = file.readline().strip(" ").strip("\n")
                        fail_monkey = int(line.replace("If false: throw to monkey ", ""))
                    line = file.readline()
                monkey = Monkey(starting_items.copy(), operation, test, success_monkey, fail_monkey)
                line = file.readline()
            else:
                line = file.readline()
    return out


def apply_relief(monkey: Monkey):
    for i in range(len(monkey.items)):
        item = monkey.items[i]
        monkey.items[i] = int(item / 3)


read_input()

num_rounds = 20
for r in range(num_rounds):
    for monkey in Monkey.monkeys:
        monkey.inspect_items()
        apply_relief(monkey)
        monkey.throw_items()

inspections = [m.inspections for m in Monkey.monkeys]
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
