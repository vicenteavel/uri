while True:
   try:
      expression = input()
      stack = []
      is_correct = True

      for c in expression:
         if c == ")":
            if len(stack) == 0:
               is_correct = False
               break

            stack.pop()

         elif c == '(':
            stack.append('(')
      
      if len(stack) > 0:
         is_correct = False

      print("correct" if is_correct else "incorrect")

   except EOFError:
      break