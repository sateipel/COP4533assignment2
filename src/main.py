#You are given:
#A cache of capacity ( k )
#A sequence of ( m ) requests ( r_1, r_2,.., r_m )
#For each request:
#If the item is already in the cache, this is a hit.
#Otherwise, this is a miss. Insert the item:
#If the cache is not full, simply insert it.
#If the cache is full, evict one item according to the policy.


#FIFO
# Evict the item that has been in the cache the longest.

#LRU
#Evict the item whose most recent access time is the oldest.

#OPTFF (Belady’s Farthest-in-Future, optimal offline)
#Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again).