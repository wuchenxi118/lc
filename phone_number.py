class Solution:
    def letterCombinations(self, digits):
        dic = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
              '5':['j','k','l'],
              '6':['m','n','o'],
              '7':['p','q','r','s'],
              '8':['t','u','v'],
              '9':['w','x','y','z']}

        number = list(digits)

        while len(number)>1:
            list_1 = dic[number[0]]
            list_2 = dic[number[1]]
            list_merge = list_1.append(list_2)
            del number[0]
            del number[1]



if __name__ == 'main':
    def merge_list( x, y):
        res = []
        for i in x:
            for j in y:
                res.append(i + j)


    

