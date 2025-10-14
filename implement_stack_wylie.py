# David Wylie
# CIS256 24903
# Programming Assignment 3 (PA 3)
# Execise 3: Implement Stack for Undo/Redo
# I reused logic from the previous program, EX 2

from collections import deque

class StackEditor:
    """
    This class allows us to enter text and undo or redo these entries
    :attributes: undo_stack: the deque for undo actions
                 redo_stack: the deque for undo actions
                 current_text: the text string to mainpulate undo/redo
    """


    def __init__(self):
        self.undo_stack = deque()
        self.redo_stack = deque()
        self.current_text = ""
    
    def type_text(self, text):
        """
        function to add text for us to undo/redo when text is entered, it clears the 
        redo deque
        :params: text: str - a text string to manipulate. 
        """
        self.undo_stack.append(self.current_text)
        self.current_text += text
        self.redo_stack.clear()
    
    def undo(self):
        """
        Implments the undo action by checking if there is something in the undo deque,
        then adds current text to the redo stack, and removes the last item in undo deque,
        clearing the last item.
        """
        if self.undo_stack:
            self.redo_stack.append(self.current_text)
            self.current_text = self.undo_stack.pop()
    
    def redo(self):
        """
        Implments the redo action by checking if there is something in the redo deque,
        then adds the redo stack to current text, and removes the last item in redo deque,
        clearing the last item.
        """
        if self.redo_stack:
            self.undo_stack.append(self.current_text)
            self.current_text = self.redo_stack.pop()

    def user_interface(self):
        """
            Helper function to interact with stacks of text to redo/undo
            :params: Student list object
            :return: None, Uses all helper functions to interact with student list
        """
        # Main program loop - continues until user chooses to exit
        while True:
            try:
                print("""
Select from the Following Options
        1. Enter Text
        2. Undo Action
        3. Redo Action
        4. Exit Application
                    """)

                response = int(input("Enter Option: "))
                match response:
                    case 1:
                        self.type_text(str(input("Enter Text: ")))
                        print(f"\nCurrent Text: {self.current_text}")
                    case 2:
                        self.undo()
                        print(f"\nCurrent Text: {self.current_text}")
                    case 3:
                        self.redo()
                        print(f"\nCurrent Text: {self.current_text}")
                    case 4:
                        print("Goodbye!")
                        exit()
                    case _:
                        print("Please Enter a Number from 1 to 4.")
            except ValueError:
                print("Error: Please enter a valid integer.")


def main():
    """
    Main Entry point for the program, Change debug to True
    to see the program work without user interface.
    """
    DEBUG = False
    stack = StackEditor()

    if DEBUG == True:
        print("Beginning Text:")
        stack.type_text("Entry 1")
        stack.type_text(" Entry 2")
        print(stack.current_text)
        print("\nExecuting Undo:")
        stack.undo()
        print(stack.current_text)
        print("\nExecuting Redo:")
        stack.redo()
        print(stack.current_text)
    else:
        print("---Welcome to the Stack Undo/Redo Program---")
        stack.user_interface()


main()