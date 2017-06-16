#pragma once

#ifdef WIN32
  #define GREETINGS_EXPORT __declspec(dllexport)
#else
  #define GREETINGS_EXPORT
#endif

class GREETINGS_EXPORT Greetings
{
	public:
            Greetings();
            void fr();
            void en();
};
