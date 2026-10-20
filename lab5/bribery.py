"""
Author: Ilaria Teberneac
File Name: bribery.py
Bribery queue, to help professors get the bribe from their students.
The student enters a bribe, and bigger bribes move up the queue.
A bribe of 0 tells the student failed a class (just to scare), but de facto places the student at the end of the queue.
"""

from priorityqueue import PriorityQueue

def main():

    pq = PriorityQueue()

    while True:

        answer = input("How much you got? (q to quit) ")

        if answer == "q":
            break

        amount = float(answer)
        
        position = pq.push(-amount)

        if amount == 0:
            print("You failed my class!")
        else:
            print("Excellent, you are now in position #" + str(position) + " in the queue")

        print()

main()
