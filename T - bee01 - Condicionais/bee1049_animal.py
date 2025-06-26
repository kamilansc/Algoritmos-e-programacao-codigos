def main():
    caracteristica_animal = input()
    tipo_animal = input()
    tipo_alimento = input()

    if caracteristica_animal == 'vertebrado':
        if tipo_animal == 'ave':
            if tipo_alimento == 'carnivoro':
                animal = 'aguia'
            elif tipo_alimento == 'onivoro':
                animal = 'pomba'

        elif tipo_animal == 'mamifero':
            if tipo_alimento == 'onivoro':
                animal = 'homem'
            elif tipo_alimento == 'herbivoro':
                animal = 'vaca'

    elif caracteristica_animal == 'invertebrado':
        if tipo_animal == 'inseto':
            if tipo_alimento == 'hematofago':
                animal = 'pulga'
            elif tipo_alimento == 'herbivoro':
                animal = 'lagarta'

        elif tipo_animal == 'anelideo':
            if tipo_alimento == 'hematofago':
                animal = 'sanguessuga'
            elif tipo_alimento == 'onivoro':
                animal = 'minhoca'

    print(animal)


main()