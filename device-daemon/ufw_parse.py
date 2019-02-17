def format_log_data(testLine):
    """
    Takes in a log file ufw log file as an input and
    formats it into a Python dictionary.

    Args:
        recent_network_calls: Unformatted list of network calls

    Returns:
        list: A list of dictonaries corresponding to formated log data.
    """

    formatted_logs = []

    for line in testLine:
        new_data = {}
        new_data["date"] = line.split(" raspberrypi")[0]
        line = line.split(" ")

        # print(line)

        for element in line:
            if "SRC" in element:
                new_data["source"] = element.split("=")[1]
            elif "MAC" in element:
                new_data["mac"] = element.split("=")[1]
            elif "PROTO" in element:
                new_data["protocol"] = element.split("=")[1]
            elif "LEN" in element:
                new_data["packetLength"] = element.split("=")[1]

        formatted_logs.append(new_data)

    return(formatted_logs[0])


if __name__ == "__main__":
    testLine = ["Feb 17 07:25:57 raspberrypi kernel: [ 1350.091508] [UFW BLOCK] IN=wlan0 OUT= MAC=b8:27:eb:bb:4a:3f:d4:61:9d:0b:a4:e6:08:00 SRC=172.20.10.2 DST=172.20.10.4 LEN=64 TOS=0x00 PREC=0x00 TTL=255 ID=0 DF PROTO=TCP SPT=55372 DPT=8290 WINDOW=65535 RES=0x00 SYN URGP=0"]
    format_log_data(testLine)
