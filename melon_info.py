"""Print out all the melons in our inventory."""


from melons import melon_data


def print_melon(melon_data):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s are {flesh_color} on outside, {rind_color} inside, they {have_or_have_not} seeds, weigh {average_weight} and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i], melon_flesh_color[i], melon_rind_color[i], melon_average_weight[i])
