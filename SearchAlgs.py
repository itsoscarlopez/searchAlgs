# The Following 3 Algorithms Return Only the Index at
# Which A Pattern Was Found
from time import time #to measure time it takes for a search
import sys

# The Following 3 search methods will return a list with 5 times:
#    (0) method name,
#    (1) index of pattern match,
#    (2) # of charc comparisons,
#    (3) # of pattern shifts and,
#    (4) time elpased for
""" Return the lowest index of T at which substring P begins (or else -1)."""
def find_brute(T, P):
    comparisons = 0                         # counter for characters compared
    shifts = 0                              # counter for # of pattern shifts
    start = time()                          # start the timer
    n,m =  len(T), len(P)                   # inroduce convenient notations
    for i in range(n-m+1):                  # try every potential starting index within T
        k = 0                               # an index into pattern P
        while k < m and T[i+k] == P[k]:     # kth character of P mathces
            k += 1
            comparisons += 1
        if k == m:                          # found a match
            end = time()                    # end the timer
            return ["Brute Force Method", i, comparisons, shifts, end - start]
            # return [method name, index of match, # of charcs compared, # of pattern shifts, time elapsed for search]
        comparisons += 1                    # increase comparison counter
        shifts += 1                         # increase pattern shifts counter
    return -1

""" Return the lowest index of T at which substring P begins (or else -1)."""
def find_boyer_moore(T,P):
    start = time()                          # start the timer
    comparisons = 0                         # counter for characters compared
    shifts = 0                              # counter for # of pattern shifts
    n, m = len(T), len(P)                   # introduce concenient notations
    if m == 0: return 0                     # trivial search for empty string
    last = {}                               # build 'last' dictionary
    for k in range(m):
        last[P[k]] = k                      # later occurence overwrites
    # align end of pattern at index m-1 of text
    i = m-1                             	# an index into T
    k = m-1                             	# an index into P
    while i < n:
        if T[i] == P[k]:                    # a matching character
            if k == 0:
                end = time()                # end the timer
                return ["Boyer Moore Method", last, comparisons, shifts, end - start]  # pattern begins at index i of text
            else:
                i -= 1                      # examine previous character
                k -= 1                      # of both T and P
                comparisons += 1
        else:
            comparisons += 1                # increase charc comparison counter
            shifts += 1                     # increase pattern shifts counter
            j = last.get(T[i], -1)          # last (T[i]) is -1 if not found
            i += m - min(k, j+1)            # case analysis for jump step
            k = m -1                        # restart at end of pattern
    return -1

""" Return the lowest index of T at which substring P begins (or else -1)."""
def find_kmp(T,P):
    start = time()                          # start the timer
    comparisons = 0                         # counter for characters compared
    shifts = 0                              # counter for # of pattern shifts
    n,m = len(T), len(P)                    # introduce convenient notations
    if m == 0:
        return 0                            # trivial search for empty string
    fail = compute_kmp_fail(P)              # rely on utility to precompute
    j = 0                                   # index into text
    k = 0                                   # index into pattern
    while j < n:
        if T[j] == P[k]:                	# P[0:1+k] matched thus far
            comparisons += 1
            if k == m-1:                	# match is complete
                end = time()                # end the timer
                return ["KMP  Search Method", j - m + 1, comparisons, shifts, end - start]
            j += 1                          #try to extend the match
            k += 1
        elif k > 0:
            k = fail[k-1]                   # reuse suffix of P[0:k]
            comparisons += 1                # increase charc comparison counter
            shifts += 1                     # increase pattern shifts counter
        else:
            j += 1
            comparisons += 1                # increase charc comparison counter
            shifts += 1                     # increase pattern shifts counter
    return -1                               # reached end without match

