#write a program to generate a multiplication 
# table from 2 to 20 and write it to the different files 
# place these files in a folder

for i in range(2,21):
    with open(f"MultiplicationTable/TableOf{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")

