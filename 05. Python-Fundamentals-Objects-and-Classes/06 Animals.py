#   Just acting like we're animals
class Animal:
    def __init__(self, *tokens):
        self.type, self.name, self.age, self.attribute = tokens
        self.age = int(self.age)
        self.attribute = int(self.attribute)
        
        attribute_label = {
                'Dog': 'Number Of Legs',
                'Cat': 'IQ',
                'Snake': 'Cruelty'
        }
        talk_strings = {
                'Dog': "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.",
                'Cat': "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.",
                'Snake': "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."
        }
        self.attribute_label = attribute_label[self.type]
        self.talk_string = talk_strings[self.type]

    def talk(self):
        print(self.talk_string)

    def __str__(self):
        out_string = [self.type.title() + ': ' + self.name, 'Age: ' + str(self.age), self.attribute_label + ': ' + str(self.attribute)]
        result = ', '.join(out_string)
        return(result)

    def __gt__(self, other):
        result = self.type == 'Dog' and other.type in ['Cat', 'Snake'] or \
            self.type == 'Cat' and other.type == 'Snake'
        return(result)

    def __eq__(self, other):
        result = self.type == other.type
        return(result)

animal_list = {}

while True:
    user_input = input()
    if user_input == "I'm your Huckleberry":
        animal_list_out = sorted([animal for animal in animal_list.values()], reverse = True) 
        print(*animal_list_out, sep = '\n')
        break

    user_input_split = user_input.split()
        
    if user_input_split[0] == 'talk':
        if user_input_split[1] in animal_list.keys():
            animal_list[user_input_split[1]].talk()
        continue
    
    cur_animal = Animal(*user_input_split)
    animal_list[cur_animal.name] = cur_animal

