# Python Backend Project

A lightweight backend application built with **Python 3.13**.  
It includes API logic, environment isolation, and containerization via **Docker** for easy deployment and scalability.

## How to run

To deploy this project

```
 git clone https://github.com/Homa4/Back-end.git
```

Open Docker

```bash
  docker build -t app .
```

```
  docker run --rm app
```

OR

You can deploy it manualy

```
  python3 -m venv venv
```

```
  source ./venv/bin/activate
```

```
  python3 -m pip install -r requirements.txt
```

```
  python3 main.py
```
