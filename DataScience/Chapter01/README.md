Chapter01 - IPython 和 Jupyter 入門
=====
* ### Launching the IPython Shell
    ```
    $ ipython
    ```
* ### Launching the Jupyter Notebook
    ```
    $ jupyter lab
    ```
* ### Accessing Documentation with ?
    ```
    In [1]: help(len)
    Help on built-in function len in module builtins:

    len(obj, /)
        Return the number of items in a container.
    ```
    ```
    In [2]: len?
    Signature: len(obj, /)
    Docstring: Return the number of items in a container.
    Type:      builtin_function_or_method
    ```
    ```
    In [3]: L = [1, 2, 3]
    In [4]: L.insert?
    Signature: L.insert(index, object, /)
    Docstring: Insert object before index.
    Type:      builtin_function_or_method
    ```
    ```
    In [5]: L?
    Type:        list
    String form: [1, 2, 3]
    Length:      3
    Docstring:  
    Built-in mutable sequence.

    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    ```
    ```
    In [6]: def square(a):
      ....:     """Return the square of a."""
      ....:     return a ** 2
      ....:
    ```
    ```
    In [7]: square?
    Signature: square(a)
    Docstring: Return the square of a.
    File:      <ipython-input-6>
    Type:      function
    ```
* ### Accessing Source Code with ??
    ```
    In [8]: square??
    Signature: square(a)
    Source:   
    def square(a):
        """Return the square of a."""
        return a ** 2
    File:      <ipython-input-6>
    Type:      function
    ```
    * ### If you play with this much, you'll notice that sometimes the ?? suffix doesn't display any source code: this is generally because the object in question is not implemented in Python, but in C or some other compiled extension language.
    * ### If this is the case, the ?? suffix gives the same output as the ? suffix.
    * ### You'll find this particularly with many of Python's built-in objects and types, including the len function from earlier.
    ```
    In [9]: len??
    Signature: len(obj, /)
    Docstring: Return the number of items in a container.
    Type:      builtin_function_or_method
    ```
* ### Exploring Modules with Tab Completion
    * ### Tab completion of object contents
        ```
        In [10]: L.<TAB>
                    append() count    insert   reverse 
                    clear    extend   pop      sort    
                    copy     index    remove
        ```
        ```
        In [10]: L.c<TAB>
                    clear() count()
                    copy()         

        In [10]: L.co<TAB>
                    copy()  count()
        ```
        ```
        In [10]: L.cou<TAB>
        ```
        * ### Though Python has no strictly enforced distinction between public/external attributes and private/internal attributes, by convention a preceding underscore is used to denote the latter.
        * ### For clarity, these private methods and special methods are omitted from the list by default, but it's possible to list them by explicitly typing the underscore.
        ```
        In [10]: L._<TAB>
                __add__             __delattr__     __eq__      
                __class__           __delitem__     __format__()
                __class_getitem__() __dir__()       __ge__            >
                __contains__        __doc__         __getattribute__
        ```
        * ### Most of these are Python's special double-underscore methods (often nicknamed "dunder" methods).
    * ### Tab completion when importing
        ```
        In [10]: from itertools import co<TAB>
                combinations()                  compress()
                combinations_with_replacement() count()
        ```
        ```
        In [10]: import <TAB>
                    abc                 anyio                          
                    activate_this       appdirs                        
                    aifc                appnope        >
                    antigravity         argon2                         

        In [10]: import h<TAB>
                    hashlib html   
                    heapq   http   
                    hmac
        ```
    * ### Beyond tab completion: Wildcard matching
        ```
        In [10]: *Warning?
        BytesWarning                  RuntimeWarning
        DeprecationWarning            SyntaxWarning
        FutureWarning                 UnicodeWarning
        ImportWarning                 UserWarning
        PendingDeprecationWarning     Warning
        ResourceWarning
        ```
        ```
        In [11]: str.*find*?
        str.find
        str.rfind
        ```
* ### Keyboard Shortcuts in the IPython Shell
    * ### Navigation Shortcuts
        | Keystroke | Action |
        | - | - |
        | Ctrl-a | Move cursor to beginning of line |
        | Ctrl-e | Move cursor to end of the line |
        | Ctrl-b or the left arrow key | Move cursor back one character |
        | Ctrl-f or the right arrow key | Move cursor forward one character |
    * ### Text Entry Shortcuts
        | Keystroke | Action |
        | - | - |
        | Backspace key |	Delete previous character in line |
        | Ctrl-d | Delete next character in line |
        | Ctrl-k | Cut text from cursor to end of line |
        | Ctrl-u | Cut text from beginning of line to cursor |
        | Ctrl-y | Yank (i.e., paste) text that was previously cut |
        | Ctrl-t | Transpose (i.e., switch) previous two characters |
    * ### Command History Shortcuts
        | Keystroke | Action |
        | - | - |
        | Ctrl-p (or the up arrow key) | Access previous command in history |
        | Ctrl-n (or the down arrow key) | Access next command in history |
        | Ctrl-r | Reverse-search through command history |
    * ### Miscellaneous Shortcuts
        | Keystroke | Action |
        | - | - |
        | Ctrl-l | Clear terminal screen |
        | Ctrl-c | Interrupt current Python command |
        | Ctrl-d | Exit IPython session |
<br />
