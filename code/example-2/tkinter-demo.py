"""A simple tkinter example
   ========================

    Example use of **mainloop()** to create an event-driven program.

"""
from tkinter import Tk, Button

class SimpleGUI:
    """_summary_
    """
    def __init__(self, root: Tk):
        """Constructor for a simple tkinter GUI
        :param root: The root tk application
        :type root: Tk
        """
        self.__root = root

        self.start_button = Button(self.__root, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = Button(self.__root, text="Stop", command=self.stop)
        self.stop_button.pack()

    def start(self):
        """The start action.  Performed when the start button is pressed.
        """
        print("Starting...")

    def stop(self):
        """The stop action.  Performed when the stop button is pressed.
        """
        print("Stopping...")

if __name__ == "__main__":
    root = Tk()
    my_gui = SimpleGUI(root)
    root.mainloop()
    print("Goodbye")