"""Utility that computes and returns KMP 'fail" list."""
def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    # by default, presume overlap of 0 everywhere
    j = 1
    k = 0
    while j < m:                            # compute f(j) during this pass, if nonzero
        if P[j] == P[k]:                    # k + 1 characters match thus far
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:                         # k follows a matching prefix
            k = fail[k-1]
        else:                               # no match found starting at j
            j += 1
    return fail

"""
    The following 3 algorithms are the same as the ones above. The difference is they visualize the search method one step at a time.
"""
def brute(T,P):
    border("BRUTE FORCE METHOD")
    start = time()
    n,m =  len(T), len(P)                   # inroduce convenient notations
    print("This is text length:", n, "and this is length of pattern:", m, "\n")
    
    text = list(T)                          # creates a list of text T
    patt = list(P)                          # creates a list of pattern P
    pointer_text = ["↓"]                    # creates a pointer '↓' for
    pointer_patt = ["↑"]                    # creates a pointer '↑' for P
    comparisons = 1                         # counter for number of comparisos made in algorithm
    shifts = 0                              # counter for number of pattern shifts
    for i in range(n-m+1):                  # try every potential starting index within T
        k = 0                               # an index into pattern P
        print("This is comparison ", comparisons, "", sep = " ||| ")
        print("I'm comparing text letter [", T[i+k], "] and pattern letter  [", P[k], "]" )
        print("".join(pointer_text))        # items of text pointer separated w/ spaces
        print("".join(text))                # items of T separated w/ spaces
        print("".join(patt))                # items of P separated w/ spaces
        print("".join(pointer_patt))        # items of patt pointer separated w/ spaces
        pointer_text.insert(0, " ")         # Adding spaces " " to move pointer "P"
        pointer_patt.insert(0, " ")         # Adding spaces " " to move pointer "d"
        
        while k < m and T[i+k] == P[k]:     # kth character of P mathces
            k += 1
            comparisons += 1                # Increases comparison count
            if k == m:                      # Indicates a pattern match!
                print("I found the match on index ", i)
                end = time()
                print("This took ", end - start, "seconds.")
                print("I made ", comparisons, "comparisons and ", shifts, "pattern shifts.")
                return ["Brute Force Method", i, comparisons, shifts, end - start]
            print("This is comparison ", comparisons, "", sep = " ||| ")
            print("I'm comparing text letter [", T[i+k], "] and pattern letter  [", P[k], "]" )
            print("¡¡¡ They Match !!!")
            print("".join(pointer_text))    # Unpacks text pointer list and separate w/ spaces
            print("".join(text))            # Unpacks text list and separate words w/ spaces
            print("".join(patt))            # Unpacks patt list and separate words w/ spaces
            print("".join(pointer_patt))    # Unpacks patt pointer list and separates w/ spaces
            pointer_text.insert(0, " ")     # Adding spaces " " to move pointer "P"
            pointer_patt.insert(0, " ")     # Adding spaces " " to move pointer "d"
        comparisons += 1                    # Increases comparison count
        shifts += 1                         # Increase patter shift count
        patt.insert(0, " ")                 # Adding space ' ' to front of patt list...
                                            # ...to move the pointer for P
        for space in range(k):               # We remove spaces added to either pointers...
            pointer_text.remove(" ")        # ...from the while loop above since k!=m
            pointer_patt.remove(" ")
    print("End of of text, no matches. I am big sad :'( \n")
    return -1

