# For Conan demo

simple C++ class

## How to build

Frist, get the source code
```
git clone https://github.com/cyan21/cpp_greetings.git
cd cpp_greetings
```
>  Requires Visual Studio Compiler and CMAKE

### with  CMAKE

```
// create a build folder
mkdir build && cd build

// Generate build files for compilation 
cmake .. -G "Visual Studio 15 Win64"

// build sources
cmake --build . --config Release

// test the code
cd Release
./greet.exe
```

### without CMAKE

> exemple with Visual Studio Code

1. in VS Code, open the folder containing the source code
2. Press **Ctrl+Shift+B**, this will generate **.vscode/tasks.json**
3. Copy paste this snippet in **.vscode/tasks.json**
```
{
    "version": "0.1.0",
    "command": "build.bat",
    "isShellCommand": true,
    "showOutput": "always"
}
```

4. Press **Ctrl+Shift+B** to compile
5. Execute the exe file


## How to generate the conan package

>  Requires Conan Client

1. Fetch the conanfile.py from the repository

```
git clone https://github.com/cyan21/cpp_greetings.git
cd cpp_greetings && git checkout conan_deps
```

2. Generate the template files for your future package, it will create the following files in the *test_package* :
- CMakeLists.txt
- conanfile.py
- example.cpp

> the existing conanfile.py will be modified !  
> use "git checkout -- conanfile.py" to restore it 


```
conan new Greetings/0.1@yannc/dev -t
```

3. Edit the example.cpp to test your package
```
vim test_package/example.cpp

#include <iostream>
#include "Greetings.h"

int main() {
        en();
}
```

4. Build your package and run test_package
```
conan test_package
```

5. You should get a message and your package in now in your local cache
```
// use this command to look for your package in your local cache
conan search
```




