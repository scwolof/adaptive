cmake_minimum_required(VERSION 3.5)

project(Adaptive)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall -DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H")
set(THRIFT_DIR "/usr/local/include/thrift")
set(BOOST_DIR "/usr/lib/")

include_directories(${THRIFT_DIR} ${BOOST_DIR} ${CMAKE_SOURCE_DIR})
link_directories(/usr/local/lib)

set(SERVER_FILE ../Adaptive_server.cpp)
file(GLOB server_SRC
     "../interface/*.h"
     "../interface/*.cpp"
)

add_executable(Adaptive ${SERVER_FILE} ${server_SRC})
target_link_libraries(Adaptive thrift)
