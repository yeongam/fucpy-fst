def span(eggs):
    print("ham:", ham)
    print("eggs1:", eggs)
    eggs.append(1)
    print("eggs1:", eggs)
    eggs = [2, 3]
    print("eggs2:", eggs)
    print("ham:", ham)

ham = [0]
span(ham)
print(ham)