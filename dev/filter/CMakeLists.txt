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

add_library(filter-lib filter_main.c ap_filter.c filters0.c filters1.c fltpcon.c fltprepro.c)
set_target_properties(filter-lib PROPERTIES OUTPUT_NAME filter)
target_link_libraries(filter-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(filter main.c)
target_link_libraries(filter filter-lib)

my_install(filter)

