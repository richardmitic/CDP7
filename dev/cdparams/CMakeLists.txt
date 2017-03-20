if(APPLE)
  set(CMAKE_C_FLAGS "-O2 -Wall -mmacosx-version-min=10.5 -Dunix")
else()
  if(MINGW)
    set(CMAKE_C_FLAGS "-O2 -Wall -DWIN32 -D_WIN32")
  else()
    set(CMAKE_C_FLAGS "-O2 -Wall -Dlinux -Dunix")
  endif()
endif()

link_directories(../cdp2k ../sfsys)

include_directories(../../include)

add_library(cdparams-lib cdparams_main.c display.c flagnames.c parnames.c)
set_target_properties(cdparams-lib PROPERTIES OUTPUT_NAME cdparams)
target_link_libraries(cdparams-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(cdparams main.c)
target_link_libraries(cdparams cdparams-lib)

my_install(cdparams)
