# WAP in python that reads a file and adds backslash (\) before every double quote it encounters.
# And then writes it to another file in the same folder.

# If the file name is testFile1.txt with text Jack said, "Hello Pune". The output to the file testFile2.txt
# Should be Jac said,\"Hello Pune\".

f1 = open("testFile1.txt", "r")
f2 = open("testFile2.txt", "w+")
# f = f1.readlines()
for i in f1.readlines():
    if i == 'H':
        print(i)

f1.close()
f2.close()