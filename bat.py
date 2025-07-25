import random
import time

# import time && random


class main:
    word = ["@", "#"]

    def gen(self, name):
        output = []
        worn = []  # eror cath the bin
        for i in range(1500):
            pw1 = (
                random.choice(self.word)
                + random.choice(self.word)
                + random.choice(self.word)
            )
            pw2 = random.choice(self.word) + random.choice(self.word)
            pw3 = (
                random.choice(self.word)
                + random.choice(self.word)
                + random.choice(self.word)
                + random.choice(self.word)
            )
            if pw1 == "@#@" or pw1 == "#@#" or pw1 == "#@@" or pw1 == "###":
                worn.append(pw1)
            else:
                output.append(pw1)
            if pw2 == "#@" or pw2 == "@#" or pw2 == "##" or pw2 == "@@":
                worn.append(pw2)
            else:
                output.append(pw2)
            if (
                pw3.startswith("##")
                or pw3.startswith("@#")
                or pw3.startswith("#@")
                or pw3.startswith("@@")
            ):
                worn.append(pw3)
            else:
                output.append(pw3)
        with open(f"{name}.txt", "w") as f:
            for word_to in output:
                f.write(word_to + "\n")
            time.sleep(2.3)
            print(f"\033[0;31m{name}.txt\033[0m file open word list.")
            print("\033[7;32mREAD:\033[0m The basic word list genrte tool, 3900+")

    def main(self):
        print("""
        ▀█████████▄╶╶╶╶╶▄████████╶╶╶╶╶███╶╶╶╶╶ 
        ╶╶███╶╶╶╶███╶╶╶███╶╶╶╶███╶▀█████████▄╶ 
        ╶╶███╶╶╶╶███╶╶╶███╶╶╶╶███╶╶╶╶▀███▀▀██╶ 
        ╶▄███▄▄▄██▀╶╶╶╶███╶╶╶╶███╶╶╶╶╶███╶╶╶▀╶ 
        ▀▀███▀▀▀██▄╶╶▀███████████╶╶╶╶╶███╶╶╶╶╶ 
        ╶╶███╶╶╶╶██▄╶╶╶███╶╶╶╶███╶╶╶╶╶███╶╶╶╶╶ 
        ╶╶███╶╶╶╶███╶╶╶███╶╶╶╶███╶╶╶╶╶███╶╶╶╶╶ 
        ▄█████████▀╶╶╶╶███╶╶╶╶█▀╶╶╶╶╶▄████▀╶╶╶ 
        ╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶ """)

        print("\033[0;31m➠ \033[0;32mBat word list.")
        w1 = input("\033[1;34m[\033[0;32m+\033[1;34m]\033[0;35m Name : \033[0m")
        w2 = input("\033[1;34m[\033[0;32m+\033[1;34m]\033[0;35m Number : \033[0m")
        w3 = input("\033[1;34m[\033[0;32m+\033[1;34m]\033[0;35m Other :\033[0m")
        is_name = input("\033[1;32m Enter the word list name \033[0;34m: \033[0m")

        self.word.append(w1)
        self.word.append(w2)
        self.word.append(w3)
        self.gen(is_name) #call the funtion


m = main()
m.main()