def boyer(T,P):
    border("BOYER-MOORE METHOD")
    print("Calculating Length of Text and Pattern. \n")
    n, m = len(T), len(P)                   # introduce convenient notations
    print("This is text length:", n, "and this is length of pattern:",m, "\n")
    if m == 0: return 0                     # trivial search for empty string
    last = {}                               # build 'last' dictionary
    for k in range(m):
        last[P[k]] = k
    # align end of pattern at m-1 of text
    i = m-1                                 # an index into T
    k = m-1                                 # an index into P
    print("Here's the pattern dictionary:", last, "\n")
    print("Pointers are on index", i, "\n")
    
    comparisons = 1                         # measures times alg compared text and pattern
    shifts = 0                              # measures times P "shifted" after mismatch
    start = time()                          # capture time at start of search
    text = list(T)                          # List of Text to match Pattern's placement
    patt = list(P)                          # List of Pattern contents
    pointer_text = ["↓"]                    # creates a pointer '↓' for T
    pointer_patt = ["↑"]                    # creates a pointer '↑' for P
    
    for space in range(m-1):                # aligns patt pointer to end of pattern
        pointer_patt.insert(-1, " ")

    for i in range(n-m+1):                  # try every potential starting index within T
        while i < n:
            print("This is comparison ", comparisons, " ", sep = " ||| ")
            print("Text Index:", i, " Pattern Index:", k)
            print("Comparing text letter [", T[i], "] and pattern letter [", P[k], "]")
            print("".join(pointer_text))    # Items of text pointer separated w/ spaces
            print("".join(text))            # Items of T separated w/ spaces
            print("".join(patt))            # Items of P separated w/ spaces
            print("".join(pointer_patt))    # Items of patt pointer separated w/ spaces
            if T[i] == P[k]:                # a matching character!
                if k == 0:                  # reached the end of the pattern!
                    end = time()            # capture time at end of search
                    print("I found the start of the pattern on text index", i, "!")
                    print("The search took ", end - start, "seconds.")
                    print("I made ", comparisons, "comparisons and ", shifts, "pattern shifts.")
                    return ["Boyer-Moore Method", i, comparisons, shifts, end - start]
                else:
                    pointer_text.remove(" ")    # move both pointers left one
                    pointer_patt.remove(" ")
                    comparisons += 1            # no shift += 1 b/c T[i] matches P[k]
                    i -= 1                      # Examine previous character
                    k -= 1                      # of both T and P
                    print("Moved text pointer over one to index", i)
                    print("Moved pattern pointer over one to index", k, "\n")
    
            else:                           # indicates mismatch and pattern
                comparisons += 1            # made one comparison, a mistmatch
                shifts += 1                 # since T and P mismatched
                j = last.get(T[i], -1)      # last(T[i]) is -1 if not found
                jump = m - min(k, j+1)      # jump step
                i += jump                   # jump step of text index
                K = k                       # to keep track of k before update line below
                k = m - 1                   # restart end of pattern
                print("\n ¡¡¡ Mismatch !!! \n")
                print("Moved text pointer over", jump,"to index", i)
                print("Moved pattern pointer to index", k, "\n")
                
                N = len(pointer_text)       # length of text pointer array before jump
                M = len(pointer_patt)       # length of patt pointer array before jump
                
                #print("BEFORE JUMP - Ptext is:", N, " and Ppatt is:", M)
                if N != M:                  # before pointers line up...
                    if N + jump <= M:        # ...text pointer only moves
                        move(pointer_text, jump)   # move pointer over "jump" times
                    elif N + jump >= M:      # text pointer 'catches up' to text pointer
                        move(pointer_text, jump)
                        move(patt, N-M+jump)
                        move(pointer_patt, N-M+jump)
                else:                       # K = m (length of pattern), everything shifts of size 'jump'
                    move(pointer_text, jump)
                    move(patt, jump)
                    move(pointer_patt, jump)
        print("End of text, no matches. I am big sad :'( \n")
        return -1

