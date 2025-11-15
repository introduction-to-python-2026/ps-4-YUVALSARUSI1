def split_before_each_uppercases(formula):
    start = 0
    split_formula = []

    if not formula:
        return split_formula
    
    
    for end in range(1, len(formula)): 
        if formula[end].isupper():
            
            split_formula.append(formula[start:end])
           
            start = end

   
    split_formula.append(formula[start:])
    
    return split_formula

def split_at_first_digit(formula):
 for char_index, char in enumerate(formula):
  if char.isdigit():
    return formula[:char_index], int(formula[char_index:])
 return formula, 1
