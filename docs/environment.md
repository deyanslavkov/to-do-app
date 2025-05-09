## Development Environment and Code Management

The project is hosted in a GitHub repository. All code changes are tracked using Git version control and follow a structured workflow:

- A dedicated **GitHub repository** is used to store the codebase. Sensitive or unnecessary files (e.g., database files, environment configs, editor settings) are excluded via a `.gitignore` file.

- **Feature branches** are used to isolate new features and changes. Each branch follows the naming convention `feature/<description>` and is merged into `main` via pull requests.

- Every pull request (PR) is linked to a corresponding **GitHub Issue** that describes the task. This ensures clarity, traceability, and cleaner collaboration. PRs include references like `Closes #3` to automatically close the associated issue when merged.

- The repository includes only essential files for building and running the application. Transient, OS-specific, or build-generated files are excluded from version control.

This workflow ensures a clean and maintainable codebase, with clear history and structured progress tracking.