def kmp(T,P):
    border("    KMP METHOD    ")            # title of method
    print("Calculating Length of Text and Pattern. \n")
    n,m = len(T), len(P)                    # introduce convenient notations
    print("This is text length:", n, "and this is length of pattern:",m, "\n")
    if m == 0: return 0                     # trivial search for empty string
    fail = compute_kmp_fail(P)              # rely on utility to precompute
    j = 0                                   # index into text
    k = 0                                   # index into pattern
    comparisons = 1                         # measures times alg compared text and pattern
    shifts = 0                              # measures times P "shifted" after mismatch
    start = time()                          # capture time at start of search
    text = list(T)                          # List of Text to match Pattern's placement
    patt = list(P)                          # List of Pattern contents
    pointer_text = ["↓"]                    # creates a pointer '↓' for T
    pointer_patt = ["↑"]                    # creates a pointer '↑' for P
    while j < n:
        print("This is comparison ", comparisons, " ", sep = " ||| ")
        print("Text Index:", j, " Pattern Index:", k)
        print("Comparing text letter [", T[j], "] and pattern letter [", P[k], "]")
        print("".join(pointer_text))        # Items of text pointer separated w/ nothing
        print("".join(text))                # Items of T separated w/ nothing
        print("".join(patt))                # Items of P separated w/ nothing
        print("".join(pointer_patt))        # Items of patt pointer separated w/ nothing
        if T[j] == P[k]:                    # P[0:1+k] matched thus far
            comparisons += 1
            if k == m-1:                    # match is complete
                end = time()                # capture time at end of search
                print("I found the start of the pattern on text index", j - m + 1, "!")
                print("The search took ", end - start, "seconds.")
                print("I made ", comparisons, "comparisons and ", shifts, "pattern shifts.")
                return ["KMP  Search Method", j - m + 1, comparisons, shifts, end - start]
            j += 1                          #try to extend the match
            k += 1
            pointer_text.insert(0, " ")     # only move pointers since charcs match
            pointer_patt.insert(0, " ")
        elif k > 0:                         # mismatched inside pattern k > 0
            comparisons += 1
            shifts += 1
            K = k                           # save k value before update below
            k = fail[k-1]                   # reuse suffix of P[0:k]
            move(patt, K-k)                 # move patt over, idk why this works yet....
        else:                               # mismatched at beginning of pattern, k = 0
            comparisons += 1
            shifts += 1
            j += 1
            pointer_text.insert(0," ")
            pointer_patt.insert(0, " ")
            patt.insert(0, " ")
    print("End of of text, no matches. I am big sad :'( \n")
    return -1

" This function adds certain characters to an array a certain number of times."
def move(array, jump = 0, char = " "):
    for space in range(jump):
        array.insert(0, char)
    return array
    
" This function creates a border around a sentence."
def border(text, w = 25):                   # w is width
    sentence = "="*w + str(text) + "="*w    # the sentence to be bordered
    length = len(sentence)                  # length of sentence to know border width
    
    for blank in range(3): print("\n")
    for line in range(2): print("="*length)
    print(" "*w + text + " "*w)
    for line in range(2): print("="*length)
    print("\n")

" Allows user to run a method at least once using T and P and choose step-by-step view or not."
def relay(T,P,steps = True):
    #dictionary to save total time for all runs,"0" is brute, "1" is boyer, "2" is kmp
    search = {"Brute Force Method": 0, "Boyer-Moore Method": 0, "KMP  Search Method":0}
    if steps:                               # user wants step-by-step view
        runs = input("\nHow many times do you want to test the algorithm? Enter a number!   ")
        if runs.isdigit():                  # checks if user entered a number
            for run in range(int(runs)):
                time_brute = find_brute(T,P)[4]         # save the search method output
                time_boyer = find_boyer_moore(T,P)[4]
                time_kmp   = find_kmp(T,P)[4]
                for method in search:       # add time elpased for 1 run
                    if method == "Brute Force Method": search[method] += time_brute
                    if method == "Boyer-Moore Method": search[method] += time_boyer
                    if method == "KMP  Search Method": search[method] += time_kmp
            brute(T,P)                      # display step-by-step view
            boyer(T,P)
            kmp(T,P)
            print("\n")
            fastest = []                    # list to be ordered least to greatest
            for method in search:           # finished with the relay
                print(method, "took an average of", search[method]/float(runs), "seconds per search.")
                fastest += [search[method]/float(runs)]   #
            search = sorted(search)
                # sort search dictionary from least to greatest
        else:
            runs = print("That's not a number. Please enter a number!\n")
            relay(method)                   # loop back to have user enter number
    else:                                   # user does not want step-by-step view
        brutte = brute(T,P)                 # save the search method output
        boyyer = boyer(T,P)
        kmmp   = kmp(T,P)
        searches = [brutte, boyyer, kmmp]   # organize search methods into a list
        print("\nThe pattern [", P, "] first appears on index", brutte[1], ".\n")
        for method in searches:             # output summary of each search method
            print(method[0], "made", method[2], "comparisons and", method[3], "pattern shifts in", method[4], "seconds.")
    return search

