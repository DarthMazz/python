import psutil

psutil.virtual_memory()
import memory_profiler as MP

b1 = MP.memory_usage()[0]
b2 = MP.memory_usage()[0]
print(b2 - b1)

import pythonnet
from pythonnet import load

b2 = MP.memory_usage()[0]
print(f"load: {b2 - b1}")
load("coreclr")
b2 = MP.memory_usage()[0]
print(f"loaded coreclr: {b2 - b1}")
import clr

b2 = MP.memory_usage()[0]
print(b2 - b1)
clr.AddReference("CSharpDLL")
b2 = MP.memory_usage()[0]
print(b2 - b1)
import CSharpDLL as calc

cal = calc.Calculation()
# intの足し算
ret = cal.Add(1, 2)
print(ret, type(ret))
b2 = MP.memory_usage()[0]
print(b2 - b1)
