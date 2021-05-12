#Practice with random and string modules.

import random
import string

word_list_one=['You are such a']

word_list_two=[
'great',
'capable',
'kind',
'nice',
'leader of a'
]

word_list_three=[
'gerbil',
'giraffe',
'anteater',
'hedgehog',
]

word_list_four=[
'wrangler',
'breeder',
'veteranarian',
'fighter',
]


var1=(random.choice(word_list_one))

var2=(random.choice(word_list_two))

var3=(random.choice(word_list_three))

var4=(random.choice(word_list_four))

print(var1, var2, var3, var4)
