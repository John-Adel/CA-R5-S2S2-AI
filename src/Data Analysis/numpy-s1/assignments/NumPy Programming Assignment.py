import numpy as np

def array_factory(mode: str, shape: tuple|int, value: int = None) -> np.ndarray | None:
    ''' This function generates four different types of ndarrays

    


    Args:
        mode (str): This is the type of the matrix that you want, four options are allowed:
            * 'zeros': A matrix of zeros.
            * 'ones': A matrix of ones.
            * 'full': A matrix of a number that you provide, if value wasn't provided, you will get a matrix of None.
            * 'identity': An identity matrix.
        
        shape (tuple|int): This is the dimentionality of your matrix, if one number is provided, shape will be treated as the number of elemnts in the 1D array.
        
        value (int, optional): This is the value that you provide for the full matrix of your specific number.

    Returns:
        ndarray 
    '''
    try:
        if mode.lower() == "zeros":
            return np.zeros(shape)
        elif mode.lower() == "ones":
            return np.ones(shape)
        elif mode.lower() == "full":
            return np.full(shape, value)
        elif mode.lower() == "identity":
            return np.identity(shape)
    except TypeError as t:
        raise TypeError(f"Invalid shape input: {t}")

out = array_factory("full", (10, 2), 5)


#Part 2: The secure_reshape_and_stack Function.
#This function demonstrates how to handle data integration by transforming a flat data structure into a matrix and then combining it with an existing dataset
def secure_reshape_and_stack(data1: list|np.ndarray, data2: list|np.ndarray, new_shape: tuple|int) -> np.ndarray:
    '''
    1. Validates and converts inputs to NumPy arrays.
    2. Reshapes the first dataset to a specific dimension.
    3. Vertically stacks both datasets into one matrix.



    
    Args:
        data1: This is the first matrix that will be reshaped by the new_shape argument, data1 must be reshaped to have the same number of columns as data2, otherwise, a ValueError would be raised.
        data2: This is the second matrix that will be add to the reshaped data1
        new_shape: This is the reshaping tuple or integer that would be used to resahpe data1, if an integer was provided, it will reshape data1 into a 1D array with the number of columns being the rows * columns of data1. If a tuple was provided, make sure the reshaping must result in the same number of elements when multiplying the number of rows * the number of columns of data1, and the number of columns must match the number of columns of data2 so they could be combined.

    Returns:
        ndarray
    '''
    try:
        # Convert inputs to ndarray to ensure they are processed as Tensors
        # arr = np.array(data1)

        arr1 = np.array(data1)
        arr2 = np.array(data2)

        # Rule: Change the shape of arr1 to new_shape
        # Common usage: turning a vector (1D) into a matrix (2D) by using reshape function
        reshaped_arr1 = arr1.reshape(new_shape)

        # Rule: Vertical Stacking (vstack)
        # Requirement: Both matrices must have the same number of columns
        combined_dataset = np.vstack((reshaped_arr1, arr2))

        return combined_dataset

    except ValueError as e:
        # Handle cases where reshape size doesn't match or stack columns don't match
        raise ValueError(f"Company-grade Error: {e}")

print(secure_reshape_and_stack(array_factory("full", (2, 7), 6), array_factory("identity", 16), 16))