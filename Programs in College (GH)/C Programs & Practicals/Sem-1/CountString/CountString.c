#include<stdio.h>
#include<conio.h>
void main()
{
	char a[100];
	int i,len=0,vowels=0,consonants=0,digits=0,spaces=0,spl_char=0;
	printf("Enter a string :");
	gets(a);
	while(a[len]!=0)
	{
		if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'||a[i]=='A'||a[i]=='E'||a[i]=='I'||a[i]=='O'||a[i]=='U')
		{
			vowels++;
		}
	    else if((a[i]>='a' && a[i]<='z')||(a[i]>='A'&&a[i]<='Z'))
	    {
		    consonants++;
       	}
       	else if(a[i]>='0'&&a[i]>='9')
       	{
       	    digits++;	
		}
		else if(a[i]=='\0')
		{
			spaces++;
		}
		else
		{
			spl_char++;
		}
	printf("\n Vowels:%d\n Consonants:%d\n Digits:%d\n Spaces:%d\n Special Characters:%d",vowels,consonants,digits,spaces,spl_char);
	getch();
	}
}
