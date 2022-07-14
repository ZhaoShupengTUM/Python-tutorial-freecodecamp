from Class_Chef import Chef

class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken")  #overwrite the function of the father class

    def make_fried_rice(self):
        print("The chef makes fried rice")