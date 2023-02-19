class Action:

    def __init__(self, name):
        self.name = name
        self.infomassage = "Action"

    def __call__(self):
        print(f"For {self.name} provide required {self.infomassage}")


class Human:
    def __init__(self, name):
        self.name = name
        self.__action = Action(name)

    @property
    def action(self):
        return self.__action


class HumanIterator:
    def __init__(self, array):
        self.array = array
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.array) == self.position:
            raise StopIteration

        item = self.array[self.position]
        self.position += 1
        return item


class RangeIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.position = start_index
        if start_index < 0 or len(sequence) <= start_index:
            raise Exception("Sorry, start index cannot be less than zero or grater than len of sequence")
        if end_index < 0 or len(sequence) <= end_index:
            raise Exception("Sorry, end index cannot be less than zero or grater than len of sequence")
        if start_index > end_index:
            raise Exception('Incorrect data')

    def __iter__(self):
        return self

    def __next__(self):
        if self.position > self.end_index:
            raise StopIteration

        item = self.sequence[self.position]
        self.position += 1
        return item


if __name__ == "__main__":
    humans = HumanIterator([Human("Alex"), Human("Ivan"), Human("Bob")])
    for human in humans:
        human.action()

    range_numbers = RangeIterator([1, 2, 3], 0, 2)
    for number in range_numbers:
        print(number)


