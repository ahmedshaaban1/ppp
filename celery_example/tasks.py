from __future__ import absolute_import
from . import app

def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

@app.task
def fibonacci(n):
    return fib(n)
