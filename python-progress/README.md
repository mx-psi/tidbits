# `progress`

A class for managing waiting messages in Python.
It is intended to be used in a `with` block, as in:

``` python
with progress("message"):
  do_something()
```

This snippet will print a progress `message` until `do_something` finishes.
The progress printing thread is terminated even when exceptions are raised.

As an important note, `do_something` must NOT print anything, otherwise the output will be garbled.

You may run the Python file as a script to see an example in action.

Inspired by <stackoverflow.com/a/39504463/3414720>.
