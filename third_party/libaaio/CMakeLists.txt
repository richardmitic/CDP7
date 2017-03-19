set(AAIO_SRCS aaio.c)
set(AAIO_HEADERS aaio.h)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -pedantic -std=c99")

add_library(aaio ${AAIO_SRCS})