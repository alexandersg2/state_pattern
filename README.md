# State Design Pattern

The State Pattern is a behavioural design pattern. It lets an object change its behaviour when its internal state changes. It appears as if the object changed its class.

The State Pattern is similar to a Finite-State Machine. There are a finite number of states the program can be in, with the program behaving differently in each state. The state can be changed from one to another, based on some defined rules.

![Finite-State Machine](./finite_state_machine.png?raw=true)

State machines are often implemented with complicated conditionals:

```
if a:
 ...
else if b:
 if x:
  ...
 else if y:
  ...
else:
 ...
```

This approach can work at first but becomes very difficult to manage as complexity increases and conditionals are added.

Use the State Pattern when:
- You have an object that behaves different based on its current state and its state changes often
- You have a class that contains long conditionals that are based on the current instance variables
- There is duplicated code across different states/conditionals


## The example:
This example models a simple audio player with 4 controls; lock, play, next, previous. We will explore how using the State 
Pattern can help us to remove complex conditionals and easily manage different program states.

## Class Diagram:

State Pattern class diagrams:

![State Pattern Class Diagrams](./state_pattern_class_diagrams.png?raw=true)


Example State Pattern class diagrams:

![State Pattern Class Diagrams](./example_class_diagrams.png?raw=true)

Ref: https://refactoring.guru/design-patterns/state