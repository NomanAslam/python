import sys
import timeit
from timeit import default_timer as timer
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
from functools import reduce
import logging
import json
import random, secrets
import numpy as np
import functools
from multiprocessing import Process, Value, Array, Lock
import os
import time
from threading import Thread, current_thread#, Lock
#from queue import Queue
from multiprocessing import Queue

type = 17
#List: is a collection datatype which is ordered, mutable, allows duplicate (created using Square Brackets)
if type == 1:
    list1 = ['apple', 'banana']

    list1.append('orange')
    list1.insert(1, 'mango')
    list1.pop(0)
    list1.remove('banana')
    list1.reverse()
    list1.sort()

    print (list1)

    list2 = [0] * 5
    print(list2)

    list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print (list2 + list3)

    print(list3[0:2])
    print(list3[:4])
    print(list3[::2])
    print(list3[::-1])          #it will reverse the list

    list4 = ['apple', 'banana']
    list5 = list4               #any change in one list also changes other list because both list refer the same list inside the memory
    list4.append('mango')
    print(list5)

    list4 = ['apple', 'banana']
    list5 = list4.copy()
    list5 = list(list4)
    list5 = list4[:]
    list4.append('mango')
    print(list5)

    list6 = [1, 2, 3, 4, 5]
    list7 = [i*i for i in list6]
    print(list7)

#Tuple: is a collection datatype which is ordered, immutable, allows duplicate values (created using parenthesis)
elif type == 2:
    tuple1 = ('apple', 'banana')
    print(tuple1)

    tuple2 = 'apple', 'banana'
    print(tuple1)
    print(tuple1[1])

    tuple3 = tuple(['apple', 'banana'])
    print(tuple3)

    for item in tuple3:
        print(item)

    if 'apple' in tuple3:
        print('yes')
    else:
        print('no')

    list8 = list(tuple3)
    tuple4 = tuple(list8)
    print(list8)
    print(tuple4)

    tuple5 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(tuple5[:2])
    print(tuple5[:])
    print(tuple5[1:])
    print(tuple5[::2])
    print(tuple5[::-1])

    #unpack a tuple
    fruit1, fruit2 = tuple1
    print(fruit1)
    print(fruit2)

    i1, *i2, i3 = tuple5
    print(i1)
    print(i2)
    print(i3)

    #tuple takes less size
    list11 = [1, 2, 'Apple', 'Banana', True]
    tuple11 = (1, 2, 'Apple', 'Banana', True)
    print(sys.getsizeof(list11), 'bytes')
    print(sys.getsizeof(tuple11), 'bytes')

    #tuples takes less time to create than a list
    print(timeit.timeit(stmt="[1,2,3,4,5]", number=1000000))
    print(timeit.timeit(stmt="(1,2,3,4,5)", number=1000000))

#Distionaries, is a collection datatype which is in key-Value pairs, unordered and mutable (braces are used to create it)
elif type == 3:
    dic1 = {"name": "Noman", "age": 30, "City": "Isb"}
    print(dic1)

    dic2 = dict(name="Noman", age=20)
    print(dic2)

    print(dic1["name"])
    print(dic2["age"])

    dic1["email"] = "noman@gmail.com"
    dic1["name"] = "Noman Aslam"
    print(dic1)

    del dic1["email"]
    print(dic1)

    dic1.pop("name")
    print(dic1)

    dic1.popitem()
    print(dic1)

    if "name" in dic2:
        print("Yes")
    else:
        print("No")

    for key, value in dic2.items():
        print(key + ": " + str(value))

    dic1.update(dic2)
    print(dic1)

    dic3 = {3:9, 6:36, 9:81}
    print(dic3)
    print(dic3[3])

#Sets, unordered, mutable, no duplicates (braces are used to create it)
elif type == 4:
    set1 = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1}
    print(set1)

    set2 = set({1,2,3,2,1})
    print(set2)

    set3 = set("Hello")
    print(set3)

    set1.add(7)
    set1.remove(1)
    set1.discard(9)
    set1.pop()
    print(set1)

    for i in set1:
        print(i)

    if 1 in set1:
        print("yes")
    else:
        print("no")

    print(set1.union(set2))
    print(set1.intersection(set2))
    print(set1.difference(set2))
    print(set1.symmetric_difference(set2))

    set1.update(set2)
    print(set1)

    set1.intersection_update(set2)
    print(set1)

    set1.difference_update(set2)
    print(set1)

    set1.symmetric_difference_update(set2)
    print(set1)

    set1 = {1, 2, 3, 4, 5, 6}
    set2 = {1, 2, 3}

    print(set1.issubset(set2))
    print(set1.issuperset(set2))
    print(set1.isdisjoint(set2))

    set3 = frozenset([1,2,3,4,5])       #cannot change frozenset (it is immutable)
    print(set3)

