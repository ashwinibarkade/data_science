""" """

""" PYTHON INTERPRETED

By interpreted it is meant each time a program is run the interpreter checks through the code for errors
and the interprets the instructions into machine-readable ``bytecode''. Perl is perhaps the best known example of an interpreted language.

This is different to a compiled language (such as C) which is compiled only once and produces a binary executable
which can then be run again and again, even on different physical systems of the same architecture1.2.
This means programs written in Python generally run more slowly than programs written in C.
Run-time speed reductions ranging from factors of two to an order of magnitude or more are typical.
However, the compile-debug cycle and prototyping of algorithms is much quicker an interpreted language such as Python.
In general programs may be written in less time in Python but will take longer to run.


An “interpreted” language either doesn’t have any compilation at all3, or compiles to an intermediate representation,
like bytecode. Bytecode is instructions for a virtual machine, not a piece of hardware.
Python falls into this latter category: the Python compiler’s job is to generate bytecode for the Python interpreter.


The Python interpreter’s job is to make sense of the bytecode via the virtual machine.

Article reference:
http://akaptur.com/blog/2013/12/03/introduction-to-the-python-interpreter-4/
http://www.techdarting.com/2014/04/python-compiled-or-interpreted-language.html


DYNAMIC TYPING

when we do 

1. a = b + c
2. print(5)
3. print("abc")


Above line is compiled to bytecode by compiler without knowing what type will b and c be. Or if what type is being printed by 'print'

It just emmits some instructions based on code we write.
 
It is interpreter's job to figure out what 'print' is going to print type wise of what type are 'b' and 'c'
 
print will behave differently based on what type is passed to it.
 
 
While a general definition of “compiling” and “interpreting” can be difficult to nail down, in the context of Python
it’s fairly straightforward. Compiling is generating the code objects, including the bytecode.
Interpreting is making sense of the bytecode in order to actually make things happen.
One of the ways in which Python is “dynamic” is that the same bytecode doesn’t always have the same effect.
More generally, in Python the compiler does relatively little work, and the intrepreter relatively more.

"""