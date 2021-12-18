import pymorphy2
morph = pymorphy2.MorphAnalyzer()

class Kernel: 
    #Kernel elements, which gain us stop evaluations and sentenses
    def __init__(self, set_of_elements = set()):
        self.elements = set_of_elements

    def _and(self, set_of_elements): #there must be __and__
        return self.elements & set_of_elements
    
    def update(self, list_of_elements):
        self.elements.update(list_of_elements)
    #we won't delete any elements in class, while the functionality is
    # unnesssary 
    pass

class Sentense:
    #Sentense container, which save all linguistic information about sentense
    def __init__(self, secuense):
        self.full_sequense = secuense
    def getkernelsentense(self): #We made it primitivly: only nouns in 
        list_of_phrases = self.full_sequense.split() #name part have any sense
        answer_list = []
        for string_element in list_of_phrases:
            if string_element[-1] == ',':
                string_element = string_element[:-1]
            string_info = morph.parse(string_element)[0]
            if 'NOUN' in string_info.tag:
                answer_list.append(string_info.normal_form)
        return answer_list
pass

class TaskSenseKernel:#form, which have ranges in our transcription
        #fundamental sense that our task have sense in 1-st range(neighbour)
        def __init__(self, set_of_kernal_elements):
            self.priority_list_kernel[1] = set(set_of_kernal_elements)
        def upgrade():#function getting definitions by other sources
            return 0
        #not implemented
        def compare(self, set_of_kernal_elements):#filter by other task
            for priority_list in self.priority_list_kernel:
                priority_list = set_of_kernal_elements & priority_list
        def getinfo(self):
            return self.priority_list
        def get_full_set(self):
            new_set = set()
            for set_list in self.priority_list_kernel:
                new_set |= set_list
            return new_set
pass

def getmetrics(Task1, Task2, Kernelis = Kernel()):
    Common_elements = Kernelis._and(Task1.get_full_set & Task2.get_full_set)
    unsuccessparameter = [0,0]
    #unimplemented

def main():
    print("Hello World")

main()