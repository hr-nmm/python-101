## classes do not define their own scope
class Nutrimatic:
    output = "Something almost, but not quite, entirely unlike tea."

    def request(self, beverage):
        return self.output


machine = Nutrimatic()
print(
    machine, type(machine)
)  # <__main__.Nutrimatic object at 0x7f56168f3910> <class '__main__.Nutrimatic'>

mug = machine.request("Tea")
print(mug)  # Something almost, but not quite, entirely unlike tea.
print(machine.output)  # Something almost, but not quite, entirely unlike tea.
print(Nutrimatic.output)  # Something almost, but not quite, entirely unlike tea.
