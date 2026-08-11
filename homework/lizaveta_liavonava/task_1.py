class Flower:
    def __init__(self, freshness , color, stem_length, cost, average_lifespan):
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.average_lifespan = average_lifespan


class Rose(Flower):
    def __init__(self, freshness, color, stem_length, cost, average_lifespan):
        super().__init__(freshness, color, stem_length, cost, average_lifespan)
        self.name = 'Rose'

class Tulip(Flower):
    def __init__(self, freshness, color, stem_length, cost, average_lifespan):
        super().__init__(freshness, color, stem_length, cost, average_lifespan)
        self.name = 'Tulip'


class Sunflower(Flower):
    def __init__(self, freshness, color, stem_length, cost, average_lifespan):
        super().__init__(freshness, color, stem_length, cost, average_lifespan)
        self.name = 'Sunflower'


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_cost(self):
        total = 0
        for flower in self.flowers:
            total += flower.cost
        return total

    def avg_wilting_time(self):
        total = 0
        for flower in self.flowers:
            total += flower.average_lifespan
        return total / len(self.flowers)

    def sort_by_freshness(self):
        return sorted(self.flowers, key=lambda flower: flower.freshness)

    def sort_by_color(self):
        return sorted(self.flowers, key=lambda flower: flower.color)

    def sort_by_stem_length(self):
        return sorted(self.flowers, key=lambda flower: flower.stem_length)

    def sort_by_cost(self):
        return sorted(self.flowers, key=lambda flower: flower.cost)

    def search_by_lifespan(self, min_lifespan):
        result = []
        for flower in self.flowers:
            if flower.average_lifespan >= min_lifespan:
                result.append(flower)
        return result

rose1 = Rose(3, 'blue', 100, 20, 10)
tulip1 = Tulip(1, 'red', 85, 15, 7)
sunflower1 = Sunflower(50, 'yellow', 125, 30, 8)

flowers = [rose1, tulip1, sunflower1]
bouquet = Bouquet(flowers)

print(bouquet.total_cost())
print(bouquet.avg_wilting_time())
for flower in bouquet.sort_by_cost():
    print(flower.name, flower.cost)
for flower in bouquet.search_by_lifespan(8):
    print(flower.name, flower.average_lifespan)
for flower in bouquet.sort_by_freshness():
    print(flower.name, flower.freshness)