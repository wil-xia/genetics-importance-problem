# William Xia
# 10/9/23
# Assignment 3: Genetic Algorithms README

HOW TO RUN:

Open command prompt and switch to the directory containing the genetics.py
Type python genetics.py in the command line

The program will prompt you to select the # of indivuals/genomes generated,
the # of generations (culling cycles), and the % mutation chance.

ASSUMPTIONS:

While selecting fit individuals as parents, each parent is selected randomly, 
with favor based on those with higher fitness scores. The same individual can 
be selected multiple times as a parent, and it's possible that not all 
individuals in the population will be selected as parents. (Those with a
fitness of 0 will never be selected as they have 0 weight/chance)

While crossing over 2 individuals to get a new offspring, their children are
created by randomly determining a split point, then combining the first half of
parent1 with the second half of parent 2, and vice versa.

The fitness value of each individual is calculated based on maximum importance
value held. The heuristic value is exactly that of the maximum importance value.
The only caveat is that any overweight backpack will automatically have a
fitness value of 0.

One major assumption/limit enforced is that the mutation chance must be at most
50% or less. This is to prevent the mass mutation of individuals that could
potentially result in the destruction of fit individuals.

TOKEN USED:
This assignment was due Monday 10/30, I used a token to extend the deadline
to Friday 11/3.