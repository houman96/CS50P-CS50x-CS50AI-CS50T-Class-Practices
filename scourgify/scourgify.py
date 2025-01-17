import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            makeclear(sys.argv[1], sys.argv[2])


def makeclear(input, output):
    try:
        with open(input) as input:
            reader = csv.DictReader(input)
            with open(output, "w") as output:
                header = ["firstname", "lastname", "house"]
                writer = csv.DictWriter(output, fieldnames = header)
                writer.writeheader()
                for student in reader:
                    lastname, firstname = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"firstname": firstname, "lastname": lastname, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()
