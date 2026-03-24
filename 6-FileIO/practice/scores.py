def main():
    nstudents = 0
    scores = {}
    total = 0
    largest = ()
    filename = input("enter filename: ")
    with open("scores.txt", "r") as infile, open(filename, "w") as outfile:
        for row in infile:
            name, score = row.strip().split(",")
            scores[name] = int(score)
            nstudents += 1
        for score in scores.values():
            total = total + score
        average = total / nstudents
        highest = 0
        for score in scores.values():
            if score > highest:
                highest = score
        for name, score in scores.items():
            if score == highest:
                top_student = name

        outfile.write(f"total students = {nstudents}\n")
        outfile.write(f"average score = {average} \n")
        outfile.write(f"highest score = {top_student}, ({highest}) \n")


if __name__ == "__main__":
    main()
