a = 33
print("Block1")  # Block1

if a == 3:
    print("Block2")  # Block2
    print("Block2")  # Block2
else:
    print("Block3")  # Block3
    print("Block3")  # Block3

    if a < 10:  # Dieser Block ist ein Unterblock des else-Blocks
        print("Block4")  # Block4
        print("Block4")
        print("Block4")
        print("Block3")
        print("Block1")
    print("Block3")