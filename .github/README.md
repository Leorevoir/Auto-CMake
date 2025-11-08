# AutoCMake

<h1 align="center">
  Auto-CMake<br>
  <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/palette/macchiato.png" width="600px"/>
  <br>
</h1>

<div align="center">
  <p></p>
  <div align="center">
     <a href="https://github.com/Leorevoir/Auto-CMake/stargazers">
        <img src="https://img.shields.io/github/stars/Leorevoir/Auto-CMake?color=F5BDE6&labelColor=303446&style=for-the-badge&logo=starship&logoColor=F5BDE6">
     </a>
     <a href="https://github.com/Leorevoir/Auto-CMake/">
        <img src="https://img.shields.io/github/repo-size/Leorevoir/Auto-CMake?color=C6A0F6&labelColor=303446&style=for-the-badge&logo=github&logoColor=C6A0F6">
     </a>
     <a href="https://github.com/Leorevoir/Auto-CMake/blob/main/LICENSE">
        <img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=GPL3&colorA=313244&colorB=F5A97F&logo=unlicense&logoColor=F5A97F&"/>
     </a>
  </div>
  <br>
</div>

<p align="center">
  Auto-CMake<br>
  A modular & opinionated CMake project generator for C/C++ 
</p>

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

Temporary install to try it:

```bash
git clone https://github.com/Leorevoir/Auto-CMake
cd Auto-CMake
alias auto-cmake="$(pwd)/auto-cmake"
```

Then use it in your project

```bash
mkdir my-project
cd my_project
auto-cmake
```

## TODO:

- Auto-detect external or submodules | dependencies

## License

See [**LICENSE**](./LICENSE)
