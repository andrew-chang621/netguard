def format_log_data(log_file_path: str) -> list:
    """
    Takes in a log file ufw log file as an input and
    formats it into a Python dictionary.

    Args:
        log_file_path (str): Path to the log file to be parsed.

    Returns:
        list: A list of dictonaries corresponding to formated log data.
    """

    formatted_logs = []

    with open(logs_file_path) as log_file:
        content = log_file.readlines()

        for line in content:
            new_data = {}
            new_data["date"] = line.split(" raspberrypi")[0]
            line = line.split(" ")

            for atribute in line:
                if "SRC" in atribute:
                    new_data["source"] = atribute.split("=")[1]
                elif "MAC" in atribute:
                    new_data["mac"] = atribute.split("=")[1]
                elif "PROTO" in atribute:
                    new_data["protocol"] = atribute.split("=")[1]
                elif "LEN" in atribute:
                    new_data["packetLength"] = atribute.split("=")[1]

            formatted_logs.append(new_data)

    return formatted_logs


if __name__ == "__main__":
    logs_file_path = "./test-logs.txt"

    for log in format_log_data(logs_file_path):
        print(log)
