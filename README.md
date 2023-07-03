# missile-defence-python

## Overview
  In this project work of 2d air defence system is simulated.
  Linear regression (LR) is used as a mathematical tool. LR was not taken from any library.
  Numpy was used to obtain pseudo-inverse matrix. All math behind project is explained in this document.
  Pygame library is used to create visualisation. 
  The project is not fully ready; development continues.
  This is not a final version of README file

## Code design
  Project contains three main classes: __Missile__, __DefenceSystem__, __Scene__.

  __Missile__ class implements missile behaviour, i.e. moving along trajectory (more about trajectory in math section).

  __DefenceSystem__ class implement defence system behaviour, i.e. obtains information about missile which is being observer, and launch defence missile (defence missile is instance of Missile class).

  __Scene__ class controls interaction of objects, user input, object updating and rendering.

  There is also __Settings__ class, which just contains static constants (screen size, missile size, etc.).

## Math behind
  Position of missile is given by parametrise function $f(t) = (x(t), y(t))$, where $t$ is a time parameter.
  
  For now, I consider $x(t), y(t) \in R[t]_{<=3}$. Note, that in code polynomials are given as a list of parameters.
  We will call $x(t), y(t)$ - trajectories of missile along X and along Y respectively, and $f(t)$ - position function.

  Defence system obtains information about position of a missile (in real world one can do it using radio-waves) with some noise.
  So, defence system eventually will have $$T = \{t_0, t_1, ..., t_n\}; X = \{x_0, x_1, ..., x_n\}; Y = \{y_0, y_1, ..., y_n\}$$

  Note, that since there is a noise in an obtained data the following is true: $$\exists i \in \{1, 2, ..., n\}: f(t_i) \neq (x_i, y_i)$$, where $f$ is a missile position function. Moreover, in a generic (not general) case: $$\forall i \in \{1, 2, ..., n\}: f(t_i) \neq (x_i, y_i)$$

  Now, one wants to use LR to find approximation of missile trajectories. 
  
  The idea of LR is to find $g(x) = \theta_0 + \theta_1x + ... + \theta_kx^k$, s.t. $g(t)$ approximates $f(t)$.
  In our case $k = 3$. I won't explain the whole LR here, but in order to find this approximation
  we need to find pseudo inverse matrix.

## Future ideas
  1. More trajectories for missile
  2. Smarter observation system
  3. New methods of approximation
  4. 


