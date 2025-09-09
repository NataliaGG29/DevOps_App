# DevOps_app

![CI](https://github.com/NataliaGG29/DevOps_App/actions/workflows/ci.yml/badge.svg)

This project combines **a Python calculator** with **basic DevOps practices**.  
The goal is to learn how to apply **Continuous Integration (CI)** using GitHub Actions while developing a simple app.

---

## 🧮 Calculator Features

- Basic operations: `+`, `-`, `*`, `/`
- Decimal support
- Clear button `C`
- `Calculator` class for better maintainability
- Graphical user interface with Tkinter

---

## ⚙️ DevOps Features

- GitHub Actions pipeline that runs on push or pull request to the `main` branch
- Continuous Integration (CI) pipeline:
  - Linting with `flake8`.
  - Enforces clean and consistent code style.  

---

## 🛠️ Tech Stack
- **Language**: Python 3.x  
- **GUI Library**: Tkinter  
- **DevOps Tools**: GitHub Actions, flake8
---

## 📂 Project Structure
```bash
DevOps_App/
│── .github/workflows/ci.yml   # GitHub Actions workflow
│── calculatorApp.py            # Main calculator app
│── README.md                   # Project documentation
