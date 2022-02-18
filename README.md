# ECM2429-event-loop
Event loop demos

## What is an event-loop?

### A simple interactive program

## Why use an event-loop?

### A simple tkinter GUI

### A simple web server

## Is this "multi-tasking"?

No, on its own an event loop doesn't implement "multi-tasking", that is *concurrency*.  For true concurrency programs
need to be able to do two or more thing at the same time.  However, there are ways of using an event-loop to
create the appearance of concurrency through what is termed *asynchronous* programming.


### An asynchronous tkinter UI

### An asynchronous curses UI

## Does this mean we never need "threads"?

## Reading

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop>

<https://en.wikipedia.org/wiki/Event_loop>

<https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html>

<https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Concepts>
