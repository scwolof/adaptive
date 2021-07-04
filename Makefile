.PHONY: all clean thrift python

DIV = "-------------------------------"

BASEDIR = adaptive
INTERFACEDIR = ${BASEDIR}/thrift
CLIENTDIR = ${BASEDIR}/client

all: clean thrift python

clean:
	@echo ${DIV}
	rm -r -f build dist adaptive.egg-info
	make clean-thrift -C ${INTERFACEDIR}

thrift:
	@echo ${DIV}
	@echo "Compile thrift"
	make build-thrift -C ${INTERFACEDIR}

python:
	@echo ${DIV}
	@echo "python setup install"
	python setup.py -q install