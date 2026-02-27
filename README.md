# Project Dependencies

This project uses Python and requires the installation of the packages listed in `requirements.txt`.

## How to Install Dependencies

1. Make sure you have Python installed (recommended: Python 3.8+).
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install the dependencies with:
   ```bash
   pip install -r requirements.txt
   ```

## About requirements.txt

The `requirements.txt` file contains the complete list of libraries needed to run the project. Whenever you add or remove packages, update this file with:

```bash
pip freeze > requirements.txt
```

## Notes
- You do not need to upload the installed libraries or the virtual environment folder to the repository.
- Only the `requirements.txt` file should be versioned.

---

