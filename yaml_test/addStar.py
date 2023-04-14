in_name = "D:/VacQ/vacq/yaml_test/" + "noStar.yaml"
out_name = "D:/VacQ/vacq/yaml_test/" + "star.txt"

fin = open(in_name, "r", encoding="utf8")
fout = open(out_name, "w", encoding="utf8")

for line in fin:
    if line[0] != "*" and line[:3] != "/**" and line[:2] != "*/" and line.strip() != "":
        fout.write("* "+line)
    else:
        fout.write(line)
fout.close()
