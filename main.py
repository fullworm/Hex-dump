import sys

def convert_to_hex(data):
  chunk_size = 4
  hex_string = "".join(hex(byte)[2:] for byte in data)
  return [hex_string[i:i + chunk_size] for i in range(0, len(hex_string), chunk_size)]

def main():
  file = sys.argv[1]
  with open(file, "rb") as f:
    content = f.read()
    content_hex = convert_to_hex(content)
  print(content_hex)


if __name__ == "__main__":
  main()