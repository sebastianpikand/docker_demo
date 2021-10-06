from sp_calculator import Calculator

def main():
  calc = Calculator()
    
  allowed_operations = ['*','/','+','-', 'nth_root', 'reset']
  
  while True:
    operation = input('Choose an operation [*,/,+,-, nth_root, reset] or [q] for quitting: ')
    
    if operation == 'q':
      break
    
    if (operation in allowed_operations):
      
      if (operation != 'reset'):
        value = input('Choose a value (int or float): ')
        
        match operation:
          case '*':
            res = calc.multiply(value)
            print(res)
          case '/':
            res = calc.divide(value)
            print(res)
          case '+':
            res = calc.add(value)
            print(res)
          case '-':
            res = calc.subtract(value)
            print(res)
          case 'nth_root':
            res = calc.nth_root(value)
            print(res)
      else:
        res = calc.reset()
        print(res)
    
        

if __name__ == '__main__':
  main()