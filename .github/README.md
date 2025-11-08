# AutoCMake

![Build Status](https://img.shields.io/github/actions/workflow/status/Leorevoir/AutoCMake/main.yml?branch=main&style=for-the-badge)
![License](https://img.shields.io/github/license/Leorevoir/AutoCMake?style=for-the-badge)

## Description

An Optionated, interactive CMake project generator for C & C++.

## Why ?

I was tired of writing CMake from scratch or copy-paste my old templates for **every project**.<br>
So I made Auto-CMake to automate these tasks.<br>
I also wanted **modular** and **readable** `.cmake`, even if its codegen by Auto-CMake python script.

## Features

- Auto-detect project name
- Auto-generate valid CMakeLists.txt and many **modular** configurations files in `./cmake/*.cmake`
- Interactive for language | linking | standard versions ect...

## Usage

temp install it in order to try it!

```bash
git clone https://github.com/Leorevoir/Auto-CMake
cd Auto-CMake
alias auto-cmake="$(pwd)/auto-cmake"
```

use it in your project

```bash
mkdir my-project
cd my_project
auto-cmake
```

## TODO:

- Auto-detect external or submodules | dedendencies

## License

See [**LICENSE**](./LICENSE)
