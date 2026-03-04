from .item import Item

class Room:

    def __init(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exits: dict[str, 'Room'] = {}
        self.items: list[Item] = []

    def add_exit(self, direction: str, room: Room):
        self.exits[direction] = room

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def get_exits(self, direction: str):
        return self.exits[direction]

    def __str__(self):
        return f'Комната {self.name} - {self.description}. Здесь {len(self.exits.keys())} выходов.'