" A fxn to run through all 3 algoritms w/ step-by-step view."
def All_Methods_STEP(T,P):
    yes = ['y', 'Y', 'yes', 'YES']          # confirmation option run alg X number of times
    no  = ['n', 'N', 'no', 'NO']            # negating option run alg once
    help = ["help", "HELP", "h", "H"]       # help function to describe what (y/n/help) does
    exit = ['exit', 'exit ', 'EXIT', 'exit()', 'EXIT()', 'e', 'E']
    
    relayy = input("\nDo you want to loop the methods? (y/n/help)   ")
    # to loop methods for avg time
    
    if   relayy in yes: relay(T,P,True)          # considers user wants step-by-step view
    elif relayy in  no: relay(T,P,False)         # run all methods once
    elif relayy in help:
        help_me("ALL_Methods_STEP")         # describe what (y/n/help) does here
        All_Methods_STEP(T,P)
    elif relay in exit: brexit()            # exit program
    else: All_Methods_STEP(T,P)
    return -1

" A fxn to run through all 3 algorithms w/o step-by-step view."
def All_Methods(T,P):
    brute = find_brute(T,P)                 # save the search method output
    boyer = find_boyer_moore(T,P)
    kmp = find_kmp(T,P)
    searches = [brute, boyer, kmp]          # organize search methods into a list
    print("\nThe pattern [", P, "] first appears on index", brute[1], ".\n") # index of pattern
    for method in searches:                 # output summary of each search method
        print(method[0], "made", method[2], "comparisons and", method[3], "pattern shifts in", method[4], "seconds.")
    return brute[1]                         # return index of patern

" A fxn to process whether user wants a step-by-step view of algorithm."
def step_option(T = "", P = "", steps = True):
    method = input("\nWhich method do you want to use? Enter a number! \n (0) All Methods \n (1) Brute-Force \n (2) Boyer-Moore \n (3) KMP             ")
    if method in ["exit", "exit()", "exit "]: brexit()
    if method.isdigit():                # checks user entered a number
        method = int(method)            # converts method to an integer
        if steps:                       # user wants to see step-by-step process
            if   method == 0: All_Methods_STEP(T,P)
            elif method == 1: brute(T,P)
            elif method == 2: boyer(T,P)
            elif method == 3: kmp(T,P)
            else:
                print("\nLooks like the choice you made isn't an option.")
        else:                           # user doesn't want step-by-step process
            if   method == 0: All_Methods(T,P)
            elif method == 1: find_brute(T,P)
            elif method == 2: find_boyer_moore(T,P)
            elif method == 3: return find_kmp(T,P)
            else:
                print("\nLooks like the choice you made isn't an option.")
    else:
        print("\nLooks like the choice you made isn't an option. Please enter a number!")
        step_option(T,P)

"A function to exit program at anytime."
def brexit():
    print("\nGoodbye!\n")
    sys.exit()

def help_me(method = ""):
    if method == "choices": print("\nChoosing 'y' will show you a step-by-step process of the search algorithm.\nChoosing 'n' will tell you how long the search took. \nTo end program type 'exit'.")
    elif method == "repeat": print("\nChoosing 'y' will use the same text and pattern as before.\nChoosing 'n' will let you use a different text and pattern. \nTo end program type 'exit'.")
    elif method == "ALL_Methods_STEP": print("\nChoosing 'y' will run the search methods however many times you want and tell you the average time it took for a search.\nChoosing 'n' will run the search methods once. \nTo end program type 'exit'.")

