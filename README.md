# aal

The module [`aal.py`](./aal.py) contains a simple and illustrative implementation of the method presented in the paper [Rotation Invariant Distance Measures for Trajectories][1] (2004), by Michail Vlachos et al., to convert a sequence of points in the XY space to another sequence of points in the Angle-Arc-Length (AAL) space.

## Installation

First, I recommend that you create a [virtual environment][2], so that you don't pollute your global space. If you're using PyCharm, see [their documentation][3] on how to create it directly from the IDE.

Now, you can install this package with the following command

    pip install -e .

You can omit `-e` if you don't need or want to see the effect of the changes that you make.

## Examples

I've prepared 2 examples that illustrate the implemented method. You can find them inside the folder [`examples`](./examples). 

To execute one of them, run the corresponding module

    python examples/example1.py

or

    python examples/example2.py

If you get an error related to [Qt][4] or [PyQt][5], you might need to install Qt first, because that's the backend that is being used by matplotlib in these examples. Alternatively, you can change [the backend that matplotlib uses][6].


 [1]: https://dl.acm.org/doi/10.1145/1014052.1014144
 [2]: https://docs.python.org/3/library/venv.html
 [3]: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
 [4]: https://www.qt.io/
 [5]: https://riverbankcomputing.com/software/pyqt/intro
 [6]: https://matplotlib.org/3.5.0/users/explain/backends.html#the-builtin-backends
