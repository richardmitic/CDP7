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

add_library(combine-lib main.c combine.c ap_combine.c combine_main.c)
set_target_properties(combine-lib PROPERTIES OUTPUT_NAME combine)
target_link_libraries(combine-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(combine main.c)
target_link_libraries(combine combine-lib)

my_install(combine)

