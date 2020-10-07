# State

State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

## Problem

At any given moment, there’s a finite number of states which a program can be in. Within any unique state, the
 program behaves differently, and the program can be switched from one state to another instantaneously. However, depending on a current state, the program may or may not switch to certain other states. These switching rules, called transitions, are also finite and predetermined.

Imagine that we have a `Document` class. A document can be in one of three states: `Draft`, `Moderation` and `Published`. The `publish` method of the document works a little bit differently in each state:

In `Draft`, it moves the document to moderation.
In `Moderation`, it makes the document public, but only if the current user is an administrator.
In `Published`, it doesn't do anything at all.

The biggest weakness reveals itself once we start adding more states and state-dependent behaviors to the
 `Document` class. Most methods will contain monstrous conditionals that pick the proper behavior of a method according to the current state. Code like this is very difficult to maintain because any change to the transition logic may require changing state conditionals in every method.

The problem tends to get bigger as a project evolves. It’s quite difficult to predict all possible states and transitions at the design stage. Hence, a lean state machine built with a limited set of conditionals can grow into a bloated mess over time.

## Solution

The State pattern suggests that you create new classes for all possible states of an object and extract all state-specific behaviors into these classes.

Instead of implementing all behaviors on its own, the original object, called context, stores a reference to one of the state objects that represents its current state, and delegates all the state-related work to that object.

To transition the context into another state, replace the active state object with another object that represents that new state. This is possible only if all state classes follow the same interface and the context itself works with these objects through that interface.

This structure may look similar to the [Strategy](../strategy/README.md) pattern, but there’s one key difference
. In the State pattern
, the
 particular states may be aware of each other and initiate transitions from one state to another, whereas strategies almost never know about each other.
 
## How to Implement

1. Decide what class will act as the context. It could be an existing class which already has the state-dependent code; or a new class, if the state-specific code is distributed across multiple classes.

1. Declare the state interface. Although it may mirror all the methods declared in the context, aim only for those that may contain state-specific behavior.

1. For every actual state, create a class that derives from the state interface. Then go over the methods of the context and extract all code related to that state into your newly created class.

    While moving the code to the state class, you might discover that it depends on private members of the context. There are several workarounds:

    - Make these fields or methods public.
    - Turn the behavior you’re extracting into a public method in the context and call it from the state class. This
     way is ugly but quick, and you can always fix it later.
    - Nest the state classes into the context class, but only if your programming language supports nesting classes.
1. In the context class, add a reference field of the state interface type and a public setter that allows overriding the value of that field.

1. Go over the method of the context again and replace empty state conditionals with calls to corresponding methods of the state object.

1. To switch the state of the context, create an instance of one of the state classes and pass it to the context. You can do this within the context itself, or in various states, or in the client. Wherever this is done, the class becomes dependent on the concrete state class that it instantiates.
