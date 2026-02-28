# COP4533assignment2
Problem Statement
Implement and compare three cache eviction policies on the same request sequence:

FIFO (First-In, First-Out)

LRU (Least Recently Used)

OPTFF (Belady’s Farthest-in-Future, optimal offline)

You will also complete a short written component, including a proof that OPTFF is optimal.

You are given:

A cache of capacity ( k )

A sequence of ( m ) requests ( r_1, r_2,.., r_m )

For each request:

If the item is already in the cache, this is a hit.

Otherwise, this is a miss. Insert the item:

If the cache is not full, simply insert it.

If the cache is full, evict one item according to the policy.

Eviction Policies
FIFO: Evict the item that has been in the cache the longest.

LRU: Evict the item whose most recent access time is the oldest.

OPTFF: Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again).

Input Format
Your program must read input from a file with the following format:

k m
r1 r2 r3 ... rm
Where:

( k ) = cache capacity ( ( k >= 1 ) )

( m ) = number of requests

( r_1, .., r_m ) = sequence of integer IDs

Output Format
Your program must output:

FIFO  : <number_of_misses>
LRU   : <number_of_misses>
OPTFF : <number_of_misses>
Written Component
Submit a short PDF or Markdown file answering the following questions.

Question 1: Empirical Comparison
Use at least three nontrivial input files (each containing 50 or more requests).

For each file, report the number of cache misses for each policy.

Input File	k	m	FIFO	LRU	OPTFF
File1					
File2					
File3					
 

Briefly comment:

Does OPTFF have the fewest misses?

How does FIFO compare to LRU?

Question 2: Bad Sequence for LRU or FIFO
For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs strictly fewer misses than LRU (or FIFO).

If such a sequence exists:

Construct one.

Compute and report the miss counts for both policies.

If you believe no such sequence exists for the policy you chose:

Provide a clear justification.

In either case, briefly explain your reasoning.

Question 3: Prove OPTFF is Optimal
Let OPTFF be Belady’s Farthest-in-Future algorithm.

Let ( A ) be any offline algorithm that knows the full request sequence.

Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

Submission and Deliverables (GitHub)
As discussed in class, you will submit your work as a GitHub repository on Canvas.

If working in partners, only one partner should submit.

Your repository must include:

1. Source Code
All source code needed to compile and run your implementation.

2. Example Inputs and Outputs
At least one example input file (e.g., example.in)

The corresponding expected output file (e.g., example.out)

Your README must explain how to reproduce the output.

3. README.md (Required)
Your README must include:

Student name(s) and UFID(s)

Instructions to compile/build the code (if applicable)

Instructions to run the program, including example commands

Any assumptions (input/output format, dependencies, etc.)

Your solutions to the written component

4. Organized Repository Structure
Use a clean layout such as:

src/
data/
tests/
Use meaningful filenames.

Do not submit an unstructured dump of files.

5. Reproducibility
A grader must be able to:

git clone <repository>
and follow the README to compile (if needed) and run your programs without additional steps.
