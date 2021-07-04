BASEDIR = ..

PYGENDIR = interface_py
PYNAMESPACE = adaptive/interface
PYMVDIR = ${BASEDIR}/interface

build-thrift: build-python-thrift

clean-thrift: \
	pre-clean-python \
	post-clean-python \

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
