## Python Parallel Programming Presentation

Chris Kotfila
<br>
Kitware Inc.
<br>

---
## Plan of Action
+ What is parallel programming?
+ How can I do it in Python?

---

## What is Parallel Programming?

+++

## What is regular programming?

```python
ds = xr.open_dataset('/path/to/some.nc')
```

+++ 

## What is regular programming?

+ Inputs
+ Functions
+ Outputs

+++ 

## Functions are where the work gets done

```python
ds = xr.open_dataset('/path/to/some.nc')

avg = ds.groupby('time.season') / ds.astype(float).groupby('time.season').sum()
```
Some times the work takes a long time.
<br>
We can't calculate ```avg``` until the ```ds = ... ``` statement is complete.
<br>
One after another, input, transformation, output

+++

## What is Parallel Programming?

+ Parallel programming is the process of 'pitching' work to some other process.
+ Once we've pictched to work to something else,  we can continue to the next statement.
