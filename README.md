# Direct execution 

correct output, but all output delayed until the process completes.
`$./main.py`

Actual:

```
Printing something to STDERR at start
err: 0
err: 1
err: 2
err: 3
err: 4
Printing something to STDERR at finish
Printing something to STDOUT at start
out: 0
out: 1
out: 2
out: 3
out: 4
Printing something to STDOUT at finish
```

Expected:

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
