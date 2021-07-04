
SKELETONFILE = interface/Adaptive_server.skeleton.cpp

build-server: move-skeleton cmakes

clean-skeleton:
	rm -f ${SKELETONFILE}

move-skeleton:
	[ ! -f ${SKELETONFILE} ] || mv ${SKELETONFILE} .

clean:
	rm -r server_build/CMakeFiles server_build/CMakeCache.txt server_build/Adaptive server_build/cmake_install.cmake server_build/Makefile

cmakes:
	cmake -Bserver_build -Hserver_build
	cmake --build server_build
