#include<stdio.h>
#include<conio.h>
void quicksort(int x[], int first, int last);

int main(){
	int size;
	printf("Enter size of the array: ");
	scanf("%d",&size);
	int x[size];
	printf("Enter elements of the array: \n");
	for(int i = 0; i < size; i++){
		scanf("%d",&x[i]);
	}
	quicksort(x,0,size-1);
	printf("Sorted elements: (Using Quick Sort)\n ");
	for(int i = 0; i < size; i++){
		printf("%d ",x[i]);
	}
	getch();
}

void quicksort(int x[], int first, int last){
	int pivot,j,temp,i;
	if(first<last){
		pivot = first;
		i = first;
		j = last;
		while(i<j){
			while(x[i] <= x[pivot]&&i<last)
				i++;
			while(x[j]>x[pivot])
				j--;
				if(i<j){
					temp = x[i];
					x[i] = x[j];
					x[j] = temp;
				}
			}
			temp = x[pivot];
			x[pivot] = x[j];
			x[j] = temp;
			quicksort(x,first,j-1);
			quicksort(x,j+1,last);
		}
}