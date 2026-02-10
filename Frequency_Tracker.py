class FrequencyTracker(object):

    def __init__(self):
        self.my_dict = {}
        self.dict_values = {}
        

    def add(self, number):
        self.my_dict[number] = self.my_dict.get(number, 0) + 1
        self.dict_values[self.my_dict[number]] = self.dict_values.get(self.my_dict[number], 0) + 1
        self.dict_values[self.my_dict[number]-1] = self.dict_values.get(self.my_dict[number]-1, 0) - 1

    def deleteOne(self, number):
        if number in self.my_dict and self.my_dict[number] > 0:
            self.dict_values[self.my_dict[number]] = self.dict_values.get(self.my_dict[number], 0) - 1
            self.dict_values[self.my_dict[number]-1] = self.dict_values.get(self.my_dict[number]-1, 0) + 1
            self.my_dict[number] = self.my_dict.get(number, 0) - 1

    def hasFrequency(self, frequency):
        if frequency in self.dict_values and self.dict_values[frequency] > 0:
            return True
        else:
            return False
