class TreeNode:
    
    def __init__(self,question):
        self.question = question
        self.choices = []
        self.chosen = []
    
    def add_child(self,node):
        self.choices.append(node)
    
    def traverse(self):
        question_node = self
        print(question_node.question)
        while len(question_node.choices) > 0:
            choice = input("Enter 1 or 2 to continue: ")
            if choice not in ['1','2']:
                print("Invalid choice. Try again")
            else:
                chosen_index = int(choice) - 1
                chosen_child = question_node.choices[chosen_index]
                print(chosen_child.question)
                question_node = chosen_child
