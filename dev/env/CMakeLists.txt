if(APPLE)
  set(CMAKE_C_FLAGS "-O2 -Wall -mmacosx-version-min=10.5  -arch i386  -Dunix")
else()
  if(MINGW)
    set(CMAKE_C_FLAGS "-O2 -Wall -DWIN32")
  else()
    set(CMAKE_C_FLAGS "-O2 -Wall -Dlinux -Dunix")
  endif()
endif()

link_directories(../cdp2k ../sfsys)

include_directories(../../include)

add_library(envel-lib envel_main.c ap_envel.c envel.c envfuncs.c envimpos.c envprepro.c
	envprocess.c envxtract.c pluck.c)
set_target_properties(envel-lib PROPERTIES OUTPUT_NAME envel)
target_link_libraries(envel-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(envel main.c)
target_link_libraries(envel envel-lib)

my_install(envel)

