class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #create a empty stack (LIFO)
        #LIKE A STACK OF PLATES, you stack them. 
        #And when removing a plate you remove the most recent plate that u put in.


        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in closeToOpen: #CHECKS IF CLOSES W/ RIGHT PARENTHESIS
                if stack and stack[-1] == closeToOpen[c]: 
                    #CHECKING RIGHT PAIR MATCHING 
                    stack.pop() #REMOVE FROM STACK 
                else:
                    return False 
            else:
                stack.append(c) #seperate until you can find its closing bracket

        return not stack
        #just have spearated brackets that cannot be matched