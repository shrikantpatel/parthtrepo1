#the first part of the code is named under class solution
class Solution:
    #We now define the code
    #self allows us to access the the items of the class solution
    #we define num list as a list of integers and sum as an int
    #-> allows the program to return the answer in boolean form
    def pairMatchingSum(self, numList: list[int], sum: int) -> bool:
        # complement set will store all the numbers that we get from subtracting numbers from numList and sum
        complementList = []
        # x is a number in the numList
        for x in numList:
            #we get the complement by subtracting i from the sum
            complement = sum - x
            #if i is in the complement list then the program is finished because the complement must add to some other number in the list if it is in the complment list
            if x in complementList:
                return True
            else:
                #add the number to the complement set
                complementList = complementList + [complement]
        # the program was not able to find any pairs
        return False;

if __name__ == "__main__" :
    Program = Solution()
Program.pairMatchingSum([1, 2, 3, 4, 5], 9) == True 
Program.pairMatchingSum([1, 2, 3, 4, 7,], 10) == False
Program.pairMatchingSum([2, 2, 3, 4, 5], 4) == True
Program.pairMatchingSum([1, 3, 3, 4, 5], 9) == True
Program.pairMatchingSum([5, 2, 3, 4, 1], 9) == True
    