#String, ordered, immutable, text representation
elif type == 5:
    s1 = "Hello"
    print(s1)

    s2 = """Hello \
        Word"""
    print(s2)

    s3 = "My String"
    print(s3[0:5])
    print(s3[:])
    print(s3[::2])         
    print(s3[::-1])         #reverse string

    for i in s1:
        print(i)

    if "elo" in s1:
        print("yes")
    else:
        print("No")

    s4 = "   Hello   "
    print(s4.strip())
    print(s1.upper())
    print(s1.lower())
    print(s1.startswith("He"))
    print(s1.endswith("lo"))
    print(s1.find("l"))         #returns first index of a character
    print(s1.count("l"))
    print(s1.replace("lo", "lo World"))

    s5 = "How are you doing"
    s5List = s5.split()
    s6 = ''.join(s5List)
    print(s5List)
    print(s5)

    var1 = "ABC"
    s7 = "This is a %s" %var1
    print(s7)

    var1 = "ABC"
    s7 = "This is a {}".format(var1)
    print(s7)

    var1 = "ABC"
    s7 = f"This is a {var1}"
    print(s7)

#Collection, counter, namedtuple, OrderedDict, defaultdict, deque
elif type == 6:

    #counter
    a = "aabbbbccdddd"
    count = Counter(a)
    print(count)
    print(count.keys())
    print(count.most_common(2))
    print(count.most_common(1)[0])
    print(count.most_common(1)[0][0])

    print(list(count.elements()))

    #namedtuple
    Point = namedtuple('Point', 'x,y')
    pt = Point(1, -4)
    print(pt)
    print(pt.x)
    print(pt.y)

    #OrderedDict
    ordered_dict = OrderedDict()
    ordered_dict['a'] = 1
    ordered_dict['b'] = 2
    ordered_dict['c'] = 3
    ordered_dict['d'] = 4
    print(ordered_dict)

    #defaultdict (it has a default value if key has not beet set yet)
    d = defaultdict(int)
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4
    print(d)
    print(d['a'])
    print(d['e'])

    #deque (double ended queue that can be used to add or remove elements from both side)
    d = deque()
    d.append(1)
    d.append(2)
    d.appendleft(3)
    print(d)
    
    d.pop()
    d.popleft()
    print(d)

    d.extend([4,5,6])
    print(d)

    d.extendleft([7,8,9])
    print(d)

    d.rotate(2) #rotate all element to n number of places to right side
    print(d)

#Itertools: product, permutation, combination, accumulate, groupby, and infinite iterators
elif type == 7:
    #product
    a = [1, 2]
    b = [3, 4]
    prod = product(a, b)
    print(list(prod))

    prod = product(a, b, repeat = 2)
    #print(list(prod))

    #permutation
    a = [1, 2, 3]
    perm = permutations(a)
    print(list(perm))

    perm = permutations(a, 2)
    print(list(perm))

    #combinations
    a = [1, 2, 3, 4]
    comb = combinations(a, 2)
    print(list(comb))

    comb = combinations_with_replacement(a, 2)
    print(list(comb))

    #accumulate
    a = [1, 2, 3, 4]
    accu = accumulate(a)
    print(list(accu))

    a = [1, 2, 3, 4]
    accu = accumulate(a, func=operator.mul)
    print(list(accu))

    a = [1, 2, 5, 3, 4]
    accu = accumulate(a, func=max)
    print(list(accu))

    #groupby
    def smallerThanThree(x):
        return x < 3
    
    a = [1,2,3,4]
    group_by = groupby(a, key=smallerThanThree)
    for key, value in group_by:
        print(key, list(value))

    #infinite iterators
    for i in count(10):
        print(i)
        if (i == 15):
            break

    a = [1,2,3]
    for i in cycle(a):
        print(i)

    for i in repeat(1, 4):
        print(i)

#lambda arguments: expression (one line function)
elif type == 8:
    add10 = lambda x: x + 10
    print(add10(5))

    mult = lambda x,y: x * y
    print(mult(3,4))

    #map
    a = [1,2,3,4,5]
    b = map(lambda x: x*2, a)
    print(list(b))

    c = [x*2 for x in a]
    print(c)

    #filter
    a = [1,2,3,4,5,6]
    b = filter(lambda x: x%2==0, a)
    print(list(b))

    c = [x for x in a if x%2==0]
    print(c)

    #reduce
    a = [1,2,3,4]
    prod = reduce(lambda x, y: x*y, a)
    print(prod)

#Errors and exceptions
elif type == 9:
    try:
        a = 5 / 1
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print("everything is fine")
    finally:
        print("Cleaning up...")

    class ValueTooHighError(Exception):
        pass

    class ValueTooSmallError(Exception):
        def __init__(self, message, value):
            self.message = message
            self.value = value

    def test_value(x):
        if x > 100:
            raise ValueTooHighError('Value is too high')
        
        if (x < 5):
            raise ValueTooSmallError('Value is too small', x)
        
    try:
        test_value(1)
    except ValueTooHighError as e:
        print(e)
    except ValueTooSmallError as e:
        print(e.message, e.value)

