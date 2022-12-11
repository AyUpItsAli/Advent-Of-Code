from typing import Callable


class Monkey:
    monkeys = []

    def __init__(self, starting_items: list, operation: Callable, test_factor: int, success_monkey: int, fail_monkey: int):
        self.items = starting_items
        self.operation = operation
        self.test_factor = test_factor
        self.success_monkey = success_monkey
        self.fail_monkey = fail_monkey
        self.inspections = 0
        Monkey.monkeys.append(self)
    
    @staticmethod
    def create_monkey(starting_items: list, operation: Callable, test_factor: int, success_monkey: int, fail_monkey: int):
        return Monkey(starting_items, operation, test_factor, success_monkey, fail_monkey)

    def inspect_items(self, common_multiple: int):
        for i in range(len(self.items)):
            item = self.items[i]
            self.items[i] = self.operation(item) % common_multiple
            self.inspections += 1

    def test(self, item) -> bool:
        return item % self.test_factor == 0

    def throw_items(self):
        for item in self.items:
            if self.test(item):
                Monkey.monkeys[self.success_monkey].items.append(item)
            else:
                Monkey.monkeys[self.fail_monkey].items.append(item)
        self.items = []


def apply_relief(monkey: Monkey):
    for i in range(len(monkey.items)):
        item = monkey.items[i]
        monkey.items[i] = int(item / 3)


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


def setup_monkeys():
    Monkey.monkeys = []
    with open("day11input.txt", "r") as file:
        line = file.readline()
        while line:
            if line.startswith("Monkey"):
                line = file.readline()
                starting_items: list
                operation: Callable
                test_factor: int
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
                        test_factor = int(line.replace("Test: divisible by ", ""))
                        line = file.readline().strip(" ").strip("\n")
                        success_monkey = int(line.replace("If true: throw to monkey ", ""))
                        line = file.readline().strip(" ").strip("\n")
                        fail_monkey = int(line.replace("If false: throw to monkey ", ""))
                    line = file.readline()
                Monkey.create_monkey(starting_items, operation, test_factor, success_monkey, fail_monkey)
                line = file.readline()
            else:
                line = file.readline()


def get_inspections(num_rounds: int, relief: bool = True):
    common_multiple = 1
    for monkey in Monkey.monkeys:
        common_multiple *= monkey.test_factor

    for r in range(num_rounds):
        for monkey in Monkey.monkeys:
            monkey.inspect_items(common_multiple)
            if relief: apply_relief(monkey)
            monkey.throw_items()

    return [m.inspections for m in Monkey.monkeys]


# Part 1
setup_monkeys()
inspections = get_inspections(20)  # 20 rounds, with relief.
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])

# Part 2
setup_monkeys()
inspections = get_inspections(10000, False)  # 10000 rounds. Relief no longer applied.
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
