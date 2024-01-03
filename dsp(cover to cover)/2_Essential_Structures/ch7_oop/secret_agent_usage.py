from secret_agent import SecretAgent

kobe = SecretAgent("Kobe24")
mouse = SecretAgent("Mouse")
fox = SecretAgent("Fox")

print(kobe)
print(mouse)
print(fox)

kobe.add_secrets("this guy knows krav maga")

print(kobe)

print(SecretAgent._codeword)  # nba
SecretAgent._codeword = "ipl"
print(SecretAgent._codeword)  # ipl
kobe._codeword = "nba"
print(SecretAgent._codeword)  # ipl (unchanged)
# if a value is assigned to the name on an instance, it will create an instance attribute with the same name, which shadows the class attribute on that instance, without affecting other instances.
print(kobe._codeword)  # nba


## changing class attribute by using class method:
SecretAgent.inform("comma ai")
print(SecretAgent._codeword)  # comma ai

## calling class method from object changes class attribute, unlike line:18
mouse.inform("tinygrad")
print(SecretAgent._codeword)  ## changed to tinygrad
print(mouse._codeword)  # tinyrgrad

## using static method:
SecretAgent.inquire("running with class?")  # I know nothing
kobe.inquire("running with object?")  # I know nothing
