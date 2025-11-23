# Julia

Julia is a high-level open-source programming language developed by a group of four at MIT. Julia is a dynamic, high-performance programming language used to perform scientific computing operations. Like the R programming language, Julia is used for statistical computing and data analysis. Julia was developed primarily for the speed of programming. It runs much faster than Python or R. analysis.

## Installing Julia

The instructions which follow are for a Ubuntu (or debian) linux OS. To install, simply run the curl command:

```
curl -fsSL https://install.julialang.org | sh
```
If this does not work because you haven't install Curl, go ahead and do so:

```
sudo apt install curl
```

The installation process will make changes to your ~/.bashrc file - so to see these in effect after installation is completed, you can reload it:

```
source ~/.bashrc
```

Then you can check it works by:

```
julia
```

which will open the interactive julia prompt, which we will not use during this course. Exit this by typing:

```
exit()
```

## J-1 Hello World

Your first Julia code is the standard "Hello World" code, located in folder J-1-Hello-World. From the root directory of this repository, type this to run it:

```
julia ./J-1-Hello-World/main.jl
```