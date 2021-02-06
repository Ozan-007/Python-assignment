prime = []

        for i in range(2, 101):
               d = 0
               for b in range(2, i//2 + 1):
                       if i % b == 0:
                               d = 1
                               break
               if d == 0:
                        prime.append(i)

        print(prime)
        #https://github.com/Ozan-007/Python-assignment
