if(APPLE)
  set(CMAKE_C_FLAGS "-O2 -Wall -mmacosx-version-min=10.5  -arch i386 -Dunix")
else()
  if(MINGW)
    set(CMAKE_C_FLAGS "-O2 -Wall -DWIN32")
  else()
    set(CMAKE_C_FLAGS "-O2 -Wall -Dlinux -Dunix")
  endif()
endif()

link_directories(../cdp2k ../sfsys)

include_directories(../../include)

add_library(formants-lib formants_main.c ap_formants.c formants.c)
set_target_properties(formants-lib PROPERTIES OUTPUT_NAME formants)
target_link_libraries(formants-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(formants main.c)
target_link_libraries(formants formants-lib)

my_install(formants)

