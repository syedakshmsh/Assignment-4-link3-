# hum user ko prompt dety h or usy kuch input lety h or hum input lekr funny story generate karty h...
def mad_libs():
    print("lets start  a playgame you fill in the box and enjoy the story")
    name = input("Give me a name:  ")
    place = input("Give me a place:  ")
    funny_adj   = input("Give me a funny adjective: ")
    random_obj = input("Give me a random_obj : ")
    animals = input("Give me a animal : ")
    action_verb = input("Give me a Action verb :")
    funny_exclamtion = input("Give me a funny_exclamtion :")


    story = f'''
    Once upon a time {name} sitting in a {place} and she is thinking {funny_adj} and she realise
    some {random_obj} around of her so she is scared and look this right side so see this biggest {animals} arounde
    {action_verb} for bananaa and she is so laughing and say {funny_exclamtion}

    '''
    print("your story is very funny and enjoyeble")
    print(story)
    
if __name__ == "__main__":
    print(mad_libs())
