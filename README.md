# Graph traveral benchmark for python

This bit of code benchmarks the performance of a recursive graph traversal, a non-recursive graph traversal and hard-coded graph traversal. Results shows that the recursive version is roughly twice as fast as the hard-coded version and roughly 4 times as fast as the derecursified version.


## Graph generation

For each node, the number of children follows a given distribution. Graphs with too few nodes are discarded.

## Recursive traversal

The function `traversal()` is recursively called. The end result is the number of nodes in the graph, just to verify that all goes right.

## Hard-coded traversal

This time we generate a python code that does the same traversal. The result code looks like that :

```python3
def mjuezudcgi():
    accu = 0
    accu += toebelnzgi()
    accu += jmqpcteqlq()
    return accu + 1

def toebelnzgi():
    accu = 0
    return accu + 1

def jmqpcteqlq():
    accu = 0
    return accu + 1

def run():
    return mjuezudcgi()
```

Again, the whole code returns the number of nodes in the hard-coded graph.

Then we import this code and we run the function `run()`

## Derecursified traversal

This time we manage the call stack ourselves with python builtin data structures.


## Results

`experiments.png` shows the durations for 1000 experiments. The duration for each method is compared with the number of nodes in the graph. The recursive version is roughly twice as fast as the hard-coded version and roughly 4 times as fast as the derecursified version.

The performance gap between the recursive version and the hard-coded version surprised me a bit since the number of call and the number of arithmetic instructions are roughly the same. I suspect some magic caching to make frequent call to `traversal()` faster but I don't know python internals enough to have a satisfying explanation.

The performance gap between the recursive version and the non-recursive version just shows that python manages a call stack better than we can do naively with python builtin data structures.
