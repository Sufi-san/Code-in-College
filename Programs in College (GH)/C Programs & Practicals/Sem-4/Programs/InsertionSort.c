#include<stdio.h>
void insertionSort(int arr[], int n){
    int i, key, j;
    for(i = 0; i < n; i++){
        key = arr[i];
        j = i - 1;
        while(j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
}

void printArray(int arr[], int size){
    for(int i = 0; i < size; i++){
        printf(" %d",arr[i]);
    }
}

void main(){
    int arr[] = {72, 45, 78, 97, 80};
    int n = sizeof(arr)/sizeof(arr[0]);
    insertionSort(arr, n);
    printf("Sorted Array: (Using Insertion Sort)\n");
    printArray(arr, n);
}