import os
import subprocess

def archive():
  usersfile = open('data/users.txt', 'w+')
  users = []
  d = os.path.expanduser('~/../')
  for o in os.listdir(d):
    if os.path.isdir(os.path.join(d,o)):
      os.path.join(d,o)
      users.append((o+'\n'))
  usersfile.writelines(users)
  # subprocess.call(['ls',d,'>','data/users3.txt'])

if __name__ == '__main__':
  archive()
