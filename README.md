# Job Scheduling Problem Solver Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Modules](#modules)
5. [How to Use](#how-to-use)
6. [Contributing](#contributing)
7. [License](#license)
8. [Appendix](#appendix)

## 1. Introduction <a name="introduction"></a>
   This project aims to solve the Job Scheduling Problem using different algorithms, including backtracking and genetic algorithms. It provides both command-line and graphical interfaces for easy interaction.

## 2. Installation <a name="installation"></a>
   - **System Requirements:**
      - Python 3.x
   - **Dependencies:**
      - `tkinter` (for GUI)
   - **Installation Steps:**
      ```bash
      pip install -r requirements.txt
      ```

## 3. Project Structure <a name="project-structure"></a>
   - The project is structured into modules, including Models, Algorithms, Utils, and GUI.
   - Main files include `main.py` for command-line interaction and `gui/main_window.py` for the GUI.

## 4. Modules <a name="modules"></a>

### 4.1. Models
   - **Resource:** Represents a resource with an ID and capacity.
   - **Job:** Represents a job with an ID, processing time, and optional dependency.
   - **JobSchedulingProblem:** Defines a scheduling problem with a set of jobs and resources.

### 4.2. Algorithms
   - **BacktrackingAlgorithm:** Solves the scheduling problem using a backtracking approach.
   - **GeneticAlgorithm:** Applies a genetic algorithm to find an optimal schedule.

### 4.3. Utils
   - **RandomGenerator:** Generates random instances of jobs and resources.
   - **SchedulerEvaluator:** Evaluates the performance of scheduling algorithms.

### 4.4. GUI
   - **AlgorithmComparisonWindow:** GUI window for comparing backtracking and genetic algorithms.

## 5. How to Use <a name="how-to-use"></a>

### 5.1. Command-Line Interface
   - Run the project using `python main.py`.
   - Specify the input parameters as needed.

### 5.2. Graphical User Interface
   - Run the GUI using `python gui/main_window.py`.
   - Click the "Random" button to compare algorithms with random instances.

## 6. Contributing <a name="contributing"></a>
Contributions are welcome! Feel free to fork the project and submit pull requests.


## 8. License <a name="license"></a>
This project is licensed under the [MIT License](LICENSE).

## 9. Appendix <a name="appendix"></a>
   - Check the resources folder.

