# Direct execution 

Results vary: 

## option1:
correct output, but all output delayed until the process completes.
`$./main.py`

```
Printing something to STDOUT at start
out: 0
out: 1
out: 2
out: 3
out: 4
Printing something to STDOUT at finish
Printing something to STDERR at start
err: 0
err: 1
err: 2
err: 3
err: 4
Printing something to STDERR at finish
```

## option2

Occasionally, stdout is left out.

```
Printing something to STDERR at start
err: 0
err: 1
err: 2
err: 3
err: 4
Printing something to STDERR at finish
```
# Execution with python: 

## `python main.py` 

SAME result as direct execution

## Execution with python -u: 

`python -u main.py`

STDERR streams as expected, but STDOUT is not flushed until the end.

```
Printing something to STDERR at start
err: 0
err: 1
err: 2
err: 3
err: 4
Printing something to STDOUT at start
out: 0
out: 1
out: 2
out: 3
out: 4
Printing something to STDOUT at finish
```
