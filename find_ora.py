with open("alert_sample.log", encoding="utf-8") as f:
    for line in f:
        if "ORA-" in line:
            print(line.strip())
            break
