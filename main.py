import sys

def convert_to_hex(data: bytes) -> list[str]:
  chunk_size = 4
  hex_string = "".join(hex(byte)[2:].zfill(2) for byte in data)
  new = [hex_string[i:i + chunk_size] for i in range(0, len(hex_string), chunk_size)]
  temp = []
  for i in range(0, len(new), 8):
      temp.append(new[i:i + 8])
  new = temp
  return new

def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    return

  file = sys.argv[1]

  try:
    with open(file, "rb") as f:
      content = f.read()
      content_hex = convert_to_hex(content)
      for i in range(len(content_hex)):
          print(content_hex[i])
  except FileNotFoundError:
    print(f"Error: File '{file}' not found")

if __name__ == "__main__":
  main()