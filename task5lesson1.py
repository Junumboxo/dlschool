array = ['agfkd.,f', 'Qksdf;sb&..', 'asdoo*', 'bgf...d', 're54()kj[]].']
count_dots = list(map(lambda x: x.count('.'), array))
print(count_dots)
more_than_two = list(filter(lambda x: x.count('.') > 2, array))
print(more_than_two)
