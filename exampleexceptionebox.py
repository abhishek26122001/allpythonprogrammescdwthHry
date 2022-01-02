def getMonth(m):
    if m<1 or m>12:
        raise ValueError("Invalid")
    print(m)
getMonth(6)

print("\n")

#example 2

def foo():
    try:
        return 1
    finally:
        return 2
        
k = foo()
print(k)

print("\n")

#Example 3
def print_Square(num):
    print("Square: {}".format(num * num))
if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t1.join()
    print("Done!")
 