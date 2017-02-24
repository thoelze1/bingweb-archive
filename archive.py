import subprocess

def archive():
  subprocess.call(["ls", "~/../", ">", "data/users2.txt"])

if __name__ == '__main__':
  archive()
