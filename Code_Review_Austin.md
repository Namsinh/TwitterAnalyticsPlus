**Project name:** Twitter Analytics+

**Programmers:** Riccardo Angiolini, Rabah Habiss, Monique Namsinh, Rita Sachechelashvili, Ben Wasserman

**Code Reviewer:** Austin Bohannon

*On a scale of 1 to 6, I give this code a rating of **5** based on the following criteria:*

1. I was not able to compile the program due to insufficient information in the README.md file.

2. At least one of the programs has syntax errors and does not compile

3. The programs compile successfully but at least one generates runtime errors

4. The programs compile and run but the project does not perform correctly and does not produce correct results.
Specifically:

5. **The programs compile and produce technically correct results but does not perform according to the documentation or does not comply with Chapman Coding Standards.** Specifically:
    * The documentation states that the code conforms to Python 2.4.0+, but the use of `input()` instead of `raw_input()` implies that it is actually aimed at Python 3.x. Though, fixing this problem, by either shifting to Python3 or changing to `raw_input()` solves the issue.
    * The docker file builds and runs, but it has the same issue as above on my machine.
    * The files are not documented according to the Chapman Coding Standards.
    * `./sentiment.py` does not produce output like the README implies it should.

6. The program produces correct output and is well written and well documented, following the Chapman Coding Standards.

*Suggestions for improving the code (for extra credit!):*
* The sentiment analysis output of `./test.py` is not intuitive (i.e. I do not know what the numbers mean). Formatting this section better, would help me understand what is going on.
* Document your functions in your code (especially `./content.py`), as this makes reading it easier (this is also part of the Chapman Coding Standards).
