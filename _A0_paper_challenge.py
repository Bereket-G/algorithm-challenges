# The papers in the A series are numbered A0, A1, A2, and so on until infinity. A0 is the largest of these papers. The area of an A0 paper is exactly 1 square meter.
# All paper sizes in the A series have the same aspect ratio. More precisely, the ratio between the longer side and the shorter side of any paper in the A series is exactly equal to the square root of 2.

# For each i, the longer side of the A(i+1) paper is equal to the shorter side of the A(i) paper.
# From the previous two definitions it follows that the A series has the following useful property: Whenever you take an A(i) paper and you cut it in half (using a cut that passes through the centers of its longer sides), you will get two pieces of an A(i+1) paper. In other words, A1 is one half of A0, A2 is one half of A1, and so on.

# You are given a A. A[i] represents the number of papers of size A(i) you have in stock. For example, A[4] is the number of A4 papers you currently have.
# You are not allowed to cut paper in any way. You can only connect papers (seamlessly and without any waste) by taping them together. The papers you connect this way must not overlap. Can you take some of the papers you have and assemble a paper of size A0? Return "Possible" if it can be done and "Impossible" otherwise.


class A0Paper:
    def canBuild(self, _array_):
        paper_size = 0
        for indx, x in enumerate(_array_):
            paper_size += (x* (2**indx))
            print(str(paper_size))
            if ( paper_size >= 1 ):
                return "Possible"
        return str("Impossible")


print(A0Paper.canBuild('',{0,1,2}))