# Job Scheduling Problem Solver

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive solution for the Job Scheduling Problem using multiple algorithms including Backtracking and Genetic Algorithm approaches. Features both graphical and command-line interfaces for easy interaction and algorithm comparison.

## 🚀 Features

- **Multiple Algorithms**: Backtracking and Genetic Algorithm implementations
- **Dual Interface**: Both GUI and CLI support
- **Algorithm Comparison**: Built-in performance comparison tools
- **Input Validation**: Robust error handling and input validation
- **Dependency Support**: Handle job dependencies in scheduling
- **Resource Constraints**: Manage resource capacity limitations
- **Performance Metrics**: Detailed scheduling metrics and visualizations

## 📋 Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Project Structure](#project-structure)
4. [Usage](#usage)
5. [Algorithms](#algorithms)
6. [API Reference](#api-reference)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)

## 💻 Installation

### System Requirements
- Python 3.7 or higher
- tkinter (usually included with Python)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AhmedFatthy1040/Job-Scheduling-Problem-Solver.git
   cd Job-Scheduling-Problem-Solver
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python main.py --help
   ```

## 🚀 Quick Start

### GUI Mode (Default)
```bash
python main.py
```

### Command Line Mode
```bash
python main.py --cli
```

### Run Tests
```bash
python test_scheduling.py
```

## 📁 Project Structure

```
Job-Scheduling-Problem-Solver/
│
├── main.py                    # Main application entry point
├── test_scheduling.py         # Comprehensive test suite
├── requirements.txt           # Project dependencies
├── README.md                 # Project documentation
│
├── algorithms/               # Algorithm implementations
│   ├── __init__.py
│   ├── backtracking_algorithm.py    # Backtracking solver
│   └── genetic_algorithm.py         # Genetic algorithm solver
│
├── models/                   # Data models
│   ├── __init__.py
│   ├── job.py               # Job class definition
│   ├── resource.py          # Resource class definition
│   └── job_scheduling_problem.py    # Problem instance class
│
├── gui/                     # Graphical user interface
│   ├── __init__.py
│   ├── main_window.py       # Main GUI window
│   ├── result_window.py     # Results display window
│   └── algorithms_comparison_window.py  # Algorithm comparison GUI
│
├── utils/                   # Utility modules
│   ├── __init__.py
│   ├── random_generator.py  # Random instance generator
│   └── scheduler_evaluator.py       # Performance evaluator
│
└── resources/              # Documentation and diagrams
    ├── documentation.pdf
    ├── package_diagram.PDF
    └── use_case_diagram.jpg
```

## 🎯 Usage

### GUI Interface

1. **Launch the application:**
   ```bash
   python main.py
   ```

2. **Add Jobs:**
   - Enter processing time
   - Optionally specify dependency (job ID that must complete first)
   - Click "Add Job"

3. **Add Resources:**
   - Enter capacity (total processing time available)
   - Click "Add Resource"

4. **Solve:**
   - Choose "Solve with Backtracking" or "Solve with Genetic"
   - View results in the popup window

5. **Compare Algorithms:**
   - Click "Algorithm Comparison" for automated testing

### Command Line Interface

**Algorithm Comparison:**
```bash
python main.py --cli
```

This will:
- Generate 5 random problem instances
- Solve each with both algorithms
- Compare performance and solution quality
- Display detailed results

### Programming Interface

```python
from models.job import Job
from models.resource import Resource
from models.job_scheduling_problem import JobSchedulingProblem
from algorithms.backtracking_algorithm import BacktrackingAlgorithm

# Create problem instance
jobs = [
    Job(1, 3, None),      # Job 1: 3 time units, no dependency
    Job(2, 2, 1),         # Job 2: 2 time units, depends on Job 1
    Job(3, 4, None)       # Job 3: 4 time units, no dependency
]

resources = [
    Resource(1, 10),      # Resource 1: capacity 10
    Resource(2, 8)        # Resource 2: capacity 8
]

problem = JobSchedulingProblem(jobs, resources)

# Solve with backtracking
algorithm = BacktrackingAlgorithm(problem)
solution = algorithm.solve()

if solution:
    print("Solution found!")
    for job, resource in solution:
        print(f"Job {job.job_id} → Resource {resource.resource_id}")
```

## 🔬 Algorithms

### Backtracking Algorithm
- **Approach**: Exhaustive search with pruning
- **Guarantees**: Optimal solution (if exists)
- **Time Complexity**: O(R^J) where R = resources, J = jobs
- **Best For**: Small to medium problems, exact solutions required

### Genetic Algorithm
- **Approach**: Evolutionary optimization
- **Guarantees**: Near-optimal solution
- **Time Complexity**: O(G × P × J) where G = generations, P = population, J = jobs
- **Best For**: Large problems, approximate solutions acceptable

### Algorithm Features
- **Dependency Handling**: Both algorithms properly handle job dependencies
- **Resource Constraints**: Respect resource capacity limitations
- **Validation**: Comprehensive solution validation
- **Performance Tracking**: Built-in timing and quality metrics

## 📊 API Reference

### Core Classes

#### Job
```python
Job(job_id: int, processing_time: int, dependency: Optional[int] = None)
```
- `job_id`: Unique identifier
- `processing_time`: Time required (must be positive)
- `dependency`: ID of prerequisite job (optional)

#### Resource
```python
Resource(resource_id: int, capacity: int)
```
- `resource_id`: Unique identifier
- `capacity`: Maximum processing time available (must be positive)

#### JobSchedulingProblem
```python
JobSchedulingProblem(jobs: List[Job], resources: List[Resource])
```
- `jobs`: List of jobs to schedule
- `resources`: List of available resources

### Algorithm Classes

#### BacktrackingAlgorithm
```python
BacktrackingAlgorithm(problem_instance: JobSchedulingProblem)
```
- `solve()`: Returns optimal schedule or None
- `is_valid_schedule(schedule)`: Validates a given schedule

#### GeneticAlgorithm
```python
GeneticAlgorithm(problem_instance, population_size=50, generations=100, 
                 crossover_prob=0.8, mutation_prob=0.2)
```
- `evolve()`: Returns best schedule found
- `fitness(schedule)`: Calculates schedule fitness (lower is better)

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_scheduling.py
```

**Test Coverage:**
- ✅ Model validation (Job, Resource)
- ✅ Algorithm correctness (Backtracking, Genetic)
- ✅ Input validation and error handling
- ✅ Schedule validation
- ✅ Integration testing
- ✅ Random generation utilities

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes and add tests**
4. **Run tests:** `python test_scheduling.py`
5. **Commit changes:** `git commit -m 'Add amazing feature'`
6. **Push to branch:** `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add type hints for new functions
- Include docstrings for all public methods
- Add tests for new functionality
- Update README for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic job scheduling optimization problems
- Built with Python's tkinter for cross-platform GUI support
- Uses evolutionary algorithms for heuristic optimization

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/AhmedFatthy1040/Job-Scheduling-Problem-Solver/issues)
- **Documentation**: Check the `resources/` folder for additional diagrams
- **Email**: [Contact the maintainer](mailto:your.email@example.com)

---

**Made with ❤️ by Ahmed Fathy**

