# import calculator

# print(calculator.CONSTANTS)
# print(calculator.add(1,2))
# print(calculator.sub(2,1))
# print(calculator.mul(1,2))
# print(calculator.div(4,2))

# a = calculator.A()
# print(type(a))
# # module name is calculator and class name is A 

# Filtered Import
from calculator import *
from calculator import (add as addition,
mul as multiplication,
a,
b,
c,
d,
e,
f)

print(globals())
print(addition(2,3))
print(sub(3,2))
print(a)

import calculator as lib #aliases

print("#####################################################################")
print(lib.add(1,2))

#below mymath is a package
import mymath
print("======================================================================")
print(mymath.a)

print("**********************************************************************")
#from package import module
# from mymath import (simple, 
# complex)
# print(simple.add(1,2))
# print(complex.cube(4))

print("////////////////////////////////////////////////////////////////////////////////////////")
from mymath import *
print(simple.add(1,2))
print(complex.cube(4))


print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

import asyncio
import time

async def waiter(n):
    await asyncio.sleep(n)
    print(f"waited for {n} seconds")

async def main():
    # Event loop
    task1 = asyncio.create_task(waiter(2)) #The worker thread was involved and the thread started executing.
    task2 = asyncio.create_task(waiter(3))

    print(time.strftime('%X'))
    # await task1
    # await task2
    await asyncio.sleep(3)
    print(time.strftime('%X'))

if __name__ == '__main__':
    asyncio.run(main())