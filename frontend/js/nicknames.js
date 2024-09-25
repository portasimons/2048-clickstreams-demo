var animals = [
    "Fox","Bear", "Rabbit", "Gepard", "Panda", "Cat",
    "Dog", "Hedgehog", "Elephant", "Pig", "Scorpio",
    "Dragon", "Penguin", "Duck", "Deer", "Hamster",
    "Giraffe", "Fish", "Bull"
]

var adjectives = [
    "Funny", "Sleepy", "Dreamy", "Dancing", "Hungry", "Giant",
    "Majestic", "Playful", "Intelligent", "Adorable",
    "Curious", "Loyal", "Mysterios", "Colorful",
    "Chunky", "Blue"
]

var nicknames = animals.flatMap(d => adjectives.map(v => v + " " + d))
