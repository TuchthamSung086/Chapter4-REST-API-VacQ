in_name = "D:/VacQ/vacq/yaml_test/" + "hospitalModel.yaml"
out_name = "D:/VacQ/vacq/yaml_test/" + "hospitalModelStar.txt"

fin = open(in_name, "r", encoding="utf8")
fout = open(out_name, "w", encoding="utf8")

fout.write("/**\n")
fout.write("* @swagger\n")
for line in fin:
    l = "* " + line
    fout.write(l)
fout.write("\n*/")
fout.close()
