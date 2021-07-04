.PHONY: all clean thrift

DIV = "-------------------------------"

BASEDIR = adaptive
INTERFACEDIR = ${BASEDIR}/thrift

all: clean thrift

clean:
	@echo ${DIV}
	rm -r -f build dist adaptive.egg-info
	make clean-thrift -C ${INTERFACEDIR}

thrift:
	@echo ${DIV}
	@echo "Compile thrift"
	make build-thrift -C ${INTERFACEDIR}
