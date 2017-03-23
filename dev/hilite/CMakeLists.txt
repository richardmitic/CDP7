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

add_library(hilite-lib hilite_main.c ap_hilite.c hilite.c)
set_target_properties(hilite-lib PROPERTIES OUTPUT_NAME hilite)
target_link_libraries(hilite-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(hilite main.c)
target_link_libraries(hilite hilite-lib)

my_install(hilite)

