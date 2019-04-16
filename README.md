# a very simple RL demo

`a WIP project` 

This is a demo of an very simple RL process, in which an agent trying to default an opponent, controlled by a deterministic algorithm, in a rock scissors paper game. 

-----------------

### Introduction
This is a demo of a very simple RL framework; it consists of these modules:
* enviroment (a built-in simple game)
  * an algorithm (hidden to agent) generating rock/scissors/paper actions 
* agent
  * agent has a ML part
* ML core engine (pytorch based)
  * a network
  * an experience data buffer
* main: a master controller for running the system
  * the main loop
  * the hyperparameters

To run, type
`> python rl_main.py`

### Algorithm

* Policy Gradient (but not exactly)
* Use SGD to find the optimal Policy Network

### Todo
* better documentation
* real policy gradient

###  Contact
whoji@null.net