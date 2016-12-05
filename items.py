class Item():
    def __init__(self, name, description):
        self.name=name
        self.description=description
    def __str__(self):
        return "{}\n=====\n{}\n".format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage=damage
        super().__init__(name, description)
    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.damage)


class UnconquerableLightSpeedDestruction(Weapon):
    def __init__(self):
        super().__init__(name="Unconquerable Light-Speed Destruction",
                         description="A rifle, monstrously powerful; used for sport hunting in the real world, perhaps, but used for obliteration in this world. (hunting rifle).",
                         damage=24)

        
          
