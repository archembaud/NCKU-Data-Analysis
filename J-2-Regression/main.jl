using DataFrames, GLM, StatsBase

function create_data_frame()
    println("Inside create_data_frame()")
    df = DataFrame(X=[1,2,3], Y=[2,4,7])
    println("DataFrame created:")
    return df
end

# Create the data frame and perform a linear regression
print("Creating data frame...\n")
df = create_data_frame()
println(df)
println("Fitting OLS model...")
ols = lm(@formula(Y ~ X), df)
println(ols)