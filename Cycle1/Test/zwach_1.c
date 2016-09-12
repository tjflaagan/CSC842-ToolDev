#include <stdio.h>

int main()
{
int d;
scanf("%d", &d);

while(d != 0)
{
    if(d < 3){
        printf("%d", d * 2);
    }
    else{
        printf("%d ", d);
    }
    scanf("%d", &d);
}
return 0;
}