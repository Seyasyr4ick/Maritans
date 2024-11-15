import random
distance = [1, 2, 3, 4, 5, 6, 7]
total_weight = 713
box_1 = random.randint(1, total_weight)
box_2 = random.randint(1, total_weight - box_1)
box_3 = total_weight - box_1 - box_2
counting_weight = 0
while True:
    num1, num2, num3 = map(int, input('Enter your numbers: ').split())
    first, second, third = random.sample(distance, k=3)
    random_km = []
    random_km.extend([first, second, third])
    if num1 in random_km:
        random_km.remove(num1)
        counting_weight += box_1
    if num2 in random_km:
        random_km.remove(num2)
        counting_weight += box_2
    if num3 in random_km:
        counting_weight += box_3
    if counting_weight == total_weight:
        print(f'Your box in {num1}, {num2}, {num3} kilometers')
        break
    counting_weight = 0
    distance = [1, 2, 3, 4, 5, 6, 7]
    distance.remove(first)
    distance.remove(second)
    distance.remove(third)
    print(f"Your boxes aren't in {num1}, {num2}, {num3} kilometers, try again")