world = input()
world = ''.join(sorted(world))

world_ordered = ''
numbers = ''

for i in world:    

    cant = world.count(i)
    if not(i in world_ordered):  
         
        if (len(numbers) > 0) :
            for k in range(0,len(world_ordered)):
                
                if str(cant) > numbers[k]:                    
                    numbers = numbers[0:k] + str(cant) + numbers.replace(numbers[0:k],'')
                    world_ordered = world_ordered[0:k] + i + world_ordered.replace(world_ordered[0:k],'')

                    break
                elif (str(cant) < numbers[k]) and (k == (len(world_ordered) -1)):                    
                    numbers = numbers + str(cant) 
                    world_ordered = world_ordered + i  
                    
                
                elif (str(cant) == numbers[k]): 
                    for j in range(k, len(world_ordered)):
                        if (str(cant) != numbers[j]):                                      
                            numbers = numbers[0:j] + str(cant) + numbers.replace(numbers[0:j],'')
                            world_ordered = world_ordered[0:j] + i + world_ordered.replace(world_ordered[0:j],'')                            
                            break

                        elif (j == (len(world_ordered) -1)):                            
                            numbers = numbers[0:j+1] + str(cant) + numbers.replace(numbers[0:j+1],'')
                            world_ordered = world_ordered[0:j+1] + i + world_ordered.replace(world_ordered[0:j+1],'')                            
                            break
                            
                    break
                            
                            


        else:            
            world_ordered +=  i
            numbers += str(world.count(i))
    
    
world_final = ''

for i in range(0, len(world_ordered)):
    world_final += world_ordered[i] * int(numbers[i])
    
print(world_final)
