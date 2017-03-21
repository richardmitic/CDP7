if(APPLE)
  set(CMAKE_C_FLAGS "-O2 -Wall -mmacosx-version-min=10.5 -Dunix")
else()
  if(MINGW)
    set(CMAKE_C_FLAGS "-O2 -Wall -DWIN32")
  else()
    set(CMAKE_C_FLAGS "-O2 -Wall -Dlinux -Dunix")
  endif()
endif()

link_directories(../cdp2k ../sfsys)

include_directories(../../include)

add_library(extend-lib extend_main.c ap_extend.c drunk.c extprepro.c iterate.c zigzag.c)
set_target_properties(extend-lib PROPERTIES OUTPUT_NAME extend)
target_link_libraries(extend-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(extend main.c)
target_link_libraries(extend extend-lib)

my_install(extend)

