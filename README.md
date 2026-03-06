Names & IDs:
-Stephanie Teipel: 69604935
-Katie Boetig: 52055316


Instructions to Compile/build (if applicable):
- No compilation is required
-This project is written in Python 3
- Python 3 must be installed on the system
- The program uses only standard Python libraries (collections, sys), so no additional packages need to be installed


Instructions to run the program, including example commands:
- Clone the repository
	git clone https://github.com/sateipel/COP4533assignment2.git
- Navigate into the project directory
	cd COP4533assignment2
- Run the program using an input file
	python src/main.py data/example.in

## Any assumptions (input/output format, dependencies, etc.):

 \-Input format(.in files):
 	\-k m
 	\-r1 r2 r3 ... rm

 	\-Where:
 		\-( k ) \= cache capacity ( ( k \>= 1 ) )
		\-( m ) \= number of requests
 		\-( r\_1, .., r\_m ) \= sequence of integer IDs

 \-Output Format(.out files):
 	\-FIFO  : \<number\_of\_misses\>
 	\-LRU   : \<number\_of\_misses\>
	\-OPTFF : \<number\_of\_misses\>



## Question 1: Empirical Comparison

Use **at least three nontrivial input files** (each containing 50 or more requests).  
For each file, report the number of cache misses for each policy.

| Input File | k | m | FIFO | LRU | OPTFF |
| :---- | :---- | :---- | :---- | :---- | :---- |
| File1 | 3 | 50 | 38 | 42 | 26 |
| File2 | 4 | 50 | 38 | 38 | 16 |
| File3 | 2 | 50 | 50 | 50 | 35 |

Briefly comment:

* **Does OPTFF have the fewest misses?**  
Yes. In all three test files, OPTFF produces fewer cache misses than FIFO and LRU. This is expected because OPTFF (Belady’s algorithm) uses knowledge of the future request sequence and evicts the page whose next use occurs farthest in the future.

* **How does FIFO compare to LRU?**  
FIFO and LRU perform similarly in some cases but can differ depending on the request pattern. In File1, FIFO performs slightly better than LRU, while in File2 and File3 they perform the same. This shows that LRU does not always outperform FIFO and the effectiveness of each policy depends on the structure of the request sequence.

## Question 2: Bad Sequence for LRU or FIFO

For ( k \= 3 ), investigate whether there exists a request sequence for which OPTFF incurs **strictly fewer misses** than LRU (or FIFO).

For k = 3, the following request sequence shows that OPTFF can incur strictly fewer misses than LRU:

1 2 3 4 1 2 5 1 2 3 4 5

Miss counts:

| Policy | Misses |
|------|------|
| LRU | 10 |
| OPTFF | 7 |

Explanation:

LRU makes decisions based only on past accesses, while OPTFF knows the future request sequence. In this sequence, OPTFF evicts the page that will be used farthest in the future, while LRU sometimes evicts a page that will be needed soon. Because of this, OPTFF produces strictly fewer cache misses.

## Question 3: Prove OPTFF is Optimal

Let OPTFF be Belady’s Farthest-in-Future algorithm.  
Let ( A ) be any offline algorithm that knows the full request sequence.  
Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

Let A= offline schedule algorithm   
Let B=Belady’s OPTFF algorithm 

Assume algorithm A makes different eviction decisions than algorithm B.

They disagree at some page request, call it k. 

Case 1: k is already in cache (hit)  
	Nothing is evicted from either and they are both hits.  
Case 2: k element is not in cache (miss)  
	i) if A’s kth element and B’s kth element are equal, they agree so continue,\\\\.   
	ii) if A’s kth element is not equal to B’s kth.  
		Cache A selects element ‘a’.  
		Cache B selects element ‘b’.  
		It follows that ‘b’ must be equal to or further in the future than ‘a’ by Belady’s  
		So, page ‘a’ (from algorithm A) will be requested sooner or equal to page ‘b’. This is because request time ‘b’ \>= request time ‘a’ (by def. of B) so keeping ‘b’ cannot cause an earlier miss.  
		Thus, we can replace ‘a’ with ‘b’, which will not increase the number of misses in A.  
	A and B now agree at element k. Repeat this process for any disagreement. 

Thus, proving that B (OPTFF) cannot have a larger number of misses than A (offline schedule), and is optimal. 
