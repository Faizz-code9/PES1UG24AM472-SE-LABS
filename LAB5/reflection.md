# Lab 5: Static Code Analysis — Reflection

### 1. How did Pylint, Bandit, and Flake8 complement each other during this lab?
Each tool targeted a distinct layer of software quality:
- **Bandit** focused exclusively on security vulnerabilities that linters might ignore, catching high-risk flaws like `eval()`, `os.system()` command injection, weak `MD5` hashing, predictable PRNG (`random`), and hardcoded secrets.
- **Pylint** acted as a deep code quality and design reviewer, catching logical bugs and Python anti-patterns such as mutable default arguments (`baggage_tags=[]`), bare `except:` blocks, unclosed file handles (`open()` without `with`), variable shadowing, and missing docstrings.
- **Flake8** enforced PEP 8 style consistency, flagging line lengths exceeding 79 characters, `== None` comparisons, unused variables/imports, and missing blank lines between top-level functions.

### 2. Which issue found in `flight_reservation_system.py` was the most critical, and why?
The most critical issues were the **security vulnerabilities in `calculateBaggageFee` (`eval()`) and `exportFlightManifest` (`os.system()`)**. Passing user-controlled strings into `eval()` allows arbitrary Python code execution on the server, while concatenating `filename` into `os.system("echo ... " + filename)` enables OS command injection. Replacing `eval()` with direct floating-point multiplication and replacing `os.system()` with native Python output completely eliminated the attack surface.

### 3. Were there any issues that required careful trade-offs or human judgment to fix?
Yes:
- **Mutable Default Arguments (`baggage_tags=[]`)**: Simply removing the default would break callers expecting an optional parameter. Changing the default to `None` and initializing a new list inside the function preserved the function signature while preventing state leakage across calls.
- **Exception Handling (`cancelBooking`)**: Replacing the bare `except:` required identifying what specific exception could legitimately occur (`KeyError` when an invalid flight number is passed) rather than catching broad `Exception` or letting the program crash.

### 4. How does integrating static code analysis into a CI/CD pipeline improve software maintainability?
Running Bandit, Pylint, and Flake8 automatically on every commit or pull request acts as an automated quality gate. It prevents security vulnerabilities, subtle runtime bugs (like mutable defaults or swallowed exceptions), and formatting inconsistencies from ever reaching production. This reduces human code-review fatigue, enforces a uniform coding standard across the team, and lowers long-term technical debt.
