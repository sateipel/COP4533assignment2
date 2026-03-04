Names & IDs:
-Stephanie Teipel: 69604935
-Katie Boetig: UFID


Instructions to Compile/build (if applicable:
-...
-...
-...


Instructions to run the program, including example commands:
-...
-...
-...


Any assumptions (input/output format, dependencies, etc.):
-Input format(.in files):
	-k m
	-r1 r2 r3 ... rm
	-Where:
		-( k ) = cache capacity ( ( k >= 1 ) )
		-( m ) = number of requests
		-( r_1, .., r_m ) = sequence of integer IDs
-Output Format(.out files):
	-FIFO  : <number_of_misses>
	-LRU   : <number_of_misses>
	-OPTFF : <number_of_misses>


Your solutions to the written component:
-Question 1: Empirical Comparison


Use at least three nontrivial input files (each containing 50 or more requests).
For each file, report the number of cache misses for each policy.

        k   m    FIFO     LRU      OPTFF
File1
File2
File3


Briefly comment:
-Does OPTFF have the fewest misses?
-How does FIFO compare to LRU?


Question 2: Bad Sequence for LRU or FIFO
For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs strictly fewer misses than LRU (or FIFO).
If such a sequence exists:
-Construct one.
-Compute and report the miss counts for both policies.


If you believe no such sequence exists for the policy you chose:
-Provide a clear justification.
-In either case, briefly explain your reasoning.


Question 3: Prove OPTFF is Optimal
Let OPTFF be Belady’s Farthest-in-Future algorithm.
Let ( A ) be any offline algorithm that knows the full request sequence.
Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.
-Let A= offline schedule algorithm 
-Let B=Belady’s OPTFF algorithm 


Assume A&B match and agree for the first k elements (same cache misses)
Now, go to the k+1th element


Case 1: element is already in cache (hit)
	- Nothing is evicted from either and they are both hits.

	
Case 2: element is not in cache (miss)
	- i) if A’s k+1th element and B’s k+1th element are equal, they agree so continue 
	- ii) f A’s k+1th element is not equal to B’s k+1th 
		- Say cache A selects element a
		- Say cache B selects element b
		- It follows that b must be equal to or further in the future than a by Belady’s
		- Thus, we can replace a with b and have equivalent or more optimal solution

		
Continue with all elements until A=B
Thus, proving that B (OPTFF) cannot have a larger number of misses than A (offline schedule)
