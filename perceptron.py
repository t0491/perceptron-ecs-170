import sys

def perceptron(threshold, adj_fact, initial_weights, examples, num_passes):
    # Print all the meta data for user reference.
    print("Starting weights: " + str(initial_weights))
    print("Threshold: " + str(threshold) + "    Adjustment: " + str(adj_fact))
    
    for i in range(1, num_passes+1):
        print("\nPass " + str(i) + "\n")
        
        for current_example in examples:
            print("inputs: " + str(current_example[1]))
            
            # Iterate through the inputs which is the [1] index of the examples list.
            input_index = 0
            sumInputWeight = 0
            for j in current_example[1]:

                # Multiply the input by the weights and sum them.
                sumInputWeight += j * initial_weights[input_index]
            
                input_index += 1

            # print(sumInputWeight)
            
            # Check if the sum meets the indicated threshold and act accordingly.
            output = -999
            if sumInputWeight > threshold:
                output = True
            elif sumInputWeight <= threshold and sumInputWeight > -999:
                output = False
            else:
                # Output is -999 here, sum had an error so terminate the program.
                print("Something went wrong for sum calculation.")
                exit()

            correct_output = current_example[0]
            print("prediction: " + str(output) + "    answer: " + str(correct_output))

            # If our output doesn't match the correct output, then adjust weights.
            if output != correct_output:
                adj_index = 0
                # Adjust the weights with a corresponding input of 1.
                for h in current_example[1]:
                    if h == 1:
                        # Perceptron more sensitive if < threshold and wrong.
                        if sumInputWeight < threshold:  
                            initial_weights[adj_index] += adj_fact

                        # Perceptron les sensitive if > threshold and wrong.
                        elif sumInputWeight > threshold:
                            initial_weights[adj_index] -= adj_fact

                    adj_index += 1
            # Print the now adjusted weights.
            print("adjusted weights: " + str(initial_weights))
    return
