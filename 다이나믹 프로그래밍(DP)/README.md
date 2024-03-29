1. LIS(최장 증가 부분 수열) 문제

[개념]
 

LIS의 개념은 단어 그대로 가장 긴 증가하는 부분 수열을 구하는 것이다. 

어떠한 수열이 주어질 때, 그 수열에서 일부 원소를 뽑아내어 새로 만든 수열을 '부분 수열'이라고 하며, 이 수열이 오름차순을 유지하면 '증가하는 부분 수열'이 되는 것이다. 

그러므로 어떤 수열에서 만들 수 있는 부분 수열 중에서 가장 길면서 오름차순을 유지하는 수열이 LIS이다.

[4 ,2 ,1 ,3 ,5 ,8 ,6 ,7 ]

예를 들어 위와 같은 길이가 8인 수열이 주어진다고 하자.

이 수열에서 증가하는 부분 수열을 뽑는다면 다음과 같이 여러 수열이 나올 것이다. 

[2, 3] , [1, 3] , [2, 5] , [2, 3, 5] , [1 ,3, 5] ....

 

그 중에서 가장 길이가 긴 수열은 [2,3,5,6,7] 이다. 


물론 [1,3,5,6,7] 도 가장 길이가 긴 수열로 가능하며, 이와 같이 LIS는 반드시 하나로 결정되는 것은 아니다.

따라서 문제에서도 답으로 LIS의 길이를 출력하도록 하거나, 수열을 구한다면 답이 여러 개가 되도록 출제된다.

출처 : https://rebro.kr/33

1) O(n^2)의 시간복잡도 알고리즘:

  1. 수열의 길이와 같은 dp배열을 하나 선언한다. 
  2. 수열을 처음부터 끝까지 순서대로 1개씩 탐색한다. ( 현재 위치 = i )
        (1) dp[i]에 넣을 값을 초기화해준다. (val)
        (2) 현재 위치(i)보다 이전에 있는 원소(j) 중에서 현재 원소보다 작은지 체크한다. (크거나 같으면 LIS 불가능)
        (3) 현재 원소보다 작다면, dp[j]가 val 보다 큰지 체크한다. 이 때 val보다 크다면 j번째 원소를 포함했을 때가,
            지금까지 확인한 최장 증가 부분 수열보다 더 길다는 의미이므로 val에 dp[j]를 할당해준다. 
        (4) 현재 원소도 포함해주어야 하므로 최종적으로 dp[i]에 val + 1을 할당해준다.
  3.dp배열의 원소 중에서 가장 큰 값을 출력한다. 
2) O(nlogn)의 시간복잡도 알고리즘-길이만 구하기:
  이 알고리즘을 위해서는 lower_bound를 이용해야 한다. 
  즉, 원래의 O(n^2) 알고리즘에서 이전의 원소들을 탐색하는 과정(O(n)) 을 lower_bound(O(logn))을 이용하여 시간을 줄여주는 것이다. 
  핵심 아이디어는, LIS를 만들기 위해서는 만드는 과정에서 LIS의 마지막 원소가 가능한 작을수록 더 긴 LIS를 생성할 수 있다는 것이다.
  그러므로 원소가 들어올 때, 만약 현재 생성된 LIS의 마지막 원소보다 작은 경우, LIS에 들어갈 위치를 찾은 후(O(logn)) 원소를 대체한다. 
  간단한 예시로, [1, 2, 3, 7, 5, 6] 수열이 있을 때, 5까지 탐색을 한 경우 가능한 LIS는
  [1, 2, 3, 7], [1, 2, 3, 5] 두가지가 만들어 진다. 
  이 때, 우리가 구하고자 하는 것은 최장 길이를 가지기만 하면 되므로 둘 다 LIS를 만족하는데, 더 긴 LIS를 만들기 위해서는 [1, 2, 3, 7] 보단 [1, 2, 3, 5]가 적합하다.
  실제로 마지막 원소 6이 들어올 때에는 [1, 2, 3, 7]로는 생성할 수 없고, [1, 2, 3, 5]에 붙어 [1, 2, 3, 5, 6]을 만들 수 있다.
3)O(nlogn)의 시간복잡도 - 길이와 수열 모두 구하기:
  LIS를 이루는 부분수열도 구하기 위해서는 어떤 작업을 거쳐야 할까?
  2번의 알고리즘에서 주어진 수열의 각각의 원소들이 K 배열에 들어가는 index를 배열로 별도로 저장한다. 
  그리고 나서 마지막원소부터 LIS의 길이를 감소시켜 가면서, 처음으로 해당 길이의 index가 나오는 원소만 뽑아낸다. 
  [3, 5, 2, 6, 1] 배열을 예로 들면, 
  1. K = [3]
  2. 2. K = [3, 5]
  3. 3. K = [2, 5]
  4. 4. K = [2, 5, 6]
  5. 5. K = [1, 5, 6]
  이므로 3은 1번째, 5는 2번째, 2는 1번째, 6은 3번째, 1은 1번째 index에 들어가게 된다. 즉, index 배열은 [1, 2, 1, 3, 1]이 되는 것이다. 
  LIS의 길이는 현재 3이므로 index 배열의 뒤에서부터 처음으로 3이 나오는 원소는 6이며, 
  그 다음 처음으로 2가 나오는 원소는 5, 그 다음 처음으로 1이 나오는 원소는 3이 된다. 
  따라서 이를 역으로 정렬하면 [3, 5, 6] 으로 우리가 구하고자 하는 LIS가 나오게 된다. 
  
  
