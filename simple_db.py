import sys

file_db = 'db.txt'
#first_arg = sys.argv[1]
#second_arg = sys.argv[2]


def write_to():
    db = open(file_db,'a')
    db.write(enc('work') + '\n')
    db.write(enc('now'))
    db.close()

def enc(str):
	return ' '.join(format(ord(x), 'b') for x in str)

def read():
    file_db = open("db.txt", "rb")
    file_r = file_db.read().decode("utf-8")     
    file_r = ''.join(chr(int(file_r[i*8:i*8+8],2))for i in range(len(file_r)//8))
    print(file_r)


if __name__ == "__main__":
    write_to()
    read()