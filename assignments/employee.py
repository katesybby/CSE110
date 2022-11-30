with open("hr_system.txt") as f:    #error = can't find file
    for line in f:
        clean_line = line.strip()
        parts = line.split(" ")
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])

        paid = salary/24

        if title.lower() == "engineer":
            paid += 1000

        print(f"{name} (ID: {id_number}), {title} - ${paid:.2f}")