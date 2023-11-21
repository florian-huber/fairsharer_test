def fair_sharer(values, num_iterations, share=0.1):
    for i in range(num_iterations): 
        highest_index = values.index(max(values))
        
        values[highest_index-1] = values[highest_index-1]+0.1 * values[highest_index]
        values[highest_index+1] = values[highest_index+1]+0.1 * values[highest_index]
        values[highest_index] = values[highest_index]- 2*share*values[highest_index]
        print(values[highest_index], highest_index)

    return values
    





    

    # code
test = fair_sharer([0, 1000, 800, 0], 2, 0.1)
print(test)



    



