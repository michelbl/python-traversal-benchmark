#!/usr/bin/python3
# coding: utf-8

import numpy as np
import random
import string
import py_compile
import time
import importlib
import sys
from matplotlib import pyplot as plt


debug = False

# Generate distribution

distribution = np.array([0.5, 0.1, 0.32, 0.08])
values = np.arange(len(distribution))
distribution_mass = distribution.sum()
assert(abs(distribution_mass - 1.) < 1e-15), 'Distribution must have a mass equal to 1'
distribution_norm = (distribution * values).sum()
print('Distribution norm : %f'%distribution_norm)
print('Mean number of nodes : %f'%(distribution_norm/(1-distribution_norm)))
assert(distribution_norm < 0.99), 'Be careful with distribution norms close to 1 !'


# Generate graph

def generate_node(nodes):
    begining = True
    random_string = ''
    while begining or (random_string in nodes):
        begining = False
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    nodes.append(random_string)
    return random_string


def generate_children(node, nodes, children):
    nb_children = np.random.choice(values, p=distribution)
    children_list = []
    for i in range(nb_children):
        child = generate_node(nodes)
        generate_children(child, nodes, children)
        children_list.append(child)
    children[node] = children_list


# Graph traversal

def traversal(node, nodes, children):
    accu = 0
    for child in children[node]:
        accu += traversal(child, nodes, children)
    return accu + 1


# Generate python code

def generate_python_code(root, nodes, children):
    python_code = ''

    for node in nodes:
        function_code = 'def %s():\n'%node
        function_code += '    accu = 0\n'
        for child in children[node]:
            function_code += '    accu += %s()\n'%child
        function_code += '    return accu + 1\n'

        python_code += function_code
        python_code += '\n'


    run_code = 'def run():\n'
    run_code += '    return %s()'%root
    run_code += '\n'

    python_code += run_code

    return python_code




# Make one experiment

def make_experiment():

    # Generate graph

    begining = True
    nb_nodes = 0
    while begining or nb_nodes < 100:
        begining = False

        nodes = []
        children = {}
        root = generate_node(nodes)
        generate_children(root, nodes, children)
        nb_nodes = len(nodes)

    if debug:
        print('The graph has %d nodes.'%nb_nodes)


    # Graph traversal

    t0 = time.time()
    result_traversal = traversal(root, nodes, children)
    duration_traversal = time.time() - t0
    if debug:
        print('Graph traversal result : %d'%result_traversal)
        print('Graph traversal took %f µs.'%(duration_traversal*1000))


    # Generate python code

    python_code = generate_python_code(root, nodes, children)

    script_name = 'generated_python'
    with open(script_name + '.py', 'w') as f:
        f.write(python_code)

    py_compile.compile(script_name + '.py')  # useless for the moment


    # Run generated code

    generated_module = importlib.import_module(script_name)
    generated_module = importlib.reload(generated_module)

    t0 = time.time()
    result_run = generated_module.run()
    duration_run = time.time() - t0
    if debug:
        print('Code execution result : %d'%result_run)
        print('Code execution took %f µs.'%(duration_run*1000))

    assert (result_traversal == result_run)

    return nb_nodes, duration_traversal, duration_run

nb_exp = 1000
nb_nodes_list = []
duration_traversal_list = []
duration_run_list = []
for i in range(nb_exp):
    nb_nodes, duration_traversal, duration_run = make_experiment()

    nb_nodes_list.append(nb_nodes)
    duration_traversal_list.append(duration_traversal)
    duration_run_list.append(duration_run)

    sys.stdout.write('.')
    sys.stdout.flush()
sys.stdout.write('\n')

fig = plt.figure()
plt.title('Traversal duration vs run duration for %d experiments'%nb_exp)
plt.ylabel('Execution time in seconds')
plt.xlabel('Number of nodes')
scat_tr = plt.scatter(nb_nodes_list, duration_traversal_list, color='b')
scat_run = plt.scatter(nb_nodes_list, duration_run_list, color='g')
plt.legend((scat_tr, scat_run), ('Traversal', 'Run'))
#max_duration = max(max(duration_traversal_list), max(duration_run_list))
max_nb_nodes = max(nb_nodes_list)
axes = plt.gca()
axes.set_ylim([0., 0.005])
axes.set_xlim([0., max_nb_nodes])
plt.savefig('experiments.png')
