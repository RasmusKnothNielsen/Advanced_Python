

## The GIL
Python Global Interpreter Lock (GIL) is a type of process lock which is used by python whenever it deals with processes. 
Generally, Python only uses only one thread to execute the set of written statements. 
This means that in python only one thread will be executed at a time. 
The performance of the single-threaded process and the multi-threaded process will be the same in python 
and this is because of GIL in python. 
We can not achieve multithreading in python because we have global interpreter lock which restricts the threads 
and works as a single thread.

### Processes and threads
Processes are typically independent, while threads exist as subsets of a process. 
processes carry considerable state information, 
whereas multiple threads within a process share state as well as memory and other resources. 
processes have separate address spaces, whereas threads share their address space.

###How does two processes communicate with each other?
If the processes don't share threads, then they have to use sockets. Unix/Linux has something called UnixSockets, 
that enables you to share between processes.
This is because only threads that share ressources (The same memory).
To be specific, threads share 
- Data
- Code 
- Heap

But not Stack, since threads have independent call stacks.
 


## Classes
