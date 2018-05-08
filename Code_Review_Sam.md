**Project name:** Twitter Analytics Plus

**Programmers:** Ben Wasserman, Rabah Habiss

**Code Reviewer:** Sam Kagan

On a scale of 1 to 6, I give this code a rating of **3** based on the following criteria:  
1  I was not able to compile the program due to insufficient information in the README.md file.  
2  At least one of the programs has syntax errors and does not compile  
3  The programs compile successfully but at least one generates runtime errors  
4  The programs compile and run but the project does not perform correctly and does not produce correct results.  
5  The programs compile and produce technically correct results but does not perform according to the documentation or does not comply with Chapman Coding Standards.  
6  The program produces correct output and is well written and well documented, following the Chapman Coding Standards.

**Specifically:**  
Using the given Docker image (which uses Python 2.7), I encountered a run-time error at line 29 in `test.py`.
This didn't happen when I ran `test.py` outside of the Docker image with Python 3.5; however, in 3.5
  I got a different runtime error (line 88, simple_content.py) because `dict.iteritems` isn't in that version.
When I changed `input` to `raw_input` on line 29 of `test.py` and rebuilt the docker image, everything worked fine. Since it's so small, I really don't think this runtime error is that big a deal. If I weren't being such a stickler, I'd probably give this code a 5.

#### Suggestions for improving the code:
I had to look in `sentiment.py` to understand what the sentiment scores at the end mean;
I'd appreciate some explanation in the program output itself.

Something like the file header in `tweet_processing.py` (along with author name and a few other things as per the
  [Chapman Coding Standards](https://blackboard.chapman.edu/bbcswebdav/pid-742589-dt-content-rid-5114708_1/courses/SPRING2018S-CPSC-353-02/Chapman%20Coding%20Standards.pdf))
  should be at the beginning of every file.

While your in-line commenting is generally good, many of your methods don't have a block comment at all. Most of the ones that do lack a description of the arguments and return values,
  which is especially crucial in Python since it's not immediately obvious what types variables have. The block comments also aren't all in standard Python docstring format
    (as per [PEP-8](https://www.python.org/dev/peps/pep-0257/)), which doesn't really matter that much unless you want Python to be able to interpret them to make documentation for you.
