
"""
Given 3 Sorted arrays, A,B,C find the Common elemensts among them and return the common elem.
INPUT:
      A = [1,5,100,20,40,80]
      B = [6,7,20,80,100]
      c = [3,4,15,20,30,70,80,120]

OUTPUT = [20,80]
"""
Class Solution:
  def commonElems(slef, A: List[int],  B: List[int],  C: List[int] ) -> List[int]:
    i = j = k = 0
    common = []

    while i < len(A) and j < len(B) and K < len(C):
      if A[i] == B[j] == C[k]:
        if not common or common[-1] ! = A[i]:
          common.append(A[i])
          i += 1
          j += 1
          K += 1
      elif A[i] < B[j]:
         i += 1
      elif B[j] < C[k]:
         j += 1
      else:
        k += 1
    return common

         
        
