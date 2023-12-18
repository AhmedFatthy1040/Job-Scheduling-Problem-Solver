# Project Documentation

## 1. Introduction
   This project aims to solve the Job Scheduling Problem using different algorithms, including backtracking and genetic algorithms. It provides both command-line and graphical interfaces for easy interaction.

## 2. Installation
   - **System Requirements:**
      - Python 3.x
   - **Dependencies:**
      - `tkinter` (for GUI)
   - **Installation Steps:**
      ```bash
      pip install -r requirements.txt
      ```

## 3. Project Structure
   - The project is structured into modules, including Models, Algorithms, Utils, and GUI.
   - Main files include `main.py` for command-line interaction and `gui/main_window.py` for the GUI.

## 4. Modules

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

## 5. How to Use

### 5.1. Command-Line Interface
   - Run the project using `python main.py`.
   - Specify the input parameters as needed.

### 5.2. Graphical User Interface
   - Run the GUI using `python gui/main_window.py`.
   - Click the "Random" button to compare algorithms with random instances.

## 6. Contributions
   - Contributions are welcome! Follow the guidelines in the CONTRIBUTING.md file.

## 7. Future Work
   - Planned enhancements include additional algorithms and improved GUI features.

## 8. License
   - This project is licensed under the MIT License.

## 9. Appendix
   - Additional diagrams, resources, or detailed explanations.

## 10. References
   - List of references used during the project.
