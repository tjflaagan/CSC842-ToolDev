#include <stdio.h>

int main()
{
int d;
scanf("%d", &d);

while(d != 0)
{
	printf("%d ", d * 2);
	scanf("%d", &d);
}
return 0;
}
