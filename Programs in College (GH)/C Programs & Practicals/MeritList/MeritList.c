#include<stdio.h>
#include<conio.h>

struct student
{
	char name[20];
	int rollno;
	int physics,chem,maths,total;
};
 
void main()
{
	struct student s[100],temp;
	int n,i,j;
	printf("Enter the number of students:");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("\n Enter the student's name,rollno and marks in three subjects :");
		scanf("%s %d %d %d %d",&s[i].name,&s[i].rollno,&s[i].physics,&s[i].chem,&s[i].maths);
		s[i].total=s[i].physics+s[i].chem+s[i].maths;
	}
	for(i=0;i<=n-1;i++)
	{
		for(j=0;j<=n-2;j++)
		{
			if(s[i].total<s[j+1].total)
			{
				temp = s[j];
				s[j]=s[j+1];
				s[j+1]=temp;
			}
		}
	}
	printf("\nName\t Roll No\tPhysics\t\t Chemistry\t Maths\t Total\n");
	printf("----------------------------------------------------------------------------------------------------\n");
	for(i=0;i<=n-1;i++)
	{
		printf("%s\t %d \t\t %d \t\t %d \t\t %d \t %d\n",s[i].name,s[i].rollno,s[i].physics,s[i].chem,s[i].maths,s[i].total);
	}
	getch();
}
