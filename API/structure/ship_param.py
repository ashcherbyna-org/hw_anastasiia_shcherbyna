class Ship:
    def __init__(self, manufacturer, cost_in_credits, length, max_atmosphering_speed):
        '''

        :param manufacturer: ship parameter
        :param cost_in_credits: ship parameter
        :param length: ship parameter
        :param max_atmosphering_speed: ship parameter
        '''
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
