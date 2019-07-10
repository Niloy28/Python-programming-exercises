# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?


def solve(num_head, num_leg):
    for possible_chicken in range(num_head + 1):
        possivle_rabbit = num_head - possible_chicken

        if possible_chicken * 2 + possivle_rabbit * 4 == num_leg:
            return [possible_chicken, possivle_rabbit]

    return []


result = solve(35, 94)
print(f"No. of chickens: {result[0]}\nNo. of rabbits: {result[1]}")
