# -*- encoding: utf-8 -*-
import re


def main(path, fst_col, scd_col, thrd_col):
    points = None
    num_aruco = None
    names_pictures = None
    with open(path, "r", encoding="UTF-8") as f:
        res_line = ""
        big_string = f.read().split("\n")

        for line in big_string:
            if re.search("aruco text", line.lower()):
                num_aruco = re.findall('"[0-9]+"', line)
                names_pictures = re.findall('"[А-ЯA-Z][\w\s]+"*', line)
            if re.search("points", line.lower()):
                points = re.findall('"[a-zA-Zа-яА-Я]+"|"[a-zA-Zа-яА-Я]+ \d+"', line)
            if points and num_aruco and names_pictures:
                for i in range(len(points)):
                    res_line += f"Patrolling {i+1}"
                    res_line += " "*(fst_col - len(res_line) - len(num_aruco[i])) + num_aruco[i]
                    res_line += " "*(scd_col+thrd_col - len(res_line) - len(names_pictures[i])) + names_pictures[i]
                    res_line += "\n"

                    if res_line:
                        saver(res_line)
                        res_line = ""

                points = None
                num_aruco = None
                names_pictures = None


def saver(log):
    with open("res.txt", "a", encoding="utf-8") as f:
        if log:
            f.write(log)


if __name__ == "__main__":
    fst_col = 20
    scd_col = 5
    thrd_col = 40
    path = "log.txt"
    saver(main(path, fst_col, scd_col, thrd_col))