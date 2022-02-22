# ECM2429-event-loop

Event-loop programming examples.

## What is an event-loop?

An event loop is an endlessly repeating loop that receives *events* and then dispatches them for appropriate processing depending on the details of the event.

Programs that use an event-loop are called event-driven programs.

### A simple interactive program

We can write our own event-loop in Python using a ```while``` loop and an ```input()``` statement to read commands typed by the user and perform different actions depending on the command given.

This example uses a ```while``` loop and an ``if elif`` block.  The condition ```True``` means loop repeats forever, or until a ```break``` statement is reached.

See [code/example-1/interactive.py](code/example-1/interactive.py) for the full program.  Here is the event-loop.

```py
while True:
        # Wait here until the user types a command
        command = input("enter a command > ")

        if command == "help":
            print_help()
        # Can match the command to one of several words using 'in'
        elif command in ("quit", "exit"):
            break
        elif command == "dir":
            do_dir()
        elif command == "pwd":
            do_pwd()
        else:
            print_unknown(command)
```


## Why use an event-loop?

The event-loop style simplifies the design and implementation of many kinds of software.  Most productivity software such as word processors use this style, but it is also used internally in computer operating systems and network communication software to process events and messages.

### A simple tkinter GUI

This example of a graphical user interface uses the tkinter library.  You would be forgiven for not immediately spotting the event-loop here.  It's the very last line of the program ```root.mainloop()```.  Once this method runs the only other code that will run are the methods called by ```mainloop()```.  We tell the event-loop what these events are using the ```command``` argument to the ```Button``` contructor.  That is, each of our ```Button``` objects in the user interface has an event-handler associated with it.

See [code/example-4/tkinter-demo.py](code/example-2/tkinter-demo.py)

```py
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
```

When using an event-loop we defined the appearance and behaviour of our GUI, and then hand over to the event-loop to run our program.

## Pros and cons of the event-loop pattern

The event-loop pattern is widely used for a huge variety of software systems.

* REPL - read-evaluate-print loop, is a common style of interactive program.  The user types a line of text, and the program executes the commands.  REPL programs include the Python shell (when you run Python without a file or arguments) and the DOS terminal.

* GUIs - all modern user-interface frameworks use an event-loop.

* Web and mobile application - the event-loop is at the heart of the JavaScript language used to write web applications.

### Advantages

Programs have a simple structure making them easier to design, build and maintain.  Adding, or removing, features is generally very easy.

Users are able to quickly discover the features of a program, especially if a GUI is provided.  Programs are more flexible with the user able to do what they want, when the want to.

### Disadvantages

Not imposing a strict sequence of activities on the user now means there is no obvious flow.  It is not always clear to the user what they can, or should, do next.  I'm sure you've all experienced this when learning to use a new application. Worse still, without careful design it is likely that users will attempt to perform actions in the wrong order and cause a program to crash.


### Is this "multi-tasking"?

No, on its own an event-loop doesn't implement "multi-tasking", or what computer scientists call *concurrency*.  For true concurrency our programs
need to be able to do two or more thing at the same time.  However, there are ways of using an event-loop to
create the appearance of concurrency through what is termed *asynchronous* programming.

## Asynchronous programming

### An asynchronous tkinter UI

Our simple tkinter example has two buttons, one for "Start" and another for "Stop".  At the moment these don't do anything except print messages.  So let us add some code so that "Start" will start a countdown - 10, 9, 8.. 3, 2, 1, Go",
and "Stop" will stop the countdown.

See [code/example-4/tkinter-countdown.py](code/example-4/tkinter-countdown.py)

```txt
10
9
8
7
6
5
4
3
2
1
Go!
Stopping...
Stopping...
Stopping...
Stopping...
```

What we find is that although our GUI seems to work fine with simple actions associated with the buttons, once we have a long running action we see that the GUI is waiting for each action to complete before starting the next.  We can also see that button clicks are being queued, so when it is able to process the stop button presses, there are several waiting.

#### How can we fix this?

Before we attempt to fix our program, we should first think about why it is behaving as it is.  The program is not broken, it is doing exactly what the Python instructions tell it to do.  Our program is *single threaded*, which means it can only do one thing at a time.  At the heart of our program is the event-loop which decides which processes events in order, but requires each event to complete before starting the next.  

However we can, if we wish, temporarily return control to the event-loop, to allow it to check for any new event, and handle that event.  The change required is very simple.

```py
def start(self):
        """The start action.  Performed when the start button is pressed.
        """
        for i in range(10,0,-1):
            print(i)
            self.__root.update()
            sleep(1.0)
        print("Go!")
```

To actually stop the countdown will require some changes to the logic of the program. See [code/example-4/tkinter-countdown-stop.py](code/example-4/tkinter-countdown-stop.py) for appropriate changes.

**Is this a good solution?**

It seems to work, but there are still problems.  If the start button is pressed again during the countdown, a new countdown begins - this probably isn't desireable behaviour. Similarly, we can stop without first starting. A common solution to this issue is to disable the buttons when their use is not allowed.  In this way our GUI becomes "modal", i.e. it has different modes.

There are other potential problems. The countdown timer sleeps for 1 second between counts, and so our event-loop updates only occur each second.  This is probably usable, but if the intervals were longer, say 60 seconds, then the delay would be unacceptable.  And we now have update() calls scattered throughout our program, which might be acceptable for a small program, but would be very difficult to test and maintain if done in a large program. 

#### A better implementation

Although not obvious, the most significant flaw in the program at present is the use of ```time.sleep()```.  If we could avoid using this our program could respond to button clicks immediately. Of course if we just remove the sleep() call, the countdown would be too fast.  What we need is something that achieves the same outcome, a delay, but allows the UI to check frequently for user input.

### An asynchronous terminal user interface

There are situations where we don't need a full graphical user interface, but still require an asynchronous interface.  For example to pause and restart a long running program, or periodically check for new messages.  The built-in Python ```input()``` function **blocks**, that is it causes our program to wait until the user has typed some text before our program can continue.  If we don't want this behaviour then there are changes we can make to our program.  In this example I'll use the Python curses library, which as well as providing a non-blocking means of reading the keyboard also provide other useful features such as positioning text and coloured text and backgrounds.

See [code/example-5/curses-countdown.py](code/example-5/curses-countdown.py).

To run this example on Windows requires the **windows-curses** module.

```sh
pip install windows-curses
```

For more information on the features of curses see <https://docs.python.org/3/howto/curses.html>

### Does this mean we never need "threads"?

Concurrency solves the problem of doing two or more things at the same time, and there are many situations where this is necessary, or desireable.  However, the advice always given to those new to programming is to avoid concurrency - it has a reputation for creating more problems than it solved.  You will already have experienced some of these problems without necessarily knowing that concurrency was behind it. Here are a few -

 * Inadvertently clicking a button/icon more than once and having multiple copies of an application start when you only wanted one copy.

 * An application freezing/crashing when trying to open or save a documents.

 * Freezing or crashing when you have "too many" windows or applications open.

Asynchronous programming avoids some of the technical issues that arise when using true concurrency with multiple threads or processes, however designing, building and testing asynchronous programs can be just as challenging.

## Reading

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop>

<https://en.wikipedia.org/wiki/Event_loop>

<https://en.wikipedia.org/wiki/Event-driven_architecture>

<https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html>

<https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Concepts>
