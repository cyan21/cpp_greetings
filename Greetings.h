#pragma once

#if defined(GREETINGS_EXPORT) 
#   define  GREETINGS  __declspec(dllexport)
#else // outside DLL
#   define GREETINGS  __declspec(dllimport)
#endif  // XYZLIBRARY_EXPORT

class GREETINGS Greetings
{
	public:
            Greetings();
            void fr();
            void en();
};
