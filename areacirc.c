#include <stdio.h>
#include <stdlib.h>
#define pi 3.141592

int main(int argc, char *argv[]) {
	
	float raio,area;
	
	printf("\nRaio do circulo e: ");
	scanf("%f", &raio);
	
	area = pi * raio * raio;
	printf("\nA area do circulo e: %f", area);
	
	return 0;
}
