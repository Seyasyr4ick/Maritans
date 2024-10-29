import random

distance = [1, 2, 3, 4, 5, 6, 7]
while True:

    num1, num2, num3 = map(int, input().split())
    first, second, third = random.sample(distance, k=3)
    random_km = []
    random_km.extend([first, second, third])
    if num1 in random_km:
        random_km.remove(num1)
        if num2 in random_km:
            random_km.remove(num2)
            if num3 in random_km:
                print(f'Your box in {num1}, {num2}, {num3} kilometers')
                break
    distance = [1, 2, 3, 4, 5, 6, 7]
    distance.remove(first)
    distance.remove(second)
    distance.remove(third)
    print(f"Your boxes aren't in {num1}, {num2}, {num3} kilometers, try again")