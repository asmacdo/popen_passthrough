To run, execute `./main.py`, and observe the output.


Compare to the output of `./test_script.py`


`./main.py`

```
============= python -u (unbuffered)
Printing something to STDOUT at start
Printing something to STDERR at start
out: 0
err: 0
out: 1
err: 1
out: 2
err: 2
out: 3
err: 3
out: 4
err: 4
Printing something to STDOUT at finish
Printing something to STDERR at finish
=============
---------------  direct execution ---------------
Printing something to STDOUT at start
Printing something to STDERR at start
out: 0
err: 0
out: 1
err: 1
out: 2
err: 2
out: 3
err: 3
out: 4
err: 4
Printing something to STDOUT at finish
Printing something to STDERR at finish
------------------------------
```

`./test_script.py`

Correct execution should have out and err interleaved similar to below:

```
Printing something to STDOUT at start
Printing something to STDERR at start
out: 0
err: 0
out: 1
err: 1
out: 2
err: 2
out: 3
err: 3
out: 4
err: 4
Printing something to STDOUT at finish
Printing something to STDERR at finish
```
