def save_to_file(data, file):
    fp = open(file, "a")
    fp.write("Headers: \r\n")
    fp.write(str(data.headers) + "\r\n")
    fp.write("Body: \r\n")
    fp.write(str(data.data) + "\r\n")
    fp.close()