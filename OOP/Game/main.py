from player import Player

tutul = Player("Tutul")

print(tutul.name)
print(tutul.lives)
tutul.lives -= 1
print(tutul)

tutul.lives -= 1
print(tutul)

tutul.lives -= 1
print(tutul)

tutul.lives -= 1
print(tutul)

tutul._lives = 9
print(tutul)

tutul.level = 2
print(tutul)

tutul.level += 5
print(tutul)

tutul.level = 3
print(tutul)

tutul.score = 500
print(tutul)
