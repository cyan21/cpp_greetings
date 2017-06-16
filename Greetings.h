#pragma once

/*
 * namespace LanguageLib 
{
    class Greetings 
    {
//        public:
            Greetings();
            void fr();
            void en();
    };
}
*/

#ifdef WIN32
  #define HELLO_EXPORT __declspec(dllexport)
#else
  #define HELLO_EXPORT
#endif


HELLO_EXPORT void en();
