.PHONY: all clean thrift python cpp

DIV = "-------------------------------"

BASEDIR = adaptive
INTERFACEDIR = ${BASEDIR}/thrift
CLIENTDIR = ${BASEDIR}/client
SIMULDIR = ${BASEDIR}/simul
SERVERDIR = ${BASEDIR}/server

all: clean thrift python cpp

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

cpp:
	@echo ${DIV}
	@echo "Compile c++"
	make build-server -C ${SERVERDIR}

server:
	./${SERVERDIR}/server_build/Adaptive
