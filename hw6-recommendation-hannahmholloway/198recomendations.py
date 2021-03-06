from math import sqrt

def sim_pearson(prefs, p1, p2):
	# Get the list of mutually rated items
	si = {}
	for item in prefs[p1]:
	    if item in prefs[p2]:
	        si[item] = 1
	# If they are no ratings in common, return 0
	if len(si) == 0:
	    return 0
	# Sum calculations
	n = len(si)
	# Sums of all the preferences
	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])
	# Sums of the squares
	sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
	# Sum of the products
	pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
	# Calculate r (Pearson score)
	num = pSum - sum1 * sum2 / n
	den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
	if den == 0:
	    return 0
	r = num / den
	return r

def getRecommendations(prefs,person,t=5,b=-5,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)

    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:
	    
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item]+=prefs[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim

  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items()]

  # Return the sorted list
  rankings.sort()
  rankings.reverse()
  return rankings[:t], rankings[b:]

movies={}
for line in open('./ml-100k/u.item'):
	(id,title)=line.split('|')[0:2]
	movies[id]=title

# Load data
prefs={}
for line in open('./ml-100k/u.data'):
	(user,movieid,rating,ts)=line.split('\t')
	prefs.setdefault(user,{})
	prefs[user][movies[movieid]]=float(rating)

(toprec, botrec) = getRecommendations(prefs, '198')
print 'The top 5 recommendations for user 37 are:'
print str(toprec[0]) + '\n' + str(toprec[1]) + '\n' + str(toprec[2]) + '\n' + str(toprec[3]) + '\n' + str(toprec[4]) + '\n'
print 'The least 5 recommendations for user 198 are:'
print str(botrec[0]) + '\n' + str(botrec[1]) + '\n' + str(botrec[2]) + '\n' + str(botrec[3]) + '\n' + str(botrec[4]) + '\n'


