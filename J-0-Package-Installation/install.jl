    # This script will install the packages needed for the examples in this repository
    # By default, these go to a hidden folder in your home directory (~/.julia)
    import Pkg
    Pkg.add("DataFrames")
    Pkg.add("GLM")
    Pkg.add("StatsBase")