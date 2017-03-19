add_subdirectory(portsf)
add_subdirectory(fastconv)
add_subdirectory(reverb)
add_subdirectory(mctools)

if(BUILD_PAPROGS)
  add_subdirectory(paprogs)
endif()
