#define max 255
int randomnumber(int high,int prev){
	int x = time(0) % prev;
	srand(x);
	return rand() % high;
}