# Mathematics Expert System

A beginner-friendly, rule-based Mathematics Expert System built in Python. It accepts supported natural-language math questions, identifies the mathematical topic, applies knowledge-base rules, calls the appropriate solver, and returns a result with an explanation and a transparent verification status.

## Features

- Natural-language question handling for documented question patterns.
- Rule-based inference engine with a traceable reasoning path.
- Algebra: linear and quadratic equations and symbolic simplification.
- Calculus: symbolic differentiation and integration using SymPy.
- Geometry: circle, rectangle, and triangle calculations.
- Trigonometry: sine, cosine, and tangent (angles in degrees).
- Clear errors for unsupported or incomplete questions.
- Terminal interface and Streamlit web interface.
- Automated unit tests and GitHub Actions test workflow.

## Project structure

```text
math_expert_system/
  __init__.py
  app.py                 # Streamlit web interface
  cli.py                 # terminal interface
  core.py                # coordinates the complete reasoning pipeline
  inference_engine.py    # matches facts to expert rules
  knowledge_base.py      # production rules
  nlp.py                 # parses supported question patterns
  solvers.py             # mathematical operations
  verifier.py            # checks results where possible
tests/
  test_expert_system.py
.github/
  workflows/tests.yml    # automated tests on GitHub
requirements.txt
```

## Install and run locally

Python 3.10 or newer is recommended.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Run the terminal version

Run this command from the repository root:

```bash
python -m math_expert_system.cli
```

### Run the Streamlit version locally

```bash
streamlit run math_expert_system/app.py
```

Streamlit will show a local URL in the terminal. Open that URL in your browser.

## Deploy on Streamlit Community Cloud

1. Push or merge the completed project files into the GitHub repository's `main` branch.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with GitHub.
3. Choose **Create app** and select this repository.
4. Select branch `main`.
5. Set **Main file path** to `math_expert_system/app.py`.
6. Select **Deploy**. Streamlit installs the packages listed in `requirements.txt`.

If the app is not found, check that the selected branch contains the `math_expert_system/app.py` file and that the main file path is typed exactly as shown.

## Example questions

- `solve 2*x + 3 = 7`
- `solve x^2 - 5*x + 6 = 0`
- `differentiate x^3 + 2*x`
- `integrate 3*x^2`
- `area of circle radius 4`
- `circumference of circle radius 4`
- `area of rectangle length 5 width 3`
- `area of triangle base 10 height 6`
- `sin 30`
- `cos 60`
- `simplify x + x + 2`

Use `help` in the terminal application to see examples, or `quit` to exit. Use `^` or `**` for powers.

## Run automated tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions also runs the test suite on pushes to the project branch and on pull requests targeting `main`.

## How the expert system works

1. **Input:** the user enters a mathematics question.
2. **NLP parser:** converts a supported question into structured operation data.
3. **Knowledge base:** stores production rules describing supported mathematical tasks.
4. **Inference engine:** matches the question to relevant rules and records the selected rule.
5. **Solver:** performs the calculation with Python or SymPy.
6. **Verifier:** checks results where an appropriate check is available. It reports when a symbolic result has not been independently verified.
7. **Output:** displays the answer, explanation, verification status, and reasoning trace.

This is an educational project. The parser supports specific question patterns; it does not claim to understand every possible sentence. Numerical finiteness checks are not a proof of mathematical correctness.
