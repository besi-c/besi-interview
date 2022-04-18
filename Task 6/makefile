IDIR =../include
CFLAGS = -I$(IDIR)
ODIR = obj
LDIR = ../lib

%.o: %.c
	clang -c -o $@ $<

getmac: main.o
	clang -o getmac main.o

.PHONY: clean

clean:
	rm -f getmac *.o