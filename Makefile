objects = main.o BPlusTree.o
test: $(objects)
	cc -g -o test  $(objects)
main.o: main.c BPlusTree.h
	cc -g -c main.c BPlusTree.h
BPlusTree.o: BPlusTree.c BPlusTree.h
	cc -g -c BPlusTree.c BPlusTree.h
.PHONY: clean
clean:
	-rm test $(objects)