" This fxn provides a choice to which alorithm should be used."
def choices(T,P):                           # gives user a choice on which alg to use
    steps = input("\nDo you want to see the step by step process of each algorithm? (y/n/help) ")
    yes = ['y', 'Y', 'yes', 'YES']          # confirmation option to see of step-by-step process
    no  = ['n', 'N', 'no', 'NO']            # negating option to see step-by-step process
    search = ['all', 'brute', 'boyer, "kmp']      # used to skip into algorithms on entry
    help = ["help", "HELP", "h", "H"]
    exit = ['exit', 'exit ', 'EXIT', 'exit()', 'EXIT()', 'e', 'E']
    if steps in yes:
        step_option(T,P)
    elif steps in no:
        step_option(T,P, False)
    elif steps in search:
        if   steps == "all": All_Methods_STEP(T,P)
        elif steps == "brute": brute(T,P) 
        elif steps == "boyer": boyer(T,P)
        elif steps == "kmp"  : kmp(T,P)
    elif steps in help:
        help_me("choices")
        choices(T,P)
    elif steps in exit: brexit()
    else:
        print("\nLooks like the choice you made isn't an option.")
        repeat(T,P)

" A function to start the program again using the same text and pattern."
def repeat(T = "", P = ""):
    ans = input("\nDo you want to run this again using the same text and pattern? (y/n/help)   ")
    yes = ['y', 'Y', 'yes', 'YES']          # confirmation option to see of step-by-step process
    no  = ['n', 'N', 'no', 'NO']            # negating option to see step-by-step process
    help = ['help', 'HELP', 'h', 'H']       # help option
    exit = ['exit', 'exit()', 'e', 'E', 'EXIT', 'EXIT()'] # exit option to end program
    if ans in ["exit", "EXIT", "exit()", "EXIT()"]: brexit()    # exit out of program
    elif ans in yes:                        # run program with same text and pattern
        choices(T,P)
        return True                         # bool for the while loop in _main() function
    elif ans in no:                         # run program so as to use diff text and pattern
        _main()
        return False
    elif ans in help:                       # explain what (y/n/help) means
        help_me("repeat")
        repeat(T,P)
    elif ans in exit: brexit()              # exit out of program

def _main():
    exit = ['exit', 'exit ', 'exit()','e', 'E', 'EXIT', 'EXIT()'] # exit option to end program
    text  = input("What is the text you want to compare? \n")
    if text in exit: brexit()
    #text = "baron and barbara went to buy a barbell at barget then went to bacon street to go to the barbers to get a haircut by babby."
    #text = "aacaaaaab"
    pattern = input("\nWhat is the pattern you want to look for? \n")
    if pattern in exit: brexit()
    #pattern = "aab"
    #pattern = "babby"
    choices(text, pattern)  # gives a choice on which search method to run
    run_again = True        # variable to keep repeating search
    while run_again:
        run_again = repeat(text,pattern)

if __name__ == "__main__":
    _main()

"""
   - - - - - Here are Some Example Sentences for Text input - - - - -
   
   Baron and Barbara went to the Barbers.
   Baron and Barbara went to the barbers.
   Baron and barbara went to the barbers.
   baron and barbara went to the barbers.
   Baron and Barbara went to buy a Barbell at Barget then went to Bacon Street to go to the Barber.
   baron and barbara went to buy a barbell at barget then went to bacon street to go to the barbers to get a haircut by babby.
   
"""

"""
    POTENTIAL IMPROVEMENTS:
    - Take into consideration minor time delay when updating the comparisons/shifts counters.
    - Visuals of how the three algorithms move side by side.
"""
