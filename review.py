# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


# Issue: Using a mutable list [] as default argument will make the same list to be reused across function calls and leading error
# Review 1 fixed:
def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

# Issue: Wrong string formatting syntax, missing f-string
# Review 2 fixed:
def format_greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3
class Counter:
    count = 0
    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count
    
# Issue: Count is a class variable, shared by all instances, self.count is an instance variable, unique to each instance
# Review 3 fixed:
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


# Review 4
import threading
class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()

threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

# Issue: The SafeCounter implementation is not thread-safe and will lead to race conditions
# Review 4 fixed:
import threading

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()  # Add lock for thread safety
    
    def increment(self):
        with self.lock:  # Use lock to ensure thread-safe access
            self.count += 1
    
    def get_count(self):
        with self.lock:
            return self.count

def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1
        else:
            counts[item] = 1
    return counts


# Issue: Using =+ instead of += for increment operation
# Review 5 fixed:
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] =+ 1
        else:
            counts[item] = 1
    return counts


