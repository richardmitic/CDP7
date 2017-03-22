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

add_library(focus-lib focus_main.c ap_focus.c focus.c)
set_target_properties(focus-lib PROPERTIES OUTPUT_NAME focus)
target_link_libraries(focus-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(focus main.c)
target_link_libraries(focus focus-lib)

my_install(focus)

