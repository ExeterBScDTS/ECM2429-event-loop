"""A simple tkinter example
   ========================

    Example use of **mainloop()** to create an event-driven program.

"""
from tkinter import Tk, Button
from time import sleep


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

    def start(self):
        """The start action.  Performed when the start button is pressed.
        """
        self.stop_countdown = False
        for i in range(10, 0, -1):
            print(i)
            self.__root.update()
            if self.stop_countdown:
                break
            sleep(1.0)

        self.__root.update()
        if not self.stop_countdown:
            print("Go!")

    def stop(self):
        """The stop action.  Performed when the stop button is pressed.
        """
        print("Stopping...")
        self.stop_countdown = True


if __name__ == "__main__":
    root = Tk()
    my_gui = SimpleGUI(root)
    root.mainloop()
    print("Goodbye")
