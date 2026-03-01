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
    #while item in requests:
        #if item in queue:
            #hit+=1
        #else:
            #miss+=1
            #if cache is full:
                #dequeue the first (oldest) item
            #insert the new item (to the end)
    #return misses
    #return hits for initial testing

def FIFO(cache, requests):
    misses=0
    hits=0
    queue=deque()
    for request in requests:
        if request in queue:
            hits+=1
        else:
            misses+=1
            if len(queue)==cache:
                queue.popleft()
            queue.append(request)
    #return only misses once more is written, this is just for testing
    return misses, hits

#LRU
#Evict the item whose most recent access time is the oldest.

#OPTFF (Belady’s Farthest-in-Future, optimal offline)
#Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again).


#main not yet implemented for input/output files 
#this is just to test functionality of functions as its created 
def main():
    cache=3
    requests=[1,2,3,1,2,3,4,1,2,3]
    misses,hits=FIFO(cache, requests)
    print(f"misses: {misses}")
    print(f"hits: {hits}")
#this output gives 7 misses and 3 hits (correct)

if __name__ == "__main__": main()
