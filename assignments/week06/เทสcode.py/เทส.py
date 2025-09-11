class หมา:
    def __init__(self, name):
        self.name = name

    def เสียง(self):
        return "โฮ่งๆ"

class แมว:
    def __init__(self, name):
        self.name = name

    def เสียง(self):
        return "เหมียวๆ"

dog = หมา("เจ้าตูบ")
cat = แมว("เจ้าเหมียว")

print(f"{dog.name}: {dog.เสียง()}")
print(f"{cat.name}: {cat.เสียง()}")