BASEDIR = ..

PYGENDIR = interface_py
PYNAMESPACE = adaptive/interface
PYMVDIR = ${BASEDIR}/interface

CPPGENDIR = interface_cpp
CPPMVDIR = ${BASEDIR}/server/interface

build-thrift: build-python-thrift build-cpp-thrift

clean-thrift: \
	pre-clean-python \
	post-clean-python \
	pre-clean-cpp \

build-python-thrift: \
	pre-clean-python \
	gen-python-thrift \
	copy-python-thrift \
	post-clean-python

pre-clean-python:
	rm -r -f ${PYMVDIR}

gen-python-thrift:
	mkdir -p ${PYGENDIR}
	thrift -r -out ${PYGENDIR} --gen py Makefile.thrift

copy-python-thrift:
	cp -r ${PYGENDIR}/${PYNAMESPACE} ${PYMVDIR}

post-clean-python: 
	rm -r -f ${PYGENDIR}

build-cpp-thrift: \
	pre-clean-cpp \
	gen-cpp-thrift \
	copy-cpp-thrift \
	post-clean-cpp

pre-clean-cpp:
	rm -r -f ${CPPMVDIR}

gen-cpp-thrift:
	mkdir -p ${CPPGENDIR}
	thrift -r -out ${CPPGENDIR} --gen cpp Makefile.thrift

copy-cpp-thrift:
	mkdir -p ${CPPMVDIR}
	cp -r ${CPPGENDIR}/* ${CPPMVDIR}

post-clean-cpp: 
	rm -r -f ${CPPGENDIR}
