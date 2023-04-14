in_name = "D:/VacQ/vacq/yaml_test/" + "original.txt"
out_name = "D:/VacQ/vacq/yaml_test/" + "noStar.txt"

fin = open(in_name, "r", encoding="utf8")
fout = open(out_name, "w", encoding="utf8")

for line in fin:
    if line[:2] == "* ":
        fout.write(line[2:])
    else:
        fout.write(line)
fout.close()
