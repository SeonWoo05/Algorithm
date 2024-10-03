// 재귀쓰면 시간초과
#include <stdio.h>

int factorial(int N) {
    if (N == 1) return 1;
    
    return N * factorial(N-1);
}

int main(void) {
    int N;

    scanf("%d", &N);
    printf("%d", factorial(N));

    return 0;
}

// 그냥 반복문 이용
#include <stdio.h>

int factorial(int N) {
    int result = 1;

    for (int i = 2; i <= N; i++) {
        result *= i;
    }

    return result;
}

int main(void) {
    int N;

    scanf("%d", &N);
    printf("%d\n", factorial(N));

    return 0;
}