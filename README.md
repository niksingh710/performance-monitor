# Performance Monitor

Simple Decorator to represent the time took by a function execution.

## Installation

Run the following to install:

```python
pip install performance-monitor
```

## Usage

```python
from performance_monitor import *

@performance
def my_func():
    for _ in range(1000000):
        pass

my_func()

# Output
'''

:-: my_func --> 18.163681030273438 ms

'''

```

## Options

| Unit             | Decorator        |
| ---------------- | ---------------- |
| millisecond (ms) | @performance     |
| second (sec)     | @performance_sec |
| minute (min)     | @performance_min |
| hour (hr)        | @performance_hr  |
