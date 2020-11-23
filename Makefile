PREFIX=/usr
BINDIR = ${PREFIX}/bin

all: bar

bar: bar.c
	$(CC) -o bar $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) bar.c -lfoo

install: bar
	mkdir -p $(DESTDIR)$(BINDIR)
	install bar $(DESTDIR)$(BINDIR)/
