"""A simple tkinter example
   ========================

    Example use of **mainloop()** to create an event-driven program.

"""
from tkinter import Tk, Button, StringVar, Label
from datetime import timedelta, datetime


class SimpleGUI:
    def __init__(self, root: Tk):
        """Constructor for a simple tkinter GUI
        :param root: The root tk application
        :type root: Tk
        """
        self.__root = root
        self.__root.title("Countdown")

        self.start_button = Button(self.__root, text="Start", command=self.start)
        self.start_button.pack()

        self.stop_button = Button(self.__root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.countdown_text = StringVar()
        self.countdown_label = Label(self.__root, textvar=self.countdown_text)
        self.countdown_label.pack()

        self.deadline = None
        self.__root.after(0, self.countdown)

    def countdown(self):
        # after() does not block, so do this first.
        # Called after a number of milliseconds.
        # Choose a rate that makes sense for your application.
        self.__root.after(500, self.countdown)
        if self.deadline:
            remaining = self.deadline - datetime.now()
            self.countdown_text.set(remaining)

    def start(self):
        """The start action.  Performed when the start button is pressed.
        """
        self.deadline = datetime.now() + timedelta(seconds=10)

    def stop(self):
        """The stop action.  Performed when the stop button is pressed.
        """
        print("Stopping...")
        self.deadline = None


if __name__ == "__main__":
    root = Tk()
    my_gui = SimpleGUI(root)
    root.mainloop()
    print("Goodbye")
