def loadMovieLens(path='./ml-100k'):
  # Get movie titles
  movies={}
  for line in open(path+'/u.item'):
    (id,title)=line.split('|')[0:2]
    movies[id]=title
  
  # Load data
  prefs={}
  for line in open(path+'/u.data'):
    (user,movieid,rating,ts)=line.split('\t')
    prefs.setdefault(user,{})
    prefs[user][movies[movieid]]=float(rating)
  return prefs
  
if __name__ == '__main__':
	
	prefs=loadMovieLens()
	print("324's movies: " )
	print (prefs['324'])
	
	
