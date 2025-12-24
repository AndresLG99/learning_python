from pathlib import Path

base = Path.home()
guide = Path(base,"Europe","Spain","Barcelona","Sagrada_Familia.txt")
guide2 = guide.with_name("La_Pedrera.txt")
print(base)
print(guide)
print(guide2)
print(guide.parent.parent)
print(guide2.parent)

print(100 * "-")

guide = Path("D:\\Documents Local","Portfolio","learning_python","background","day6","class_material","Europe")

for txt in Path(guide).glob("*.txt"):
    print(txt)

print(100 * "-")

for txt in Path(guide).glob("**/*.txt"):
    print(txt)

print(100 * "-")

guide = Path("Europe","Spain","Barcelona","Sagrada_Familia.txt")

in_europe = guide.relative_to(Path("Europe"))
print(in_europe)

in_spain = guide.relative_to(Path("Europe","Spain"))
print(in_spain)