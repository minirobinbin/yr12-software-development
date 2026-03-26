print("VORAR POPULATION AND COST ESTIMATOR\n\n")

species = input("Enter the species. (b = baw baw frog, m = mountain pygmy possum, t = tiger quoll) > ")

if species =='b':
    # baw baw frog selected
    pop_limit = 50000
    growth_rate = 1.75
    cost_multiplier = 25
elif species == 'm':
    # mountain Pygmy possum
    pop_limit = 6000
    growth_rate = 1.30
    cost_multiplier=78
elif species == 't':
    # tiger quoll selected 
    pop_limit = 1500
    growth_rate = 1.50
    cost_multiplier = 165

print("\n")
starting_pop = int(input("Enter the current population of the species. > "))
print("\n")

year= 0

pop = starting_pop
cost = pop**0.8*cost_multiplier

while pop < pop_limit:
    print(f'Year: {year} Population: {round(pop)} Annual cost: $ {round(cost)}\n')
    pop *=growth_rate
    year += 1
    cost = pop**0.8*cost_multiplier

print(f"Population limit of {pop_limit} reached in Year {year}")