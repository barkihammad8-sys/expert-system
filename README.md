# Mathematics Expert System

A beginner-friendly, rule-based Mathematics Expert System built in Python. It accepts simple natural-language math questions, identifies the mathematical topic, applies knowledge-base rules, calls the appropriate solver, and returns a verified result with an explanation.

## Features

- Natural-language question handling for supported question patterns.
- Rule-based inference engine with traceable rule matches.
- Algebra: linear and quadratic equations, plus symbolic expression simplification.
- Calculus: symbolic differentiation and integration (powered by SymPy).
- Geometry: circle, rectangle, and triangle calculations.
- Trigonometry: sine, cosine, and tangent in degrees.
- Clear errors for unsupported or incomplete questions.
- Command-line interface and optional Streamlit web interface.
- Automated tests.

## Project structure

```text
math_expert_system/
  __init__.py
  app.py                 # optional Streamlit interface
  cli.py                 # terminal interface
  core.py                # coordinates parsing, inference, solving and verification
  inference_engine.py    # rule matching and inference trace
  knowledge_base.py      # expert rules and topic knowledge
  nlp.py                 # natural-language question parser
  solvers.py              # mathematical operations
  verifier.py             # result checks
tests/
  test_expert_system.py
requirements.txt
```

## Setup

Python 3.10 or newer is recommended.

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
pip install -r requirements.txt
```

## Run the command-line application

From the repository root:

```bash
python -m math_expert_system.cli
```

Try questions such as:

- `solve 2*x + 3 = 7`
- `solve x^2 - 5*x + 6 = 0`
- `differentiate x^3 + 2*x`
- `integrate 3*x^2`
- `area of circle radius 4`
- `area of rectangle length 5 width 3`
- `sin 30`

Type `help` for examples or `quit` to exit.

## Run the optional web interface

```bash
streamlit run math_expert_system/app.py
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## How the expert system works

1. **Input:** the user enters a mathematics question.
2. **NLP parser:** extracts the operation and values from supported natural-language patterns.
3. **Knowledge base:** stores topic rules and supported capabilities.
4. **Inference engine:** matches the question to relevant rules and records the reasoning trace.
5. **Solver:** performs the calculation using Python and SymPy where symbolic mathematics is needed.
6. **Verifier:** checks the returned result when a reliable check is available.
7. **Output:** displays the answer, explanation, matched rule, and verification status.

This is an educational expert system, not a replacement for a mathematics teacher or a computer algebra system. It deliberately supports a documented set of question patterns rather than claiming to understand every possible sentence.
