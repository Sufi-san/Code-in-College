#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
	char str1[100],str2[100];
	int len1=0,len2=0,choice;
	printf("Enter first string: ");
	gets(str1);
	printf("\nEnter second string: ");
	gets(str2);
	printf("\n 1.Calculate length of string. \n 2.Concatenate the string. \n 3.Reverse the string. \n 4.Copy the string. \n 5.Compare the two strings. \n Enter your choice: ");
	
	scanf("%d",&choice);
	printf("\n");
	
	switch(choice)
	{
		case 1:len1 = strlen(str1);
		printf("The length of string 1 is : %d \n",len1);
		
		len2=strlen(str2);
		printf("The length of string 2 is: %d \n",len2);
		break;
		
		case 2:
		strcat(str1,str2);
		printf("The concatenated string is: %s",str1);
		break;
		
		case 3:
		strrev(str1);
		printf("The reverse string1 is: %s\n",str1);
		strrev(str2);
		printf("The reverse string2 is: %s\n",str2);
		break;
		
		case 4:
		strcpy(str2,str1);
		printf("Source string: %s \n",str1);
		printf("Destination string: %s \n",str2);
		break;
		
		case 5:
		if(strcmp(str1,str2)==0)
		{
			printf("Entered strings are equal.\n");
		}
		else
		{
			printf("Entered strings are not equal.\n");
		}
		break;
		
		default: printf("Invalid choice");
	}
	getch();
}
