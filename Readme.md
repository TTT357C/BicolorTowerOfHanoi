<br/>
<p align="center">
  <h3 align="center">Bicolor Towers of Hanoi</h3>

  <p align="center">
    Python solver
    <br/>
    <br/>
    <a href="https://github.com/TTT357C/BicolorTowerOfHanoi/blob/main/Latex/doc.pdf"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

The objective of this project is to solve the problem of the Tower of Hanoi in its two-color variant. Two methodologies are employed for the resolution: specific search algorithms for the problem and the implementation of a problem model written in PDDL.

This project aims to explore and compare these two methods/approaches for solving the Tower of Hanoi problem, providing an in-depth analysis of the advantages and limitations of each approach.

## Built With

Python, Cython and PDDL
(PDDL uses enhsp-20 as a Solver - https://gitlab.com/enricos83/ENHSP-Public/-/tree/enhsp-20 written i Java by Prof. Enrico Scala)

## Getting Started

Some libraries are needed for running the program.

### Prerequisites

The libraries that are needed for the program are:

* Cython>=3.0.5
* line_profiler>=4.1.1 #optional
* numpy>=1.25.1
* setuptools>=65.5.0
* tk>=0.1.0

You can find also the requirements.txt file in the main folder. (pip install -r requirements.txt)


### Installation

Download the zip folder.
Unzip it.

if you are on windows run the file launcher.bat, otherwise open a terminal in the folder where MainWindow.py is located and run MainWindow.py
(This i needed because the GUI need to find the path to some component)

## Authors

* **Thomas Causetti** - [Thomas Causetti](https://github.com/TTT357C/) - *Programmer*
* **Paolo Gandinelli** - [Paolo Gandinelli](https://github.com/pGandinelli) - *Programmer*
* **Mirko Rossi** - [Mirko Rossi](https://github.com/Zphyr19) - *Programmer*

## Acknowledgements

* [Enrico Scala](https://gitlab.com/enricos83/ENHSP-Public/-/tree/enhsp-20)
