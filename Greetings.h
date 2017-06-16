#pragma once

#ifdef WIN32
  #define GREETINGS_EXPORT __declspec(dllexport)
#else
  #define GREETINGS_EXPORT
#endif

GREETINGS_EXPORT void en();
