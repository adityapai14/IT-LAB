#include<bits/stdc++.h>
#include<omp.h>

using namespace std;

void print(int** matrix, int m, int n) {
	for(int i = 0; i < m;i++) {
		for(int j = 0;j < n;j++) {
			printf("%4d ",matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

int** init(int m, int n) {
	int** matrix = new int * [m]; 
	for(int i = 0;i < m;i++)
		matrix[i]= new int [n];

	for(int i = 0;i < m;i++){
		for(int j = 0;j < n;j++){
			matrix[i][j] = (rand()%100)+1; 
		}
	}
	return matrix;
}

int** multiplyMatrix(int** A,int** B,int m,int n,int p,double &time){
	double start = omp_get_wtime(); 
	int **result = new int * [m]; 
	for(int i = 0; i < m;i++)
		result[i] = new int[p];

	for(int i = 0;i < m;i++) {
		for(int j = 0;j < p;j++){
			for(int k = 0; k < n;k++){
				result[i][j] += A[i][k] * B[k][j];
			}
		}
	}
	double end = omp_get_wtime();
	time = end-start;
	return result;
}


int main(){
	int x = 300,y = 500 ,z = 700;

	int** matrixA = init(x,y);
	int** matrixB = init(y,z); 
    double time = 0;
	int **result = multiplyMatrix(matrixA,matrixB,x,y,z, time);

    // print(result, x, z);
	printf("Serial matmul Time : %f\n",time);
}