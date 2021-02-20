# Your code here!!
def sing():
    first_para = "let it be, "
    second_para = "whisper words of wisdom, "
    third_para = "there will be an answer, "

    for i in range(4):
        print(first_para)
    for i in range(1):
        print(second_para + (first_para * 2))
    for i in range(3):
        print(first_para)
    for i in range(1):
        print(third_para + first_para[:9])
        

sing()

