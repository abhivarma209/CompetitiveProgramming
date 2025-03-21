class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        n = len(recipes)
        d = {}
        for i in range(n):
            d[recipes[i]] = ingredients[i]
        while True:
            new_supplies = []
            for recipy in d:
                cookable = True
                for ingredient in d[recipy]:
                    if ingredient not in supplies:
                        cookable = False
                if cookable:
                    new_supplies.append(recipy)
            if len(new_supplies) == 0:
                return res
            for item in new_supplies:
                res.append(item)
                supplies.append(item)
                del d[item]
        return res