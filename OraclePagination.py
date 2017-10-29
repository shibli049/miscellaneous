def generatePagingQuery(query, startIndex, endIndex) :
    paginQuery = ("SELECT * FROM ( SELECT A.*, rownum rn FROM ( " 
                  + query 
                  + " ) A WHERE rownum < " + str(endIndex) 
                  + "  ) B WHERE rn >= " + str(startIndex)
                 ) 
    return paginQuery