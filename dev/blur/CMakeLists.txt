if(APPLE)
  set(CMAKE_C_FLAGS "-O2 -Wall -mmacosx-version-min=10.5  -arch i386 -Dunix")
else()
  if(MINGW)
    set(CMAKE_C_FLAGS "-O2 -Wall -DWIN32 -D_WIN32")
  else()
    set(CMAKE_C_FLAGS "-O2 -Wall -Dlinux -Dunix")
  endif()
endif()

link_directories(../cdp2k ../sfsys)

include_directories(../../include)

add_library(cdpblur ap_blur.c blur.c blur_main.c)
target_link_libraries(cdpblur cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(blur main.c)
target_link_libraries(blur cdpblur)

my_install(blur)
