i = 0
j = 1
s = 0
while s < 50:
    print(i)
    s = i + j
    i = j
    j = s


class aBc:
    def __init__(self, year):
        self.__year = year #private
        self.year1 = year
        self._year2 = year #protected
    def get_year(self):
        return self.__year
    def get_year2(self):
        return self._year2
a = aBc(100)
print(a.get_year())
print(a.year1)
print(a.get_year2())