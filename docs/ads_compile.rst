Compilation tool
================
Compile ads & adsd.

Usage
  ads_compile [options] <path-to-source>

Options
  -o <dir>       Build output directory (default ./build)
  -r             Install all dependencies (may require sudo)
  -R             Only install dependencies (may require sudo)
  -d             Enable debug build
  -m <options>   Make additional options
  -c <options>   Cmake additional options
  -i             Install binaries (may require sudo)

Notes
-----

Debug build has shorter blocktime and other helpful options.

`-i` Installs compiled binaries ads and adsd to /usr/local/bin.
