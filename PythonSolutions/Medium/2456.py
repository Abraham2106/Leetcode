class Solution(object):
    def mostPopularCreator(self, creators, ids, views):

        cDict = {key: 0  for key in creators}  
        sDict = {key: ''  for key in creators} 
        vDict = {key: 0 for key in creators}  

        for i in range(len(creators)):
            creator = creators[i]
            videoId = ids[i]
            view = views[i]

            cDict[creator] += view

            if view > vDict[creator] or (view == vDict[creator] and videoId < sDict[creator]):
                vDict[creator] = view
                sDict[creator] = videoId
        
        mostPopular = max(cDict.values())
         
        result = []
        for creator in cDict:
            if cDict[creator] == mostPopular:
                maxId = sDict[creator]
                if maxId == '':
                    maxId = ids[creators.index(creator)]
                
                result.append([creator, maxId])

        return result
    