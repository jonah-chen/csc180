#include<bits/stdc++.h>

using namespace std;
vector<int> rb(500);

bool eq(int start, int end) // determines wheather rice balls in [start, end) all have the same size.
{
    int size = rb[start];
    for(int i = start + 1; i < end; ++i)
    {
        if(rb[i] != size)
            return false;
    }
    return true;
}

int max(int a, int b) // return the larger of the two args
{
    if(a >= b)
        return a;
    return b;
}

int size(int start, int end) // return maximum size of rice balls that can be formed in [start, end)
{
    int balls = end - start;
    
    // dealing with edge cases
    if(balls == 0)
        return 0;
    if(balls == 1)
        return rb[start];

    if(eq(start, end))
        return balls * rb[start]; // merge here
    
    // combining three balls
    if(balls == 3 && rb[start] == rb[start + 2])
        return 2 * rb[start] + rb[start + 1]; // merge here

    return max(size(start, end - 1), size(start + 1, end));
}

int main()
{
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; ++i)
        scanf("%d", &rb[i]);
    printf("%d", size(0, N));

    return 0;
}