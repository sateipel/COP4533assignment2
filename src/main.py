from collections import deque
#You are given:
#A cache of capacity ( k )
#A sequence of ( m ) requests ( r_1, r_2,.., r_m )
#For each request:
#If the item is already in the cache, this is a hit.
#Otherwise, this is a miss. Insert the item:
#If the cache is not full, simply insert it.
#If the cache is full, evict one item according to the policy.


#FIFO
# Evict the item that has been in the cache the longest. (aka a queue)
#declare the function 
    #misses =0
    #hits=0
    #cacheCount=0
    #while items in requests:
        #if cacheCount<cache: (if the cache is not full)
            #if item is in the queue
                #hit+=1
             #else
                #insert item into queue (queue will put it at the end)
                #count it as a miss (miss +=1)
                #cacheCount +=1
        #else (once cache is full)
            #if item is in the queue
                #hit+=1
            #else
                #dequeue the first item (the one that has been in the cache the longest)
                #insert the new item into the queue( will automatically be put at the end)
                #miss+=1

#def FIFO(cache, requests):

#LRU
#Evict the item whose most recent access time is the oldest.

#OPTFF (Belady’s Farthest-in-Future, optimal offline)
#Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again).