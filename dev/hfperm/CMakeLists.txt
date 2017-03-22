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

add_library(hfperm-lib hfperm_main.c ap_hfperm.c hfperm.c)
set_target_properties(hfperm-lib PROPERTIES OUTPUT_NAME hfperm)
target_link_libraries(hfperm-lib cdp2k sfsys ${EXTRA_LIBRARIES})

add_executable(hfperm main.c)
target_link_libraries(hfperm hfperm-lib)

my_install(hfperm)

