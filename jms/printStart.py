import adder
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print(adder.add(5,50))
print(adder.add(100,200))
def a(a,b):
    if(a>b):
        print("a is bigger than b")
    else:
        print("a즐")

a(10,20)
a(20,1)
