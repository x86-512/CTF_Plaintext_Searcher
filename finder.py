def main() -> None:
  flag_format = input("What is the format of the flag:\n> ")
  bin_name = input("What is the format of the flag:\nExample: HTB{X}\n> ")
  to_find = bin_name.split("X")[0]
  trail = bin_name.split("X")[1]
  try:
    with open(bin_name, "r") as bin:
      

if __name__=="__main__":
  main()