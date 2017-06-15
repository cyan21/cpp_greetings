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
mkdir build

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


