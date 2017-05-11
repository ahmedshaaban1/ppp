## Python Parallel Programming Presentation

Chris Kotfila
<br>
Kitware Inc.
<br>

---
## Plan of Action
+ What is parallel programming?
+ How can I do it in Python?
+ Notebook Examples

---

## What is Parallel Programming?

+++

## What is regular programming?

```python
ds = xr.open_dataset('/path/to/some.nc')
```
+ Inputs
+ Functions
+ Outputs

+++ 

## Functions are where the work gets done

```python
ds = xr.open_dataset('/path/to/some.nc')

avg = ds.groupby('time.season') / ds.astype(float).groupby('time.season').sum()
```
+ Some times the work takes a long time.
+ Can't calculate ```avg``` until the ```open_dataset`` is complete.
+ One after another, input, transformation, output

+++

## What is Parallel Programming?

+ Parallel programming is the process of 'pitching' work to some one else.
+ Once we've pictched to work to someone else,  we can continue to the next statement.

## What is Parallel Programming?

+ We're still taking input, doing work and getting output
+ Except now the 'work' is to give our real work to someone else
+ The output is usually a reference to where we can get the result of the work when it's done.

+++

## What is Parallel Programming?

+ Wait.. if we're pitching work, then waiting for it to complete,  what is the difference?

## What is Parallel Programming?

+ We can pitch as many jobs as we like, then wait for them all to complete

+++

## What is Parallel Programming?

If I have a function that takes 30 seconds and I need to run it 10 times, that will take me 5 minutes in wall time.  If I can pitch those 10 jobs to 10 different CPU's, then waiting for it to complete should only take ~30 seconds (thats 10x improvement!)

+++ 

## Embarassingly Parallel Programming

+ File conversion
+ Extract, Transform, Load pipelines
+ Paramater Sweeps 
+ Anything that can be cut up, worked on, and stitched back together. 


+++
## Who's pitching, Who's Catching?


--

## How can I do it in Python?

+++

## How can I do it in Python?
### (A curated list)
+ Subprocess
+ Multiprocessing
+ IPyParallel
+ Celery

+++

## Subprocess

+++

## Multiprocessing

+++

## IPyParallel

+++

## Celery

+++

