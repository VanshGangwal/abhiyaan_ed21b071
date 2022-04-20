#include <stdio.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNINGS

int main()
{
	int m, n;
	char find[5];
	int i, j,k=0;
	int a[5] = { 0,0,0,0,0 }, b[5] = { 0,0,0,0,0 };
	int result;

	scanf("%d %d\n", &m, &n);
	scanf(" %s\n",find);
	//printf("%d and %d\n", m, n);

	char row[50];

	for (i = 0; i < m; i++)
	{
		gets_s(row);

		//char string[50] = "Hello! We are learning about strtok";
		char* token = strtok(row, " ");
		j = 0;

		while (token != NULL) {
			//printf("%s\n", token); //printing each token
			result = strcmp(token, find);
			if (result == 0)
			{
				*(a + k) = i;
				*(b + k) = j;
				k++;
			}
			j++;
			token = strtok(NULL, " ");
		}
	}
	int l;
	if (k > 0)
	{
		printf("\nTrue\n");
	}
	else
	{
		printf("\nFalse\n");
	}
	for (l = 0; l < k; l++)
	{
		printf("%d %d\n", *(a + l), *(b + l));
	}
	
	return 0;
}