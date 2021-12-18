import pymorphy2
morph = pymorphy2.MorphAnalyzer()

class Kernel: 
    #Kernel elements, which gain us stop evaluations and sentenses
    def __init__(self, list_of_elements):
        self.update(list_of_elements)

    #def __and__(self, list_of_elements):
 #       return self.elements & set(list_of_elements)
    
    def update(self, list_of_elements):
        self.elements.update(list_of_elements)
    #we won't delete any elements in class, while the functionality is
    # unnesssary 
    pass

class Sentense:
    #Sentense container, which save all linguistic information about sentense
    def __init__(self, secuense):
        self.full_sequense = secuense
    def getkernelsentense(self):
        list_of_phrases = self.full_sequense.split()
        answer_list = []
        for string_element in list_of_phrases:
            if string_element[-1] == ',':
                string_element = string_element[:-1]
            string_info = morph.parse(string_element)[0]
            if 'NOUN' in string_info.tag:
                answer_list.append(string_info.normal_form)
        return answer_list
    pass

a = Sentense('Пес словил овцу и съел, а потом съел')
print(a.getkernelsentense())