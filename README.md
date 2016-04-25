# Graph traveral benchmark for python

This bit of code benchmarks the performance of a graph traversal against a python hard-coded version of the same graph traversal. Results shows that the dynamic version is about twice as fast as the hard-coded version.


## Graph generation

For each node, the number of children follows a given distribution. This is a very simple graph generation model. Graphs with too few nodes are discarded.

## Dynamic traversal

The function `traversal()` is recursively called. The end result is the number of nodes in the graph, just to verify that all goes right.

## Hard-coded traversal

This time we generate a python code that does the same traversal. The result code looks like that :

```python3
def mjwozqdoda():
    accu = 0
    return accu + 1

def cepjkjjmkv():
    accu = 0
    return accu + 1

def yzuqxjygmx():
    accu = 0
    return accu + 1

def run():
    return mjuezudcgi()
```

Again, the whole code returns the number of nodes in the hard-coded graph.

Then we import this code and we run the function `run()`

## Results

`experiments.png` shows the durations for 1000 experiments. The duration for each method is compared with the number of nodes in the graph. The dynamic version is about twice as fast as the hard-coded version.