#Logging
elif type == 10:
    logging.debug("debug Message")
    logging.info("info Message")
    logging.warning("warning Message")
    logging.error("error Message")
    logging.critical("critical Message")

    try:
        a = [1,2,3]
        val = a[4]
    except IndexError as e:
        logging.error(e, exc_info=True)

#JSON
elif type == 11:

    #encode dictionary into json
    person = {"name": "Noman", "age": 30, "is_married": True, "title": ["Engineer", "Developer"]}
    personJson = json.dumps(person, indent=2, sort_keys=True)
    print(person)
    print(personJson)

    with open('zz.txt', 'w') as file:
        json.dump(person, file, indent=4)

    #decode json into dictionary
    person = json.loads(personJson)
    print(person)

#Random Numbers
elif type == 12:
    #random
    a = random.random()
    print(a)

    a = random.uniform(1, 10)
    print(a)

    a = random.randint(1, 10)
    print(a)

    a = random.randrange(1, 10)
    print(a)

    #secrets
    print(secrets.randbelow(10))
    print(secrets.randbits(4))
    print(secrets.randbelow(10))

    #numpy
    a = np.random.rand(3)
    print(a)

    print(np.random.randint(2, 10))

    print(np.random.randint(2, 10, 3))
    print(np.random.randint(2, 10, (3, 4)))

#Decorators: Function decorators and Class decorators
elif type == 13:

    def start_end_decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("start")
            result = func(*args, **kwargs)
            print("end")
            return result
        
        return wrapper

    @start_end_decorator
    def print_name():
        print("Hello Noman")

    @start_end_decorator
    def add5(x):
        return x+5

    #print_name = start_end_decorator(print_name)

    print_name()
    result = add5(10)
    print(result)

    print(help(add5))

    def repeat(num_times):
        def repeat_decorator(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for _ in range(num_times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return repeat_decorator
    
    @repeat(num_times=3)
    def greet(name):
        print(f'Hello dear {name}')

    greet("Noman")

    #class decorator
    class CountCalls:

        def __init__(self, func):
            self.func = func
            self.num_calls = 0

        def __call__(self, *args, **kwargs):
            self.num_calls += 1
            print(f"this is executed {self.num_calls} times")
            return self.func(*args, **kwargs)
        
    @CountCalls
    def say_hello():
        print('hello')

    say_hello()
    say_hello()

#Generators: are functions that return an object that can be iterated over.
elif type == 14:

    def my_generator():
        yield 1
        yield 2
        yield 3

    g = my_generator()
    for i in g:
        print(i)

    g = my_generator()

    value = next(g)
    print(value)

    value = next(g)
    print(value)

    print(sum(g))

#Threading and Multiprocessing
elif type == 15:

    def square_number():
        for i in range(100):
            i * i
            time.sleep(0.1)

    """ processes = []
    num_process = os.cpu_count()

    for i in range(num_process):
        p = Process(target=square_number)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join() """

    print("end main")

    #threads
    threads = []
    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=square_number)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("end main")

#Threading
elif type == 16:
    database_value = 0

    def increase(lock):
        global database_value

        with lock:
            local_copy = database_value

            #processing
            local_copy +=1
            time.sleep(0.1)
            database_value = local_copy
        
    if __name__ == "__main__":

        lock = Lock()
        print('start value: ', database_value)

        thread1 = Thread(target=increase, args=(lock,))
        thread2 = Thread(target=increase, args=(lock,))
    
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        print('end value: ', database_value)

        #queue
        q = Queue()

        q.put(1)
        q.put(2)
        q.put(3)

        first = q.get()
        print(first)
        q.task_done()

        print(q.empty())

        def worker(q, lock):
            while True:
                value = q.get()
                #processing
                with lock:
                    print(f"in {current_thread().name} got {value}")
                q.task_done()

        q = Queue()
        lock = Lock()
        num_threads = 10

        for i in range(num_threads):
            thread = Thread(target=worker, args=(q,lock))
            thread.daemon = True
            thread.start()

        for i in range(1, 21):
            q.put(i)
        
        q.join()

#Threading
elif type == 17:

    def add_100(numbers, lock):
        for i in range(100):
            time.sleep(0.01)
            for i in range(len(numbers)):
                with lock:
                    numbers[i] += 1

    def square(numbers, queue):
        for i in numbers:
            queue.put(i*i)

    def make_negative(numbers, queue):
        for i in numbers:
            queue.put(-1*i)
            
    if __name__ == "__main__":

        lock = Lock()
        shared_array = Array('d', [0.0, 100.0, 200.0])
        print('Array at beginning is', shared_array[:])

        p1 = Process(target=add_100, args=(shared_array,lock))
        p2 = Process(target=add_100, args=(shared_array,lock))

        p1.start()
        p2.start()
        
        p1.join()
        p2.join()

        print('Array at end is', shared_array[:])

        #Queue
        numbers = range(1,6)
        q = Queue()

        p1 = Process(target=square, args=(numbers, q))
        p2 = Process(target=make_negative, args=(numbers, q))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        while not q.empty():
            print(q.get())

        print("Good Job 1")

        print("Good Job 2")

