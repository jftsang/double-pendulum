# Double Pendulum — Chaotic Dynamics Simulation

A double pendulum simulator built from scratch: the equations of motion were hand-derived using Lagrangian mechanics, then numerically integrated and visualized in Python. The project also includes a side-by-side chaos demonstration, comparing two pendulums released from nearly identical starting angles to show sensitive dependence on initial conditions.

![Double pendulum animation](assets/thethingy.gif)

## Overview

A double pendulum is a simple-looking mechanical system — two rods, two masses, one pivot — that produces chaotic motion for large swing angles. Small changes in starting conditions lead to wildly different trajectories over time, making it a classic example of deterministic chaos.

This project:
- Derives the system's equations of motion from the Lagrangian by hand
- Converts the resulting coupled, nonlinear, second-order ODEs into a first-order system suitable for numerical integration
- Solves the system using `scipy.integrate.solve_ivp`
- Animates the result in real time with `matplotlib.animation.FuncAnimation`
- Demonstrates chaos directly by running two pendulums with a 0.1° difference in initial angle and tracking how fast they diverge

## Features

- **Live animation** of the double pendulum, rendered as connected rod segments with bob markers
- **Growing trail** behind the second bob, tracing its path through space
- **Two phase portraits** (θ₁ vs ω₁, θ₂ vs ω₂) — these reveal the qualitative difference between regular and chaotic motion far more clearly than an angle-vs-time plot
- **Lyapunov-style divergence panel** — plots the angular separation between two near-identical pendulums on a log scale over time, making the exponential divergence characteristic of chaos visible as a straight line
- All four panels (animation, two phase portraits, divergence plot) are laid out together in a single 2×2 figure

## Physics background

Starting from the Lagrangian for two coupled pendulums, applying the Euler-Lagrange equations for $\theta_1$ and $\theta_2$ gives two coupled, nonlinear second-order ODEs for the angular accelerations $\ddot\theta_1$ and $\ddot\theta_2$.

To integrate numerically, the system is rewritten in first-order form by introducing angular velocities $\omega_1 = \dot\theta_1$, $\omega_2 = \dot\theta_2$ as state variables alongside the angles themselves:

$$
\frac{d}{dt}\begin{bmatrix}\theta_1 \\ \theta_2 \\ \omega_1 \\ \omega_2\end{bmatrix} =
\begin{bmatrix}\omega_1 \\ \omega_2 \\ \ddot\theta_1(\theta_1,\theta_2,\omega_1,\omega_2) \\ \ddot\theta_2(\theta_1,\theta_2,\omega_1,\omega_2)\end{bmatrix}
$$

This is the standard method for turning higher-order ODEs into a first-order system that `solve_ivp` can integrate.

## Tech stack

- **Python** — core implementation, object-oriented design (`Pendulum` class)
- **NumPy** — vectorized trigonometric/array operations, angle unit conversion
- **SciPy** (`scipy.integrate.solve_ivp`, `scipy.constants`) — numerical ODE integration, physical constants
- **Matplotlib** (`pyplot`, `animation.FuncAnimation`) — real-time animation, multi-panel static plotting, log-scale visualization

## Project structure

```
double-pendulum/
├── lagrangian.py   # Pendulum class, EOMs, simulation, all plotting/animation
├── particle.py     # Early single-particle force/motion experiment (unused by lagrangian.py, kept for reference)
└── README.md
```

## Running it locally

```bash
pip install numpy scipy matplotlib
python lagrangian.py
```
I had a venv but I guess pip for normal installs, I don't know how all this works but meh.
A window will open showing the animated double pendulum (with trail), two phase portraits, and the divergence plot, all updating together. Initial conditions (lengths, masses, starting angles) can be changed where the `Pendulum` objects are constructed near the bottom of `lagrangian.py` inside the if statement.

## License

MIT — feel free to use or adapt this for your own learning.
