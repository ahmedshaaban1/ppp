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
Inputs - Functions - Outputs

+++ 

## Functions are where the work gets done

```python
ds = xr.open_dataset('/path/to/some.nc')

avg = ds.groupby('time.season') / ds.astype(float).groupby('time.season').sum()
```
+ Some times the work takes a long time.
+ Can't calculate ```avg``` until ```open_dataset``` is complete.
+ One after another, input, transformation, output

+++

## What is Parallel Programming?

+ Parallel programming is the process of 'pitching' work to some one else.
+ Once we've pitched to work to someone else,  we can continue to the next statement.

+++

+ We're still taking input, doing work and getting output
+ Except now the 'work' is to give our real work to someone else
+ The output is usually a reference to where we can get the result of the work when it's done.

+++


Wait.. if we're pitching work then jus waiting for it to complete,  what is the difference?

+++ 


We can pitch as many jobs as we like off to other workers then wait for them all to complete

+++


This is like me trying to solve four rubix cubes versus handing off four rubix cubes to my friends. 

+++ 

If I have a function that takes 30 seconds and I need to run it 10 times, that will take me 5 minutes in wall time.  If I can pitch those 10 jobs to 10 different CPU's, then waiting for it to complete should only take ~30 seconds (that's 10x improvement!)

+++ 

## Embarrassingly Parallel Programming

+ File conversion
+ Extract, Transform, Load (ETL) pipelines
+ Parameter Sweeps 
+ Anything that can be cut up, worked on, and stitched back together. 


+++

## General Considerations
+ Who's pitching the work? 
+ Who's catching the work?
+ What exactly is being thrown?


---

## How can I do it in Python?

+++

## A curated list of parallel programming libraries
+ Subprocess
+ Multiprocessing
+ IPyParallel
+ Celery

+++

## Subprocess
+ Run a command line script from python
+ Built-in module (batteries included)
+ The ```subprocess``` module pitches
+ The operating system catches that work
+ Pitch a string that runs the command

+++

## Multiprocessing
+ Run a function in a different process
+ Built-in module (batteries included)
+ the ```multiprocessing``` module pitches
+ A ```Pool``` of process objects catches
+ Pitch a python function through the magic of forking

+++

## IPyParallel
+ Run functions in parallel from Jupyter Cells
+ a special ```view``` object does the pitching
+ The ```ipcluster``` or ```ipengine``` commands catch
+ Can be run across computers (but this takes a little work)
+ Pitch messages that contain data/function


+++

## Celery
+ Resiliently run hundreds of millions of functions.
+ A decorated function pitches itself
+ A message queue (```rabbitmq```) catches the work
+ The queue passes this to the ```celery worker``` command
+ Pitch messages the contain data/function
+ The technology that powers instagram. 

+++

## Notebook!

